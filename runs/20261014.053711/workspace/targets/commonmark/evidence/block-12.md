# Evidence: Block 12 · Service (block-12)

- block type: block
- date: 2026-10-14
- resulting state: closed/verified
- story points (combined assembled cost): 4813
- execution id: 20261014.064009.029Z-03c1a38f

## Stories built
- Render images with plain-text alt and verify links, images and emphasis against the corpus. (images) [story]

## Stacked context
- compass: COMPASS.md (SP 1072)
- implements: FEATURE-Images.md (SP 1634)
- context: ARCHITECTURE_compact.md (SP 335)
- stack: common_compact.md (SP 1199)
- stack: python_compact.md (SP 390)

## Build directory changes
- mdparser/inlines.py
- tests/test_images.py
- tests/test_links.py

## Pre-build acceptance observation
- RED: images-corpus-sections (FEATURE-Images.md)
  intent: The Emphasis and strong emphasis, Links and Images conformance sections (roughly 240 cases) pass in full.
  return code: 1
  stdout:
    Example 519 (lines 7902-7906) Links
    [![moon](moon.jpg)](/uri)
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><a href="/uri"><img alt="moon" src="moon.jpg"></a></p>
    +<p><a href="/uri">![moon](moon.jpg)</a></p>
    
    Example 522 (lines 7925-7929) Links
    ![[[foo](uri1)](uri2)](uri3)
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><img alt="[foo](uri2)" src="uri3"></p>
    +<p>![[[foo](uri1)](uri2)](uri3)</p>
    
    Example 533 (lines 8058-8064) Links
    [![moon](moon.jpg)][ref]
    
    [ref]: /uri
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><a href="/uri"><img alt="moon" src="moon.jpg"></a></p>
    +<p><a href="/uri">![moon](moon.jpg)</a></p>
    
    Example 574 (lines 8566-8570) Images
    ![foo](/url "title")
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><img alt="foo" src="/url" title="title"></p>
    +<p>![foo](/url &quot;title&quot;)</p>
    
    Example 575 (lines 8573-8579) Images
    ![foo *bar*]
    
    [foo *bar*]: train.jpg "train & tracks"
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><img alt="foo bar" src="train.jpg" title="train &amp; tracks"></p>
    +<p>![foo *bar*]</p>
    
    Example 576 (lines 8582-8586) Images
    ![foo ![bar](/url)](/url2)
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><img alt="foo bar" src="/url2"></p>
    +<p>![foo ![bar](/url)](/url2)</p>
    
    Example 577 (lines 8589-8593) Images
    ![foo [bar](/url)](/url2)
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><img alt="foo bar" src="/url2"></p>
    +<p>![foo [bar](/url)](/url2)</p>
    
    Example 578 (lines 8603-8609) Images
    ![foo *bar*][]
    
    [foo *bar*]: train.jpg "train & tracks"
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><img alt="foo bar" src="train.jpg" title="train &amp; tracks"></p>
    +<p>![foo *bar*][]</p>
    
    Example 579 (lines 8612-8618) Images
    ![foo *bar*][foobar]
    
    [FOOBAR]: train.jpg "train & tracks"
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><img alt="foo bar" src="train.jpg" title="train &amp; tracks"></p>
    +<p>![foo *bar*][foobar]</p>
    
    Example 580 (lines 8621-8625) Images
    ![foo](train.jpg)
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><img alt="foo" src="train.jpg"></p>
    +<p>![foo](train.jpg)</p>
    
    Example 581 (lines 8628-8632) Images
    My ![foo bar](/path/to/train.jpg  "title"   )
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>My <img alt="foo bar" src="/path/to/train.jpg" title="title"></p>
    +<p>My ![foo bar](/path/to/train.jpg &quot;title&quot; )</p>
    
    Example 582 (lines 8635-8639) Images
    ![foo](<url>)
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><img alt="foo" src="url"></p>
    +<p>![foo](&lt;url&gt;)</p>
    
    Example 583 (lines 8642-8646) Images
    ![](/url)
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><img alt="" src="/url"></p>
    +<p>![](/url)</p>
    
    Example 584 (lines 8651-8657) Images
    ![foo][bar]
    
    [bar]: /url
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><img alt="foo" src="/url"></p>
    +<p>![foo][bar]</p>
    
    Example 585 (lines 8660-8666) Images
    ![foo][bar]
    
    [BAR]: /url
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><img alt="foo" src="/url"></p>
    +<p>![foo][bar]</p>
    
    Example 586 (lines 8671-8677) Images
    ![foo][]
    
    [foo]: /url "title"
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><img alt="foo" src="/url" title="title"></p>
    +<p>![foo][]</p>
    
    Example 587 (lines 8680-8686) Images
    ![*foo* bar][]
    
    [*foo* bar]: /url "title"
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><img alt="foo bar" src="/url" title="title"></p>
    +<p>![*foo* bar][]</p>
    
    Example 588 (lines 8691-8697) Images
    ![Foo][]
    
    [foo]: /url "title"
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><img alt="Foo" src="/url" title="title"></p>
    +<p>![Foo][]</p>
    
    Example 589 (lines 8703-8711) Images
    ![foo] 
    []
    
    [foo]: /url "title"
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><img alt="foo" src="/url" title="title"> []</p>
    +<p>![foo] []</p>
    
    Example 590 (lines 8716-8722) Images
    ![foo]
    
    [foo]: /url "title"
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><img alt="foo" src="/url" title="title"></p>
    +<p>![foo]</p>
    
    Example 591 (lines 8725-8731) Images
    ![*foo* bar]
    
    [*foo* bar]: /url "title"
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><img alt="foo bar" src="/url" title="title"></p>
    +<p>![*foo* bar]</p>
    
    Example 593 (lines 8748-8754) Images
    ![Foo]
    
    [foo]: /url "title"
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><img alt="Foo" src="/url" title="title"></p>
    +<p>![Foo]</p>
    
    222 passed, 22 failed, 0 errored, 411 skipped
  stderr:
    --- drydock: progress ---
    cases: pass=222 fail=22 error=0 skip=411 total=655 from=result.stdout
    --- drydock: end progress ---
    --- drydock: values at failure ---
      result = CompletedProcess(args=['/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261014.053711/build/commonmark/.venv/bin/python', 'sources/spec_tests.py', '--program', '/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261014.053711/build/commonmark/commonmark', '--spec', 'sources/spec.txt', '--pattern', '^Emphasis and strong emphasis$|^Links$|^Images$'], returncode=22, stdout='Example 5… (+4557 chars)
    --- drydock: end values ---
    Traceback (most recent call last):
      File "images-corpus-sections.py", line 22, in <module>
        assert result.returncode == 0
               ^^^^^^^^^^^^^^^^^^^^^^
    AssertionError
- RED: images-inline-image (FEATURE-Images.md)
  intent: An inline image renders one img element carrying the supplied src, alt and title.
  return code: 1
  stdout:
    <p>![my alt](/path/pic.jpg &quot;a title&quot;)</p>
  stderr:
    --- drydock: values at failure ---
      result = CompletedProcess(args=['./commonmark'], returncode=0, stdout='<p>![my alt](/path/pic.jpg &quot;a title&quot;)</p>\n', stderr='')
    --- drydock: end values ---
    Traceback (most recent call last):
      File "images-inline-image.py", line 10, in <module>
        assert result.stdout.count("<img ") == 1
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    AssertionError
- RED: images-alt-is-plain-text (FEATURE-Images.md)
  intent: Emphasis inside an image description does not appear as markup in the alt attribute.
  return code: 1
  stdout:
    <p>![foo *bar*](/u)</p>
  stderr:
    --- drydock: values at failure ---
      result = CompletedProcess(args=['./commonmark'], returncode=0, stdout='<p>![foo *bar*](/u)</p>\n', stderr='')
    --- drydock: end values ---
    Traceback (most recent call last):
      File "images-alt-is-plain-text.py", line 6, in <module>
        assert result.stdout.count("<img ") == 1
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    AssertionError
- RED: images-reference-forms (FEATURE-Images.md)
  intent: Full, collapsed and shortcut image references each resolve against a definition.
  return code: 1
  stdout:
    <p>![text][foo]</p>
  stderr:
    --- drydock: values at failure ---
      result = CompletedProcess(args=['./commonmark'], returncode=0, stdout='<p>![text][foo]</p>\n', stderr='')
    --- drydock: end values ---
    Traceback (most recent call last):
      File "images-reference-forms.py", line 8, in <module>
        assert result.stdout.count("<img ") == 1
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    AssertionError
- RED: images-inside-link (FEATURE-Images.md)
  intent: An image inside a link produces one a element containing one img element.
  return code: 1
  stdout:
    <p><a href="/uri">![moon](moon.jpg)</a></p>
  stderr:
    --- drydock: values at failure ---
      result = CompletedProcess(args=['./commonmark'], returncode=0, stdout='<p><a href="/uri">![moon](moon.jpg)</a></p>\n', stderr='')
    --- drydock: end values ---
    Traceback (most recent call last):
      File "images-inside-link.py", line 7, in <module>
        assert result.stdout.count("<img ") == 1
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    AssertionError

## Post-build programmatic acceptance
- PASS: images-corpus-sections (FEATURE-Images.md)
  intent: The Emphasis and strong emphasis, Links and Images conformance sections (roughly 240 cases) pass in full.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261014.053711/build/commonmark/.venv/bin/python
  provisioning: not required
  return code: 0
  stdout:
    244 passed, 0 failed, 0 errored, 411 skipped
- PASS: images-inline-image (FEATURE-Images.md)
  intent: An inline image renders one img element carrying the supplied src, alt and title.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261014.053711/build/commonmark/.venv/bin/python
  provisioning: not required
  return code: 0
  stdout:
    <p><img src="/path/pic.jpg" alt="my alt" title="a title" /></p>
- PASS: images-alt-is-plain-text (FEATURE-Images.md)
  intent: Emphasis inside an image description does not appear as markup in the alt attribute.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261014.053711/build/commonmark/.venv/bin/python
  provisioning: not required
  return code: 0
  stdout:
    <p><img src="/u" alt="foo bar" /></p>
- PASS: images-reference-forms (FEATURE-Images.md)
  intent: Full, collapsed and shortcut image references each resolve against a definition.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261014.053711/build/commonmark/.venv/bin/python
  provisioning: not required
  return code: 0
  stdout:
    <p><img src="/url" alt="text" /></p>
    
    <p><img src="/url" alt="foo" /></p>
    
    <p><img src="/url" alt="foo" /></p>
- PASS: images-inside-link (FEATURE-Images.md)
  intent: An image inside a link produces one a element containing one img element.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261014.053711/build/commonmark/.venv/bin/python
  provisioning: not required
  return code: 0
  stdout:
    <p><a href="/uri"><img src="moon.jpg" alt="moon" /></a></p>

## Build summary
Images are currently kept as literal source. I'll replace that with a real `Image` node. Its alt text needs plain text, which the current `Html` nodes don't carry, so `Html` gets a `text` field too.Now the `parse_inline` construction sites, so every `Html` node carries its plain text.Next, rendering, the bracket close for images, and the matcher helpers.Now I'll update the interim test that pinned the old literal-image behaviour, then check for leftover single-argument `Html(` calls.Now the test file. The four declared acceptance checks are transcribed as written, and the remaining tests cover the behaviour around them.Running the project's test suite, which includes the scoped corpus check.One more interim assertion from the links story expected the image to stay literal. The new output is the correct rendering, so I'll update that expectation.The scoped gate passes. Let me confirm the set of files I changed.RESULT: SUCCESS

FILES CHANGED:
- mdparser/inlines.py
- tests/test_links.py
- tests/test_images.py

SUMMARY:
Images are now real nodes instead of literal source. An `![` opener that closes with an inline, full, collapsed or shortcut tail renders `<img src alt title />`. The src is percent-encoded and escaped like a link href, and the title is omitted when empty. The alt is the plain text of the description: emphasis, links and nested images contribute their text, code spans contribute their content, and the result is escaped.

To get plain text, `Html` nodes now carry a `text` field alongside their rendered HTML. The helpers `_text` and `_raw` build them. The code-span and autolink matchers now return `Html` nodes. Images inside links, and `\![foo]` and `!\[foo]`, behave as the spec requires.

Two interim assertions from the links story pinned the old literal-image output. I updated them to the rendered output: `test_image_construct_is_rendered_as_an_image_not_a_link` and `test_image_opener_does_not_deactivate_earlier_link_openers`. Neither is a declared acceptance assertion.

`tests/test_images.py` transcribes the four declared checks with their assertions kept as written. It adds finer tests for attributes, alt rules, reference forms, nesting and the executable.

Verification:
- Scoped corpus gate `sources/spec_tests.py --pattern "^Emphasis and strong emphasis$|^Links$|^Images$"`: exit 0, 244 passed, 0 failed (411 skipped by the pattern).
- Project suite `.venv/bin/python -m pytest -q`: 611 passed, 1 skipped (`test_foundation.py`, pre-existing parametrization skip), 1 failure, which I then fixed. The final run of `test_links.py` and `test_images.py` passed 89 of 89.
- I did not run `sources/full_test.sh`, since the criteria declare the scoped invocation only.
- Nothing was committed.

Choices I made:
- Raw HTML inside an image description contributes its source text to alt, escaped. This follows cmark's plain-text behaviour. The spec has no example for it, so it is untested.

BLOCKERS:
- None.

<blueprint-decisions>
[{"spec":"FEATURE-Images.md","severity":"Low","subject":"Raw HTML inside an image description","decision":"Raw inline HTML contributes its literal source text to alt, escaped, as cmark does in plain-text mode. The spec gives no example for this case. Is that acceptable?"}]
</blueprint-decisions>
