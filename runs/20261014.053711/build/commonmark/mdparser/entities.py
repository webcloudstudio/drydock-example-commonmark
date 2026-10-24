"""Character references and backslash escapes.

Responsibility: decode named entities (from the standard library table `html.entities.html5`,
names ending in a semicolon only) and numeric character references, and provide the backslash
unescape helper and the shared destination, title and info-string helper.
"""

import html.entities
import re
import string

# The ASCII punctuation characters that a backslash may escape.
ASCII_PUNCTUATION = frozenset(string.punctuation)

# A named reference: `&`, a name, then `;`. The table lookup adds the semicolon back.
NAMED_REFERENCE_PATTERN = re.compile(r"&([A-Za-z][A-Za-z0-9]*);")
# A decimal reference has 1 to 7 digits. A hexadecimal reference has `x` or `X` and 1 to 6 digits.
DECIMAL_REFERENCE_PATTERN = re.compile(r"&#([0-9]{1,7});")
HEXADECIMAL_REFERENCE_PATTERN = re.compile(r"&#[xX]([0-9A-Fa-f]{1,6});")
REPLACEMENT_CHARACTER = "�"
MAX_CODE_POINT = 0x10FFFF


def match_reference(text: str, start: int) -> tuple[str, int] | None:
    """Return the decoded text of the character reference at `start` and the index just past it.

    Returns None when no recognized reference starts at `start`, so the `&` is literal text. An
    unknown name, or a name without its semicolon, is not a reference.
    """
    named = NAMED_REFERENCE_PATTERN.match(text, start)
    if named is not None:
        value = html.entities.html5.get(named.group(1) + ";")
        if value is None:
            return None
        return value, named.end()
    decimal = DECIMAL_REFERENCE_PATTERN.match(text, start)
    if decimal is not None:
        return _code_point_text(int(decimal.group(1), 10)), decimal.end()
    hexadecimal = HEXADECIMAL_REFERENCE_PATTERN.match(text, start)
    if hexadecimal is not None:
        return _code_point_text(int(hexadecimal.group(1), 16)), hexadecimal.end()
    return None


def _code_point_text(code_point: int) -> str:
    """Return the character for a numeric reference. Zero, surrogates and out-of-range values
    become U+FFFD."""
    if code_point == 0 or code_point > MAX_CODE_POINT or 0xD800 <= code_point <= 0xDFFF:
        return REPLACEMENT_CHARACTER
    return chr(code_point)


def unescape(text: str) -> str:
    """Apply backslash escapes to `text`, for destinations, titles and info strings.

    A backslash before ASCII punctuation yields that character. A backslash before any other
    character, or at the end of the text, is kept. Escapes are read left to right and each one is
    consumed whole, so `\\\\` yields one backslash and the character after it is not escaped.
    """
    out: list[str] = []
    index = 0
    while index < len(text):
        char = text[index]
        if char == "\\" and index + 1 < len(text) and text[index + 1] in ASCII_PUNCTUATION:
            out.append(text[index + 1])
            index += 2
            continue
        out.append(char)
        index += 1
    return "".join(out)


def unescape_and_decode(text: str) -> str:
    """Apply backslash escapes and character references to `text` in one left-to-right pass.

    This is the shared helper for link destinations, titles and info strings. The pass is single
    so that an escape is never read as the start of a reference: `\\&amp;` yields the literal text
    `&amp;`, not `&`.
    """
    out: list[str] = []
    index = 0
    while index < len(text):
        char = text[index]
        if char == "\\" and index + 1 < len(text) and text[index + 1] in ASCII_PUNCTUATION:
            out.append(text[index + 1])
            index += 2
            continue
        if char == "&":
            reference = match_reference(text, index)
            if reference is not None:
                value, index = reference
                out.append(value)
                continue
        out.append(char)
        index += 1
    return "".join(out)
