# Evidence: Block 9 · Service (block-9)

- block type: block
- date: 2026-10-14
- resulting state: closed/verified
- story points (combined assembled cost): 5421
- execution id: 20261014.061842.732Z-41490866

## Stories built
- Implement the delimiter stack, flanking rules, and the process-emphasis algorithm. (emphasis) [story]

## Stacked context
- compass: COMPASS.md (SP 1072)
- implements: FEATURE-Emphasis.md (SP 2139)
- context: ARCHITECTURE_compact.md (SP 335)
- stack: common_compact.md (SP 1199)
- stack: python_compact.md (SP 390)

## Build directory changes
- mdparser/inlines.py
- tests/test_emphasis.py

## Pre-build acceptance observation
- RED: emphasis-star-and-underscore (FEATURE-Emphasis.md)
  intent: Single star and single underscore wrap supplied words in one em element each.
  return code: 1
  stdout:
    <p>*wordy*</p>
  stderr:
    --- drydock: values at failure ---
      result = CompletedProcess(args=['./commonmark'], returncode=0, stdout='<p>*wordy*</p>\n', stderr='')
    --- drydock: end values ---
    Traceback (most recent call last):
      File "emphasis-star-and-underscore.py", line 8, in <module>
        assert result.stdout.count("<em>") == 1
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    AssertionError
- RED: emphasis-strong (FEATURE-Emphasis.md)
  intent: Doubled delimiters produce one strong element.
  return code: 1
  stdout:
    <p>**wordy**</p>
  stderr:
    --- drydock: values at failure ---
      result = CompletedProcess(args=['./commonmark'], returncode=0, stdout='<p>**wordy**</p>\n', stderr='')
    --- drydock: end values ---
    Traceback (most recent call last):
      File "emphasis-strong.py", line 8, in <module>
        assert result.stdout.count("<strong>") == 1
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    AssertionError
- RED: emphasis-intraword-rules (FEATURE-Emphasis.md)
  intent: Intraword emphasis works with star but not with underscore.
  return code: 1
  stdout:
    <p>foo*bar*baz</p>
    
    <p>foo_bar_baz</p>
  stderr:
    --- drydock: values at failure ---
      star = CompletedProcess(args=['./commonmark'], returncode=0, stdout='<p>foo*bar*baz</p>\n', stderr='')
    --- drydock: end values ---
    Traceback (most recent call last):
      File "emphasis-intraword-rules.py", line 9, in <module>
        assert star.stdout.count("<em>") == 1
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    AssertionError
- GREEN (prepassed): emphasis-flanking-whitespace (FEATURE-Emphasis.md)
  intent: A delimiter run followed or preceded by whitespace does not form emphasis.
  return code: 0
  stdout:
    <p>a * foo bar*</p>
    <p>foo bar *</p>
- RED: emphasis-nesting (FEATURE-Emphasis.md)
  intent: Triple delimiters give one em containing one strong, and nested forms keep both elements.
  return code: 1
  stdout:
    <p>***word***</p>
    
    <p>*a **b** c*</p>
  stderr:
    --- drydock: values at failure ---
      triple = CompletedProcess(args=['./commonmark'], returncode=0, stdout='<p>***word***</p>\n', stderr='')
    --- drydock: end values ---
    Traceback (most recent call last):
      File "emphasis-nesting.py", line 9, in <module>
        assert triple.stdout.count("<em>") == 1
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    AssertionError
- GREEN (prepassed): emphasis-code-span-binds-tighter (FEATURE-Emphasis.md)
  intent: A star inside a code span cannot close emphasis.
  return code: 0
  stdout:
    <p>*foo<code>*</code></p>

## Post-build programmatic acceptance
- PASS: emphasis-star-and-underscore (FEATURE-Emphasis.md)
  intent: Single star and single underscore wrap supplied words in one em element each.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261014.053711/build/commonmark/.venv/bin/python
  provisioning: not required
  return code: 0
  stdout:
    <p><em>wordy</em></p>
    
    <p><em>wordy</em></p>
- PASS: emphasis-strong (FEATURE-Emphasis.md)
  intent: Doubled delimiters produce one strong element.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261014.053711/build/commonmark/.venv/bin/python
  provisioning: not required
  return code: 0
  stdout:
    <p><strong>wordy</strong></p>
    
    <p><strong>wordy</strong></p>
- PASS: emphasis-intraword-rules (FEATURE-Emphasis.md)
  intent: Intraword emphasis works with star but not with underscore.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261014.053711/build/commonmark/.venv/bin/python
  provisioning: not required
  return code: 0
  stdout:
    <p>foo<em>bar</em>baz</p>
    
    <p>foo_bar_baz</p>
- PASS: emphasis-flanking-whitespace (FEATURE-Emphasis.md)
  intent: A delimiter run followed or preceded by whitespace does not form emphasis.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261014.053711/build/commonmark/.venv/bin/python
  provisioning: not required
  return code: 0
  stdout:
    <p>a * foo bar*</p>
    <p>foo bar *</p>
- PASS: emphasis-nesting (FEATURE-Emphasis.md)
  intent: Triple delimiters give one em containing one strong, and nested forms keep both elements.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261014.053711/build/commonmark/.venv/bin/python
  provisioning: not required
  return code: 0
  stdout:
    <p><em><strong>word</strong></em></p>
    
    <p><em>a <strong>b</strong> c</em></p>
- PASS: emphasis-code-span-binds-tighter (FEATURE-Emphasis.md)
  intent: A star inside a code span cannot close emphasis.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261014.053711/build/commonmark/.venv/bin/python
  provisioning: not required
  return code: 0
  stdout:
    <p>*foo<code>*</code></p>

## Build summary
The build directory already has an `mdparser` package, a `tests` directory, and a `commonmark` launcher from earlier blocks. I'll read those before changing anything.The inline parser is already in place with code spans, autolinks, raw HTML, and entities. Emphasis needs a delimiter stack wired into that scanner. Next I'll read the call sites and test conventions.The existing `parse_inline` returns strings directly, so emphasis needs a node list it can wrap after the scan. Before I change it, I'll check which tests depend on the current inline functions.Existing tests only exercise inline text without a matched pair of delimiters, so they should stay green. I'll rewrite `inlines.py` so the scan builds nodes, then add the delimiter stack and the Appendix process-emphasis procedure on top.Next, the scanner: switch `parse_inline` to build nodes and hand delimiter runs to the stack.The scanner and stack are in place. I'll run a few inputs through the executable and the existing suite before writing new tests.Every spec example I tried matches the expected CommonMark output, and the existing 419 tests still pass. Next I'll write `tests/test_emphasis.py`: the declared acceptance checks transcribed as written, plus exact-output tests beside them.Before running the new file, I'll drop the unused `project_root` fixture from the pure-inline tests and check line lengths against the repo's 100-column style.The implementation is right and my expected value was wrong. The inner `*b*` pairs with the nearest opener, then the final `*` pairs with the outer opener, giving nested em. I'll correct that test and fix the lines over 100 columns.The edit script stopped before writing because the function signature had already lost its fixture argument. Nothing was saved, so I'll rerun it with the correct text.The same assertion fired again, so the file's signature doesn't match what I assumed. I'll check the actual line.The regex-based trim missed this one. I'll make the fix with exact edits instead.Both files show as changed on disk; that's from my own scripted edits, and the suite passes at 459. I'll confirm the current content, then finish the cleanup: remove the remaining unused `project_root` parameters and shorten line 229.The emphasis file is clean at 40 passing tests. I'll run the full suite once more and check which files changed.RESULT: SUCCESS

FILES CHANGED:
- mdparser/inlines.py
- tests/test_emphasis.py

SUMMARY:
- `parse_inline` now builds a node list instead of joining strings. Code spans, autolinks, raw HTML, escapes and entities are `Html` nodes. Each `*` or `_` run is a `Text` node pushed on a `DelimiterStack`, with `can_open`/`can_close` set from the flanking rules.
- Flanking uses `unicodedata`: Unicode whitespace is tab, LF, FF, CR or Zs, and the line edges count as whitespace. Punctuation is categories P* and S*. `*` and `_` have their own open/close rules.
- `DelimiterStack.process_emphasis(stack_bottom=None)` follows the Appendix algorithm. It uses a doubly linked stack with a bottom sentinel, `openers_bottom` per character, closer length mod 3 and closer-can-open, the multiple-of-3 rule, and strong versus em selection. Unmatched runs stay as escaped literal text. Wrapping moves the nodes between a matched pair into an `Element`.
- Tests: `tests/test_emphasis.py` (40 tests). The six declared acceptance checks are transcribed with their assertions unchanged. The rest check exact output for single and double delimiters, triple and nested runs, flanking, the rule of 3, unmatched and empty runs, and code-span interaction.
- Results: `python3 -m pytest -q` gives 459 passed, 0 failed. That is the existing 419 plus 40 new.
- I did not run `sh sources/full_test.sh`. The corpus section for Emphasis needs links, so the spec gates it in the images story.

Choices I made that you may want to redirect:
- `openers_bottom` is keyed by the closer's original length mod 3, not the current length. The spec says "length"; the rule of 3 depends on original lengths.
- The stack operates on a sibling node list passed in at construction. Links will need one stack per bracket level, which the links story can add.

<blueprint-decisions>
[{"spec":"FEATURE-Emphasis.md","severity":"Low","subject":"openers_bottom key uses original delimiter length mod 3","decision":"The spec says closer length mod 3. I keyed openers_bottom on the closer's original length, because the multiple-of-3 rule is defined on original lengths and a current-length key could skip a valid opener. Is that acceptable, or should it read the spec literally?"}]
</blueprint-decisions>

BLOCKERS:
- None.
