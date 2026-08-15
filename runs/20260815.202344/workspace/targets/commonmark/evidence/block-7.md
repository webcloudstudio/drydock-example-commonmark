# Evidence: Block 7 · Service (block-7)

- block type: block
- date: 2026-08-15
- resulting state: closed/verified
- story points (combined assembled cost): 59935
- execution id: 20260815.212638.785Z-cc3019ff

## Stories built
- Parse inline and reference links together with images. (inline-003) [story]

## Stacked context
- compass: COMPASS.md (SP 1455)
- implements: FEATURE-Inline-Links-Images.md (SP 495)
- context: spec.txt (SP 51527)
- context: spec_tests.py (SP 1609)
- context: cmark.py (SP 339)
- context: normalize.py (SP 1631)
- context: ARCHITECTURE_compact.md (SP 87)
- stack: common_compact.md (SP 1179)
- stack: python_compact.md (SP 1534)

## Build directory changes
- commonmark

## Pre-build acceptance observation
- RED: links-images-conformance (FEATURE-Inline-Links-Images.md)
  intent: The implementation passes every supplied conformance example owned by links and images.
  return code: 1
  stdout:
    Example 490 (lines 7610-7614) Links
    [link](/my uri)
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>[link](/my uri)</p>
    +<p><a href="/my%20uri">link</a></p>
    
    Example 493 (lines 7633-7639) Links
    [link](<foo
    bar>)
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>[link](<foo bar>)</p>
    +<p><a href="">link</a></p>
    
    Example 495 (lines 7652-7656) Links
    [link](<foo\>)
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>[link](&lt;foo&gt;)</p>
    +<p><a href="foo%5C">link</a></p>
    
    Example 496 (lines 7661-7669) Links
    [a](<b)c
    [a](<b)c>
    [a](<b>c)
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>[a](&lt;b)c [a](&lt;b)c&gt; [a](<b>c)</p>
    +<p><a href="%3Cb">a</a>c <a href="%3Cb">a</a>c&gt; <a href="%3Cb%3Ec">a</a></p>
    
    Example 497 (lines 7673-7677) Links
    [link](\(foo\))
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><a href="(foo)">link</a></p>
    +<p><a href="(foo%5C">link</a>)</p>
    
    Example 498 (lines 7682-7686) Links
    [link](foo(and(bar)))
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><a href="foo(and(bar))">link</a></p>
    +<p><a href="foo(and(bar">link</a>))</p>
    
    Example 499 (lines 7691-7695) Links
    [link](foo(and(bar))
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>[link](foo(and(bar))</p>
    +<p><a href="foo(and(bar">link</a>)</p>
    
    Example 500 (lines 7698-7702) Links
    [link](foo\(and\(bar\))
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><a href="foo(and(bar)">link</a></p>
    +<p><a href="foo(and(bar%5C">link</a>)</p>
    
    Example 502 (lines 7715-7719) Links
    [link](foo\)\:)
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><a href="foo):">link</a></p>
    +<p><a href="foo%5C">link</a>:)</p>
    
    Example 507 (lines 7776-7784) Links
    [link](/url "title")
    [link](/url 'title')
    [link](/url (title))
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><a href="/url" title="title">link</a> <a href="/url" title="title">link</a> <a href="/url" title="title">link</a></p>
    +<p><a href="/url" title="title">link</a> <a href="/url" title="title">link</a> <a href="/url%20(title">link</a>)</p>
    
    Example 510 (lines 7810-7814) Links
    [link](/url "title "and" title")
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>[link](/url &quot;title &quot;and&quot; title&quot;)</p>
    +<p><a href="/url" title="title &quot;and&quot; title">link</a></p>
    
    Example 512 (lines 7844-7849) Links
    [link](   /uri
      "title"  )
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><a href="/uri" title="title">link</a></p>
    +<p>[link]( /uri &quot;title&quot; )</p>
    
    Example 514 (lines 7865-7869) Links
    [link [foo [bar]]](/uri)
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><a href="/uri">link [foo [bar]]</a></p>
    +<p>[link [foo [bar]]](/uri)</p>
    
    Example 516 (lines 7879-7883) Links
    [link [bar](/uri)
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>[link <a href="/uri">bar</a></p>
    +<p><a href="/uri">link [bar</a></p>
    
    Example 519 (lines 7902-7906) Links
    [![moon](moon.jpg)](/uri)
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><a href="/uri"><img alt="moon" src="moon.jpg"></a></p>
    +<p><a href="moon.jpg">![moon</a>](/uri)</p>
    
    Example 520 (lines 7911-7915) Links
    [foo [bar](/uri)](/uri)
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>[foo <a href="/uri">bar</a>](/uri)</p>
    +<p><a href="/uri">foo [bar</a>](/uri)</p>
    
    Example 521 (lines 7918-7922) Links
    [foo *[bar [baz](/uri)](/uri)*](/uri)
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>[foo <em>[bar <a href="/uri">baz</a>](/uri)</em>](/uri)</p>
    +<p><a href="/uri">foo *[bar [baz</a>](/uri)*](/uri)</p>
    
    Example 522 (lines 7925-7929) Links
    ![[[foo](uri1)](uri2)](uri3)
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><img alt="[foo](uri2)" src="uri3"></p>
    +<p><img alt="[[foo" src="uri1">](uri2)](uri3)</p>
    
    Example 526 (lines 7962-7966) Links
    [foo <bar attr="](baz)">
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>[foo <bar attr="](baz)"></p>
    +<p><a href="baz">foo &lt;bar attr=&quot;</a>&quot;&gt;</p>
    
    Example 528 (lines 7976-7980) Links
    [foo<https://example.com/?search=](uri)>
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>[foo<a href="https://example.com/?search=%5D(uri)">https://example.com/?search=](uri)</a></p>
    +<p><a href="uri">foo&lt;https://example.com/?search=</a>&gt;</p>
    
    Example 530 (lines 8029-8035) Links
    [link [foo [bar]]][ref]
    
    [ref]: /uri
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><a href="/uri">link [foo [bar]]</a></p>
    +<p>[link [foo [bar]]]<a href="/uri">ref</a></p>
    
    Example 533 (lines 8058-8064) Links
    [![moon](moon.jpg)][ref]
    
    [ref]: /uri
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><a href="/uri"><img alt="moon" src="moon.jpg"></a></p>
    +<p><a href="moon.jpg">![moon</a>]<a href="/uri">ref</a></p>
    
    Example 534 (lines 8069-8075) Links
    [foo [bar](/uri)][ref]
    
    [ref]: /uri
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>[foo <a href="/uri">bar</a>]<a href="/uri">ref</a></p>
    +<p><a href="/uri">foo [bar</a>]<a href="/uri">ref</a></p>
    
    Example 535 (lines 8078-8084) Links
    [foo *bar [baz][ref]*][ref]
    
    [ref]: /uri
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>[foo <em>bar <a href="/uri">baz</a></em>]<a href="/uri">ref</a></p>
    +<p><a href="/uri">foo <em>bar [baz</a></em>]<a href="/uri">ref</a></p>
    
    Example 536 (lines 8093-8099) Links
    *[foo*][ref]
    
    [ref]: /uri
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>*<a href="/uri">foo*</a></p>
    +<p><em><a href="/uri">foo</em></a></p>
    
    Example 537 (lines 8102-8108) Links
    [foo *bar][ref]*
    
    [ref]: /uri
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><a href="/uri">foo *bar</a>*</p>
    +<p><a href="/uri">foo <em>bar</a></em></p>
    
    Example 543 (lines 8166-8173) Links
    [Foo
      bar]: /url
    
    [Baz][Foo bar]
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><a href="/url">Baz</a></p>
    +<p>[Foo bar]: /url</p><p>[Baz][Foo bar]</p>
    
    Example 547 (lines 8244-8250) Links
    [bar][foo\!]
    
    [foo!]: /url
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>[bar][foo!]</p>
    +<p><a href="/url">bar</a></p>
    
    Example 548 (lines 8256-8263) Links
    [foo][ref[]
    
    [ref[]: /uri
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>[foo][ref[]</p><p>[ref[]: /uri</p>
    +<p><a href="/uri">foo</a></p>
    
    Example 554 (lines 8319-8330) Links
    [
     ]
    
    [
     ]: /uri
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>[ ]</p><p>[ ]: /uri</p>
    +<p><a href="/uri"> </a></p>
    
    Example 561 (lines 8413-8419) Links
    [[*foo* bar]]
    
    [*foo* bar]: /url "title"
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>[<a href="/url" title="title"><em>foo</em> bar</a>]</p>
    +<p>[[<em>foo</em> bar]]</p>
    
    Example 562 (lines 8422-8428) Links
    [[bar [foo]
    
    [foo]: /url
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>[[bar <a href="/url">foo</a></p>
    +<p>[[bar [foo]</p>
    
    Example 566 (lines 8468-8474) Links
    [foo*]: /url
    
    *[foo*]
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>*<a href="/url">foo*</a></p>
    +<p><em><a href="/url">foo</em></a></p>
    
    Example 570 (lines 8507-8513) Links
    [foo](not a link)
    
    [foo]: /url1
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><a href="/url1">foo</a>(not a link)</p>
    +<p><a href="not%20a%20link">foo</a></p>
    
    Example 571 (lines 8518-8524) Links
    [foo][bar][baz]
    
    [baz]: /url
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>[foo]<a href="/url">bar</a></p>
    +<p>[foo][bar]<a href="/url">baz</a></p>
    
    Example 573 (lines 8543-8550) Links
    [foo][bar][baz]
    
    [baz]: /url1
    [foo]: /url2
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>[foo]<a href="/url1">bar</a></p>
    +<p>[foo][bar]<a href="/url1">baz</a></p>
    
    Example 575 (lines 8573-8579) Images
    ![foo *bar*]
    
    [foo *bar*]: train.jpg "train & tracks"
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><img alt="foo bar" src="train.jpg" title="train &amp; tracks"></p>
    +<p><img alt="foo &lt;em&gt;bar&lt;/em&gt;" src="train.jpg" title="train &amp; tracks"></p>
    
    Example 576 (lines 8582-8586) Images
    ![foo ![bar](/url)](/url2)
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><img alt="foo bar" src="/url2"></p>
    +<p><img alt="foo ![bar" src="/url">](/url2)</p>
    
    Example 577 (lines 8589-8593) Images
    ![foo [bar](/url)](/url2)
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><img alt="foo bar" src="/url2"></p>
    +<p><img alt="foo [bar" src="/url">](/url2)</p>
    
    Example 578 (lines 8603-8609) Images
    ![foo *bar*][]
    
    [foo *bar*]: train.jpg "train & tracks"
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><img alt="foo bar" src="train.jpg" title="train &amp; tracks"></p>
    +<p><img alt="foo &lt;em&gt;bar&lt;/em&gt;" src="train.jpg" title="train &amp; tracks"></p>
    
    Example 579 (lines 8612-8618) Images
    ![foo *bar*][foobar]
    
    [FOOBAR]: train.jpg "train & tracks"
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><img alt="foo bar" src="train.jpg" title="train &amp; tracks"></p>
    +<p><img alt="foo &lt;em&gt;bar&lt;/em&gt;" src="train.jpg" title="train &amp; tracks"></p>
    
    Example 587 (lines 8680-8686) Images
    ![*foo* bar][]
    
    [*foo* bar]: /url "title"
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><img alt="foo bar" src="/url" title="title"></p>
    +<p><img alt="&lt;em&gt;foo&lt;/em&gt; bar" src="/url" title="title"></p>
    
    Example 591 (lines 8725-8731) Images
    ![*foo* bar]
    
    [*foo* bar]: /url "title"
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><img alt="foo bar" src="/url" title="title"></p>
    +<p><img alt="&lt;em&gt;foo&lt;/em&gt; bar" src="/url" title="title"></p>
    
    69 passed, 43 failed, 0 errored, 543 skipped
  stderr:
    Traceback (most recent call last):
      File "links-images-conformance.py", line 20, in <module>
        assert result.returncode == 0
               ^^^^^^^^^^^^^^^^^^^^^^
    AssertionError

## Post-build programmatic acceptance
- PASS: links-images-conformance (FEATURE-Inline-Links-Images.md)
  intent: The implementation passes every supplied conformance example owned by links and images.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/.venv/bin/python3
  provisioning: not required
  return code: 0
  stdout:
    112 passed, 0 failed, 0 errored, 543 skipped

## Build summary
RESULT: SUCCESS

FILES CHANGED:
- [commonmark](/mnt/c/Users/barlo/projects/drydock/uat/Commonmark/runs/20260815.202344/build/commonmark/commonmark)

SUMMARY:
Implemented robust inline/reference link and image parsing, including balanced destinations, titles, nested brackets, label normalization, duplicate precedence, link restrictions, and image alt text.

Acceptance: 112 passed, 0 failed.

BLOCKERS:
- None
