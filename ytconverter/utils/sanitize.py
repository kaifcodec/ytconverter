import re

_BAD_CHARS = re.compile(r'[\\/*?:"<>|]')


def sanitize(name: str) -> str:
    return _BAD_CHARS.sub("", name)
