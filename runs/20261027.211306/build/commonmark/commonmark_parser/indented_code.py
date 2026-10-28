"""Indented code block recognition."""


def _strip_columns(line: str, columns: int) -> tuple[str, int]:
    # Tabs are positioned from the start of the source line. Expanding first
    # matters when a list or quote has already removed part of the indentation:
    # a later tab still lands on the original four-column tab stop.
    expanded: list[str] = []
    index = 0
    column = 0
    while index < len(line) and line[index] in " \t":
        char = line[index]
        width = 4 - column % 4 if char == "\t" else 1
        expanded.append(" " * width)
        column += width
        index += 1
    value = "".join(expanded)
    removed = min(columns, len(value))
    return value[removed:] + line[index:], removed


def parse_indented_code(lines: list[str], paragraph_open: bool = False):
    leading = 0
    for char in lines[0] if lines else "":
        if char == " ":
            leading += 1
        elif char == "\t":
            leading += 4 - leading % 4
        else:
            break
    if paragraph_open or not lines or not lines[0].strip(" \t") or leading < 4:
        return None
    kept: list[str] = []
    consumed = 0
    pending_blanks: list[str] = []
    for line in lines:
        if not line.strip(" \t"):
            # Blank lines inside an indented code block retain indentation
            # that does not reach the four-column code indentation.
            pending_blanks.append(line[4:] if len(line) > 4 else "")
            consumed += 1
            continue
        rest, removed = _strip_columns(line, 4)
        if removed < 4:
            break
        kept.extend(pending_blanks)
        pending_blanks.clear()
        kept.append(rest)
        consumed += 1
    consumed -= len(pending_blanks)
    if not kept:
        return None
    return "".join(part + "\n" for part in kept), consumed
