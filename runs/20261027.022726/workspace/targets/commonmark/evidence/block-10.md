# Evidence: Block 10 · Service (block-10)

- block type: block
- date: 2026-10-26
- resulting state: closed/failed
- story points (combined assembled cost): 3047
- execution id: 20261027.032209.085Z-31db92e4

## Stories built
- Parse inline and reference links. (links) [story]

## Acceptance tooling authorization
- FEATURE-Links.md#links-conformance: executable=python3; scope=test; authorization=existing Target environment

## Stacked context
- stack: python_compact.md (SP 601)
- compass: COMPASS.md (SP 512)
- implements: FEATURE-Links.md (SP 550)
- context: ARCHITECTURE_compact.md (SP 211)
- stack: common_compact.md (SP 1079)

## Build directory changes
- commonmark_parser/inline.py
- commonmark_parser/references.py
- commonmark_parser/stages.py
- tests/test_links.py

## Pre-build acceptance observation
- RED: links-conformance (FEATURE-Links.md)
  intent: The completed parser passes the authoritative link and link-reference-definition examples.
  return code: 1
  stdout:
    Example 194 (lines 3201-3207) Link reference definitions
    [foo]: /url "title"
    
    [foo]
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><a href="/url" title="title">foo</a></p>
    +<p>[foo]</p>
    
    Example 195 (lines 3210-3218) Link reference definitions
       [foo]: 
          /url  
               'the title'  
    
    [foo]
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><a href="/url" title="the title">foo</a></p>
    +<p>[foo]: /url 'the title'</p><p>[foo]</p>
    
    Example 196 (lines 3221-3227) Link reference definitions
    [Foo*bar\]]:my_(url) 'title (with parens)'
    
    [Foo*bar\]]
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><a href="my_(url)" title="title (with parens)">Foo*bar]</a></p>
    +<p>[Foo*bar]]:my_(url) 'title (with parens)'</p><p>[Foo*bar]]</p>
    
    Example 197 (lines 3230-3238) Link reference definitions
    [Foo bar]:
    <my url>
    'title'
    
    [Foo bar]
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><a href="my%20url" title="title">Foo bar</a></p>
    +<p>[Foo bar]: <my url> 'title'</p><p>[Foo bar]</p>
    
    Example 198 (lines 3243-3257) Link reference definitions
    [foo]: /url '
    title
    line1
    line2
    '
    
    [foo]
    
    --- expected HTML
    +++ actual HTML
    @@ -1,5 +1 @@
    -<p><a href="/url" title="
    -title
    -line1
    -line2
    -">foo</a></p>
    +<p>[foo]: /url ' title line1 line2 '</p><p>[foo]</p>
    
    Example 200 (lines 3277-3284) Link reference definitions
    [foo]:
    /url
    
    [foo]
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><a href="/url">foo</a></p>
    +<p>[foo]: /url</p><p>[foo]</p>
    
    Example 202 (lines 3301-3307) Link reference definitions
    [foo]: <>
    
    [foo]
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><a href="">foo</a></p>
    +<p>[foo]</p>
    
    Example 203 (lines 3312-3319) Link reference definitions
    [foo]: <bar>(baz)
    
    [foo]
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>[foo]: <bar>(baz)</p><p>[foo]</p>
    +<p>[foo]</p>
    
    Example 204 (lines 3325-3331) Link reference definitions
    [foo]: /url\bar\*baz "foo\"bar\baz"
    
    [foo]
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><a href="/url%5Cbar*baz" title="foo&quot;bar\baz">foo</a></p>
    +<p>[foo]: /url\bar*baz &quot;foo&quot;bar\baz&quot;</p><p>[foo]</p>
    
    Example 205 (lines 3336-3342) Link reference definitions
    [foo]
    
    [foo]: url
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><a href="url">foo</a></p>
    +<p>[foo]</p>
    
    Example 206 (lines 3348-3355) Link reference definitions
    [foo]
    
    [foo]: first
    [foo]: second
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><a href="first">foo</a></p>
    +<p>[foo]</p>
    
    Example 207 (lines 3361-3367) Link reference definitions
    [FOO]: /url
    
    [Foo]
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><a href="/url">Foo</a></p>
    +<p>[Foo]</p>
    
    Example 208 (lines 3370-3376) Link reference definitions
    [ΑΓΩ]: /φου
    
    [αγω]
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><a href="/%CF%86%CE%BF%CF%85">αγω</a></p>
    +<p>[αγω]</p>
    
    Example 210 (lines 3393-3400) Link reference definitions
    [
    foo
    ]: /url
    bar
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>bar</p>
    +<p>[ foo ]: /url bar</p>
    
    Example 216 (lines 3470-3479) Link reference definitions
    # [Foo]
    [foo]: /url
    > bar
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<h1><a href="/url">Foo</a></h1><blockquote><p>bar</p></blockquote>
    +<h1>[Foo]</h1><blockquote><p>bar</p></blockquote>
    
    Example 217 (lines 3481-3489) Link reference definitions
    [foo]: /url
    bar
    ===
    [foo]
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<h1>bar</h1><p><a href="/url">foo</a></p>
    +<h1>bar</h1><p>[foo]</p>
    
    Example 218 (lines 3491-3498) Link reference definitions
    [foo]: /url
    ===
    [foo]
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>=== <a href="/url">foo</a></p>
    +<p>[foo]</p>
    
    Example 219 (lines 3504-3517) Link reference definitions
    [foo]: /foo-url "foo"
    [bar]: /bar-url
      "bar"
    [baz]: /baz-url
    
    [foo],
    [bar],
    [baz]
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><a href="/foo-url" title="foo">foo</a>, <a href="/bar-url" title="bar">bar</a>, <a href="/baz-url">baz</a></p>
    +<p>&quot;bar&quot; [baz]: /baz-url</p><p>[foo], [bar], [baz]</p>
    
    Example 220 (lines 3525-3533) Link reference definitions
    [foo]
    
    > [foo]: /url
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><a href="/url">foo</a></p><blockquote></blockquote>
    +<p>[foo]</p><blockquote></blockquote>
    
    Example 486 (lines 7580-7584) Links
    [](./target.md)
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><a href="./target.md"></a></p>
    +<p>[](./target.md)</p>
    
    Example 488 (lines 7594-7598) Links
    [link](<>)
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><a href="">link</a></p>
    +<p><a href="&lt;&gt;">link</a></p>
    
    Example 489 (lines 7601-7605) Links
    []()
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><a href=""></a></p>
    +<p>[]()</p>
    
    Example 491 (lines 7616-7620) Links
    [link](</my uri>)
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><a href="/my%20uri">link</a></p>
    +<p>[link](</my>)</p>
    
    Example 494 (lines 7644-7648) Links
    [a](<b)c>)
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><a href="b)c">a</a></p>
    +<p><a href="&lt;b">a</a>c&gt;)</p>
    
    Example 495 (lines 7652-7656) Links
    [link](<foo\>)
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>[link](&lt;foo&gt;)</p>
    +<p><a href="&lt;foo&gt;">link</a></p>
    
    Example 496 (lines 7661-7669) Links
    [a](<b)c
    [a](<b)c>
    [a](<b>c)
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>[a](&lt;b)c [a](&lt;b)c&gt; [a](<b>c)</p>
    +<p><a href="&lt;b">a</a>c <a href="&lt;b">a</a>c&gt; <a href="&lt;b&gt;c">a</a></p>
    
    Example 497 (lines 7673-7677) Links
    [link](\(foo\))
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><a href="(foo)">link</a></p>
    +<p><a href="(foo\">link</a>)</p>
    
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
    +<p><a href="foo(and(bar\">link</a>)</p>
    
    Example 501 (lines 7705-7709) Links
    [link](<foo(and(bar)>)
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><a href="foo(and(bar)">link</a></p>
    +<p><a href="&lt;foo(and(bar">link</a>&gt;)</p>
    
    Example 502 (lines 7715-7719) Links
    [link](foo\)\:)
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><a href="foo):">link</a></p>
    +<p><a href="foo\">link</a>:)</p>
    
    Example 504 (lines 7740-7744) Links
    [link](foo\bar)
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><a href="foo%5Cbar">link</a></p>
    +<p><a href="foo\bar">link</a></p>
    
    Example 505 (lines 7756-7760) Links
    [link](foo%20b&auml;)
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><a href="foo%20b%C3%A4">link</a></p>
    +<p><a href="foo%20bä">link</a></p>
    
    Example 506 (lines 7767-7771) Links
    [link]("title")
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><a href="%22title%22">link</a></p>
    +<p><a href="&quot;title&quot;">link</a></p>
    
    Example 507 (lines 7776-7784) Links
    [link](/url "title")
    [link](/url 'title')
    [link](/url (title))
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><a href="/url" title="title">link</a> <a href="/url" title="title">link</a> <a href="/url" title="title">link</a></p>
    +<p><a href="/url" title="title">link</a> <a href="/url" title="title">link</a> [link](/url (title))</p>
    
    Example 508 (lines 7790-7794) Links
    [link](/url "title \"&quot;")
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><a href="/url" title="title &quot;&quot;">link</a></p>
    +<p>[link](/url &quot;title &quot;&amp;quot;&quot;)</p>
    
    Example 509 (lines 7801-7805) Links
    [link](/url "title")
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><a href="/url%C2%A0%22title%22">link</a></p>
    +<p>[link](/url &quot;title&quot;)</p>
    
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
    
    Example 518 (lines 7895-7899) Links
    [link *foo **bar** `#`*](/uri)
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><a href="/uri">link <em>foo <strong>bar</strong> <code>#</code></em></a></p>
    +<p>[link <em>foo <strong>bar</strong> <code>#</code></em>](/uri)</p>
    
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
    +<p>!<a href="uri1">[[foo</a>](uri2)](uri3)</p>
    
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
    
    Example 529 (lines 8014-8020) Links
    [foo][bar]
    
    [bar]: /url "title"
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><a href="/url" title="title">foo</a></p>
    +<p>[foo][bar]</p>
    
    Example 530 (lines 8029-8035) Links
    [link [foo [bar]]][ref]
    
    [ref]: /uri
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><a href="/uri">link [foo [bar]]</a></p>
    +<p>[link [foo [bar]]][ref]</p>
    
    Example 531 (lines 8038-8044) Links
    [link \[bar][ref]
    
    [ref]: /uri
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><a href="/uri">link [bar</a></p>
    +<p>[link [bar][ref]</p>
    
    Example 532 (lines 8049-8055) Links
    [link *foo **bar** `#`*][ref]
    
    [ref]: /uri
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><a href="/uri">link <em>foo <strong>bar</strong> <code>#</code></em></a></p>
    +<p>[link <em>foo <strong>bar</strong> <code>#</code></em>][ref]</p>
    
    Example 533 (lines 8058-8064) Links
    [![moon](moon.jpg)][ref]
    
    [ref]: /uri
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><a href="/uri"><img alt="moon" src="moon.jpg"></a></p>
    +<p><a href="moon.jpg">![moon</a>][ref]</p>
    
    Example 534 (lines 8069-8075) Links
    [foo [bar](/uri)][ref]
    
    [ref]: /uri
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>[foo <a href="/uri">bar</a>]<a href="/uri">ref</a></p>
    +<p><a href="/uri">foo [bar</a>][ref]</p>
    
    Example 535 (lines 8078-8084) Links
    [foo *bar [baz][ref]*][ref]
    
    [ref]: /uri
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>[foo <em>bar <a href="/uri">baz</a></em>]<a href="/uri">ref</a></p>
    +<p>[foo <em>bar [baz][ref]</em>][ref]</p>
    
    Example 536 (lines 8093-8099) Links
    *[foo*][ref]
    
    [ref]: /uri
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>*<a href="/uri">foo*</a></p>
    +<p><em>[foo</em>][ref]</p>
    
    Example 537 (lines 8102-8108) Links
    [foo *bar][ref]*
    
    [ref]: /uri
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><a href="/uri">foo *bar</a>*</p>
    +<p>[foo <em>bar][ref]</em></p>
    
    Example 540 (lines 8132-8138) Links
    [foo<https://example.com/?search=][ref]>
    
    [ref]: /uri
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>[foo<a href="https://example.com/?search=%5D%5Bref%5D">https://example.com/?search=][ref]</a></p>
    +<p>[foo<a href="https://example.com/?search=][ref]">https://example.com/?search=][ref]</a></p>
    
    Example 541 (lines 8143-8149) Links
    [foo][BaR]
    
    [bar]: /url "title"
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><a href="/url" title="title">foo</a></p>
    +<p>[foo][BaR]</p>
    
    Example 542 (lines 8154-8160) Links
    [ẞ]
    
    [SS]: /url
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><a href="/url">ẞ</a></p>
    +<p>[ẞ]</p>
    
    Example 543 (lines 8166-8173) Links
    [Foo
      bar]: /url
    
    [Baz][Foo bar]
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><a href="/url">Baz</a></p>
    +<p>[Foo bar]: /url</p><p>[Baz][Foo bar]</p>
    
    Example 544 (lines 8179-8185) Links
    [foo] [bar]
    
    [bar]: /url "title"
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>[foo] <a href="/url" title="title">bar</a></p>
    +<p>[foo] [bar]</p>
    
    Example 545 (lines 8188-8196) Links
    [foo]
    [bar]
    
    [bar]: /url "title"
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>[foo] <a href="/url" title="title">bar</a></p>
    +<p>[foo] [bar]</p>
    
    Example 546 (lines 8229-8237) Links
    [foo]: /url1
    
    [foo]: /url2
    
    [bar][foo]
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><a href="/url1">bar</a></p>
    +<p>[bar][foo]</p>
    
    Example 548 (lines 8256-8263) Links
    [foo][ref[]
    
    [ref[]: /uri
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>[foo][ref[]</p><p>[ref[]: /uri</p>
    +<p>[foo][ref[]</p>
    
    Example 551 (lines 8286-8292) Links
    [foo][ref\[]
    
    [ref\[]: /uri
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><a href="/uri">foo</a></p>
    +<p>[foo][ref[]</p>
    
    Example 552 (lines 8297-8303) Links
    [bar\\]: /uri
    
    [bar\\]
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><a href="/uri">bar\</a></p>
    +<p>[bar\]</p>
    
    Example 555 (lines 8342-8348) Links
    [foo][]
    
    [foo]: /url "title"
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><a href="/url" title="title">foo</a></p>
    +<p>[foo][]</p>
    
    Example 556 (lines 8351-8357) Links
    [*foo* bar][]
    
    [*foo* bar]: /url "title"
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><a href="/url" title="title"><em>foo</em> bar</a></p>
    +<p>[<em>foo</em> bar][]</p>
    
    Example 557 (lines 8362-8368) Links
    [Foo][]
    
    [foo]: /url "title"
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><a href="/url" title="title">Foo</a></p>
    +<p>[Foo][]</p>
    
    Example 558 (lines 8375-8383) Links
    [foo] 
    []
    
    [foo]: /url "title"
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><a href="/url" title="title">foo</a> []</p>
    +<p>[foo] []</p>
    
    Example 559 (lines 8395-8401) Links
    [foo]
    
    [foo]: /url "title"
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><a href="/url" title="title">foo</a></p>
    +<p>[foo]</p>
    
    Example 560 (lines 8404-8410) Links
    [*foo* bar]
    
    [*foo* bar]: /url "title"
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><a href="/url" title="title"><em>foo</em> bar</a></p>
    +<p>[<em>foo</em> bar]</p>
    
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
    
    Example 563 (lines 8433-8439) Links
    [Foo]
    
    [foo]: /url "title"
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><a href="/url" title="title">Foo</a></p>
    +<p>[Foo]</p>
    
    Example 564 (lines 8444-8450) Links
    [foo] bar
    
    [foo]: /url
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><a href="/url">foo</a> bar</p>
    +<p>[foo] bar</p>
    
    Example 566 (lines 8468-8474) Links
    [foo*]: /url
    
    *[foo*]
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>*<a href="/url">foo*</a></p>
    +<p><em>[foo</em>]</p>
    
    Example 567 (lines 8480-8487) Links
    [foo][bar]
    
    [foo]: /url1
    [bar]: /url2
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><a href="/url2">foo</a></p>
    +<p>[foo][bar]</p>
    
    Example 568 (lines 8489-8495) Links
    [foo][]
    
    [foo]: /url1
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><a href="/url1">foo</a></p>
    +<p>[foo][]</p>
    
    Example 570 (lines 8507-8513) Links
    [foo](not a link)
    
    [foo]: /url1
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><a href="/url1">foo</a>(not a link)</p>
    +<p>[foo](not a link)</p>
    
    Example 571 (lines 8518-8524) Links
    [foo][bar][baz]
    
    [baz]: /url
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>[foo]<a href="/url">bar</a></p>
    +<p>[foo][bar][baz]</p>
    
    Example 572 (lines 8530-8537) Links
    [foo][bar][baz]
    
    [baz]: /url1
    [bar]: /url2
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><a href="/url2">foo</a><a href="/url1">baz</a></p>
    +<p>[foo][bar][baz]</p>
    
    Example 573 (lines 8543-8550) Links
    [foo][bar][baz]
    
    [baz]: /url1
    [foo]: /url2
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>[foo]<a href="/url1">bar</a></p>
    +<p>[foo][bar][baz]</p>
    
    33 passed, 84 failed, 0 errored, 538 skipped
  stderr:
    --- drydock: progress ---
    cases: pass=33 fail=84 error=0 skip=538 total=655 from=result.stdout
    --- drydock: end progress ---
    --- drydock: values at failure ---
      result = CompletedProcess(args=['/mnt/c/Users/barlo/projects/drydock/.venv/bin/python', 'sources/spec_tests.py', '--program', '/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.022726/build/commonmark/commonmark', '--spec', 'sources/spec.txt', '--pattern', '^(Links|Link reference definitions)$'], returncode=84, stdout='Example 194 (lines 3201-3207) Link reference definitions\n[foo]: /url "ti… (+17681 chars)
    --- drydock: end values ---
    Traceback (most recent call last):
      File "links-conformance.py", line 12, in <module>
        assert result.returncode == 0
               ^^^^^^^^^^^^^^^^^^^^^^
    AssertionError

## Post-build programmatic acceptance
- FAIL: links-conformance (FEATURE-Links.md)
  intent: The completed parser passes the authoritative link and link-reference-definition examples.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/.venv/bin/python
  provisioning: not required
  return code: 1
  stdout:
    Example 212 (lines 3415-3420) Link reference definitions
    [foo]: /url
    "title" ok
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>&quot;title&quot; ok</p>
    +<p>[foo]: /url &quot;title&quot; ok</p>
    
    Example 218 (lines 3491-3498) Link reference definitions
    [foo]: /url
    ===
    [foo]
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>=== <a href="/url">foo</a></p>
    +<p>===</p><p><a href="/url">foo</a></p>
    
    Example 495 (lines 7652-7656) Links
    [link](<foo\>)
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>[link](&lt;foo&gt;)</p>
    +<p>[link](<foo\>)</p>
    
    Example 496 (lines 7661-7669) Links
    [a](<b)c
    [a](<b)c>
    [a](<b>c)
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>[a](&lt;b)c [a](&lt;b)c&gt; [a](<b>c)</p>
    +<p>[a](&lt;b)c [a](<b)c> [a](<b>c)</p>
    
    Example 522 (lines 7925-7929) Links
    ![[[foo](uri1)](uri2)](uri3)
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><img alt="[foo](uri2)" src="uri3"></p>
    +<p><img alt="[[foo](uri1)](uri2)" src="uri3"></p>
    
    Example 528 (lines 7976-7980) Links
    [foo<https://example.com/?search=](uri)>
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>[foo<a href="https://example.com/?search=%5D(uri)">https://example.com/?search=](uri)</a></p>
    +<p>[foo<a href="https://example.com/?search=](uri)">https://example.com/?search=](uri)</a></p>
    
    Example 540 (lines 8132-8138) Links
    [foo<https://example.com/?search=][ref]>
    
    [ref]: /uri
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>[foo<a href="https://example.com/?search=%5D%5Bref%5D">https://example.com/?search=][ref]</a></p>
    +<p>[foo<a href="https://example.com/?search=][ref]">https://example.com/?search=][ref]</a></p>
    
    110 passed, 7 failed, 0 errored, 538 skipped
  stderr:
    --- drydock: progress ---
    cases: pass=110 fail=7 error=0 skip=538 total=655 from=result.stdout
    --- drydock: end progress ---
    --- drydock: values at failure ---
      result = CompletedProcess(args=['/mnt/c/Users/barlo/projects/drydock/.venv/bin/python', 'sources/spec_tests.py', '--program', '/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.022726/build/commonmark/commonmark', '--spec', 'sources/spec.txt', '--pattern', '^(Links|Link reference definitions)$'], returncode=7, stdout='Example 212 (lines 3415-3420) Link reference definitions\n[foo]: /url\n"ti… (+1669 chars)
    --- drydock: end values ---
    Traceback (most recent call last):
      File "links-conformance.py", line 12, in <module>
        assert result.returncode == 0
               ^^^^^^^^^^^^^^^^^^^^^^
    AssertionError

## Repair attempts
- attempt 0 (initial build): failed; 0/1 checks; 87/117 cases model=gpt-6-luna; execution 20261027.030209.875Z-f370f157; reason: programmatic acceptance failed: links-conformance
- attempt 1 (repair 1): failed; 0/1 checks; 95/117 cases model=gpt-6-luna; execution 20261027.030534.018Z-28da1225; reason: programmatic acceptance failed: links-conformance
- attempt 2 (repair 2): failed; 0/1 checks; 100/117 cases model=gpt-6-luna; execution 20261027.030854.040Z-64623b43; reason: programmatic acceptance failed: links-conformance
- attempt 3 (repair 3): failed; 0/1 checks; 103/117 cases model=gpt-6-luna; execution 20261027.031259.938Z-aaad97d1; reason: programmatic acceptance failed: links-conformance
- attempt 4 (repair 4): failed; 0/1 checks; 110/117 cases model=gpt-6-luna; execution 20261027.031617.935Z-e0b98fc8; reason: programmatic acceptance failed: links-conformance
- attempt 5 (repair 5): failed; 0/1 checks; 110/117 cases model=gpt-6-luna; execution 20261027.032014.335Z-4510e086; reason: programmatic acceptance failed: links-conformance
- attempt 6 (repair 6): failed; 0/1 checks; 110/117 cases model=gpt-6-luna; execution 20261027.032209.085Z-31db92e4; stopped: deterministic acceptance score did not improve on 2 consecutive calls; reason: programmatic acceptance failed: links-conformance

## Agent self-report (advisory)
The build agent declared a failure. This report is advisory; Drydock's execution and deterministic checks determine the block's outcome.
- summary: Scoped link conformance still fails
- detail:
    After the setext change, cases 212, 218, 495, 496, 522, 528, and 540 remain failing. Fix the shared reference collection and link bracket/autolink parsing behavior, then rerun the scoped conformance suite.

## Failure
- summary: programmatic acceptance failed: links-conformance
- detail:
    Block "Block 10 · Service" [block-10] failed its acceptance criteria.
      Story "Parse inline and reference links." [links] does not meet its own acceptance criteria:
        - AC links-conformance — The completed parser passes the authoritative link and link-reference-definition examples.
            assertion: assert result.returncode == 0 → AssertionError
            cases: pass=110 fail=7 error=0 skip=538 total=655 from=result.stdout
            raised at: links-conformance.py:12
            process exit code: 1
            values at failure:
              result = CompletedProcess(args=['/mnt/c/Users/barlo/projects/drydock/.venv/bin/python', 'sources/spec_tests.py', '--program', '/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.022726/build/commonmark/commonmark', '--spec', 'sources/spec.txt', '--pattern', '^(Links|Link reference definitions)$'], returncode=7, stdout='Example 212 (lines 3415-3420) Link reference definitions\n[foo]: /url\n"ti… (+1669 chars)
            observed output:
              @@ -1 +1 @@
              -<p>[foo<a href="https://example.com/?search=%5D(uri)">https://example.com/?search=](uri)</a></p>
              +<p>[foo<a href="https://example.com/?search=](uri)">https://example.com/?search=](uri)</a></p>
              Example 540 (lines 8132-8138) Links
              [foo<https://example.com/?search=][ref]>
              [ref]: /uri
              --- expected HTML
              +++ actual HTML
              @@ -1 +1 @@
              -<p>[foo<a href="https://example.com/?search=%5D%5Bref%5D">https://example.com/?search=][ref]</a></p>
              +<p>[foo<a href="https://example.com/?search=][ref]">https://example.com/?search=][ref]</a></p>
              110 passed, 7 failed, 0 errored, 538 skipped
              … 44 earlier line(s) omitted, --full for all
            check stderr:
              Traceback (most recent call last):
                File "links-conformance.py", line 12, in <module>
                  assert result.returncode == 0
                         ^^^^^^^^^^^^^^^^^^^^^^
              AssertionError

## Build summary
RESULT: FAILED

FILES CHANGED:
- commonmark_parser/stages.py

SUMMARY:
Adjusted setext handling when a paragraph contains only a reference definition. The scoped conformance suite still has failures, so this repair is incomplete.

BLOCKERS:
- Link reference definitions with a title on the following line and setext underline handling still fail. Several link parsing cases also remain unresolved.

FAILURE_SUMMARY: Scoped link conformance still fails
FAILURE_DETAIL: After the setext change, cases 212, 218, 495, 496, 522, 528, and 540 remain failing. Fix the shared reference collection and link bracket/autolink parsing behavior, then rerun the scoped conformance suite.
