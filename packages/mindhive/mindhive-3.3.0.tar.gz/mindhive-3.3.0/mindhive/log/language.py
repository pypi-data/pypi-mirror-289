import os

LANGUAGE = os.getenv("LANGUAGE", "en").split(":")[0].split("_")[0]


def translate[T](language_map_result: dict[str, T]) -> T:
    return language_map_result.get(LANGUAGE, language_map_result["en"])
