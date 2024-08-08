from functools import lru_cache
from typing import Mapping

from datadog import get_hostname  # pyright: ignore [reportPrivateImportUsage]

from ..process.unit import Unit


def unit_tags(unit: Unit) -> Mapping[str, str]:
    return {
        "customer": unit.customer,
        "site": f"{unit.customer}-{unit.site}",
        "unit": f"{unit.customer}-{unit.site}-{unit.unit}",
    }


@lru_cache()
def running_tags(unit: Unit) -> Mapping[str, str]:
    hostname = get_hostname(hostname_from_config=False)
    if not hostname:
        return unit_tags(unit)
    result = {"host": hostname}
    result.update(unit_tags(unit))
    return result
