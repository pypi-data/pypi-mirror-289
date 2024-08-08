import ddtrace

from ..debug.external_output import block_external_output
from .datadog_agent import has_datadog_agent

tracer = ddtrace.tracer


if not has_datadog_agent() or block_external_output():
    tracer.configure(enabled=False)
