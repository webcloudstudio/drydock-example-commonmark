# Evidence: Block 23 · Service (block-23)

- block type: block
- date: 2026-10-14
- resulting state: closed/verified
- story points (combined assembled cost): 4956
- execution id: 20261014.083418.725Z-16326237

## Stories built
- Make tab columns work for block structure and verify the remaining corpus sections. (cont-tabs-slice) [story]

## Stacked context
- compass: COMPASS.md (SP 1072)
- implements: FEATURE-Tabs.md (SP 1723)
- context: ARCHITECTURE_compact.md (SP 335)
- stack: common_compact.md (SP 1199)
- stack: python_compact.md (SP 390)

## Build directory changes
- tests/test_tabs.py

## Pre-build acceptance observation
- GREEN (prepassed): tabs-corpus-and-remaining-sections (FEATURE-Tabs.md)
  intent: The Tabs, Link reference definitions, Backslash escapes, Entity and numeric character references, Raw HTML, HTML blocks, Paragraphs, Blank lines and Hard line breaks conformance sections (roughly 160 cases) pass in full.
  return code: 0
  stdout:
    159 passed, 0 failed, 0 errored, 496 skipped
- GREEN (prepassed): tabs-indented-code-and-internal-tabs (FEATURE-Tabs.md)
  intent: A leading tab opens indented code, and internal tabs inside it are kept as tabs.
  return code: 0
  stdout:
    <pre><code>a	a
    </code></pre>
- GREEN (prepassed): tabs-list-continuation (FEATURE-Tabs.md)
  intent: A tab-indented continuation paragraph belongs to the list item.
  return code: 0
  stdout:
    <ul>
    <li>
    <p>foo</p>
    <p>bar</p>
    </li>
    </ul>
- GREEN (prepassed): tabs-after-markers (FEATURE-Tabs.md)
  intent: A tab after a quote marker or list marker is consumed as columns, leaving code inside the container.
  return code: 0
  stdout:
    <blockquote>
    <pre><code>  foo
    </code></pre>
    </blockquote>
    
    <ul>
    <li><pre><code>  foo
    </code></pre>
    </li>
    </ul>
- GREEN (prepassed): tabs-as-separators (FEATURE-Tabs.md)
  intent: Tabs between a heading marker and its text, and between thematic break characters, act as spaces.
  return code: 0
  stdout:
    <h1>Foo</h1>
    
    <hr />

## Post-build programmatic acceptance
- PASS: tabs-corpus-and-remaining-sections (FEATURE-Tabs.md)
  intent: The Tabs, Link reference definitions, Backslash escapes, Entity and numeric character references, Raw HTML, HTML blocks, Paragraphs, Blank lines and Hard line breaks conformance sections (roughly 160 cases) pass in full.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261014.053711/build/commonmark/.venv/bin/python
  provisioning: not required
  return code: 0
  stdout:
    159 passed, 0 failed, 0 errored, 496 skipped
- PASS: tabs-indented-code-and-internal-tabs (FEATURE-Tabs.md)
  intent: A leading tab opens indented code, and internal tabs inside it are kept as tabs.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261014.053711/build/commonmark/.venv/bin/python
  provisioning: not required
  return code: 0
  stdout:
    <pre><code>a	a
    </code></pre>
- PASS: tabs-list-continuation (FEATURE-Tabs.md)
  intent: A tab-indented continuation paragraph belongs to the list item.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261014.053711/build/commonmark/.venv/bin/python
  provisioning: not required
  return code: 0
  stdout:
    <ul>
    <li>
    <p>foo</p>
    <p>bar</p>
    </li>
    </ul>
- PASS: tabs-after-markers (FEATURE-Tabs.md)
  intent: A tab after a quote marker or list marker is consumed as columns, leaving code inside the container.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261014.053711/build/commonmark/.venv/bin/python
  provisioning: not required
  return code: 0
  stdout:
    <blockquote>
    <pre><code>  foo
    </code></pre>
    </blockquote>
    
    <ul>
    <li><pre><code>  foo
    </code></pre>
    </li>
    </ul>
- PASS: tabs-as-separators (FEATURE-Tabs.md)
  intent: Tabs between a heading marker and its text, and between thematic break characters, act as spaces.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261014.053711/build/commonmark/.venv/bin/python
  provisioning: not required
  return code: 0
  stdout:
    <h1>Foo</h1>
    
    <hr />

## Build summary
The column helpers already exist. Let me run the scoped gate to see where things stand before changing anything.The scoped gate already passes (159 passed, 0 failed, 0 errored). Next I'll check the four declared acceptance assertions and the existing project tests.All four declared assertions pass, and the full project suite is green (1142 passed, 1 skipped). Now I'll check whether any existing test covers tab columns, since the spec asks for tests beside the code.Existing tests cover tabs only incidentally, and there is no dedicated tab test file. I'll check the outputs for a set of spec tab cases, then write `tests/test_tabs.py` with exact-output assertions.Every probed output matches the spec examples. I'll write `tests/test_tabs.py`: exact-output tests through the executable, plus direct tests of the column helpers and the partial-tab cursor state.All 31 new tests pass. I'll confirm the only file change is the new test file and that no staged assets were touched.RESULT: SUCCESS

FILES CHANGED:
- tests/test_tabs.py

SUMMARY:
The tab column handling was already in place from earlier blocks: `next_column`, `indent_columns`, the `Cursor` split-tab state (`in_tab` and `rest`), and the block rules that use them. I verified it rather than changing it, and I added the tab test file that was missing.

Declared gate (`Suite: scoped`, the nine-section `--pattern`): **159 passed, 0 failed, 0 errored, 496 skipped**. Exit status 0.

Declared acceptance assertions, all passing:
- tabs-indented-code-and-internal-tabs: pass
- tabs-list-continuation: pass
- tabs-after-markers: pass
- tabs-as-separators: pass

Project tests:
- New `tests/test_tabs.py`: 31 tests, all passing. They cover `next_column`, `indent_columns`, partial-tab `Cursor` state, and exact stdout for indented code, list continuation, quote and bullet markers, and tab separators. Expected outputs were checked against the spec examples.
- Full `pytest -q`: 1142 passed, 1 skipped (the skip is pre-existing in `test_foundation.py`).

I did not run `sources/full_test.sh`. The block's declared invocation is the scoped gate, and the staged suite's unscoped run belongs to a later block.

Choices I made:
- Tests check exact bytes of the whole output, not substrings.
- Helper tests read back returned columns and `rest` text directly.

No staged assets, protected paths, or Git history were touched. `tests/test_tabs.py` is untracked and not committed.
