import json
import logging
from functools import partial
from threading import Event
from typing import Callable, Mapping, Any

from ..log.trace import tracer
from .redis_client import RedisClient
from ..process.thread import start_thread

type ChannelJsonCallback = Callable[[str, Any], None]


class RedisJsonListener:
    def __init__(
        self,
        redis: RedisClient,
        channel_pattern_map_callback: Mapping[str, ChannelJsonCallback],
    ) -> None:
        super().__init__()
        self.log = logging.getLogger(self.__class__.__name__)
        self.channel_pattern_map_callback = channel_pattern_map_callback
        self.redis = redis
        self._stopping = Event()
        start_thread(self.log, self._thread_worker, self.stop)

    def stop(self) -> None:
        self._stopping.set()

    def _handle_message(self, callback: ChannelJsonCallback, message: Mapping):
        channel = message["channel"]
        with tracer.trace(f"redis.{channel}"):
            callback(channel, json.loads(message["data"]))

    def _thread_worker(self):
        with self.redis.pubsub(ignore_subscribe_messages=True) as pubsub:
            pubsub.psubscribe(
                **{
                    pattern: partial(self._handle_message, callback)
                    for pattern, callback in self.channel_pattern_map_callback.items()
                }
            )
            while not self._stopping.is_set():
                pubsub.get_message(timeout=self.redis.loop_time)
                # Ignore result, should always be None
