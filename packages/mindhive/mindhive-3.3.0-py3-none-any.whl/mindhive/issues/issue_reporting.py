import logging
import os
from abc import abstractmethod
from typing import Type, Sequence

import ping3
from ping3.errors import PingError

from ..errors.fatal_exception import FatalException, resolve_msg
from .issue import Issue, IssuePriority
from .issue_redis import IssueRedis
from ..log.language import translate

ping3.EXCEPTIONS = True
SWITCH_IP = os.getenv("CABINET_SWITCH_IP")
TRUNC_RAW_ERROR_TO_CHAR_COUNT = 200


def append_raw_error_to_msg(msg: str, err: Exception) -> str:
    raw_error = str(err)
    if len(raw_error) > TRUNC_RAW_ERROR_TO_CHAR_COUNT:
        raw_error = raw_error[:TRUNC_RAW_ERROR_TO_CHAR_COUNT] + "..."
    return f"{msg}\n\nThe raw error was: `` {raw_error} ``"


class IssueReportingContext:
    def __init__(self, issue_redis: IssueRedis, issue_key: str) -> None:
        self.log = logging.getLogger(self.__class__.__name__)
        self.issue_redis = issue_redis
        self.issue_key = issue_key

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        report_issue = None if exc_val is None else self._report_issue(exc_val)
        if report_issue:
            if self.cabinet_switch_off():
                report_issue = Issue(
                    translate(
                        {
                            "ja": "絞り機のMindhiveキャビネットがオフの場合",
                            "es": "El gabinete de Mindhive cerca del exprimidor está apagado",
                            "it": "Il cabinet Mindhive presso il sommergibile è spento",  # REVISIT ?
                            "de": "Der Mindhive-Schrank am Wringer ist ausgeschaltet.",
                            "en": "Mindhive cabinet at the wringer is off",
                        }
                    ),
                    translate(
                        {
                            "ja": "意図的にオフにしていない場合はパワーサイクルしてください。",
                            "es": "Si no ha sido apagado intencionalmente, trate de reiniciarlo.",
                            "it": "Se non l'hai intenzionalmente spento, prova a riavviarlo.",
                            "de": "Wenn Sie ihn nicht absichtlich ausgeschaltet haben, versuchen Sie, ihn neu zu starten.",
                            "en": "If you have not intentionally turned it off then try power cycling it.",
                        }
                    ),
                    IssuePriority.P5_INFO,
                )
            existing_issue = self.issue_redis.find(self.issue_key)
            if existing_issue and existing_issue.title == report_issue.title:
                return
            self.issue_redis.set(self.issue_key, report_issue)
        else:
            self.issue_redis.clear(self.issue_key)

    @abstractmethod
    def _report_issue(self, err: Exception) -> Issue | None: ...

    def cabinet_switch_off(self) -> bool:
        if not SWITCH_IP:
            return False
        try:
            if not ping3.ping(SWITCH_IP, timeout=1):
                return True
        except PingError:
            return True
        except:  # noqa
            self.log.warning("Ping failed", exc_info=True)
        return False


class InitFatalExceptionReporting(IssueReportingContext):
    def __init__(self, issue_redis: IssueRedis, service: str) -> None:
        super().__init__(issue_redis, f"{service}:init:fatal")

    def _report_issue(self, err: Exception) -> Issue | None:
        if not isinstance(err, FatalException):
            return None
        reboot_msg = translate(
            {
                "ja": "解決まで最大5分程度お待ちください。",
                "es": "Puede que tenga que esperar 5 minutos para que el problema se solucione por su cuenta.",
                "it": "Potrebbe essere necessario attendere fino a 5 minuti affinché questo problema si risolva da solo.",
                "de": "Es kann bis zu 5 Minuten dauern, bis sich dieses Problem von selbst löst.",
                "en": "You may have to wait up to 5 minutes for this issue to resolve itself.",
            }
        )
        return Issue(err.title, err.msg + "\n\n" + reboot_msg, IssuePriority.P1_CRITICAL)


class GeneralExceptionReporting(IssueReportingContext):
    def __init__(
        self,
        issue_redis: IssueRedis,
        issue_key: str,
        exception_type: Type[Exception],
        title: str,
        msg: Sequence[str] | str,
        priority: IssuePriority,
    ) -> None:
        super().__init__(issue_redis, issue_key)
        self.exception_type = exception_type
        self.title = title
        self.msg = resolve_msg(msg)
        self.priority = priority

    def _report_issue(self, err: Exception) -> Issue | None:
        if not isinstance(err, self.exception_type):
            return None
        return Issue(self.title, append_raw_error_to_msg(self.msg, err), self.priority)
