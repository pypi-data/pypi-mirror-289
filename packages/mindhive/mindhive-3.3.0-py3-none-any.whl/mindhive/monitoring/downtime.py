import logging
import re
from datetime import timedelta, datetime

from datadog_api_client import ApiClient, Configuration
from datadog_api_client.v2.api.downtimes_api import DowntimesApi

from mindhive.monitoring.datadog_tags import running_tags
from mindhive.process.unit import Unit

DOWNTIME_WINDOW_END_AVOID_TIME = timedelta(minutes=10)

log = logging.getLogger("downtime")


def is_downtime(unit: Unit) -> bool:
    available_tags = {f"{k}:{v}" for k, v in running_tags(unit).items()}
    try:
        configuration = Configuration()
        with ApiClient(configuration) as api_client:
            downtimes_api = DowntimesApi(api_client)
            downtimes = downtimes_api.list_downtimes_with_pagination(current_only=True)
        min_downtime_end = datetime.now().astimezone() + DOWNTIME_WINDOW_END_AVOID_TIME
        for dt in downtimes:
            attr = dt.attributes
            if not attr.message or not re.search(r"\bMAINTENANCE_WINDOW\b", attr.message):
                continue
            if not attr.scope:
                log.warning(f"Skipping downtime: {dt.id} as it has no scope")
                continue
            dt_tags = {t.replace('"', "") for t in attr.scope.split(" AND ")}
            if not available_tags.issuperset(dt_tags):
                continue
            if "current_downtime" in attr.schedule:
                dt_end = attr.schedule.current_downtime.end
            else:
                dt_end = attr.schedule.end
            if dt_end and dt_end < min_downtime_end:
                log.info(f"Avoiding end of downtime: {dt.id}")
                continue
            return True
    except Exception:  # noqa
        log.warning("Failed to check downtime", exc_info=True)
    return False


if __name__ == "__main__":
    print(is_downtime(Unit("jbs", "cactus", "wringer1")))
