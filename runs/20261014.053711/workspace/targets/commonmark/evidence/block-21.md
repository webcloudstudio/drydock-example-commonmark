# Evidence: Block 21 · Service (block-21)

- block type: block
- date: 2026-10-14
- resulting state: closed/verified
- story points (combined assembled cost): 5525
- execution id: 20261014.080449.725Z-6c39d976

## Stories built
- Parse list items: markers, indentation rules, empty items, start numbers and laziness. (list-items) [story]

## Stacked context
- compass: COMPASS.md (SP 1072)
- implements: FEATURE-List-Items.md (SP 2291)
- context: ARCHITECTURE_compact.md (SP 335)
- stack: common_compact.md (SP 1199)
- stack: python_compact.md (SP 390)

## Build directory changes
- mdparser/blocks.py
- mdparser/render.py
- tests/test_blocks.py
- tests/test_list_items.py

## Pre-build acceptance observation
- RED: items-bullet-items (FEATURE-List-Items.md)
  intent: Each bullet marker line starts one li element, and consecutive items of one marker form one ul.
  return code: 1
  stdout:
    <p>- first
    - second
    - third</p>
  stderr:
    --- drydock: values at failure ---
      items = ['first', 'second', 'third']
      result = CompletedProcess(args=['./commonmark'], returncode=0, stdout='<p>- first\n- second\n- third</p>\n', stderr='')
    --- drydock: end values ---
    Traceback (most recent call last):
      File "items-bullet-items.py", line 8, in <module>
        assert result.stdout.count("<li>") == len(items)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    AssertionError
- RED: items-ordered-start-number (FEATURE-List-Items.md)
  intent: An ordered list takes its start number from the first item, and ten digits is not a marker.
  return code: 1
  stdout:
    <p>123456789. ok</p>
    
    <p>1234567890. not ok</p>
  stderr:
    --- drydock: values at failure ---
      good = CompletedProcess(args=['./commonmark'], returncode=0, stdout='<p>123456789. ok</p>\n', stderr='')
      number = 123456789
    --- drydock: end values ---
    Traceback (most recent call last):
      File "items-ordered-start-number.py", line 10, in <module>
        assert ('start="' + str(number) + '"') in good.stdout
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    AssertionError
- RED: items-continuation-paragraph (FEATURE-List-Items.md)
  intent: A continuation paragraph indented to the content column joins the item, giving a loose item with two paragraphs.
  return code: 1
  stdout:
    <p>- one</p>
    <p>two</p>
  stderr:
    --- drydock: values at failure ---
      result = CompletedProcess(args=['./commonmark'], returncode=0, stdout='<p>- one</p>\n<p>two</p>\n', stderr='')
    --- drydock: end values ---
    Traceback (most recent call last):
      File "items-continuation-paragraph.py", line 6, in <module>
        assert result.stdout.count("<li>") == 1
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    AssertionError
- RED: items-insufficient-indent-ends-item (FEATURE-List-Items.md)
  intent: A paragraph indented less than the content column is outside the item.
  return code: 1
  stdout:
    <p>- one</p>
    <p>two</p>
  stderr:
    --- drydock: values at failure ---
      result = CompletedProcess(args=['./commonmark'], returncode=0, stdout='<p>- one</p>\n<p>two</p>\n', stderr='')
    --- drydock: end values ---
    Traceback (most recent call last):
      File "items-insufficient-indent-ends-item.py", line 6, in <module>
        assert result.stdout.count("<li>") == 1
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    AssertionError
- RED: items-empty-items (FEATURE-List-Items.md)
  intent: Empty items are allowed in the middle of a list, but an empty item cannot interrupt a paragraph.
  return code: 1
  stdout:
    <h2>- foo</h2>
    <p>- bar</p>
    
    <p>foo
    *</p>
  stderr:
    --- drydock: values at failure ---
      middle = CompletedProcess(args=['./commonmark'], returncode=0, stdout='<h2>- foo</h2>\n<p>- bar</p>\n', stderr='')
    --- drydock: end values ---
    Traceback (most recent call last):
      File "items-empty-items.py", line 9, in <module>
        assert middle.stdout.count("<li>") == 2 + 1
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    AssertionError
- RED: items-nested-and-code (FEATURE-List-Items.md)
  intent: A sublist indented to the content column nests, and a code block six spaces in is code inside the item.
  return code: 1
  stdout:
    <p>- foo
    - bar</p>
    
    <p>- foo</p>
    <pre><code>  bar
    </code></pre>
  stderr:
    --- drydock: values at failure ---
      nested = CompletedProcess(args=['./commonmark'], returncode=0, stdout='<p>- foo\n- bar</p>\n', stderr='')
    --- drydock: end values ---
    Traceback (most recent call last):
      File "items-nested-and-code.py", line 9, in <module>
        assert nested.stdout.count("<ul>") == 2
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    AssertionError
- GREEN (prepassed): items-four-spaces-is-code (FEATURE-List-Items.md)
  intent: A marker indented four spaces is code, not a list item.
  return code: 0
  stdout:
    <pre><code>1.  A paragraph
    </code></pre>

## Post-build programmatic acceptance
- PASS: items-bullet-items (FEATURE-List-Items.md)
  intent: Each bullet marker line starts one li element, and consecutive items of one marker form one ul.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261014.053711/build/commonmark/.venv/bin/python
  provisioning: not required
  return code: 0
  stdout:
    <ul>
    <li>first</li>
    <li>second</li>
    <li>third</li>
    </ul>
- PASS: items-ordered-start-number (FEATURE-List-Items.md)
  intent: An ordered list takes its start number from the first item, and ten digits is not a marker.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261014.053711/build/commonmark/.venv/bin/python
  provisioning: not required
  return code: 0
  stdout:
    <ol start="123456789">
    <li>ok</li>
    </ol>
    
    <p>1234567890. not ok</p>
- PASS: items-continuation-paragraph (FEATURE-List-Items.md)
  intent: A continuation paragraph indented to the content column joins the item, giving a loose item with two paragraphs.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261014.053711/build/commonmark/.venv/bin/python
  provisioning: not required
  return code: 0
  stdout:
    <ul>
    <li>
    <p>one</p>
    <p>two</p>
    </li>
    </ul>
- PASS: items-insufficient-indent-ends-item (FEATURE-List-Items.md)
  intent: A paragraph indented less than the content column is outside the item.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261014.053711/build/commonmark/.venv/bin/python
  provisioning: not required
  return code: 0
  stdout:
    <ul>
    <li>one</li>
    </ul>
    <p>two</p>
- PASS: items-empty-items (FEATURE-List-Items.md)
  intent: Empty items are allowed in the middle of a list, but an empty item cannot interrupt a paragraph.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261014.053711/build/commonmark/.venv/bin/python
  provisioning: not required
  return code: 0
  stdout:
    <ul>
    <li>foo</li>
    <li></li>
    <li>bar</li>
    </ul>
    
    <p>foo
    *</p>
- PASS: items-nested-and-code (FEATURE-List-Items.md)
  intent: A sublist indented to the content column nests, and a code block six spaces in is code inside the item.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261014.053711/build/commonmark/.venv/bin/python
  provisioning: not required
  return code: 0
  stdout:
    <ul>
    <li>foo
    <ul>
    <li>bar</li>
    </ul>
    </li>
    </ul>
    
    <ul>
    <li>
    <p>foo</p>
    <pre><code>bar
    </code></pre>
    </li>
    </ul>
- PASS: items-four-spaces-is-code (FEATURE-List-Items.md)
  intent: A marker indented four spaces is code, not a list item.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261014.053711/build/commonmark/.venv/bin/python
  provisioning: not required
  return code: 0
  stdout:
    <pre><code>1.  A paragraph
    </code></pre>

## Build summary
The build directory already has a container-based engine (block quotes, fences, setext). I'll add list items as a container block, group runs of items into lists at render time, and track blank-line state for tight/loose rendering. Starting with the block engine.Now the registration and the per-line blank tracking in the engine.Now the renderer: group runs of items into lists, and render tight items without `<p>`.Quick smoke run against the declared inputs and a few spec-shaped cases before writing tests:Every declared input and edge case renders as the spec expects. Now the registry assertion in the existing block tests needs the new start rule, so I'll look at it before editing.Now the test file: the seven declared checks transcribed unchanged, then block-tree and exact-output tests.Two fixes before running: I left redundant inner `import subprocess` lines in the transcribed checks, and one test expects two blank lines to end an item with content. The spec only limits blank lines at the *start* of an item, so that expectation is wrong. Fixing both.Both failures are in my test helper usage, not the parser: `paragraph_texts` walks a block's children, so passing a paragraph itself returns nothing. Reading the paragraph's content directly is the correct check.Now the full non-suite test run. Several existing test files invoke `spec_tests.py` with section patterns; per the step contract I won't run those, so I'll find exactly which test functions do and deselect them.1103 passed, 1 skipped (the skip is pre-existing in `test_foundation.py`), and the 4 deselected tests are the staged-suite invocations I held back. Checking the working tree for stray files:RESULT: SUCCESS

FILES CHANGED:
- mdparser/blocks.py
- mdparser/render.py
- tests/test_blocks.py
- tests/test_list_items.py

SUMMARY:
List items are parsed as a container block (`LIST_ITEM`) and rendered as `<ul>`/`<ol>` with `<li>` children. All seven declared checks (`items-*`) pass, and their assertions are unchanged in `tests/test_list_items.py`.

- **Markers:** `-`, `+`, `*`, and 1–9 digit ordered markers with `.` or `)`. A marker must end the line or be followed by a space or tab. Up to three columns of indentation are allowed.
- **Content column:** marker width plus 1–4 spaces. Five or more spaces make the content an indented code block, and a blank start uses marker width plus 1. The column is stored as an absolute column, so nested items work.
- **Continuation:** lines must reach the content column. Blank lines continue an item with content, but a blank line after an empty item ends it.
- **Interruption:** an empty item or a non-1 ordered item cannot interrupt a paragraph. Thematic break is registered first, so `* * *` is never an item.
- **Laziness:** handled by the existing engine's lazy paragraph rule.
- **Start numbers:** `<ol start="N">` is emitted only when N ≠ 1.
- **Tight/loose:** the engine records whether each block ended with a blank line, following the reference algorithm. Tight items render without `<p>`.

Decisions beyond the feature's stated scope:
- The spec's Purpose says grouping and tight/loose rendering belong to the lists story. The declared checks require `<ul>` counts and `<p>` counts, so I implemented grouping (runs of items with the same marker kind and delimiter) and tightness at render time. The lists story can extend this rather than redo it.
- An existing registry test in `tests/test_blocks.py` asserted the exact start-rule tuple. I added `LIST_ITEM` to it, as the setext step did.

Verification:
- `.venv/bin/python -m pytest -q` with the four staged-suite invocations deselected: 1103 passed, 1 skipped. The skip is pre-existing in `test_foundation.py`.
- Deselected, not run: `test_autolinks_corpus_section_passes_in_full`, `test_codespans_corpus_sections_pass_in_full`, `test_images_corpus_sections`, `test_breaks_corpus_sections`. These call `spec_tests.py` with section patterns from earlier steps. I did not run them because this step's criteria don't invoke the staged suite. Lists can appear in those sections, so their gates should be checked in the step that owns them.
- I did not run `sources/full_test.sh` or `spec_tests.py`.
- Nothing was committed or staged.

<blueprint-decisions>
[{"spec":"FEATURE-List-Items.md","severity":"Material","subject":"List grouping and tight/loose rendering implemented in this step","decision":"The spec's Purpose assigns grouping items into lists and tight/loose rendering to the lists story. The declared acceptance checks require one <ul> for consecutive same-marker items, an <ol start> attribute, and <p> counts that depend on tightness, so I implemented a minimal version at render time: runs of items sharing a marker kind and delimiter form one list, and a list is loose when a blank line separates items or blocks inside an item (commonmark.js algorithm). Is that acceptable, or should this move to the lists story on replan?"},{"spec":"FEATURE-List-Items.md","severity":"Low","subject":"Interruption decided by the matched container, not the lazy-paragraph flag","decision":"A list item's interruption rules (no empty start, ordered start must be 1) apply when the matched container is a paragraph, not when the line is merely a lazy continuation. This matches the reference algorithm, so '> foo' followed by '- bar' at top level yields a list. Acceptable?"}]
</blueprint-decisions>
