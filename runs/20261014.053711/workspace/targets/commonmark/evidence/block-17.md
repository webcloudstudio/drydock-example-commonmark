# Evidence: Block 17 · Service (block-17)

- block type: block
- date: 2026-10-14
- resulting state: closed/verified
- story points (combined assembled cost): 5275
- execution id: 20261014.072230.899Z-217d5e6f

## Stories built
- Parse fenced code blocks with info strings. (fenced-code) [story]

## Stacked context
- compass: COMPASS.md (SP 1072)
- implements: FEATURE-Fenced-Code.md (SP 2010)
- context: ARCHITECTURE_compact.md (SP 335)
- stack: common_compact.md (SP 1199)
- stack: python_compact.md (SP 390)

## Build directory changes
- mdparser/blocks.py
- mdparser/cli.py
- mdparser/render.py
- tests/test_blocks.py
- tests/test_fenced_code.py

## Pre-build acceptance observation
- RED: fenced-backtick-and-tilde (FEATURE-Fenced-Code.md)
  intent: Backtick and tilde fences each render one pre element containing the supplied body.
  return code: 1
  stdout:
    <p><code>some body text</code></p>
  stderr:
    --- drydock: values at failure ---
      result = CompletedProcess(args=['./commonmark'], returncode=0, stdout='<p><code>some body text</code></p>\n', stderr='')
    --- drydock: end values ---
    Traceback (most recent call last):
      File "fenced-backtick-and-tilde.py", line 9, in <module>
        assert result.stdout.count("<pre>") == 1
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    AssertionError
- RED: fenced-info-string-language-class (FEATURE-Fenced-Code.md)
  intent: The first word of the info string becomes the language class.
  return code: 1
  stdout:
    <p><code>ruby extra words code </code></p>
  stderr:
    --- drydock: values at failure ---
      result = CompletedProcess(args=['./commonmark'], returncode=0, stdout='<p><code>ruby extra words code </code></p>\n', stderr='')
      language = 'ruby'
    --- drydock: end values ---
    Traceback (most recent call last):
      File "fenced-info-string-language-class.py", line 8, in <module>
        assert ('class="language-' + language + '"') in result.stdout
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    AssertionError
- RED: fenced-closing-fence-rules (FEATURE-Fenced-Code.md)
  intent: A fence of the other character, or a shorter fence, does not close the block.
  return code: 1
  stdout:
    <p>````
    aaa
    ~~~
    ```</p>
  stderr:
    --- drydock: values at failure ---
      result = CompletedProcess(args=['./commonmark'], returncode=0, stdout='<p>````\naaa\n~~~\n```</p>\n', stderr='')
    --- drydock: end values ---
    Traceback (most recent call last):
      File "fenced-closing-fence-rules.py", line 9, in <module>
        assert result.stdout.count("<pre>") == 1
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    AssertionError
- RED: fenced-unclosed-runs-to-end (FEATURE-Fenced-Code.md)
  intent: An unclosed fence consumes the rest of the document as code.
  return code: 1
  stdout:
    <p>```
    first</p>
    <p>still code</p>
  stderr:
    --- drydock: values at failure ---
      result = CompletedProcess(args=['./commonmark'], returncode=0, stdout='<p>```\nfirst</p>\n<p>still code</p>\n', stderr='')
    --- drydock: end values ---
    Traceback (most recent call last):
      File "fenced-unclosed-runs-to-end.py", line 7, in <module>
        assert result.stdout.count("<pre>") == 1
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    AssertionError
- RED: fenced-interrupts-paragraph (FEATURE-Fenced-Code.md)
  intent: A fence interrupts a paragraph and text after it starts a new paragraph.
  return code: 1
  stdout:
    <p>foo
    <code>bar</code>
    baz</p>
  stderr:
    --- drydock: values at failure ---
      result = CompletedProcess(args=['./commonmark'], returncode=0, stdout='<p>foo\n<code>bar</code>\nbaz</p>\n', stderr='')
    --- drydock: end values ---
    Traceback (most recent call last):
      File "fenced-interrupts-paragraph.py", line 6, in <module>
        assert result.stdout.count("<pre>") == 1
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    AssertionError
- GREEN (prepassed): fenced-two-backticks-not-a-fence (FEATURE-Fenced-Code.md)
  intent: Two backticks do not open a fence; they form a code span instead.
  return code: 0
  stdout:
    <p><code>foo</code></p>
- RED: fenced-indentation-stripped (FEATURE-Fenced-Code.md)
  intent: Content indentation up to the fence indentation is removed, and unindented lines are kept.
  return code: 1
  stdout:
    <p><code>aaa aaa</code></p>
  stderr:
    --- drydock: values at failure ---
      result = CompletedProcess(args=['./commonmark'], returncode=0, stdout='<p><code>aaa aaa</code></p>\n', stderr='')
    --- drydock: end values ---
    Traceback (most recent call last):
      File "fenced-indentation-stripped.py", line 6, in <module>
        assert result.stdout.count("<pre>") == 1
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    AssertionError

## Post-build programmatic acceptance
- PASS: fenced-backtick-and-tilde (FEATURE-Fenced-Code.md)
  intent: Backtick and tilde fences each render one pre element containing the supplied body.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261014.053711/build/commonmark/.venv/bin/python
  provisioning: not required
  return code: 0
  stdout:
    <pre><code>some body text
    </code></pre>
    
    <pre><code>some body text
    </code></pre>
- PASS: fenced-info-string-language-class (FEATURE-Fenced-Code.md)
  intent: The first word of the info string becomes the language class.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261014.053711/build/commonmark/.venv/bin/python
  provisioning: not required
  return code: 0
  stdout:
    <pre><code class="language-ruby">code
    </code></pre>
- PASS: fenced-closing-fence-rules (FEATURE-Fenced-Code.md)
  intent: A fence of the other character, or a shorter fence, does not close the block.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261014.053711/build/commonmark/.venv/bin/python
  provisioning: not required
  return code: 0
  stdout:
    <pre><code>aaa
    ~~~
    ```
    </code></pre>
- PASS: fenced-unclosed-runs-to-end (FEATURE-Fenced-Code.md)
  intent: An unclosed fence consumes the rest of the document as code.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261014.053711/build/commonmark/.venv/bin/python
  provisioning: not required
  return code: 0
  stdout:
    <pre><code>first
    
    still code
    </code></pre>
- PASS: fenced-interrupts-paragraph (FEATURE-Fenced-Code.md)
  intent: A fence interrupts a paragraph and text after it starts a new paragraph.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261014.053711/build/commonmark/.venv/bin/python
  provisioning: not required
  return code: 0
  stdout:
    <p>foo</p>
    <pre><code>bar
    </code></pre>
    <p>baz</p>
- PASS: fenced-two-backticks-not-a-fence (FEATURE-Fenced-Code.md)
  intent: Two backticks do not open a fence; they form a code span instead.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261014.053711/build/commonmark/.venv/bin/python
  provisioning: not required
  return code: 0
  stdout:
    <p><code>foo</code></p>
- PASS: fenced-indentation-stripped (FEATURE-Fenced-Code.md)
  intent: Content indentation up to the fence indentation is removed, and unindented lines are kept.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261014.053711/build/commonmark/.venv/bin/python
  provisioning: not required
  return code: 0
  stdout:
    <pre><code>aaa
    aaa
    </code></pre>

## Build summary
Baseline is green (797 passed, 1 skipped). The indented-code work already gives me the pattern: a block type with start, continue, add-line, and finalize rules. I'll add fenced code the same way, then update the one registry test that pins the default start-rule list.Now the renderer, and the registry test that pins the default start-rule tuple.Before writing tests, a quick smoke run over the declared inputs and some spec-style cases.Most cases match the spec, but the unclosed-fence outputs have an extra trailing blank line. The cause is `cli.split_lines`: input ending in `\n` yields a final empty "line", which the fence correctly treats as content. Let me check what depends on that split before changing it.An existing test pins `split_lines("a\n") == ["a", ""]`, so I won't change `split_lines`. The final newline terminates the last line rather than starting a new one, so I'll drop that one trailing entry in `render_lines`, the document-level entry point, which leaves the pinned helper alone.Now the test file. The seven declared checks are transcribed with their assertions unchanged, following the indented-code file's pattern. The rest act on the block tree and on exact stdout.I left a broken assertion in the indentation test (an `or True` line that makes it meaningless). Fixing that, plus a few awkward test names and a missing return annotation.Now the new file and the full suite together, since the registry change could affect other tests.Four failures, all in my test expectations rather than the implementation:

1. An indented `" ```"` line followed by an unindented `code` line correctly closes the indented block, so the test needed the content indented too. A single line is the right input.
2. `parse_lines` takes lines with the document's terminator already removed, so `["```", "a", ""]` is the right input for "a\n\n" content. The `render_lines` drop is what handles the terminator.RESULT: SUCCESS

FILES CHANGED:
- mdparser/blocks.py
- mdparser/render.py
- mdparser/cli.py
- tests/test_blocks.py
- tests/test_fenced_code.py

SUMMARY:
Fenced code blocks are implemented as a new block type, `FENCED_CODE`, registered after indented code. It follows the same start, continue, add-line, and finalize pattern as the existing types.

- **Opening fence:** a run of three or more backticks or tildes, indented up to three columns. A backtick fence whose info string contains a backtick is not a fence. A fence can interrupt a paragraph.
- **Info string:** decoded with the shared `unescape_and_decode`, then the first word becomes `class="language-WORD"`, HTML-escaped.
- **Content:** up to the opening fence's indentation is stripped from each line. Content is escaped and never parsed as Markdown.
- **Closing fence:** same character, at least as long, up to three columns of indentation, followed only by spaces or tabs. It closes the block and adds no content.
- **Unclosed:** runs to the end of the document.

Changes outside the fence code, each needed for correctness:
- `cli.render_lines` drops the one empty entry left by a final newline. Without this, an unclosed fence gained a stray blank line. I left `split_lines` alone because an existing test pins its trailing-empty behaviour.
- `tests/test_blocks.py`: the registry test that pins the default start-rule tuple now includes `FENCED_CODE`.

Tests:
- The seven declared checks are transcribed with their assertions unchanged, in `tests/test_fenced_code.py`. All seven pass.
- 72 further tests cover the start rule, language extraction, content stripping, closing-fence rules, and exact stdout.
- Full `pytest -q` is 876 passed, 1 skipped. The skip predates this step.

I did not run `sources/full_test.sh` or `spec_tests.py`. No declared criterion invokes the staged suite, and this step's corpus examples are gated in the lists story.

Nothing was committed.

<blueprint-decisions>
[{"spec":"FEATURE-Fenced-Code.md","severity":"Material","subject":"Dropping the final empty line in render_lines","decision":"split_lines is pinned by an existing test to return a trailing empty entry for input ending in a newline. Changing it would break that test. I dropped the one trailing empty entry in cli.render_lines instead, so an unclosed fence does not gain a blank line. Is that acceptable, or should the line model move into blocks.parse_lines on replan?"}]
</blueprint-decisions>
