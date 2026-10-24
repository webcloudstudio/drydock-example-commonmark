# Evidence: Block 11 · Service (block-11)

- block type: block
- date: 2026-10-14
- resulting state: closed/verified
- story points (combined assembled cost): 5590
- execution id: 20261014.063246.323Z-3e8c174e

## Stories built
- Implement link and image bracket handling: inline, full, collapsed and shortcut forms. (links) [story]

## Stacked context
- compass: COMPASS.md (SP 1072)
- implements: FEATURE-Links.md (SP 2195)
- context: ARCHITECTURE_compact.md (SP 335)
- stack: common_compact.md (SP 1199)
- stack: python_compact.md (SP 390)

## Build directory changes
- mdparser/cli.py
- mdparser/inlines.py
- mdparser/links.py
- mdparser/refs.py
- tests/test_links.py

## Pre-build acceptance observation
- RED: links-inline-destination-and-title (FEATURE-Links.md)
  intent: An inline link renders one a element carrying the supplied destination, title and text.
  return code: 1
  stdout:
    <p>[label](/uri &quot;the title&quot;)</p>
  stderr:
    --- drydock: values at failure ---
      result = CompletedProcess(args=['./commonmark'], returncode=0, stdout='<p>[label](/uri &quot;the title&quot;)</p>\n', stderr='')
    --- drydock: end values ---
    Traceback (most recent call last):
      File "links-inline-destination-and-title.py", line 10, in <module>
        assert result.stdout.count("<a ") == 1
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    AssertionError
- RED: links-reference-forms (FEATURE-Links.md)
  intent: Full, collapsed and shortcut references each resolve against a definition and render one a element.
  return code: 1
  stdout:
    <p>[text][foo]</p>
  stderr:
    --- drydock: values at failure ---
      result = CompletedProcess(args=['./commonmark'], returncode=0, stdout='<p>[text][foo]</p>\n', stderr='')
    --- drydock: end values ---
    Traceback (most recent call last):
      File "links-reference-forms.py", line 8, in <module>
        assert result.stdout.count("<a ") == 1
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    AssertionError
- RED: links-reference-case-insensitive (FEATURE-Links.md)
  intent: Label matching ignores case.
  return code: 1
  stdout:
    <p>[FOO]</p>
  stderr:
    --- drydock: values at failure ---
      result = CompletedProcess(args=['./commonmark'], returncode=0, stdout='<p>[FOO]</p>\n', stderr='')
    --- drydock: end values ---
    Traceback (most recent call last):
      File "links-reference-case-insensitive.py", line 6, in <module>
        assert result.stdout.count("<a ") == 1
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    AssertionError
- GREEN (prepassed): links-undefined-reference-literal (FEATURE-Links.md)
  intent: A shortcut reference with no definition stays literal text.
  return code: 0
  stdout:
    <p>[nothing defined]</p>
- RED: links-no-nested-links (FEATURE-Links.md)
  intent: A link inside link text wins and the outer brackets stay literal, so only one a element appears.
  return code: 1
  stdout:
    <p>[foo [bar](/uri)](/uri)</p>
  stderr:
    --- drydock: values at failure ---
      result = CompletedProcess(args=['./commonmark'], returncode=0, stdout='<p>[foo [bar](/uri)](/uri)</p>\n', stderr='')
    --- drydock: end values ---
    Traceback (most recent call last):
      File "links-no-nested-links.py", line 6, in <module>
        assert result.stdout.count("<a ") == 1
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    AssertionError
- GREEN (prepassed): links-space-before-parenthesis (FEATURE-Links.md)
  intent: Whitespace between link text and the parenthesis prevents an inline link.
  return code: 0
  stdout:
    <p>[link] (/uri)</p>

## Post-build programmatic acceptance
- PASS: links-inline-destination-and-title (FEATURE-Links.md)
  intent: An inline link renders one a element carrying the supplied destination, title and text.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261014.053711/build/commonmark/.venv/bin/python
  provisioning: not required
  return code: 0
  stdout:
    <p><a href="/uri" title="the title">label</a></p>
- PASS: links-reference-forms (FEATURE-Links.md)
  intent: Full, collapsed and shortcut references each resolve against a definition and render one a element.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261014.053711/build/commonmark/.venv/bin/python
  provisioning: not required
  return code: 0
  stdout:
    <p><a href="/url">text</a></p>
    
    <p><a href="/url">foo</a></p>
    
    <p><a href="/url">foo</a></p>
- PASS: links-reference-case-insensitive (FEATURE-Links.md)
  intent: Label matching ignores case.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261014.053711/build/commonmark/.venv/bin/python
  provisioning: not required
  return code: 0
  stdout:
    <p><a href="/url">FOO</a></p>
- PASS: links-undefined-reference-literal (FEATURE-Links.md)
  intent: A shortcut reference with no definition stays literal text.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261014.053711/build/commonmark/.venv/bin/python
  provisioning: not required
  return code: 0
  stdout:
    <p>[nothing defined]</p>
- PASS: links-no-nested-links (FEATURE-Links.md)
  intent: A link inside link text wins and the outer brackets stay literal, so only one a element appears.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261014.053711/build/commonmark/.venv/bin/python
  provisioning: not required
  return code: 0
  stdout:
    <p>[foo <a href="/uri">bar</a>](/uri)</p>
- PASS: links-space-before-parenthesis (FEATURE-Links.md)
  intent: Whitespace between link text and the parenthesis prevents an inline link.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261014.053711/build/commonmark/.venv/bin/python
  provisioning: not required
  return code: 0
  stdout:
    <p>[link] (/uri)</p>

## Build summary
I'll start by checking the build directory, the existing sources, and what's already committed.The project already has an `mdparser` package from earlier blocks. I'll read the inline and reference code this step builds on.The inline scanner is a single left-to-right pass, and emphasis uses a delimiter stack. Next I need to see how the reference map reaches the inline parser, and how the existing tests are organised.The inline parser only receives raw text, so it has no access to the document's reference map yet. I'll check how the block tree holds that map, and how the existing tests call `parse_inline`.Baseline is green: 523 passed, 1 skipped. The link grammar I need (destination, title, label scan) is private in `refs.py`, so I'll check that no test depends on those private names before I make them shared.Nothing outside `refs.py` uses those helpers, so I'll make the four link-grammar helpers public. Then I'll add the link tail matcher in a new `links.py`.Now the link tail module: inline `(destination "title")` and the full, collapsed, and shortcut reference forms.Next, `inlines.py`. I'll add the link and image nodes, the bracket openers on the delimiter stack, and the look-for-link-or-image step.Next, the scanner branches and the renderer for the new nodes.Now the `DelimiterStack` methods the procedure calls: find the nearest opener, remove it, deactivate earlier `[` openers, and close one over its content.Last wiring step: the CLI passes the document's reference map into the inline parser.Before writing the test file, I'll run the six declared acceptance snippets and a few spec examples directly, so I can see the behaviour.The outputs match the spec behaviour I checked, including the spec's `[foo][bar][baz]` case and the nested-link case. Next I'll write the test file: the six declared acceptance checks transcribed as written, then finer tests for each form and boundary.Before running, I re-checked the expectations by hand and found four that are wrong: the `"` in a bare destination percent-encodes to `%22`, the `<b<c>` case has a raw HTML tag after it, and two reference tests don't test what their names say. I'll correct them.The `[x]]` replacement doesn't test what its name says, so I'll remove it rather than keep a misleading test. Then I'll run the new file and the full suite.The full suite is green: 581 passed, 1 skipped. That is the prior 523 plus my 58, with no regressions. I'll check line lengths against the project's style and remove my scratch files from `/tmp`.The `links` block is built. The six declared acceptance checks pass, and the full pytest suite is green at 581 passed with 1 skipped; the skip predates this step.

I did not run `sh sources/full_test.sh`. The Links corpus section needs image rendering, and the feature spec gates it in the images story. I also didn't run the staged conformance runner unscoped, since no criterion in this step invokes it.

**What was built**
- **Bracket procedure** (`mdparser/inlines.py`): `[` and `![` push openers on the existing delimiter stack. On `]`, the nearest opener is tried for an inline link, then full `[label]`, collapsed `[]`, and shortcut forms. Success builds a link over the nodes after the opener and runs emphasis inside it. Earlier `[` openers are deactivated so links never nest. A failed or inactive opener leaves `]` literal.
- **Link tails** (`mdparser/links.py`, new): inline `(destination "title")` matching, plus the reference forms. A following label that doesn't resolve fails the link rather than falling back to shortcut.
- **Reference map**: `parse_inline` takes an optional `references`. `cli.py` passes the document's map, so definitions after a paragraph still resolve.
- **Shared grammar**: four helpers in `refs.py` (`scan_label`, `parse_destination`, `parse_title`, `skip_whitespace_with_line_ending`) are now public so `links.py` can use them. Nothing outside `refs.py` used the old private names.
- **Tests** (`tests/test_links.py`, new, 58 tests): the six declared acceptance checks transcribed as written, plus tests per form, destination and title grammar, label boundaries (999 and 1000 characters), nesting and deactivation, and executable-level round trips.

**Choices I made that you may want to change**
- **Images**: `![` constructs are consumed correctly, but they render as their literal source (for example `![foo](/url)`). The spec leaves image rendering to the images story, and I didn't want to render `<img>` early.
- **Parentheses depth**: the spec text says "at least three levels", and I used unlimited balanced depth, which satisfies that.
- **Empty title**: an empty title is omitted from the `title` attribute, matching the reference behaviour.

FILES CHANGED are listed below. I did not stage or commit anything.

```text
<blueprint-decisions>
[{"spec":"FEATURE-Links.md","severity":"Material","subject":"Image (![) constructs","decision":"The ![ opener and its inline or reference tail are matched and consumed with the same machinery, but the image is emitted as its literal source text, escaped. Rendering <img> was left to the images story as the build instructions require. Is that acceptable, or should the images story replace this on replan?"},{"spec":"FEATURE-Links.md","severity":"Low","subject":"Destination parenthesis depth","decision":"The spec text says balanced parentheses to at least three levels. I reused the balanced-depth matcher from refs.py, which has no depth limit. Is an unlimited depth acceptable?"}]
</blueprint-decisions>

RESULT: SUCCESS

FILES CHANGED:
- mdparser/links.py
- mdparser/inlines.py
- mdparser/refs.py
- mdparser/cli.py
- tests/test_links.py

SUMMARY:
Implemented the look-for-link-or-image procedure for links with inline, full, collapsed and shortcut reference forms. The six FEATURE-Links acceptance checks pass as written (tests/test_links.py, 58 tests in that file). Full pytest suite: 581 passed, 1 skipped (pre-existing). The unscoped conformance runner (sources/full_test.sh) was not run, since the Links corpus section is gated in the images story. Images are consumed but rendered as literal source until the images story.

BLOCKERS:
- None.
```
