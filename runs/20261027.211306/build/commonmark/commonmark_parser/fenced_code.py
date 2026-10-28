"""Fenced code block recognition."""

import re

_OPEN = re.compile(r"^ {0,3}(`{3,}|~{3,})(.*)$")


def _remove_indent(line: str, indent: int) -> str:
    return line[min(indent, len(line) - len(line.lstrip(" "))):]


def parse_fenced_code(lines: list[str]):
    if not lines:
        return None
    match = _OPEN.match(lines[0])
    if not match:
        return None
    fence, info = match.groups()
    if fence[0] == "`" and "`" in info:
        return None
    info = info.strip(" \t")
    indent = len(lines[0]) - len(lines[0].lstrip(" "))
    close = re.compile(r"^ {0,3}" + re.escape(fence[0]) + r"{" + str(len(fence)) + r",}[ \t]*$")
    content = []
    for index, line in enumerate(lines[1:], 1):
        if close.match(line):
            return "".join(_remove_indent(line, indent) + "\n" for line in content), info, index + 1
        content.append(line)
    return "".join(_remove_indent(line, indent) + "\n" for line in content), info, len(lines)
