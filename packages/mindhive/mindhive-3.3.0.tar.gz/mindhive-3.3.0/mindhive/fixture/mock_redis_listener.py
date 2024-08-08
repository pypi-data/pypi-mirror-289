from typing import Mapping

from ..network.redis_listener import ChannelJsonCallback


class MockRedisJsonListener:
    def __init__(self):
        self.channel_pattern_map_callback = {}

    def mock_instantiate(self, _redis, channel_pattern_map_callback: Mapping[str, ChannelJsonCallback]) -> None:
        for pattern in channel_pattern_map_callback:
            if "*" in pattern:
                if pattern.index("*") != len(pattern) - 1:
                    raise NotImplementedError()
        self.channel_pattern_map_callback.update(channel_pattern_map_callback)

    def mock_send(self, channel: str, data: Mapping):
        matching_callbacks = [
            callback
            for pattern, callback in self.channel_pattern_map_callback.items()
            if pattern == channel or pattern.endswith("*") and channel.startswith(pattern[:-1])
        ]
        if not matching_callbacks:
            raise ValueError(f"No one listening on {channel=}")
        for callback in matching_callbacks:
            callback(channel, data)
