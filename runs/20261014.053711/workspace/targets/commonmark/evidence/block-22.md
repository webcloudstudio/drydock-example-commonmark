# Evidence: Block 22 · Service (block-22)

- block type: block
- date: 2026-10-14
- resulting state: closed/verified
- story points (combined assembled cost): 5462
- execution id: 20261014.081755.926Z-878f99f4

## Stories built
- Group list items into lists and compute tight or loose rendering. (lists) [story]

## Stacked context
- compass: COMPASS.md (SP 1072)
- implements: FEATURE-Lists.md (SP 2150)
- context: ARCHITECTURE_compact.md (SP 335)
- stack: common_compact.md (SP 1199)
- stack: python_compact.md (SP 390)

## Build directory changes
- mdparser/blocks.py
- mdparser/render.py
- tests/test_lists.py

## Pre-build acceptance observation
- RED: lists-corpus-sections (FEATURE-Lists.md)
  intent: The Lists, List items, Block quotes, Thematic breaks, ATX headings, Setext headings, Indented code blocks, Fenced code blocks and Precedence conformance sections (roughly 300 cases) pass in full.
  return code: 1
  stdout:
    Example 261 (lines 4273-4288) List items
       > > 1.  one
    >>
    >>     two
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1,2 @@
    -<blockquote><blockquote><ol><li><p>one</p><p>two</p></li></ol></blockquote></blockquote>
    +<blockquote><blockquote><ol><li>one</li></ol><pre><code>two
    +</code></pre></blockquote></blockquote>
    
    Example 262 (lines 4300-4313) List items
    >>- one
    >>
      >  > two
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<blockquote><blockquote><ul><li>one</li></ul><p>two</p></blockquote></blockquote>
    +<blockquote><blockquote><ul><li><p>one</p><p>two</p></li></ul></blockquote></blockquote>
    
    203 passed, 2 failed, 0 errored, 450 skipped
  stderr:
    --- drydock: progress ---
    cases: pass=203 fail=2 error=0 skip=450 total=655 from=result.stdout
    --- drydock: end progress ---
    --- drydock: values at failure ---
      result = CompletedProcess(args=['/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261014.053711/build/commonmark/.venv/bin/python', 'sources/spec_tests.py', '--program', '/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261014.053711/build/commonmark/commonmark', '--spec', 'sources/spec.txt', '--pattern', '^Lists$|^List items$|^Block quotes$|^Thematic breaks$|^ATX headings$|^Setext headin… (+764 chars)
    --- drydock: end values ---
    Traceback (most recent call last):
      File "lists-corpus-sections.py", line 22, in <module>
        assert result.returncode == 0
               ^^^^^^^^^^^^^^^^^^^^^^
    AssertionError
- GREEN (prepassed): lists-changing-marker-starts-new-list (FEATURE-Lists.md)
  intent: Changing the bullet character or ordered delimiter starts a new list.
  return code: 0
  stdout:
    <ul>
    <li>foo</li>
    <li>bar</li>
    </ul>
    <ul>
    <li>baz</li>
    </ul>
    
    <ol>
    <li>foo</li>
    <li>bar</li>
    </ol>
    <ol start="3">
    <li>baz</li>
    </ol>
- GREEN (prepassed): lists-tight-versus-loose (FEATURE-Lists.md)
  intent: Items without blank lines are tight, and a blank line between items makes the list loose.
  return code: 0
  stdout:
    <ul>
    <li>a</li>
    <li>b</li>
    </ul>
    
    <ul>
    <li>
    <p>a</p>
    </li>
    <li>
    <p>b</p>
    </li>
    </ul>
- GREEN (prepassed): lists-blank-inside-item-makes-loose (FEATURE-Lists.md)
  intent: A blank line between two paragraphs of one item makes the whole list loose.
  return code: 0
  stdout:
    <ul>
    <li>
    <p>a</p>
    </li>
    <li>
    <p>b</p>
    <p>c</p>
    </li>
    <li>
    <p>d</p>
    </li>
    </ul>
- GREEN (prepassed): lists-blank-in-code-stays-tight (FEATURE-Lists.md)
  intent: Blank lines inside a fenced code block do not make a list loose.
  return code: 0
  stdout:
    <ul>
    <li>a</li>
    <li><pre><code>b
    
    
    </code></pre>
    </li>
    <li>c</li>
    </ul>
- GREEN (prepassed): lists-interrupt-paragraph (FEATURE-Lists.md)
  intent: A bullet list interrupts a paragraph, and an ordered list does so only when it starts at one.
  return code: 0
  stdout:
    <p>Foo</p>
    <ul>
    <li>bar</li>
    <li>baz</li>
    </ul>
    
    <p>Intro</p>
    <ol>
    <li>item</li>
    </ol>
    
    <p>Intro
    14. item</p>

## Post-build programmatic acceptance
- PASS: lists-corpus-sections (FEATURE-Lists.md)
  intent: The Lists, List items, Block quotes, Thematic breaks, ATX headings, Setext headings, Indented code blocks, Fenced code blocks and Precedence conformance sections (roughly 300 cases) pass in full.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261014.053711/build/commonmark/.venv/bin/python
  provisioning: not required
  return code: 0
  stdout:
    205 passed, 0 failed, 0 errored, 450 skipped
- PASS: lists-changing-marker-starts-new-list (FEATURE-Lists.md)
  intent: Changing the bullet character or ordered delimiter starts a new list.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261014.053711/build/commonmark/.venv/bin/python
  provisioning: not required
  return code: 0
  stdout:
    <ul>
    <li>foo</li>
    <li>bar</li>
    </ul>
    <ul>
    <li>baz</li>
    </ul>
    
    <ol>
    <li>foo</li>
    <li>bar</li>
    </ol>
    <ol start="3">
    <li>baz</li>
    </ol>
- PASS: lists-tight-versus-loose (FEATURE-Lists.md)
  intent: Items without blank lines are tight, and a blank line between items makes the list loose.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261014.053711/build/commonmark/.venv/bin/python
  provisioning: not required
  return code: 0
  stdout:
    <ul>
    <li>a</li>
    <li>b</li>
    </ul>
    
    <ul>
    <li>
    <p>a</p>
    </li>
    <li>
    <p>b</p>
    </li>
    </ul>
- PASS: lists-blank-inside-item-makes-loose (FEATURE-Lists.md)
  intent: A blank line between two paragraphs of one item makes the whole list loose.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261014.053711/build/commonmark/.venv/bin/python
  provisioning: not required
  return code: 0
  stdout:
    <ul>
    <li>
    <p>a</p>
    </li>
    <li>
    <p>b</p>
    <p>c</p>
    </li>
    <li>
    <p>d</p>
    </li>
    </ul>
- PASS: lists-blank-in-code-stays-tight (FEATURE-Lists.md)
  intent: Blank lines inside a fenced code block do not make a list loose.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261014.053711/build/commonmark/.venv/bin/python
  provisioning: not required
  return code: 0
  stdout:
    <ul>
    <li>a</li>
    <li><pre><code>b
    
    
    </code></pre>
    </li>
    <li>c</li>
    </ul>
- PASS: lists-interrupt-paragraph (FEATURE-Lists.md)
  intent: A bullet list interrupts a paragraph, and an ordered list does so only when it starts at one.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261014.053711/build/commonmark/.venv/bin/python
  provisioning: not required
  return code: 0
  stdout:
    <p>Foo</p>
    <ul>
    <li>bar</li>
    <li>baz</li>
    </ul>
    
    <p>Intro</p>
    <ol>
    <li>item</li>
    </ol>
    
    <p>Intro
    14. item</p>

## Build summary
The two failing examples (261, 262) come from one bug. `_list_item_continues` compares an absolute content column against a cursor that already sits past the enclosing blockquote markers, so a continuation line in a blockquote can be judged against the wrong column. The fix is to store the item's padding relative to its container, which is what the spec's container-relative rule requires. I'll keep `content_column` as is, since existing tests assert it.Now I'll rerun the scoped conformance pattern from the acceptance criterion, unfiltered within that scope.The scoped conformance pattern now passes: 205 passed, 0 failed. Next I'll check the declared acceptance behaviors and a few edge cases the spec examples may not cover (looseness isolation for nested lists, blockquotes, and marker changes).The shell's `printf` read the leading `-` as an option. I'll rerun those probes with `--`.Most cases match the spec. One is wrong: `- a\n  - b\n\n  - c\n- d` renders the outer list loose, but the blank line sits between the nested items `b` and `c`, so the outer list should stay tight. The cause is that `_list_is_loose` treats a nested list's items as separate direct child blocks of the outer item. I'll make the child check skip gaps between consecutive items of the same nested list.`_same_list` asserts that its first argument is a list item, so a paragraph followed by a list item would trip that assert. I'll guard the call.Nested-list looseness now follows the spec: the outer list stays tight when the only blank line is between nested items, and loose when a blank separates blocks of the same item. I'll check the link-reference-definition rule before writing tests.The link-reference-definition case renders loose. I'm leaving that as is: the blank line sits between item `a`'s paragraph and the next item, and that matches the reference rule that blank lines between items count. It has no spec example, so I won't pin it in a test. The other rules are covered, so next I'll collect observed outputs for the test cases.All observed outputs match the spec semantics. Now I'll write `tests/test_lists.py`: the five declared checks transcribed with their assertions unchanged, plus behavior tests for grouping, start numbers, looseness, and the two fixes made here.Before running the file I want to tighten a few tests: replace the `__import__` hack with a normal `os` import, use exact-output assertions where I've observed the output, and drop the repeat-render test, which isn't a declared idempotence property. I'll get the outputs first.Now I'll run the new test file along with the existing list and block-quote tests, since the parser change touches both.The one failure is in my expected value, not the parser. The input `>- one\n>\n  > two` has only one level of blockquote markers, so `two` belongs directly in the outer blockquote and no inner blockquote should appear. The spec's example 262 uses `>>` for the nested case. I'll correct the expectation to the single-level structure.The full project suite is green. Since I changed `render.py` after the last scoped run, I'll rerun the declared scoped conformance invocation once more.The list behavior is complete and the declared scoped conformance gate passes. Lists already existed from block 21, but two spec examples failed, and I fixed a looseness bug the examples didn't catch.

Two fixes:

- **Continuation columns inside blockquotes** (spec examples 261 and 262). A list item measured its continuation column from the absolute column of its marker. On a later line the cursor sits past the enclosing blockquote markers, so the check was wrong and could go negative. `ListItem` now also stores `padding`, the offset from the container's content column, and the continuation check uses it. `content_column` is unchanged, since existing tests assert it.
- **Nested list gaps made the outer list loose** (not covered by the spec examples). In `- a\n  - b\n\n  - c\n- d`, the blank line between nested items `b` and `c` made the outer list loose. `_list_is_loose` now skips gaps between consecutive items of the same nested list.

Tests: I added `tests/test_lists.py` with the five declared checks transcribed unchanged, plus exact-output tests for grouping, start numbers, tight/loose rendering, and the two fixes above.

Results:
- Declared scoped conformance (the `lists-corpus-sections` pattern): 205 passed, 0 failed, 0 errored, 450 skipped (was 203 passed, 2 failed before the fix).
- Full project pytest: 1142 passed, 1 skipped (`test_foundation.py:38`, a pre-existing empty parameter set).
- I did not run `sources/full_test.sh`, since this step's criteria don't invoke it.

Choices I made:
- **Link reference definition after a blank line.** In `- a\n\n  [a]: /u\n- c`, the list renders loose. The blank line sits between item `a` and the next item, and the spec's definition-doesn't-count rule covers only blocks between blocks. I left it loose because the reference behavior treats it that way; no spec example pins it, so I didn't add a test.

I did not stage or commit anything.

<blueprint-decisions>
[{"spec":"FEATURE-Lists.md","severity":"Low","subject":"Looseness when a link reference definition follows a blank line inside an item","decision":"In '- a\\n\\n  [a]: /u\\n- c' the list renders loose, because the blank line between item a's paragraph and the next item is kept as an item separator even though the definition itself is not a block. Making it tight would also be defensible under the 'definitions do not count as blocks' rule. No spec example covers this, so I kept the behavior that matches the reference implementation and did not pin it in a test. Is that acceptable?"}]
</blueprint-decisions>

RESULT: SUCCESS

FILES CHANGED:
- mdparser/blocks.py
- mdparser/render.py
- tests/test_lists.py

SUMMARY:
- blocks.py: `ListItem` gains `padding` (continuation offset measured from the enclosing container's content column). `_list_item_continues` uses it, so continuation lines inside blockquotes are judged correctly. `content_column` is unchanged.
- render.py: `_list_is_loose` ignores blank-line gaps between consecutive items of the same nested list, so a nested list's own looseness doesn't leak into the outer list.
- tests/test_lists.py: the five declared checks, transcribed with assertions unchanged, plus exact-output tests for grouping, start numbers, tight/loose rendering, blank-line rules, and the two fixes.
- Scoped conformance (declared pattern, `Suite: scoped`): 205 passed, 0 failed, 0 errored, 450 skipped; was 203 passed, 2 failed.
- Full pytest: 1142 passed, 1 skipped (pre-existing skip in test_foundation.py).
- `sources/full_test.sh` was not run; this step does not invoke it.

BLOCKERS:
- None.
