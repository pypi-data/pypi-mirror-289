def slow_frame_height(line_rate: int) -> int:
    return min(line_rate, 400)


def fast_frame_height(line_rate: int) -> int:
    third_height = line_rate // 3
    third_even_height = third_height // 2 * 2
    return min(max(third_even_height, 100), 400)


def clamp_frame_height(height: int, line_rate: int) -> int:
    min_height = fast_frame_height(line_rate)
    if height < min_height:
        return min_height
    max_height = slow_frame_height(line_rate)
    if height > max_height:
        return max_height
    return height
