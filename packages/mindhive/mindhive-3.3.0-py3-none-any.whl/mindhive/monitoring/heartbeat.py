import logging

from time import monotonic

from ..log.metrics import metrics
from ..network.redis_client import RedisClient
from ..network.redis_listener import RedisJsonListener
from ..process.unit import Unit


class HeartbeatGenerator:
    def __init__(self, redis: RedisClient, unit: Unit, service: str, min_interval: float | None = None) -> None:
        self.log = logging.getLogger(f"{self.__class__.__name__}.{service}")
        self.service = service
        self.send_channel = f"{unit.redis_prefix}:heartbeat:{service}"
        self.reply_channel = f"{unit.redis_prefix}:heartbeat-reply:{service}"
        self.redis = redis
        RedisJsonListener(redis, {self.reply_channel: self.handle_reply})
        self.min_interval = min_interval
        self.last_beat_timestamp: float | None = None

    def beat(self):
        now = monotonic()
        if (
            self.min_interval is None
            or not self.last_beat_timestamp
            or (now - self.last_beat_timestamp) > self.min_interval
        ):
            self.last_beat_timestamp = now
            self.log.debug("Beat")
            self.redis.publish_json(
                self.send_channel,
                {
                    "service": self.service,
                    "replyChannel": self.reply_channel,
                },
            )
            metrics.increment("heartbeat.sent.count")

    def handle_reply(self, _, data):
        self.log.debug(f"Reply: {data}")
        metrics.increment("heartbeat.received.count", tags=[f"display:{data['display']}"])
