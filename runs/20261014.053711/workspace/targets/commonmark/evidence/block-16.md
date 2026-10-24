# Evidence: Block 16 · Service (block-16)

- block type: block
- date: 2026-10-14
- resulting state: closed/verified
- story points (combined assembled cost): 4697
- execution id: 20261014.071239.579Z-22987f6e

## Stories built
- Parse indented code blocks. (indented-code) [story]

## Stacked context
- compass: COMPASS.md (SP 1072)
- implements: FEATURE-Indented-Code.md (SP 1540)
- context: ARCHITECTURE_compact.md (SP 335)
- stack: common_compact.md (SP 1199)
- stack: python_compact.md (SP 390)

## Build directory changes
- mdparser/blocks.py
- mdparser/render.py
- tests/test_atx_headings.py
- tests/test_block_engine.py
- tests/test_blocks.py
- tests/test_indented_code.py
- tests/test_thematic_breaks.py

## Pre-build acceptance observation
- RED: indented-simple-block (FEATURE-Indented-Code.md)
  intent: Four-space-indented lines render one pre element whose code keeps the extra indentation and content.
  return code: 1
  stdout:
    <p>a simple
    indented code block</p>
  stderr:
    --- drydock: values at failure ---
      result = CompletedProcess(args=['./commonmark'], returncode=0, stdout='<p>a simple\nindented code block</p>\n', stderr='')
    --- drydock: end values ---
    Traceback (most recent call last):
      File "indented-simple-block.py", line 9, in <module>
        assert result.stdout.count("<pre>") == 1
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    AssertionError
- GREEN (prepassed): indented-cannot-interrupt-paragraph (FEATURE-Indented-Code.md)
  intent: An indented line directly after paragraph text is a continuation, not a code block.
  return code: 0
  stdout:
    <p>Foo
    bar</p>
- RED: indented-chunks-and-ending (FEATURE-Indented-Code.md)
  intent: Chunks separated by a blank line form one block, and an unindented line ends it and starts a paragraph.
  return code: 1
  stdout:
    <p>chunk1</p>
    <p>chunk2
    bar</p>
  stderr:
    --- drydock: values at failure ---
      result = CompletedProcess(args=['./commonmark'], returncode=0, stdout='<p>chunk1</p>\n<p>chunk2\nbar</p>\n', stderr='')
    --- drydock: end values ---
    Traceback (most recent call last):
      File "indented-chunks-and-ending.py", line 6, in <module>
        assert result.stdout.count("<pre>") == 1
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    AssertionError
- RED: indented-content-escaped-and-literal (FEATURE-Indented-Code.md)
  intent: Code content is escaped and not parsed as Markdown, so only the four code wrapper tags contribute angle brackets.
  return code: 1
  stdout:
    <p><a/>
    <em>hi</em></p>
  stderr:
    --- drydock: values at failure ---
      result = CompletedProcess(args=['./commonmark'], returncode=0, stdout='<p><a/>\n<em>hi</em></p>\n', stderr='')
    --- drydock: end values ---
    Traceback (most recent call last):
      File "indented-content-escaped-and-literal.py", line 6, in <module>
        assert result.stdout.count("<") == 4
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    AssertionError
- RED: indented-tab-indentation (FEATURE-Indented-Code.md)
  intent: A leading tab counts as four columns of indentation.
  return code: 1
  stdout:
    <p>foo</p>
  stderr:
    --- drydock: values at failure ---
      result = CompletedProcess(args=['./commonmark'], returncode=0, stdout='<p>foo</p>\n', stderr='')
    --- drydock: end values ---
    Traceback (most recent call last):
      File "indented-tab-indentation.py", line 6, in <module>
        assert result.stdout.count("<pre>") == 1
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    AssertionError

## Post-build programmatic acceptance
- PASS: indented-simple-block (FEATURE-Indented-Code.md)
  intent: Four-space-indented lines render one pre element whose code keeps the extra indentation and content.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261014.053711/build/commonmark/.venv/bin/python
  provisioning: not required
  return code: 0
  stdout:
    <pre><code>a simple
      indented code block
    </code></pre>
- PASS: indented-cannot-interrupt-paragraph (FEATURE-Indented-Code.md)
  intent: An indented line directly after paragraph text is a continuation, not a code block.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261014.053711/build/commonmark/.venv/bin/python
  provisioning: not required
  return code: 0
  stdout:
    <p>Foo
    bar</p>
- PASS: indented-chunks-and-ending (FEATURE-Indented-Code.md)
  intent: Chunks separated by a blank line form one block, and an unindented line ends it and starts a paragraph.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261014.053711/build/commonmark/.venv/bin/python
  provisioning: not required
  return code: 0
  stdout:
    <pre><code>chunk1
    
    chunk2
    </code></pre>
    <p>bar</p>
- PASS: indented-content-escaped-and-literal (FEATURE-Indented-Code.md)
  intent: Code content is escaped and not parsed as Markdown, so only the four code wrapper tags contribute angle brackets.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261014.053711/build/commonmark/.venv/bin/python
  provisioning: not required
  return code: 0
  stdout:
    <pre><code>&lt;a/&gt;
    *hi*
    </code></pre>
- PASS: indented-tab-indentation (FEATURE-Indented-Code.md)
  intent: A leading tab counts as four columns of indentation.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261014.053711/build/commonmark/.venv/bin/python
  provisioning: not required
  return code: 0
  stdout:
    <pre><code>foo
    </code></pre>

## Build summary
Existing code is in place from earlier blocks. Let me read the block engine and related modules before adding the indented code rule.The indented-code rule has to fit the existing per-line procedure. Before writing it, I'll check which existing tests assume four-space lines are paragraphs, since those would change behaviour.The current suite is green (755 passed). Several earlier-block tests assert that four-space lines are paragraphs, which this feature changes by definition. I'll check whether any of them are declared acceptance checks before touching them.The existing thematic-break and ATX tests that expect `    ***` or `\t# foo` to be paragraphs are finer tests, not declared acceptance checks. Under this feature those lines become code blocks, so I'll update those expectations. The declared ATX checks still hold, since `refused` has no `<h1>`.

Now I'll add the block type to the engine.Engine and renderer are wired. Next I'll write the test file, transcribing the four declared checks unchanged and adding finer tests that read back block trees and exact output.Now I'll update the five finer-grained expectations that assumed four-space or tab-indented lines were paragraphs. The declared ATX checks are untouched.Now I'll run the full project suite through its declared command, plus the declared checks' Python-level invocation.Four failures, all from my side of the change. Three are finer tests whose inputs now fall outside the paragraph case. One is a mistake in my own test, so I'll check the registry test before fixing.The registry test lists the start rules explicitly, so it needs the new one. The other two inputs (`  \t  word`, `   \tword`) have 4+ columns of indentation, so they are now correctly code blocks; I'll use space-only indentation to keep the paragraph intent. My own consecutive-block test was wrong: `b` is a paragraph, and `    c` continues it.Re-running the full suite after those fixes.Indented code blocks are implemented, and the project suite is green: 797 passed, 1 skipped. The skip was already there before this change. I did not run `sources/full_test.sh`, because this step's criteria gate only on the declared checks; the corpus examples that use lists belong to the lists story.

I also changed five earlier-block tests whose expectations conflicted with the new rule: four-space or tab-indented lines were asserted to be paragraphs, and two inputs had 4+ columns of indentation. The declared ATX and thematic-break checks are untouched.

**What changed**
- `mdparser/blocks.py`: new `INDENTED_CODE` block type, registered after ATX headings.
  - Start: a non-blank line with 4+ columns of indentation, unless the container is a leaf that takes lines (the paragraph case), so it cannot interrupt a paragraph.
  - Continue: blank lines and 4+ column lines; the first four columns are consumed, and anything beyond is kept.
  - Finalize: trailing blank lines are dropped; content is the remaining lines, each with a line ending.
- `mdparser/render.py`: renders `<pre><code>` with escaped content.
- `tests/test_indented_code.py` (new): the four declared checks transcribed unchanged, plus block-tree and exact-output tests.

**Earlier tests I updated (finer tests, not declared checks)**
- `test_atx_headings.py`: `    # foo` and `\t# foo` now expect `indented_code`.
- `test_thematic_breaks.py`: `    ***` and `\t***` expect `indented_code`; the exact-output test now expects a code block.
- `test_blocks.py`: the registry start-rule list includes `INDENTED_CODE`; the leading-whitespace test uses space-only indentation, because any tab in leading whitespace reaches column 4.
- `test_block_engine.py`: `   \tword` became `  word`, for the same reason.

**Decisions**
- The start rule gates on "container accepts lines" rather than naming the paragraph type, so future leaf types that take lines get the same no-interrupt behaviour.

**Results**
- Declared checks (`test_indented_code.py`, 4 of 4): pass.
- Full `pytest -q`: 797 passed, 1 skipped (pre-existing skip in `test_foundation.py`). It was 755 passed before this change.

RESULT: SUCCESS

FILES CHANGED:
- mdparser/blocks.py
- mdparser/render.py
- tests/test_indented_code.py
- tests/test_atx_headings.py
- tests/test_thematic_breaks.py
- tests/test_blocks.py
- tests/test_block_engine.py

SUMMARY:
Added the indented code block type (start, continue, add-line, finalize) and its HTML rendering. The four declared acceptance checks pass. The full pytest suite is green at 797 passed, 1 skipped (pre-existing). Five earlier finer tests were updated to the new four-column rule; the declared ATX and thematic-break checks are unchanged. The conformance suite was not run, as this step's criteria do not invoke it.

<blueprint-decisions>
[{"spec":"FEATURE-Indented-Code.md","severity":"Low","subject":"Start gate for indented code","decision":"The start rule refuses whenever the container is a leaf that takes lines, rather than checking for the paragraph type by name. This keeps the no-interrupt rule general. Acceptable as is?"}]
</blueprint-decisions>
