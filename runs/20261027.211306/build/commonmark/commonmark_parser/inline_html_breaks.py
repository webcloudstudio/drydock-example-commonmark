"""Recognition of inline HTML tokens and hard line breaks."""

from dataclasses import dataclass
import re


@dataclass
class InlineNode:
    type: str
    literal: str = ""


_TAG = re.compile(r"</?[A-Za-z][A-Za-z0-9-]*(?:[ \t\n]+(?:[^<>\"']|'[^']*'|\"[^\"]*\")*)?[ \t]*/?>")
_COMMENT = re.compile(r"<!--(?:>|->|--!?>|(?:(?!-->|--!>).)*?(?:-->|--!>))", re.S)
_HTML = re.compile(r"<(?:[!?](?:[^<>]|'[^']*'|\"[^\"]*\")+|\[CDATA\[.*?\]\]|/?[A-Za-z][^<>]*)>", re.S)


def _html_at(source: str, start: int) -> int | None:
    comment = _COMMENT.match(source, start)
    if comment:
        return comment.end()
    match = _HTML.match(source, start)
    if not match:
        return None
    token = match.group()
    if token.startswith("<![CDATA[") or token.startswith("<!--") or token.startswith("<?") or token.startswith("<!"):
        return match.end()
    return match.end() if _TAG.fullmatch(token) else None


def parse_inline_html_breaks(source: str) -> list[InlineNode]:
    """Split raw HTML and CommonMark hard breaks from source text."""
    result: list[InlineNode] = []
    text: list[str] = []
    def flush() -> None:
        if text:
            result.append(InlineNode("text", "".join(text)))
            text.clear()
    i = 0
    while i < len(source):
        # Code spans take precedence over both HTML recognition and hard
        # breaks. Keep a balanced backtick run in the text token so the inline
        # parser can consume the complete span (including embedded newlines).
        if source[i] == "`":
            run_end = i + 1
            while run_end < len(source) and source[run_end] == "`":
                run_end += 1
            run_length = run_end - i
            search = run_end
            close_end = None
            while search < len(source):
                candidate = source.find("`", search)
                if candidate < 0:
                    break
                end = candidate + 1
                while end < len(source) and source[end] == "`":
                    end += 1
                if end - candidate == run_length:
                    close_end = end
                    break
                search = end
            if close_end is not None:
                text.append(source[i:close_end])
                i = close_end
                continue
        # A backslash escape makes the following punctuation ordinary text.
        escaped = False
        if source[i] == "<":
            backslashes = 0
            j = i - 1
            while j >= 0 and source[j] == "\\":
                backslashes += 1
                j -= 1
            escaped = backslashes % 2 == 1
        if source[i] == "<" and not escaped:
            # A valid autolink owns its complete angle-delimited token before
            # later backticks inside it can begin a code span.
            end = source.find(">", i + 1)
            if end >= 0:
                from .autolinks import parse_autolinks
                candidate = source[i:end + 1]
                if any(node.type == "link" for node in parse_autolinks(candidate)):
                    text.append(candidate)
                    i = end + 1
                    continue
            end = _html_at(source, i)
            if end is not None:
                flush()
                result.append(InlineNode("html", source[i:end]))
                i = end
                continue
        if source[i] == "\\" and i + 1 < len(source) and source[i + 1] in "\r\n":
            flush(); result.append(InlineNode("hardbreak")); i += 2
            if source[i - 1] == "\r" and i < len(source) and source[i] == "\n": i += 1
            continue
        if source[i] in "\r\n":
            end = i
            while end > 0 and source[end - 1] == " ": end -= 1
            if end < i and i - end >= 2:
                while text and text[-1] == " ": text.pop()
                flush(); result.append(InlineNode("hardbreak"))
            else:
                text.append("\n")
            i += 2 if source[i:i + 2] == "\r\n" else 1
            continue
        text.append(source[i]); i += 1
    flush()
    return result
