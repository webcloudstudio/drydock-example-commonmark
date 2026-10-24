# Evidence: Block 10 · Service (block-10)

- block type: block
- date: 2026-10-14
- resulting state: closed/verified
- story points (combined assembled cost): 5334
- execution id: 20261014.062650.566Z-58173721

## Stories built
- Extract link reference definitions when a paragraph closes and provide label normalization. (link-reference-definitions) [story]

## Stacked context
- compass: COMPASS.md (SP 1072)
- implements: FEATURE-Link-Reference-Definitions.md (SP 1894)
- context: ARCHITECTURE_compact.md (SP 335)
- stack: common_compact.md (SP 1199)
- stack: python_compact.md (SP 390)

## Build directory changes
- mdparser/blocks.py
- mdparser/refs.py
- tests/test_foundation.py
- tests/test_link_reference_definitions.py

## Pre-build acceptance observation
- RED: defs-definition-only-renders-nothing (FEATURE-Link-Reference-Definitions.md)
  intent: A document that is only a definition, with or without a title or angle brackets, renders no paragraph.
  return code: 1
  stdout:
    <p>[foo]: /url &quot;title&quot;</p>
  stderr:
    --- drydock: values at failure ---
      result = CompletedProcess(args=['./commonmark'], returncode=0, stdout='<p>[foo]: /url &quot;title&quot;</p>\n', stderr='')
    --- drydock: end values ---
    Traceback (most recent call last):
      File "defs-definition-only-renders-nothing.py", line 7, in <module>
        assert result.stdout.count("<p>") == 0
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    AssertionError
- GREEN (prepassed): defs-remainder-is-paragraph (FEATURE-Link-Reference-Definitions.md)
  intent: Text after a definition stays as one paragraph.
  return code: 0
  stdout:
    <p>[foo]: /url
    remaining text</p>
- GREEN (prepassed): defs-trailing-text-not-definition (FEATURE-Link-Reference-Definitions.md)
  intent: Extra text after the title means the line is not a definition, so it stays a paragraph.
  return code: 0
  stdout:
    <p>[foo]: /url &quot;title&quot; ok</p>
- GREEN (prepassed): defs-cannot-interrupt-paragraph (FEATURE-Link-Reference-Definitions.md)
  intent: A definition line directly after paragraph text is part of that paragraph.
  return code: 0
  stdout:
    <p>Foo
    [bar]: /baz</p>
- GREEN (prepassed): defs-title-with-blank-line (FEATURE-Link-Reference-Definitions.md)
  intent: A title containing a blank line is not valid, so the two halves become two paragraphs.
  return code: 0
  stdout:
    <p>[foo]: /url 'title</p>
    <p>with blank line'</p>

## Post-build programmatic acceptance
- PASS: defs-definition-only-renders-nothing (FEATURE-Link-Reference-Definitions.md)
  intent: A document that is only a definition, with or without a title or angle brackets, renders no paragraph.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261014.053711/build/commonmark/.venv/bin/python
  provisioning: not required
  return code: 0
- PASS: defs-remainder-is-paragraph (FEATURE-Link-Reference-Definitions.md)
  intent: Text after a definition stays as one paragraph.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261014.053711/build/commonmark/.venv/bin/python
  provisioning: not required
  return code: 0
  stdout:
    <p>remaining text</p>
- PASS: defs-trailing-text-not-definition (FEATURE-Link-Reference-Definitions.md)
  intent: Extra text after the title means the line is not a definition, so it stays a paragraph.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261014.053711/build/commonmark/.venv/bin/python
  provisioning: not required
  return code: 0
  stdout:
    <p>[foo]: /url &quot;title&quot; ok</p>
- PASS: defs-cannot-interrupt-paragraph (FEATURE-Link-Reference-Definitions.md)
  intent: A definition line directly after paragraph text is part of that paragraph.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261014.053711/build/commonmark/.venv/bin/python
  provisioning: not required
  return code: 0
  stdout:
    <p>Foo
    [bar]: /baz</p>
- PASS: defs-title-with-blank-line (FEATURE-Link-Reference-Definitions.md)
  intent: A title containing a blank line is not valid, so the two halves become two paragraphs.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261014.053711/build/commonmark/.venv/bin/python
  provisioning: not required
  return code: 0
  stdout:
    <p>[foo]: /url 'title</p>
    <p>with blank line'</p>

## Build summary
I'll start by inspecting the build directory and the existing sources.The project already has an `mdparser` package from earlier blocks. I'll read the modules this step touches and the existing tests.Next I'll read the existing test conventions and the spec's link reference definitions section, which the feature depends on.The block engine already calls `_paragraph_finalize` when a paragraph closes, so that's the hook point. Before editing, I'll check whether any existing test feeds definition-shaped text or builds blocks outside `DocumentParser`, and confirm the test runner works.Baseline is 459 passing. No existing test uses definition-shaped text, so the change shouldn't disturb them. My plan:

- **`refs.py`**: `normalize_label`, a first-wins `ReferenceMap`, and a scanner that peels leading definitions off a paragraph's text and returns the remainder.
- **`blocks.py`**: the paragraph finalize rule stores the document-wide map on the root and drops a paragraph that is only definitions.
- **Tests**: transcribe the four declared checks, plus unit tests for the grammar edges.

I'll write `refs.py` first.I left a redundant bounds check in `_is_title_opener`, since an empty slice is never a key of `TITLE_CLOSERS`. Removing it:Next, `blocks.py`: give the root a reference map, and have the paragraph finalize rule extract definitions and drop definition-only paragraphs.Now the tests. I'll put the four declared checks in a transcribed-acceptance section (assertions unchanged), then unit tests for the grammar, the map, and the block-tree integration.Reviewing the file before running it, I see two problems. `test_empty_text...` compares `ReferenceMap` objects by identity, so it would always fail. The last test is pointless and imports `refs` only for itself. Fixing both:Now I'll run the new file, then the whole suite to check for regressions.The new tests pass and the executable output is right. The one failure is `test_foundation.py`, which expects `mdparser.refs` to be a reserved, behavior-free stub. That was true at the foundation block and is no longer true by design. I'll read that test before changing it.The file's own comment says the list shrinks as modules gain behavior, and `refs` now has behavior, so the entry comes out. I'll update the comment to match that convention.The suite is green: 523 passed, 1 skipped. The skip is the foundation test's parametrize list, now empty, which pytest reports as a skip. Before writing up, I want to check one spec rule I haven't covered: definitions may have at most three spaces of indentation, and the block engine currently strips paragraph indentation.Definitions indented four or more spaces are currently accepted. The spec says those are indented code, but indented code is a separate story that isn't built yet, so I'm leaving it for that story. The final state is below.

RESULT: SUCCESS

FILES CHANGED:
- mdparser/refs.py
- mdparser/blocks.py
- tests/test_link_reference_definitions.py
- tests/test_foundation.py

SUMMARY:
- **`mdparser/refs.py`** holds the feature. `normalize_label` strips the brackets, applies `casefold()`, and collapses spaces, tabs and line endings. `ReferenceMap` is first-wins and matches on normalized labels. `extract_definitions` peels definitions off the start of a paragraph's text and returns the remainder. It covers the label, angle and plain destination, and title rules from the spec. Destinations and titles go through `unescape_and_decode`.
- **`mdparser/blocks.py`** calls extraction in the paragraph finalize rule. The document-wide map lives on the root `Block`, and a paragraph with only definitions is removed from the tree. The root's `references` attribute is the handle the inline stories will read.
- **Tests**: the four declared checks are transcribed unchanged. I also added unit tests for the grammar, the map, block-tree integration, and exact executable output. Full suite: `.venv/bin/python -m pytest -q` gives 523 passed, 1 skipped. The skip is the foundation test's parametrize list, which is now empty.
- **`tests/test_foundation.py`**: I removed `refs` from `NO_BEHAVIOR_MODULES`. That test asserted `refs` had no public names, which stopped being true with this step. The change follows the file's own convention for modules that gained behavior. This is an edit to an existing test, so please review it.
- I did not run `sources/full_test.sh`. None of this step's criteria invoke the staged suite. Nothing was staged or committed.

Choices I made that you may want to redirect:
- The map sits on the root `Block`, not in a parser-level object, so `finalize` can reach it through the parent chain.
- `normalize_label` accepts a bracketed or unbracketed label, since the spec says it strips brackets.
- Label whitespace collapse uses space, tab, CR and LF, following the feature text, not all Unicode whitespace.
- When a title on a later line has trailing text, the definition keeps its destination and the title text stays in the paragraph. This follows the spec example.

Known gap: a definition indented four or more spaces is accepted today. The spec makes that indented code. The fix belongs with the indented-code story, which needs to record the first line's indent before this check can be correct.

<blueprint-decisions>
[{"spec":"FEATURE-Link-Reference-Definitions.md","severity":"Low","subject":"Reference map location and definition-only paragraph removal","decision":"The reference map is held on the document root Block and filled by the paragraph finalize rule, so containers and the inline stories share one map without changing the finalize signature. A paragraph left empty after extraction is removed from the tree. Acceptable, or should the map move to the parser on replan?"}]
</blueprint-decisions>
