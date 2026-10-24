# Evidence: Block 15 · Service (block-15)

- block type: block
- date: 2026-10-14
- resulting state: closed/verified
- story points (combined assembled cost): 4955
- execution id: 20261014.070515.046Z-5a98a58e

## Stories built
- Parse ATX headings. (atx-headings) [story]

## Stacked context
- compass: COMPASS.md (SP 1072)
- implements: FEATURE-ATX-Headings.md (SP 1713)
- context: ARCHITECTURE_compact.md (SP 335)
- stack: common_compact.md (SP 1199)
- stack: python_compact.md (SP 390)

## Build directory changes
- mdparser/blocks.py
- mdparser/render.py
- tests/test_atx_headings.py
- tests/test_blocks.py

## Pre-build acceptance observation
- RED: atx-levels-one-to-six (FEATURE-ATX-Headings.md)
  intent: Each opening-sequence length from 1 to 6 renders exactly one heading of that level.
  return code: 1
  stdout:
    <p># foo</p>
  stderr:
    --- drydock: values at failure ---
      result = CompletedProcess(args=['./commonmark'], returncode=0, stdout='<p># foo</p>\n', stderr='')
      level = 1
    --- drydock: end values ---
    Traceback (most recent call last):
      File "atx-levels-one-to-six.py", line 8, in <module>
        assert result.stdout.count("<h" + str(level) + ">") == 1
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    AssertionError
- GREEN (prepassed): atx-not-a-heading (FEATURE-ATX-Headings.md)
  intent: Seven hashes, a missing space, and an escaped hash do not produce headings.
  return code: 0
  stdout:
    <p>####### foo</p>
    <p>#hashtag</p>
    <p>## foo</p>
- RED: atx-closing-sequence (FEATURE-ATX-Headings.md)
  intent: A closing hash sequence is removed from the heading content.
  return code: 1
  stdout:
    <p>## foo ##</p>
  stderr:
    --- drydock: values at failure ---
      result = CompletedProcess(args=['./commonmark'], returncode=0, stdout='<p>## foo ##</p>\n', stderr='')
    --- drydock: end values ---
    Traceback (most recent call last):
      File "atx-closing-sequence.py", line 6, in <module>
        assert result.stdout.count("<h2>") == 1
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    AssertionError
- RED: atx-empty-heading (FEATURE-ATX-Headings.md)
  intent: Empty headings are allowed, one per line.
  return code: 1
  stdout:
    <p>#</p>
    <p>##</p>
  stderr:
    --- drydock: values at failure ---
      result = CompletedProcess(args=['./commonmark'], returncode=0, stdout='<p>#</p>\n<p>##</p>\n', stderr='')
    --- drydock: end values ---
    Traceback (most recent call last):
      File "atx-empty-heading.py", line 6, in <module>
        assert result.stdout.count("<h1>") == 1
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    AssertionError
- RED: atx-interrupts-paragraph (FEATURE-ATX-Headings.md)
  intent: A heading splits a paragraph without blank lines, leaving two paragraphs around it.
  return code: 1
  stdout:
    <p>Foo bar
    # baz
    Bar foo</p>
  stderr:
    --- drydock: values at failure ---
      result = CompletedProcess(args=['./commonmark'], returncode=0, stdout='<p>Foo bar\n# baz\nBar foo</p>\n', stderr='')
    --- drydock: end values ---
    Traceback (most recent call last):
      File "atx-interrupts-paragraph.py", line 6, in <module>
        assert result.stdout.count("<h1>") == 1
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    AssertionError
- RED: atx-indentation-limit (FEATURE-ATX-Headings.md)
  intent: Up to three spaces of indentation are allowed before the opening sequence, and four are not.
  return code: 1
  stdout:
    <p># foo</p>
    
    <p># foo</p>
  stderr:
    --- drydock: values at failure ---
      allowed = CompletedProcess(args=['./commonmark'], returncode=0, stdout='<p># foo</p>\n', stderr='')
    --- drydock: end values ---
    Traceback (most recent call last):
      File "atx-indentation-limit.py", line 9, in <module>
        assert allowed.stdout.count("<h1>") == 1
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    AssertionError

## Post-build programmatic acceptance
- PASS: atx-levels-one-to-six (FEATURE-ATX-Headings.md)
  intent: Each opening-sequence length from 1 to 6 renders exactly one heading of that level.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261014.053711/build/commonmark/.venv/bin/python
  provisioning: not required
  return code: 0
  stdout:
    <h1>foo</h1>
    
    <h2>foo</h2>
    
    <h3>foo</h3>
    
    <h4>foo</h4>
    
    <h5>foo</h5>
    
    <h6>foo</h6>
- PASS: atx-not-a-heading (FEATURE-ATX-Headings.md)
  intent: Seven hashes, a missing space, and an escaped hash do not produce headings.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261014.053711/build/commonmark/.venv/bin/python
  provisioning: not required
  return code: 0
  stdout:
    <p>####### foo</p>
    <p>#hashtag</p>
    <p>## foo</p>
- PASS: atx-closing-sequence (FEATURE-ATX-Headings.md)
  intent: A closing hash sequence is removed from the heading content.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261014.053711/build/commonmark/.venv/bin/python
  provisioning: not required
  return code: 0
  stdout:
    <h2>foo</h2>
- PASS: atx-empty-heading (FEATURE-ATX-Headings.md)
  intent: Empty headings are allowed, one per line.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261014.053711/build/commonmark/.venv/bin/python
  provisioning: not required
  return code: 0
  stdout:
    <h1></h1>
    <h2></h2>
- PASS: atx-interrupts-paragraph (FEATURE-ATX-Headings.md)
  intent: A heading splits a paragraph without blank lines, leaving two paragraphs around it.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261014.053711/build/commonmark/.venv/bin/python
  provisioning: not required
  return code: 0
  stdout:
    <p>Foo bar</p>
    <h1>baz</h1>
    <p>Bar foo</p>
- PASS: atx-indentation-limit (FEATURE-ATX-Headings.md)
  intent: Up to three spaces of indentation are allowed before the opening sequence, and four are not.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261014.053711/build/commonmark/.venv/bin/python
  provisioning: not required
  return code: 0
  stdout:
    <h1>foo</h1>
    
    <p># foo</p>

## Agent self-report (advisory)
The build agent declared a failure. This is advisory only; the programmatic acceptance above is the authority for this block's outcome.
- summary: Scoped ATX gate fails on Example 69, which needs the indented-code story that is not in this block.
- detail:
    The gate `spec_tests.py --pattern '^ATX headings$'` ran 18 examples: 17 pass and Example 69 (`    # foo`) fails. That example expects `<pre><code># foo</code></pre>`, which requires indented code blocks, a separate story not present in this build. The ATX implementation and all declared acceptance checks pass, and the full pytest suite passes (755 passed, 1 skipped). To clear the gate, land the indented-code story (or include it in the next block) and rerun the same scoped command. No example-specific workaround was added.

## Build summary
I'll start by inspecting the build directory and the staged sources.The project already has an `mdparser` package and tests from earlier blocks. I'll read those and the staged runner before changing anything.The thematic-break block is the pattern to follow: a registered start rule, a `BlockType`, and a renderer branch. Before designing the heading block I'll check the inline parser's signature, the rest of the thematic-break test file, and whether any existing test depends on heading behavior.The thematic-break commit changed a registry test (`test_default_registry_start_rules_are_the_thematic_break`), so adding a second start rule will affect it too. I'll run the current test suite for a baseline and check the two existing heading-adjacent tests.Baseline is 687 passed, 1 skipped. I have what I need, so here is the plan:

- **`mdparser/blocks.py`**: add an `ATX_HEADING` block type with a start rule that handles the opening run, the 1–6 limit, the space/tab/EOL rule, and content stripping. A separate helper removes the closing sequence, and the rule is registered after thematic breaks. `Block` gets a `level` field.
- **`mdparser/render.py`**: render `<hN>` with the content passed through the inline hook.
- **Tests**: a new `tests/test_atx_headings.py` that transcribes the six declared checks unchanged, plus finer tests. I'll also update the one registry test that pins the old start-rule list.

Starting with the block engine:Now the test file. The six declared checks are transcribed with their assertions unchanged. The finer tests cover each level, the boundaries, closing sequences, inline content, and interaction with paragraphs.I'll run the new heading tests and the block-engine and renderer tests first, since they cover the changed code most directly.The focused tests pass. Next is the declared gate for this step: the scoped spec run with `--pattern '^ATX headings$'`, using the same `PYTHONPATH` setup as `full_test.sh`. I'm not running the unscoped suite, since that belongs to a later step.The scoped gate runs 18 examples in the ATX section: 17 pass and 1 fails. The failure is Example 69 (`    # foo`), which expects an indented code block. Indented code is a separate story that hasn't landed, and the build instructions say this example depends on it. I won't implement it here or special-case the example. Next, the full project test suite, to confirm nothing else regressed.The ATX heading story is implemented, but the declared scoped gate does not pass: 17 of 18 examples pass, and Example 69 fails because it needs the indented-code story.

**What changed**
- `mdparser/blocks.py`: new `ATX_HEADING` block type with a start rule. It accepts 1–6 `#` after up to three spaces of indentation, requires a space, tab, or end of line after the run, and strips surrounding whitespace. A separate helper removes a closing sequence only when it is preceded by whitespace or is the whole content, so `foo#` and `foo \#` keep their hashes. `Block` gets a `level` field, and the rule is registered after thematic breaks.
- `mdparser/render.py`: renders `<hN>` with the content passed through the inline parser.
- `tests/test_blocks.py`: one registry test updated to expect both start rules, since it pinned the old list.
- `tests/test_atx_headings.py` (new): the six declared checks, transcribed with assertions unchanged, plus block-tree and exact-output tests.

**Verification**
- Full project suite: 755 passed, 1 skipped. The skip was already there before this change. The baseline was 687 passed.
- Scoped spec gate (`--pattern '^ATX headings$'`): 17 passed, 1 failed, 637 skipped. I did not run `full_test.sh`, since it belongs to a later step.

**Blocker**
- Example 69 (`    # foo`) expects `<pre><code># foo</code></pre>`, an indented code block. Nothing in this step can produce that, and the build instructions say the example depends on the indented-code story. I did not implement indented code or special-case the example. It should pass once that story lands.

**Choices I made**
- The heading level lives on `Block.level`, and content is stored at start time, with inline parsing deferred to render.

No git add or commit was run; the changes are in the working tree.

RESULT: FAILED

FILES CHANGED:
- mdparser/blocks.py
- mdparser/render.py
- tests/test_blocks.py
- tests/test_atx_headings.py

SUMMARY:
Added the ATX heading block (start rule, closing-sequence stripping, level, registration) and its HTML rendering with inline content. The six declared acceptance checks pass, and the full pytest suite is green at 755 passed, 1 skipped. The scoped spec gate `--pattern '^ATX headings$'` returns 17 passed, 1 failed, 637 skipped.

BLOCKERS:
- Spec Example 69 (`    # foo`) expects an indented code block. It needs the indented-code story, which is not in this block.

<blueprint-decisions>
[{"spec":"FEATURE-ATX-Headings.md","severity":"Low","subject":"Closing-sequence detection","decision":"The closing run is removed only when it is the whole heading content or follows a space or tab. Backslash-escaped and attached hashes (foo#, foo \\#) are kept, as the spec's guardrail requires. Options were a regex or a character scan; I chose the character scan to match the existing cursor-based start rules."}]
</blueprint-decisions>

FAILURE_SUMMARY: Scoped ATX gate fails on Example 69, which needs the indented-code story that is not in this block.
FAILURE_DETAIL: The gate `spec_tests.py --pattern '^ATX headings$'` ran 18 examples: 17 pass and Example 69 (`    # foo`) fails. That example expects `<pre><code># foo</code></pre>`, which requires indented code blocks, a separate story not present in this build. The ATX implementation and all declared acceptance checks pass, and the full pytest suite passes (755 passed, 1 skipped). To clear the gate, land the indented-code story (or include it in the next block) and rerun the same scoped command. No example-specific workaround was added.
