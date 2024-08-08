import logging
from abc import abstractmethod
from threading import Event
from typing import Mapping, Collection, Callable

from redis import RedisError

from .redis_client import RedisClient
from ..process.thread import start_thread

_log = logging.getLogger("network.redis_events")


def key_event_channel(key: str):
    return f"__keyspace@0__:{key}"


def enable_events(redis: RedisClient):
    # ensure list events are enabled
    config = redis.config_get("notify-keyspace-events")
    events = config["notify-keyspace-events"]
    _log.debug(f"Current events config: {events!r}")
    add = "".join(event_code for event_code in "KA" if event_code not in events)
    if add:
        new_events = events + add
        _log.info(f"Updating events config from: {events!r} to: {new_events!r}")
        redis.config_set("notify-keyspace-events", new_events)


class RedisKeyEventListener:
    def __init__(
        self,
        redis: RedisClient,
        key: str,
        filter: Collection[str] | None = None,
    ):
        self.key = key
        self.filter = frozenset(filter) if filter else None
        self.log = logging.getLogger(f"{self.__class__.__name__}.{key}")
        self._stop = Event()
        self.redis = redis
        enable_events(redis)
        start_thread(self.log, self._thread_worker)

    def stop(self):
        self._stop.set()

    def _thread_worker(self):
        while not self._stop.is_set():
            with self.redis.pubsub() as pubsub:
                pubsub.subscribe(key_event_channel(self.key))
                try:
                    while not self._stop.is_set():
                        message = pubsub.get_message(timeout=self.redis.loop_time)
                        if message is not None and message["data"]:
                            if not self.filter or message["data"] in self.filter:
                                self._on_event(message)
                except RedisError:
                    self.log.exception("pubsub.get_message failed, will resubscribe")

    @abstractmethod
    def _on_event(self, message: Mapping): ...


class RedisReplicatedKeyStateWatcher[T](RedisKeyEventListener):
    def __init__(self, redis: RedisClient, key: str, value_log_level=logging.DEBUG):
        # Initialize these immediately as _on_event may run from super().__init__()
        self.value_log_level = value_log_level
        self._listeners: list[Callable[[T], None]] = []
        super().__init__(redis, key)
        initial_value: T = self._read_value()
        self._value = initial_value
        if self.log.isEnabledFor(self.value_log_level):
            self.log.log(self.value_log_level, f"Initial value: {initial_value}")

    @property
    def value(self) -> T:
        return self._value

    def on_value(self, listener: Callable[[T], None]):
        listener(self.value)
        self._listeners.append(listener)

    def _on_event(self, message: Mapping):
        new_value = self._read_value()
        try:
            if self._value == new_value:
                return
        except AttributeError:
            pass  # _value hasn't been set yet
        self._value = new_value
        if self.log.isEnabledFor(self.value_log_level):
            self.log.log(self.value_log_level, f"New value: {new_value}")
        for listener in self._listeners:
            listener(new_value)

    @abstractmethod
    def _read_value(self) -> T: ...


class JsonKeyWatcher[T: Mapping](RedisReplicatedKeyStateWatcher[T]):
    def _read_value(self) -> T:
        result = self.redis.get_json(self.key)
        if result is None:
            return {}  # pyright: ignore [reportReturnType]
        return result  # pyright: ignore [reportReturnType]


class HashKeyWatcher(RedisReplicatedKeyStateWatcher[dict[str, str] | None]):
    def _read_value(self) -> dict[str, str] | None:
        return self.redis.hgetall(self.key)
