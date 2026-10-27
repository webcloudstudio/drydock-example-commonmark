# Evidence: Block 9 · Service (block-9)

- block type: block
- date: 2026-10-26
- resulting state: closed/verified
- story points (combined assembled cost): 2998
- execution id: 20261027.025756.879Z-fcca2a90

## Stories built
- Resolve emphasis and strong emphasis. (emphasis) [story]

## Acceptance tooling authorization
- FEATURE-Emphasis.md#emphasis-conformance: executable=python3; scope=test; authorization=existing Target environment

## Stacked context
- stack: python_compact.md (SP 601)
- compass: COMPASS.md (SP 512)
- implements: FEATURE-Emphasis.md (SP 514)
- context: ARCHITECTURE_compact.md (SP 211)
- stack: common_compact.md (SP 1079)

## Build directory changes
- commonmark_parser/inline.py
- tests/test_emphasis.py

## Pre-build acceptance observation
- RED: emphasis-conformance (FEATURE-Emphasis.md)
  intent: The completed inline parser passes the authoritative emphasis and strong-emphasis examples.
  return code: 1
  stdout:
    Example 352 (lines 6330-6334) Emphasis and strong emphasis
    *foo bar*
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><em>foo bar</em></p>
    +<p>*foo bar*</p>
    
    Example 357 (lines 6387-6391) Emphasis and strong emphasis
    foo*bar*
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>foo<em>bar</em></p>
    +<p>foo*bar*</p>
    
    Example 358 (lines 6394-6398) Emphasis and strong emphasis
    5*6*78
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>5<em>6</em>78</p>
    +<p>5*6*78</p>
    
    Example 359 (lines 6403-6407) Emphasis and strong emphasis
    _foo bar_
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><em>foo bar</em></p>
    +<p>_foo bar_</p>
    
    Example 366 (lines 6467-6471) Emphasis and strong emphasis
    foo-_(bar)_
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>foo-<em>(bar)</em></p>
    +<p>foo-_(bar)_</p>
    
    Example 371 (lines 6521-6525) Emphasis and strong emphasis
    *(*foo*)*
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><em>(<em>foo</em>)</em></p>
    +<p>*(*foo*)*</p>
    
    Example 372 (lines 6530-6534) Emphasis and strong emphasis
    *foo*bar
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><em>foo</em>bar</p>
    +<p>*foo*bar</p>
    
    Example 375 (lines 6562-6566) Emphasis and strong emphasis
    _(_foo_)_
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><em>(<em>foo</em>)</em></p>
    +<p>_(_foo_)_</p>
    
    Example 378 (lines 6585-6589) Emphasis and strong emphasis
    _foo_bar_baz_
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><em>foo_bar_baz</em></p>
    +<p>_foo_bar_baz_</p>
    
    Example 379 (lines 6596-6600) Emphasis and strong emphasis
    _(bar)_.
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><em>(bar)</em>.</p>
    +<p>_(bar)_.</p>
    
    Example 380 (lines 6605-6609) Emphasis and strong emphasis
    **foo bar**
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><strong>foo bar</strong></p>
    +<p>**foo bar**</p>
    
    Example 383 (lines 6635-6639) Emphasis and strong emphasis
    foo**bar**
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>foo<strong>bar</strong></p>
    +<p>foo**bar**</p>
    
    Example 384 (lines 6644-6648) Emphasis and strong emphasis
    __foo bar__
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><strong>foo bar</strong></p>
    +<p>__foo bar__</p>
    
    Example 391 (lines 6704-6708) Emphasis and strong emphasis
    __foo, __bar__, baz__
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><strong>foo, <strong>bar</strong>, baz</strong></p>
    +<p>__foo, __bar__, baz__</p>
    
    Example 392 (lines 6715-6719) Emphasis and strong emphasis
    foo-__(bar)__
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>foo-<strong>(bar)</strong></p>
    +<p>foo-__(bar)__</p>
    
    Example 395 (lines 6751-6755) Emphasis and strong emphasis
    *(**foo**)*
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><em>(<strong>foo</strong>)</em></p>
    +<p>*(**foo**)*</p>
    
    Example 396 (lines 6758-6764) Emphasis and strong emphasis
    **Gomphocarpus (*Gomphocarpus physocarpus*, syn.
    *Asclepias physocarpa*)**
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><strong>Gomphocarpus (<em>Gomphocarpus physocarpus</em>, syn. <em>Asclepias physocarpa</em>)</strong></p>
    +<p>**Gomphocarpus (*Gomphocarpus physocarpus*, syn. *Asclepias physocarpa*)**</p>
    
    Example 397 (lines 6767-6771) Emphasis and strong emphasis
    **foo "*bar*" foo**
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><strong>foo &quot;<em>bar</em>&quot; foo</strong></p>
    +<p>**foo &quot;*bar*&quot; foo**</p>
    
    Example 398 (lines 6776-6780) Emphasis and strong emphasis
    **foo**bar
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><strong>foo</strong>bar</p>
    +<p>**foo**bar</p>
    
    Example 401 (lines 6808-6812) Emphasis and strong emphasis
    _(__foo__)_
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><em>(<strong>foo</strong>)</em></p>
    +<p>_(__foo__)_</p>
    
    Example 404 (lines 6831-6835) Emphasis and strong emphasis
    __foo__bar__baz__
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><strong>foo__bar__baz</strong></p>
    +<p>__foo__bar__baz__</p>
    
    Example 405 (lines 6842-6846) Emphasis and strong emphasis
    __(bar)__.
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><strong>(bar)</strong>.</p>
    +<p>__(bar)__.</p>
    
    Example 406 (lines 6854-6858) Emphasis and strong emphasis
    *foo [bar](/url)*
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><em>foo <a href="/url">bar</a></em></p>
    +<p>*foo [bar](/url)*</p>
    
    Example 407 (lines 6861-6867) Emphasis and strong emphasis
    *foo
    bar*
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><em>foo bar</em></p>
    +<p>*foo bar*</p>
    
    Example 408 (lines 6873-6877) Emphasis and strong emphasis
    _foo __bar__ baz_
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><em>foo <strong>bar</strong> baz</em></p>
    +<p>_foo __bar__ baz_</p>
    
    Example 409 (lines 6880-6884) Emphasis and strong emphasis
    _foo _bar_ baz_
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><em>foo <em>bar</em> baz</em></p>
    +<p>_foo _bar_ baz_</p>
    
    Example 410 (lines 6887-6891) Emphasis and strong emphasis
    __foo_ bar_
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><em><em>foo</em> bar</em></p>
    +<p>__foo_ bar_</p>
    
    Example 411 (lines 6894-6898) Emphasis and strong emphasis
    *foo *bar**
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><em>foo <em>bar</em></em></p>
    +<p>*foo *bar**</p>
    
    Example 412 (lines 6901-6905) Emphasis and strong emphasis
    *foo **bar** baz*
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><em>foo <strong>bar</strong> baz</em></p>
    +<p>*foo **bar** baz*</p>
    
    Example 413 (lines 6907-6911) Emphasis and strong emphasis
    *foo**bar**baz*
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><em>foo<strong>bar</strong>baz</em></p>
    +<p>*foo**bar**baz*</p>
    
    Example 414 (lines 6931-6935) Emphasis and strong emphasis
    *foo**bar*
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><em>foo**bar</em></p>
    +<p>*foo**bar*</p>
    
    Example 415 (lines 6944-6948) Emphasis and strong emphasis
    ***foo** bar*
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><em><strong>foo</strong> bar</em></p>
    +<p>***foo** bar*</p>
    
    Example 416 (lines 6951-6955) Emphasis and strong emphasis
    *foo **bar***
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><em>foo <strong>bar</strong></em></p>
    +<p>*foo **bar***</p>
    
    Example 417 (lines 6958-6962) Emphasis and strong emphasis
    *foo**bar***
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><em>foo<strong>bar</strong></em></p>
    +<p>*foo**bar***</p>
    
    Example 418 (lines 6969-6973) Emphasis and strong emphasis
    foo***bar***baz
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>foo<em><strong>bar</strong></em>baz</p>
    +<p>foo***bar***baz</p>
    
    Example 419 (lines 6975-6979) Emphasis and strong emphasis
    foo******bar*********baz
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>foo<strong><strong><strong>bar</strong></strong></strong>***baz</p>
    +<p>foo******bar*********baz</p>
    
    Example 420 (lines 6984-6988) Emphasis and strong emphasis
    *foo **bar *baz* bim** bop*
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><em>foo <strong>bar <em>baz</em> bim</strong> bop</em></p>
    +<p>*foo **bar *baz* bim** bop*</p>
    
    Example 421 (lines 6991-6995) Emphasis and strong emphasis
    *foo [*bar*](/url)*
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><em>foo <a href="/url"><em>bar</em></a></em></p>
    +<p>*foo [*bar*](/url)*</p>
    
    Example 424 (lines 7020-7024) Emphasis and strong emphasis
    **foo [bar](/url)**
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><strong>foo <a href="/url">bar</a></strong></p>
    +<p>**foo [bar](/url)**</p>
    
    Example 425 (lines 7027-7033) Emphasis and strong emphasis
    **foo
    bar**
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><strong>foo bar</strong></p>
    +<p>**foo bar**</p>
    
    Example 426 (lines 7039-7043) Emphasis and strong emphasis
    __foo _bar_ baz__
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><strong>foo <em>bar</em> baz</strong></p>
    +<p>__foo _bar_ baz__</p>
    
    Example 427 (lines 7046-7050) Emphasis and strong emphasis
    __foo __bar__ baz__
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><strong>foo <strong>bar</strong> baz</strong></p>
    +<p>__foo __bar__ baz__</p>
    
    Example 428 (lines 7053-7057) Emphasis and strong emphasis
    ____foo__ bar__
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><strong><strong>foo</strong> bar</strong></p>
    +<p>____foo__ bar__</p>
    
    Example 429 (lines 7060-7064) Emphasis and strong emphasis
    **foo **bar****
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><strong>foo <strong>bar</strong></strong></p>
    +<p>**foo **bar****</p>
    
    Example 430 (lines 7067-7071) Emphasis and strong emphasis
    **foo *bar* baz**
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><strong>foo <em>bar</em> baz</strong></p>
    +<p>**foo *bar* baz**</p>
    
    Example 431 (lines 7074-7078) Emphasis and strong emphasis
    **foo*bar*baz**
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><strong>foo<em>bar</em>baz</strong></p>
    +<p>**foo*bar*baz**</p>
    
    Example 432 (lines 7081-7085) Emphasis and strong emphasis
    ***foo* bar**
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><strong><em>foo</em> bar</strong></p>
    +<p>***foo* bar**</p>
    
    Example 433 (lines 7088-7092) Emphasis and strong emphasis
    **foo *bar***
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><strong>foo <em>bar</em></strong></p>
    +<p>**foo *bar***</p>
    
    Example 434 (lines 7097-7103) Emphasis and strong emphasis
    **foo *bar **baz**
    bim* bop**
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><strong>foo <em>bar <strong>baz</strong> bim</em> bop</strong></p>
    +<p>**foo *bar **baz** bim* bop**</p>
    
    Example 435 (lines 7106-7110) Emphasis and strong emphasis
    **foo [*bar*](/url)**
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><strong>foo <a href="/url"><em>bar</em></a></strong></p>
    +<p>**foo [*bar*](/url)**</p>
    
    Example 439 (lines 7139-7143) Emphasis and strong emphasis
    foo *\**
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>foo <em>*</em></p>
    +<p>foo ***</p>
    
    Example 440 (lines 7146-7150) Emphasis and strong emphasis
    foo *_*
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>foo <em>_</em></p>
    +<p>foo *_*</p>
    
    Example 442 (lines 7160-7164) Emphasis and strong emphasis
    foo **\***
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>foo <strong>*</strong></p>
    +<p>foo *****</p>
    
    Example 443 (lines 7167-7171) Emphasis and strong emphasis
    foo **_**
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>foo <strong>_</strong></p>
    +<p>foo **_**</p>
    
    Example 444 (lines 7178-7182) Emphasis and strong emphasis
    **foo*
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>*<em>foo</em></p>
    +<p>**foo*</p>
    
    Example 445 (lines 7185-7189) Emphasis and strong emphasis
    *foo**
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><em>foo</em>*</p>
    +<p>*foo**</p>
    
    Example 446 (lines 7192-7196) Emphasis and strong emphasis
    ***foo**
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>*<strong>foo</strong></p>
    +<p>***foo**</p>
    
    Example 447 (lines 7199-7203) Emphasis and strong emphasis
    ****foo*
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>***<em>foo</em></p>
    +<p>****foo*</p>
    
    Example 448 (lines 7206-7210) Emphasis and strong emphasis
    **foo***
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><strong>foo</strong>*</p>
    +<p>**foo***</p>
    
    Example 449 (lines 7213-7217) Emphasis and strong emphasis
    *foo****
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><em>foo</em>***</p>
    +<p>*foo****</p>
    
    Example 451 (lines 7230-7234) Emphasis and strong emphasis
    foo _\__
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>foo <em>_</em></p>
    +<p>foo ___</p>
    
    Example 452 (lines 7237-7241) Emphasis and strong emphasis
    foo _*_
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>foo <em>*</em></p>
    +<p>foo _*_</p>
    
    Example 454 (lines 7251-7255) Emphasis and strong emphasis
    foo __\___
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>foo <strong>_</strong></p>
    +<p>foo _____</p>
    
    Example 455 (lines 7258-7262) Emphasis and strong emphasis
    foo __*__
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>foo <strong>*</strong></p>
    +<p>foo __*__</p>
    
    Example 456 (lines 7265-7269) Emphasis and strong emphasis
    __foo_
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>_<em>foo</em></p>
    +<p>__foo_</p>
    
    Example 457 (lines 7276-7280) Emphasis and strong emphasis
    _foo__
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><em>foo</em>_</p>
    +<p>_foo__</p>
    
    Example 458 (lines 7283-7287) Emphasis and strong emphasis
    ___foo__
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>_<strong>foo</strong></p>
    +<p>___foo__</p>
    
    Example 459 (lines 7290-7294) Emphasis and strong emphasis
    ____foo_
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>___<em>foo</em></p>
    +<p>____foo_</p>
    
    Example 460 (lines 7297-7301) Emphasis and strong emphasis
    __foo___
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><strong>foo</strong>_</p>
    +<p>__foo___</p>
    
    Example 461 (lines 7304-7308) Emphasis and strong emphasis
    _foo____
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><em>foo</em>___</p>
    +<p>_foo____</p>
    
    Example 462 (lines 7314-7318) Emphasis and strong emphasis
    **foo**
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><strong>foo</strong></p>
    +<p>**foo**</p>
    
    Example 463 (lines 7321-7325) Emphasis and strong emphasis
    *_foo_*
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><em><em>foo</em></em></p>
    +<p>*_foo_*</p>
    
    Example 464 (lines 7328-7332) Emphasis and strong emphasis
    __foo__
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><strong>foo</strong></p>
    +<p>__foo__</p>
    
    Example 465 (lines 7335-7339) Emphasis and strong emphasis
    _*foo*_
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><em><em>foo</em></em></p>
    +<p>_*foo*_</p>
    
    Example 466 (lines 7345-7349) Emphasis and strong emphasis
    ****foo****
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><strong><strong>foo</strong></strong></p>
    +<p>****foo****</p>
    
    Example 467 (lines 7352-7356) Emphasis and strong emphasis
    ____foo____
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><strong><strong>foo</strong></strong></p>
    +<p>____foo____</p>
    
    Example 468 (lines 7363-7367) Emphasis and strong emphasis
    ******foo******
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><strong><strong><strong>foo</strong></strong></strong></p>
    +<p>******foo******</p>
    
    Example 469 (lines 7372-7376) Emphasis and strong emphasis
    ***foo***
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><em><strong>foo</strong></em></p>
    +<p>***foo***</p>
    
    Example 470 (lines 7379-7383) Emphasis and strong emphasis
    _____foo_____
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><em><strong><strong>foo</strong></strong></em></p>
    +<p>_____foo_____</p>
    
    Example 471 (lines 7388-7392) Emphasis and strong emphasis
    *foo _bar* baz_
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><em>foo _bar</em> baz_</p>
    +<p>*foo _bar* baz_</p>
    
    Example 472 (lines 7395-7399) Emphasis and strong emphasis
    *foo __bar *baz bim__ bam*
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><em>foo <strong>bar *baz bim</strong> bam</em></p>
    +<p>*foo __bar *baz bim__ bam*</p>
    
    Example 473 (lines 7404-7408) Emphasis and strong emphasis
    **foo **bar baz**
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>**foo <strong>bar baz</strong></p>
    +<p>**foo **bar baz**</p>
    
    Example 474 (lines 7411-7415) Emphasis and strong emphasis
    *foo *bar baz*
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>*foo <em>bar baz</em></p>
    +<p>*foo *bar baz*</p>
    
    Example 475 (lines 7420-7424) Emphasis and strong emphasis
    *[bar*](/url)
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>*<a href="/url">bar*</a></p>
    +<p>*[bar*](/url)</p>
    
    Example 476 (lines 7427-7431) Emphasis and strong emphasis
    _foo [bar_](/url)
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>_foo <a href="/url">bar_</a></p>
    +<p>_foo [bar_](/url)</p>
    
    Example 480 (lines 7455-7459) Emphasis and strong emphasis
    *a `*`*
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><em>a <code>*</code></em></p>
    +<p>*a <code>*</code>*</p>
    
    Example 481 (lines 7462-7466) Emphasis and strong emphasis
    _a `_`_
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><em>a <code>_</code></em></p>
    +<p>_a <code>_</code>_</p>
    
    45 passed, 87 failed, 0 errored, 523 skipped
  stderr:
    --- drydock: progress ---
    cases: pass=45 fail=87 error=0 skip=523 total=655 from=result.stdout
    --- drydock: end progress ---
    --- drydock: values at failure ---
      result = CompletedProcess(args=['/mnt/c/Users/barlo/projects/drydock/.venv/bin/python', 'sources/spec_tests.py', '--program', '/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.022726/build/commonmark/commonmark', '--spec', 'sources/spec.txt', '--pattern', '^Emphasis and strong emphasis$'], returncode=87, stdout='Example 352 (lines 6330-6334) Emphasis and strong emphasis\n*foo bar*\n\n--- ex… (+16478 chars)
    --- drydock: end values ---
    Traceback (most recent call last):
      File "emphasis-conformance.py", line 12, in <module>
        assert result.returncode == 0
               ^^^^^^^^^^^^^^^^^^^^^^
    AssertionError

## Post-build programmatic acceptance
- PASS: emphasis-conformance (FEATURE-Emphasis.md)
  intent: The completed inline parser passes the authoritative emphasis and strong-emphasis examples.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/.venv/bin/python
  provisioning: not required
  return code: 0
  stdout:
    132 passed, 0 failed, 0 errored, 523 skipped

## Repair attempts
- attempt 0 (initial build): failed; 0/1 checks; 118/132 cases model=gpt-6-luna; execution 20261027.025004.362Z-7346629c; reason: programmatic acceptance failed: emphasis-conformance
- attempt 1 (repair 1): failed; 1/1 checks; 132/132 cases model=gpt-6-luna; execution 20261027.025349.526Z-50c875db; reason: acceptance regression: code-spans-conformance
- attempt 2 (repair 2): built; 1/1 checks; 132/132 cases model=gpt-6-luna; execution 20261027.025756.879Z-fcca2a90

## Build summary
RESULT: SUCCESS

FILES CHANGED:
- commonmark_parser/inline.py

SUMMARY:
Fixed unmatched backtick runs so suffixes cannot become code-span openers, and prevented link parsing from consuming syntax containing backticks. The code-span conformance suite passed: 22 passed, 0 failed, 633 skipped. The emphasis conformance run did not finish within the command’s 30-second wait.

BLOCKERS:
- None
