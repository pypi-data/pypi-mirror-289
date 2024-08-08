import json
import logging
import os
from typing import Mapping

from redis import Redis
from redis.sentinel import Sentinel
from redis.typing import ChannelT, KeyT

USE_REDIS_SENTINEL = os.getenv("USE_REDIS_SENTINEL", "false").lower() == "true"

IPV4_LOCALHOST = "127.0.0.1"
DEFAULT_PORT = 6379
DEFAULT_HEALTH_CHECK_TIME = 60


class RedisClient(Redis):

    def __init__(self) -> None:
        self.log = logging.getLogger(self.__class__.__name__)

        if USE_REDIS_SENTINEL:
            sentinel_service = os.getenv("SENTINEL_SERVICE", "redis-sentinel.redis-sentinel.svc.cluster.local")
            sentinel_port = int(os.getenv("SENTINEL_PORT", "26379"))
            master_set = os.getenv("SENTINEL_MASTERSET", "mymaster")

            s = Sentinel([(sentinel_service, sentinel_port)], socket_timeout=0.1)
            host, port = s.discover_master(master_set)
            self.log.info(f"Redis master: {host}:{port}")
        else:
            host = os.getenv("REDIS_HOST", IPV4_LOCALHOST)
            port = DEFAULT_PORT
            if ":" in host:
                host, port = host.split(":", 1)

        health_check_time = DEFAULT_HEALTH_CHECK_TIME
        self.loop_time = health_check_time / 2
        super().__init__(
            host,
            int(port),
            health_check_interval=health_check_time,
            socket_keepalive=True,
            socket_connect_timeout=5,
            socket_timeout=5,
            retry_on_timeout=True,
            decode_responses=True,
        )

    def set_json(self, name: KeyT, value, **kwargs) -> bool | None:
        return self.set(name, json.dumps(value), **kwargs)

    def get_json(self, name: KeyT) -> Mapping | None:
        raw_result = self.get(name)
        if not raw_result:
            return None
        return json.loads(raw_result)  # pyright: ignore [reportArgumentType]

    def publish_json(self, channel: ChannelT, message: Mapping, **kwargs):
        self.log.debug(f"Publishing to: {channel}")
        super().publish(channel, json.dumps(message), **kwargs)
