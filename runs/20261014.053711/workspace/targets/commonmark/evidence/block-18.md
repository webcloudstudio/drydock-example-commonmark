# Evidence: Block 18 · Service (block-18)

- block type: block
- date: 2026-10-14
- resulting state: closed/verified
- story points (combined assembled cost): 5202
- execution id: 20261014.073309.155Z-f06ed154

## Stories built
- Parse the seven kinds of HTML block. (html-blocks) [story]

## Stacked context
- compass: COMPASS.md (SP 1072)
- implements: FEATURE-HTML-Blocks.md (SP 2020)
- context: ARCHITECTURE_compact.md (SP 335)
- stack: common_compact.md (SP 1199)
- stack: python_compact.md (SP 390)

## Build directory changes
- mdparser/blocks.py
- mdparser/render.py
- tests/test_blocks.py
- tests/test_html_blocks.py

## Pre-build acceptance observation
- RED: htmlblock-type6-raw-lines (FEATURE-HTML-Blocks.md)
  intent: A block-level tag block passes through verbatim and its Markdown is not parsed.
  return code: 1
  stdout:
    <p><div>
    <em>foo</em>
    </div></p>
  stderr:
    --- drydock: values at failure ---
      block = '<div>\n*foo*\n</div>'
      result = CompletedProcess(args=['./commonmark'], returncode=0, stdout='<p><div>\n<em>foo</em>\n</div></p>\n', stderr='')
    --- drydock: end values ---
    Traceback (most recent call last):
      File "htmlblock-type6-raw-lines.py", line 7, in <module>
        assert block in result.stdout
               ^^^^^^^^^^^^^^^^^^^^^^
    AssertionError
- RED: htmlblock-type6-ends-at-blank-line (FEATURE-HTML-Blocks.md)
  intent: A type 6 block ends at a blank line and Markdown after it is parsed.
  return code: 1
  stdout:
    <p><div>
    raw</p>
    <p><em>bar</em></p>
  stderr:
    --- drydock: values at failure ---
      result = CompletedProcess(args=['./commonmark'], returncode=0, stdout='<p><div>\nraw</p>\n<p><em>bar</em></p>\n', stderr='')
    --- drydock: end values ---
    Traceback (most recent call last):
      File "htmlblock-type6-ends-at-blank-line.py", line 6, in <module>
        assert result.stdout.count("<p>") == 1
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    AssertionError
- RED: htmlblock-comment-spans-blank-lines (FEATURE-HTML-Blocks.md)
  intent: A comment block keeps blank lines until its end marker, and the following line is a paragraph.
  return code: 1
  stdout:
    <p>&lt;!-- Foo</p>
    <p>bar
    baz --&gt;
    okay</p>
  stderr:
    --- drydock: values at failure ---
      comment = '<!-- Foo\n\nbar\n   baz -->'
      result = CompletedProcess(args=['./commonmark'], returncode=0, stdout='<p>&lt;!-- Foo</p>\n<p>bar\nbaz --&gt;\nokay</p>\n', stderr='')
    --- drydock: end values ---
    Traceback (most recent call last):
      File "htmlblock-comment-spans-blank-lines.py", line 7, in <module>
        assert comment in result.stdout
               ^^^^^^^^^^^^^^^^^^^^^^^^
    AssertionError
- RED: htmlblock-pre-spans-blank-lines (FEATURE-HTML-Blocks.md)
  intent: A pre block keeps blank lines and does not parse the Markdown inside it.
  return code: 1
  stdout:
    <p><pre>
    <em>x</em></p>
    <p><em>y</em>
    </pre></p>
  stderr:
    --- drydock: values at failure ---
      block = '<pre>\n*x*\n\n_y_\n</pre>'
      result = CompletedProcess(args=['./commonmark'], returncode=0, stdout='<p><pre>\n<em>x</em></p>\n<p><em>y</em>\n</pre></p>\n', stderr='')
    --- drydock: end values ---
    Traceback (most recent call last):
      File "htmlblock-pre-spans-blank-lines.py", line 7, in <module>
        assert block in result.stdout
               ^^^^^^^^^^^^^^^^^^^^^^
    AssertionError
- GREEN (prepassed): htmlblock-type7-cannot-interrupt (FEATURE-HTML-Blocks.md)
  intent: A lone open tag line after paragraph text stays inside the paragraph.
  return code: 0
  stdout:
    <p>Foo
    <a href="bar">
    baz</p>
- GREEN (prepassed): htmlblock-type6-interrupts-paragraph (FEATURE-HTML-Blocks.md)
  intent: A block-level tag line interrupts a paragraph.
  return code: 0
  stdout:
    <p>Foo
    <div>
    bar
    </div></p>
- GREEN (prepassed): htmlblock-four-space-indent-is-code (FEATURE-HTML-Blocks.md)
  intent: Four spaces of indentation make an indented code block, not an HTML block.
  return code: 0
  stdout:
    <pre><code>&lt;!-- foo --&gt;
    </code></pre>

## Post-build programmatic acceptance
- PASS: htmlblock-type6-raw-lines (FEATURE-HTML-Blocks.md)
  intent: A block-level tag block passes through verbatim and its Markdown is not parsed.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261014.053711/build/commonmark/.venv/bin/python
  provisioning: not required
  return code: 0
  stdout:
    <div>
    *foo*
    </div>
- PASS: htmlblock-type6-ends-at-blank-line (FEATURE-HTML-Blocks.md)
  intent: A type 6 block ends at a blank line and Markdown after it is parsed.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261014.053711/build/commonmark/.venv/bin/python
  provisioning: not required
  return code: 0
  stdout:
    <div>
    raw
    <p><em>bar</em></p>
- PASS: htmlblock-comment-spans-blank-lines (FEATURE-HTML-Blocks.md)
  intent: A comment block keeps blank lines until its end marker, and the following line is a paragraph.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261014.053711/build/commonmark/.venv/bin/python
  provisioning: not required
  return code: 0
  stdout:
    <!-- Foo
    
    bar
       baz -->
    <p>okay</p>
- PASS: htmlblock-pre-spans-blank-lines (FEATURE-HTML-Blocks.md)
  intent: A pre block keeps blank lines and does not parse the Markdown inside it.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261014.053711/build/commonmark/.venv/bin/python
  provisioning: not required
  return code: 0
  stdout:
    <pre>
    *x*
    
    _y_
    </pre>
- PASS: htmlblock-type7-cannot-interrupt (FEATURE-HTML-Blocks.md)
  intent: A lone open tag line after paragraph text stays inside the paragraph.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261014.053711/build/commonmark/.venv/bin/python
  provisioning: not required
  return code: 0
  stdout:
    <p>Foo
    <a href="bar">
    baz</p>
- PASS: htmlblock-type6-interrupts-paragraph (FEATURE-HTML-Blocks.md)
  intent: A block-level tag line interrupts a paragraph.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261014.053711/build/commonmark/.venv/bin/python
  provisioning: not required
  return code: 0
  stdout:
    <p>Foo</p>
    <div>
    bar
    </div>
- PASS: htmlblock-four-space-indent-is-code (FEATURE-HTML-Blocks.md)
  intent: Four spaces of indentation make an indented code block, not an HTML block.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261014.053711/build/commonmark/.venv/bin/python
  provisioning: not required
  return code: 0
  stdout:
    <pre><code>&lt;!-- foo --&gt;
    </code></pre>

## Build summary
I'll start by inspecting the build directory and the existing sources.The earlier blocks are already in place. Next I'll read the block engine, since HTML blocks have to plug into it.The block engine has clean hooks for this: start rules, a continue rule, and an add-line rule, all of which fenced code already uses. Next I'll check the cli, an existing test file for style, and the exact tag-name list in the staged spec.The spec section defines the exact tag list and the type 7 grammar, so I'll read it directly rather than working from memory.The registry test at `tests/test_blocks.py:225` asserts the exact start-rule tuple, so registering a new type will need that expectation updated. I'll also check whether the inline raw-HTML grammar is already defined, so I can reuse it rather than duplicate it.I have what I need for the design. Before editing, I'll record a baseline of the existing test suite so I can tell any regressions I cause from failures that were already there.The baseline run is slow, probably because some tests spawn the conformance runner. I'll wait for it to finish before editing anything, so the edits don't contaminate the baseline.Baseline is 876 passed, 1 skipped. Now I'll implement. First, the block-tree state on `Block`, which mirrors the existing `fence` attribute.Next, the HTML block section itself: the seven start and end conditions, the type 7 paragraph restriction, and the three rules.Two things to fix in what I just wrote: `blocks.py` doesn't import `re` yet, and the type aliases should be defined before the helpers that use them. I'll correct both.Now the renderer. HTML block content is emitted verbatim, with no escaping and no extra newline, because the content already ends in one.The existing registry test pins the exact start-rule tuple, so it needs the new type added. This is a structural expectation, not one of the declared acceptance checks, so I'm updating it to match the registry.Before writing the test file, I'll smoke-test the declared acceptance inputs and a few edge cases directly against the executable.Every smoke result matches the spec behaviour: type 1 ignores blank lines, type 6 stops at a blank line, type 7 can't interrupt a paragraph, and the first-line end conditions produce single-line blocks. Now I'll write the test file, transcribing the seven declared checks unchanged and adding finer block-tree and exact-output tests beside them.Before running anything, I re-derived the expectations by hand and found three mistakes in what I wrote. A type 1 block never closes without `</pre>`, so the blank-line case should yield only `html_block`. A single-line `<!DOCTYPE html>` closes on its own line, so the following `*a*` is a paragraph. And one test name is misleading. I'll correct those before running.Now I'll run the new test file together with the two registry-adjacent files. This doesn't touch the conformance runner.Two failures, and I checked both against the spec. The first is a real bug: type 7 requires trailing spaces and tabs to be allowed after the tag, and my tag regex didn't include them. The second is a wrong test: `<span>é</span>` is not a block start (`span` is not a type 6 name, and text follows the tag), so rendering it as a paragraph is correct. I'll fix the regex and change the test to use a `<div>` line.Now I'll re-run the targeted files. Then I need a regression check across the rest of the project's unit tests. Some existing tests invoke the conformance runner on scoped sections, so I'll first find which files do that, to keep the regression run from triggering them unnecessarily.The targeted files pass (241). For a regression check I'll run the project's full declared test command. The four corpus-invoking files only run scoped sections, not the unscoped conformance run, so they're part of the normal suite, and the baseline already included them. This takes about two and a half minutes, so I'll run it in the background.While that runs, I'll review the diff read-only. I won't edit any source until the run finishes.The diff reads cleanly: the new code mirrors the fenced-code pattern, the type 7 restriction lives in the start rule, and the renderer passes content through untouched. I'll check on the full run.The full project suite passes: 948 passed, 1 skipped, against a baseline of 876 passed, 1 skipped. The 72 new tests are the seven declared checks plus the finer coverage. I'll confirm the set of files I actually changed.HTML block parsing is implemented, and the full project test suite passes. The conformance runner (`sources/spec_tests.py`) was not run, because no acceptance criterion in this step invokes it. The spec gates the corpus examples in the later cont-tabs-slice story.

**What changed**
- `mdparser/blocks.py`: the seven HTML block start and end conditions, the type 6 tag list, and the type 7 complete-tag grammar. Types 1 to 5 close on their end line, and types 6 and 7 close before a blank line. Type 7 is refused while a paragraph is open. Lines are kept raw, with their original indentation.
- `mdparser/render.py`: HTML block content is emitted unchanged, with no escaping.
- `tests/test_html_blocks.py` (new): the seven declared checks, transcribed with their assertions unchanged, plus about 65 finer tests on start and end conditions, paragraph interruption, single-line blocks, raw indentation, and exact stdout.
- `tests/test_blocks.py`: the registry test pins the exact start-rule tuple, so I added `HTML_BLOCK` to it. That is a structural expectation, not a declared check.

**Verification**
- Baseline before my edits: 876 passed, 1 skipped.
- After my edits: 948 passed, 1 skipped. All seven declared checks pass.

**Choices I made**
- For types 1 to 5, the end test runs against the whole line, including the start. So `<!-->` closes on its own line, following the spec's literal "line contains `-->`".
- Type 7 is blocked from starting inside a paragraph by checking whether the container accepts lines, the same way the indented-code rule does.

RESULT: SUCCESS

FILES CHANGED:
- mdparser/blocks.py
- mdparser/render.py
- tests/test_blocks.py
- tests/test_html_blocks.py

SUMMARY:
Implemented the seven HTML block types in the block engine as a new `html_block` leaf type, registered after fenced code. Type 7 cannot interrupt a paragraph. Rendering emits the raw lines unchanged. Added `tests/test_html_blocks.py` with the seven declared checks transcribed unchanged and finer block-tree and exact-output tests. Updated the registry expectation in `tests/test_blocks.py`. Full project pytest: 948 passed, 1 skipped (baseline 876 passed, 1 skipped). Conformance runner not invoked in this step.

<blueprint-decisions>
[{"spec":"FEATURE-HTML-Blocks.md","severity":"Low","subject":"End-condition check on the start line for types 1 to 5","decision":"The end test runs on the whole start line, so `<!-->` closes immediately because it literally contains `-->`. The spec wording 'line contains' supports this. Acceptable, or should the search begin after the opening marker?"}]
</blueprint-decisions>
