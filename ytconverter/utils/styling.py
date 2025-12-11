import re
import fontstyle as fs
from colored import fg, attr

# Re-use original colours
f_colored = fg(117)
r = fg(1)
b = attr(0)


def apply_style(text: str, style: str) -> str:
    return fs.apply(text, style)


def remove_ansi(text: str) -> str:
    ansi_escape = re.compile(r"\x1B[@-_][0-?]*[ -/]*[@-~]")
    return ansi_escape.sub("", text)
