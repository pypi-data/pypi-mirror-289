import logging
from typing import Collection

from .issue import Issue
from ..network.redis_client import RedisClient
from ..process.unit import Unit


class IssueRedis:
    def __init__(self, redis: RedisClient, unit: Unit):
        self.log = logging.getLogger(f"{self.__class__.__name__}.{unit.redis_prefix}")
        self.redis = redis
        self.redis_key = f"{unit.redis_prefix}:issues"

    def get_current_issue_keys(self) -> Collection[str]:
        return self.redis.hkeys(self.redis_key)

    def find(self, issue_key: str) -> Issue | None:
        value = self.redis.hget(self.redis_key, issue_key)
        if value is None:
            return None
        assert isinstance(value, (str, bytes))
        return Issue.from_json(value)

    def set(self, issue_key: str, issue: Issue):
        self.log.info(f"Setting alert: {issue_key} '{issue.title}'")
        self.redis.hset(self.redis_key, issue_key, issue.to_json())

    def clear(self, issue_key: str):
        cleared = self.redis.hdel(self.redis_key, issue_key)
        if cleared:
            self.log.info(f"Cleared alert: {issue_key}")
