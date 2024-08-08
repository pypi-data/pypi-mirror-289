from .healthcheck import Healthcheck
from .heartbeat import HeartbeatGenerator
from ..network.redis_client import RedisClient
from ..process.unit import Unit


class HealthcheckWithHeartbeat(Healthcheck):
    def __init__(
        self, redis: RedisClient, unit: Unit, heartbeat_service_for_display: str, debounce_interval: float = 1
    ):
        super().__init__(debounce_interval)
        self.heartbeat = HeartbeatGenerator(redis, unit, heartbeat_service_for_display, min_interval=5)

    def _notify_external(self):
        super()._notify_external()
        self.heartbeat.beat()
