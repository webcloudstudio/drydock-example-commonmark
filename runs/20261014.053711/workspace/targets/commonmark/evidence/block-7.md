# Evidence: Block 7 · Service (block-7)

- block type: block
- date: 2026-10-14
- resulting state: closed/verified
- story points (combined assembled cost): 4425
- execution id: 20261014.061208.498Z-b93a5c10

## Stories built
- Implement backslash escapes in text, destinations, titles and info strings. (backslash-escapes) [story]

## Stacked context
- compass: COMPASS.md (SP 1072)
- implements: FEATURE-Backslash-Escapes.md (SP 1218)
- context: ARCHITECTURE_compact.md (SP 335)
- stack: common_compact.md (SP 1199)
- stack: python_compact.md (SP 390)

## Build directory changes
- mdparser/entities.py
- mdparser/inlines.py
- tests/test_backslash_escapes.py
- tests/test_foundation.py

## Pre-build acceptance observation
- GREEN (prepassed): escapes-punctuation-inert (FEATURE-Backslash-Escapes.md)
  intent: An escaped asterisk prevents emphasis.
  return code: 0
  stdout:
    <p>*not emphasized*</p>
- GREEN (prepassed): escapes-non-punctuation-literal (FEATURE-Backslash-Escapes.md)
  intent: A backslash before a non-punctuation character is kept as a literal backslash.
  return code: 0
  stdout:
    <p>\A\a\3</p>
- GREEN (prepassed): escapes-block-markers (FEATURE-Backslash-Escapes.md)
  intent: An escaped heading marker does not start a heading.
  return code: 0
  stdout:
    <p># word</p>
- GREEN (prepassed): escapes-inert-in-code-span (FEATURE-Backslash-Escapes.md)
  intent: A backslash in a code span is not an escape.
  return code: 0
  stdout:
    <p><code>\*</code></p>

## Post-build programmatic acceptance
- PASS: escapes-punctuation-inert (FEATURE-Backslash-Escapes.md)
  intent: An escaped asterisk prevents emphasis.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261014.053711/build/commonmark/.venv/bin/python
  provisioning: not required
  return code: 0
  stdout:
    <p>*not emphasized*</p>
- PASS: escapes-non-punctuation-literal (FEATURE-Backslash-Escapes.md)
  intent: A backslash before a non-punctuation character is kept as a literal backslash.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261014.053711/build/commonmark/.venv/bin/python
  provisioning: not required
  return code: 0
  stdout:
    <p>\A\a\3</p>
- PASS: escapes-block-markers (FEATURE-Backslash-Escapes.md)
  intent: An escaped heading marker does not start a heading.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261014.053711/build/commonmark/.venv/bin/python
  provisioning: not required
  return code: 0
  stdout:
    <p># word</p>
- PASS: escapes-inert-in-code-span (FEATURE-Backslash-Escapes.md)
  intent: A backslash in a code span is not an escape.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261014.053711/build/commonmark/.venv/bin/python
  provisioning: not required
  return code: 0
  stdout:
    <p><code>\*</code></p>

## Build summary
I'll start by inspecting the build directory and the existing state of the project.The inline scanner already has a backslash branch from the code-spans step. Next I'll check what exists for `unescape`, whether the current suite is green, and how the earlier tests are organised.The suite is green at 291 passed. Before changing anything, I'll check how the four declared acceptance checks behave on the current code, and whether anything else already imports `ASCII_PUNCTUATION`.The inline escape behaviour already matches the spec for all the declared cases. What's missing is the shared `unescape` helper that `entities.py` is supposed to provide for destinations, titles and info strings. I'll put the punctuation set in `entities.py` as the single definition, add `unescape` there, and have `inlines.py` import the set rather than define its own copy.Now the tests. I'll transcribe the four declared acceptance checks as they're written, then add coverage for every punctuation character, the non-punctuation case, the helper's boundaries, and the idempotence-style edge cases.I wrote two sloppy expectations in that file: the punctuation parametrisation builds its expected value with a convoluted chain of `replace` calls, and the quote test slices a string literal. I'll replace both with explicit values.Now I'll run the new file, then the full project suite.The failure is a foundation guard that was written to hold `entities` behaviour-free until this step. Its own comment says a module leaves that list when it gains behaviour, which is what this step does. I'll update the list to match and say so in the summary, rather than leave the suite red.Backslash escapes are in place. The four declared acceptance checks pass, and the full project suite is green at 358 passed.

**What was already there:** the inline scanner from the code-spans step already handled `\` before ASCII punctuation in paragraph text. I checked it against every declared case and it was already correct, so I left its behaviour alone.

**What I added:**
- `mdparser/entities.py`: the single `ASCII_PUNCTUATION` set, and a shared `unescape()` helper for backslash escapes only. It leaves entities undecoded and keeps any backslash that is not followed by punctuation.
- `mdparser/inlines.py`: now imports `ASCII_PUNCTUATION` from `entities` instead of defining its own copy.
- `tests/test_backslash_escapes.py`: the four declared acceptance checks, transcribed as written. Also covers all 32 punctuation characters, constructs that stay inert when escaped, a doubled backslash, a trailing lone backslash, and the `unescape` boundaries and idempotence.
- `tests/test_foundation.py`: `entities` is removed from the "no behaviour yet" list. That list's own comment says a module leaves it when it gains behaviour, and this step gives `entities` a public helper. I changed the guard rather than deleting it; the other modules on the list are still checked.

**Choices you may want to redirect:**
- `unescape` has no caller yet. Link destinations, titles and info strings are built in later stories, which will call it. Until then it is covered only by its own tests.
- Hard breaks for a trailing backslash are left to the line-breaks story, as the spec says. A trailing backslash currently renders as a literal backslash.

I did not run `sources/full_test.sh` or `spec_tests.py`. None of this step's acceptance checks invoke the staged suite, and the build notes place the backslash-escape corpus section under a later story's gate.

RESULT: SUCCESS

FILES CHANGED:
- mdparser/entities.py
- mdparser/inlines.py
- tests/test_backslash_escapes.py
- tests/test_foundation.py

SUMMARY:
Implemented backslash escapes per FEATURE-Backslash-Escapes.md. The inline escape rule in `inlines.py` already met the spec, so the build adds the shared `unescape` helper in `entities.py` (with `ASCII_PUNCTUATION` moved there as the single definition), plus tests for the four declared acceptance checks and the escape and helper boundaries. The project suite is green at 358 passed (`.venv/bin/python -m pytest -q`). The foundation guard that held `entities` behaviour-free was updated to match. The staged conformance suite was not run because no criterion in this step invokes it.

<blueprint-decisions>
[{"spec":"FEATURE-Backslash-Escapes.md","severity":"Low","subject":"Location of the shared unescape helper and punctuation set","decision":"Placed ASCII_PUNCTUATION and unescape() in mdparser/entities.py, which the ARCHITECTURE assigns backslash unescape to, and made inlines.py import the set rather than keep its own copy. unescape() has no caller until the link and info-string stories are built. Is that acceptable, or should it live elsewhere on replan?"}]
</blueprint-decisions>

RESULT: SUCCESS

FILES CHANGED:
- mdparser/entities.py
- mdparser/inlines.py
- tests/test_backslash_escapes.py
- tests/test_foundation.py

SUMMARY:
Implemented backslash escapes per FEATURE-Backslash-Escapes.md. The inline escape rule in `inlines.py` already met the spec, so this step adds the shared `unescape` helper in `entities.py` (with `ASCII_PUNCTUATION` moved there as the single definition), plus tests for the four declared acceptance checks and the escape and helper boundaries. Project suite: 358 passed (`.venv/bin/python -m pytest -q`). The staged conformance suite was not run because no criterion in this step invokes it.
