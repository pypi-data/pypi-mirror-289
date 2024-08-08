import logging
import os
from typing import Collection

from datadog import DogStatsd  # pyright: ignore [reportPrivateImportUsage]

from ..debug.external_output import block_external_output
from .datadog_agent import has_datadog_agent

DOGSTATSD_SOCKET = "/var/run/datadog/dsd.socket"

_log = logging.getLogger("metrics")

LOG_LEVEL_MAP_EVENT_CATEGORY = {
    logging.CRITICAL: "error",
    logging.ERROR: "error",
    logging.WARNING: "warning",
    logging.INFO: "info",
}


# noinspection PyMethodMayBeStatic
class Metrics:
    AGGREGATE_PERIOD = 20

    def __init__(self, metric_prefix: str | None = None, fixed_tags: Collection[str] | None = None):
        self.metric_prefix = metric_prefix
        if self.metric_prefix and not self.metric_prefix.endswith("."):
            self.metric_prefix += "."
        self.fixed_tags = list(fixed_tags) if fixed_tags else []

    def _build_metric_name(self, metric: str):
        if not self.metric_prefix:
            return metric
        return self.metric_prefix + metric

    def _build_tags(self, tags: Collection[str] | None = None):
        if not tags:
            return self.fixed_tags
        return [*self.fixed_tags, *tags]

    def gauge(self, metric: str, value: float, tags: Collection[str] | None = None, sample_rate: float | None = None):
        metric = self._build_metric_name(metric)
        tags = self._build_tags(tags)
        if _log.isEnabledFor(logging.DEBUG):
            _log.debug(f"{metric} gauge {value}")
        if statsd:
            statsd.gauge(metric, value, tags, sample_rate)

    def increment(
        self, metric: str, value: float = 1, tags: Collection[str] | None = None, sample_rate: float | None = None
    ):
        metric = self._build_metric_name(metric)
        tags = self._build_tags(tags)
        if _log.isEnabledFor(logging.DEBUG):
            _log.debug(f"{metric} increment {value}")
        if statsd:
            statsd.increment(metric, value, tags, sample_rate)

    def histogram(
        self, metric: str, value: float, tags: Collection[str] | None = None, sample_rate: float | None = None
    ):
        metric = self._build_metric_name(metric)
        tags = self._build_tags(tags)
        if _log.isEnabledFor(logging.DEBUG):
            _log.debug(f"{metric} histogram {value}")
        if statsd:
            statsd.histogram(metric, value, tags, sample_rate)

    def distribution(
        self, metric: str, value: float, tags: Collection[str] | None = None, sample_rate: float | None = None
    ):
        metric = self._build_metric_name(metric)
        tags = self._build_tags(tags)
        if _log.isEnabledFor(logging.DEBUG):
            _log.debug(f"{metric} distribution {value}")
        if statsd:
            statsd.distribution(metric, value, tags, sample_rate)

    def timing(
        self, metric: str, seconds: float, tags: Collection[str] | None = None, sample_rate: float | None = None
    ):
        metric = self._build_metric_name(metric)
        tags = self._build_tags(tags)
        if _log.isEnabledFor(logging.DEBUG):
            _log.debug(f"{metric} timing {seconds:.3f}s")
        if statsd:
            statsd.timing(metric, seconds, tags, sample_rate)

    def event(
        self,
        title: str,
        text: str,
        log_level: int,
        aggregation_key: str | None = None,
        tags: Collection[str] | None = None,
    ):
        tags = self._build_tags(tags)
        if _log.isEnabledFor(log_level):
            _log.log(log_level, f"{title}: {text}")
        if log_level in LOG_LEVEL_MAP_EVENT_CATEGORY and statsd:
            statsd.event(title, text, LOG_LEVEL_MAP_EVENT_CATEGORY[log_level], aggregation_key, tags=tags)

    def error(self, title: str, text: str, aggregation_key: str | None = None, tags: Collection[str] | None = None):
        tags = self._build_tags(tags)
        self.event(title, text, logging.ERROR, aggregation_key, tags)

    def warning(self, title: str, text: str, aggregation_key: str | None = None, tags: Collection[str] | None = None):
        tags = self._build_tags(tags)
        self.event(title, text, logging.WARNING, aggregation_key, tags)


if has_datadog_agent() and not block_external_output():
    socket_path = DOGSTATSD_SOCKET if os.path.exists(DOGSTATSD_SOCKET) else None
    statsd = DogStatsd(socket_path=socket_path, disable_buffering=True)
else:
    statsd = None

metrics = Metrics()
