# Evidence: Block 9 · Service (block-9)

- block type: block
- date: 2026-08-12
- resulting state: closed/verified
- story points (combined assembled cost): 57681
- execution id: 20260812.183141.501Z-327e3cd9

## Stories built
- Parse emphasis and strong emphasis using delimiter rules. (inline-emphasis) [story]

## Stacked context
- compass: COMPASS.md (SP 1263)
- implements: FEATURE-INLINE-EMPHASIS.md (SP 414)
- context: spec.txt (SP 51527)
- context: spec_tests.py (SP 1609)
- context: ARCHITECTURE_compact.md (SP 116)
- stack: common_compact.md (SP 1179)
- stack: python_compact.md (SP 1534)

## Build directory changes
- renderer/html.py
- test_inline_emphasis.py

## Pre-build acceptance observation
- RED: emphasis-delimiters (FEATURE-INLINE-EMPHASIS.md)
  intent: The implementation passes delimiter-run, flanking, intraword, and modulo-three emphasis examples.
  return code: 1
  stdout:
    Example 356 (lines 6369-6382) Emphasis and strong emphasis
    *$*alpha.
    
    *£*bravo.
    
    *€*charlie.
    
    *𞋿*delta.
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>*$*alpha.</p><p>*£*bravo.</p><p>*€*charlie.</p><p>*𞋿*delta.</p>
    +<p><em>$</em>alpha.</p><p><em>£</em>bravo.</p><p><em>€</em>charlie.</p><p><em>𞋿</em>delta.</p>
    
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
    
    Example 370 (lines 6511-6515) Emphasis and strong emphasis
    *(*foo)
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>*(*foo)</p>
    +<p><em>(</em>foo)</p>
    
    Example 371 (lines 6521-6525) Emphasis and strong emphasis
    *(*foo*)*
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><em>(<em>foo</em>)</em></p>
    +<p><em>(</em>foo*)*</p>
    
    Example 374 (lines 6553-6557) Emphasis and strong emphasis
    _(_foo)
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>_(_foo)</p>
    +<p><em>(</em>foo)</p>
    
    Example 375 (lines 6562-6566) Emphasis and strong emphasis
    _(_foo_)_
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><em>(<em>foo</em>)</em></p>
    +<p><em>(</em>foo_)_</p>
    
    Example 376 (lines 6571-6575) Emphasis and strong emphasis
    _foo_bar
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>_foo_bar</p>
    +<p><em>foo</em>bar</p>
    
    Example 377 (lines 6578-6582) Emphasis and strong emphasis
    _пристаням_стремятся
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>_пристаням_стремятся</p>
    +<p><em>пристаням</em>стремятся</p>
    
    Example 378 (lines 6585-6589) Emphasis and strong emphasis
    _foo_bar_baz_
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><em>foo_bar_baz</em></p>
    +<p><em>foo</em>bar_baz_</p>
    
    Example 382 (lines 6626-6630) Emphasis and strong emphasis
    a**"foo"**
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>a**&quot;foo&quot;**</p>
    +<p>a<strong>&quot;foo&quot;</strong></p>
    
    Example 387 (lines 6674-6678) Emphasis and strong emphasis
    a__"foo"__
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>a__&quot;foo&quot;__</p>
    +<p>a<strong>&quot;foo&quot;</strong></p>
    
    Example 388 (lines 6683-6687) Emphasis and strong emphasis
    foo__bar__
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>foo__bar__</p>
    +<p>foo<strong>bar</strong></p>
    
    Example 390 (lines 6697-6701) Emphasis and strong emphasis
    пристаням__стремятся__
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>пристаням__стремятся__</p>
    +<p>пристаням<strong>стремятся</strong></p>
    
    Example 391 (lines 6704-6708) Emphasis and strong emphasis
    __foo, __bar__, baz__
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><strong>foo, <strong>bar</strong>, baz</strong></p>
    +<p><strong>foo, __bar</strong>, baz__</p>
    
    Example 393 (lines 6728-6732) Emphasis and strong emphasis
    **foo bar **
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>**foo bar **</p>
    +<p>*<em>foo bar *</em></p>
    
    Example 394 (lines 6741-6745) Emphasis and strong emphasis
    **(**foo)
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>**(**foo)</p>
    +<p>*<em>(</em>*foo)</p>
    
    Example 402 (lines 6817-6821) Emphasis and strong emphasis
    __foo__bar
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>__foo__bar</p>
    +<p><strong>foo</strong>bar</p>
    
    Example 403 (lines 6824-6828) Emphasis and strong emphasis
    __пристаням__стремятся
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>__пристаням__стремятся</p>
    +<p><strong>пристаням</strong>стремятся</p>
    
    Example 404 (lines 6831-6835) Emphasis and strong emphasis
    __foo__bar__baz__
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><strong>foo__bar__baz</strong></p>
    +<p><strong>foo</strong>bar<strong>baz</strong></p>
    
    Example 409 (lines 6880-6884) Emphasis and strong emphasis
    _foo _bar_ baz_
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><em>foo <em>bar</em> baz</em></p>
    +<p><em>foo _bar</em> baz_</p>
    
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
    +<p><em>foo *bar</em>*</p>
    
    Example 414 (lines 6931-6935) Emphasis and strong emphasis
    *foo**bar*
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><em>foo**bar</em></p>
    +<p><em>foo</em><em>bar</em></p>
    
    Example 415 (lines 6944-6948) Emphasis and strong emphasis
    ***foo** bar*
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><em><strong>foo</strong> bar</em></p>
    +<p><strong><em>foo</strong> bar</em></p>
    
    Example 418 (lines 6969-6973) Emphasis and strong emphasis
    foo***bar***baz
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>foo<em><strong>bar</strong></em>baz</p>
    +<p>foo<strong><em>bar</strong></em>baz</p>
    
    Example 419 (lines 6975-6979) Emphasis and strong emphasis
    foo******bar*********baz
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>foo<strong><strong><strong>bar</strong></strong></strong>***baz</p>
    +<p>foo<strong>*<em></strong>bar<strong></em><em></strong></em>**baz</p>
    
    Example 420 (lines 6984-6988) Emphasis and strong emphasis
    *foo **bar *baz* bim** bop*
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><em>foo <strong>bar <em>baz</em> bim</strong> bop</em></p>
    +<p><em>foo <strong>bar *baz</em> bim</strong> bop*</p>
    
    Example 427 (lines 7046-7050) Emphasis and strong emphasis
    __foo __bar__ baz__
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><strong>foo <strong>bar</strong> baz</strong></p>
    +<p><strong>foo __bar</strong> baz__</p>
    
    Example 428 (lines 7053-7057) Emphasis and strong emphasis
    ____foo__ bar__
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><strong><strong>foo</strong> bar</strong></p>
    +<p><strong>__foo</strong> bar__</p>
    
    Example 429 (lines 7060-7064) Emphasis and strong emphasis
    **foo **bar****
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><strong>foo <strong>bar</strong></strong></p>
    +<p><strong>foo *<em>bar</strong></em>*</p>
    
    Example 431 (lines 7074-7078) Emphasis and strong emphasis
    **foo*bar*baz**
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><strong>foo<em>bar</em>baz</strong></p>
    +<p><strong>foo*bar*baz</strong></p>
    
    Example 433 (lines 7088-7092) Emphasis and strong emphasis
    **foo *bar***
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><strong>foo <em>bar</em></strong></p>
    +<p><strong>foo <em>bar</strong></em></p>
    
    Example 434 (lines 7097-7103) Emphasis and strong emphasis
    **foo *bar **baz**
    bim* bop**
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><strong>foo <em>bar <strong>baz</strong> bim</em> bop</strong></p>
    +<p><strong>foo <em>bar *</em>baz</strong> bim* bop**</p>
    
    Example 440 (lines 7146-7150) Emphasis and strong emphasis
    foo *_*
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>foo <em>_</em></p>
    +<p>foo *_*</p>
    
    Example 443 (lines 7167-7171) Emphasis and strong emphasis
    foo **_**
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>foo <strong>_</strong></p>
    +<p>foo **_**</p>
    
    Example 446 (lines 7192-7196) Emphasis and strong emphasis
    ***foo**
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>*<strong>foo</strong></p>
    +<p><strong>*foo</strong></p>
    
    Example 452 (lines 7237-7241) Emphasis and strong emphasis
    foo _*_
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>foo <em>*</em></p>
    +<p>foo _*_</p>
    
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
    
    Example 458 (lines 7283-7287) Emphasis and strong emphasis
    ___foo__
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>_<strong>foo</strong></p>
    +<p><strong>_foo</strong></p>
    
    Example 459 (lines 7290-7294) Emphasis and strong emphasis
    ____foo_
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>___<em>foo</em></p>
    +<p>____foo_</p>
    
    Example 463 (lines 7321-7325) Emphasis and strong emphasis
    *_foo_*
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><em><em>foo</em></em></p>
    +<p>*<em>foo</em>*</p>
    
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
    +<p><strong>*<em>foo</strong></em>*</p>
    
    Example 467 (lines 7352-7356) Emphasis and strong emphasis
    ____foo____
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><strong><strong>foo</strong></strong></p>
    +<p><strong>__foo</strong>__</p>
    
    Example 468 (lines 7363-7367) Emphasis and strong emphasis
    ******foo******
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><strong><strong><strong>foo</strong></strong></strong></p>
    +<p><strong>*<em></strong>foo<strong></em>*</strong></p>
    
    Example 469 (lines 7372-7376) Emphasis and strong emphasis
    ***foo***
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><em><strong>foo</strong></em></p>
    +<p><strong><em>foo</strong></em></p>
    
    Example 470 (lines 7379-7383) Emphasis and strong emphasis
    _____foo_____
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><em><strong><strong>foo</strong></strong></em></p>
    +<p><strong>___foo</strong>___</p>
    
    Example 473 (lines 7404-7408) Emphasis and strong emphasis
    **foo **bar baz**
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>**foo <strong>bar baz</strong></p>
    +<p><strong>foo **bar baz</strong></p>
    
    Example 474 (lines 7411-7415) Emphasis and strong emphasis
    *foo *bar baz*
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>*foo <em>bar baz</em></p>
    +<p><em>foo *bar baz</em></p>
    
    Example 475 (lines 7420-7424) Emphasis and strong emphasis
    *[bar*](/url)
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>*<a href="/url">bar*</a></p>
    +<p><em><a href="/url">bar</em></a></p>
    
    Example 476 (lines 7427-7431) Emphasis and strong emphasis
    _foo [bar_](/url)
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>_foo <a href="/url">bar_</a></p>
    +<p><em>foo <a href="/url">bar</em></a></p>
    
    79 passed, 53 failed, 0 errored, 523 skipped
  stderr:
    Traceback (most recent call last):
      File "emphasis-delimiters.py", line 10, in <module>
        assert result.returncode == 0
               ^^^^^^^^^^^^^^^^^^^^^^
    AssertionError
- RED: emphasis-nesting (FEATURE-INLINE-EMPHASIS.md)
  intent: The implementation passes nested, overlapping, precedence, and unmatched delimiter examples.
  return code: 1
  stdout:
    Example 356 (lines 6369-6382) Emphasis and strong emphasis
    *$*alpha.
    
    *£*bravo.
    
    *€*charlie.
    
    *𞋿*delta.
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>*$*alpha.</p><p>*£*bravo.</p><p>*€*charlie.</p><p>*𞋿*delta.</p>
    +<p><em>$</em>alpha.</p><p><em>£</em>bravo.</p><p><em>€</em>charlie.</p><p><em>𞋿</em>delta.</p>
    
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
    
    Example 370 (lines 6511-6515) Emphasis and strong emphasis
    *(*foo)
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>*(*foo)</p>
    +<p><em>(</em>foo)</p>
    
    Example 371 (lines 6521-6525) Emphasis and strong emphasis
    *(*foo*)*
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><em>(<em>foo</em>)</em></p>
    +<p><em>(</em>foo*)*</p>
    
    Example 374 (lines 6553-6557) Emphasis and strong emphasis
    _(_foo)
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>_(_foo)</p>
    +<p><em>(</em>foo)</p>
    
    Example 375 (lines 6562-6566) Emphasis and strong emphasis
    _(_foo_)_
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><em>(<em>foo</em>)</em></p>
    +<p><em>(</em>foo_)_</p>
    
    Example 376 (lines 6571-6575) Emphasis and strong emphasis
    _foo_bar
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>_foo_bar</p>
    +<p><em>foo</em>bar</p>
    
    Example 377 (lines 6578-6582) Emphasis and strong emphasis
    _пристаням_стремятся
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>_пристаням_стремятся</p>
    +<p><em>пристаням</em>стремятся</p>
    
    Example 378 (lines 6585-6589) Emphasis and strong emphasis
    _foo_bar_baz_
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><em>foo_bar_baz</em></p>
    +<p><em>foo</em>bar_baz_</p>
    
    Example 382 (lines 6626-6630) Emphasis and strong emphasis
    a**"foo"**
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>a**&quot;foo&quot;**</p>
    +<p>a<strong>&quot;foo&quot;</strong></p>
    
    Example 387 (lines 6674-6678) Emphasis and strong emphasis
    a__"foo"__
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>a__&quot;foo&quot;__</p>
    +<p>a<strong>&quot;foo&quot;</strong></p>
    
    Example 388 (lines 6683-6687) Emphasis and strong emphasis
    foo__bar__
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>foo__bar__</p>
    +<p>foo<strong>bar</strong></p>
    
    Example 390 (lines 6697-6701) Emphasis and strong emphasis
    пристаням__стремятся__
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>пристаням__стремятся__</p>
    +<p>пристаням<strong>стремятся</strong></p>
    
    Example 391 (lines 6704-6708) Emphasis and strong emphasis
    __foo, __bar__, baz__
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><strong>foo, <strong>bar</strong>, baz</strong></p>
    +<p><strong>foo, __bar</strong>, baz__</p>
    
    Example 393 (lines 6728-6732) Emphasis and strong emphasis
    **foo bar **
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>**foo bar **</p>
    +<p>*<em>foo bar *</em></p>
    
    Example 394 (lines 6741-6745) Emphasis and strong emphasis
    **(**foo)
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>**(**foo)</p>
    +<p>*<em>(</em>*foo)</p>
    
    Example 402 (lines 6817-6821) Emphasis and strong emphasis
    __foo__bar
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>__foo__bar</p>
    +<p><strong>foo</strong>bar</p>
    
    Example 403 (lines 6824-6828) Emphasis and strong emphasis
    __пристаням__стремятся
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>__пристаням__стремятся</p>
    +<p><strong>пристаням</strong>стремятся</p>
    
    Example 404 (lines 6831-6835) Emphasis and strong emphasis
    __foo__bar__baz__
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><strong>foo__bar__baz</strong></p>
    +<p><strong>foo</strong>bar<strong>baz</strong></p>
    
    Example 409 (lines 6880-6884) Emphasis and strong emphasis
    _foo _bar_ baz_
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><em>foo <em>bar</em> baz</em></p>
    +<p><em>foo _bar</em> baz_</p>
    
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
    +<p><em>foo *bar</em>*</p>
    
    Example 414 (lines 6931-6935) Emphasis and strong emphasis
    *foo**bar*
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><em>foo**bar</em></p>
    +<p><em>foo</em><em>bar</em></p>
    
    Example 415 (lines 6944-6948) Emphasis and strong emphasis
    ***foo** bar*
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><em><strong>foo</strong> bar</em></p>
    +<p><strong><em>foo</strong> bar</em></p>
    
    Example 418 (lines 6969-6973) Emphasis and strong emphasis
    foo***bar***baz
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>foo<em><strong>bar</strong></em>baz</p>
    +<p>foo<strong><em>bar</strong></em>baz</p>
    
    Example 419 (lines 6975-6979) Emphasis and strong emphasis
    foo******bar*********baz
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>foo<strong><strong><strong>bar</strong></strong></strong>***baz</p>
    +<p>foo<strong>*<em></strong>bar<strong></em><em></strong></em>**baz</p>
    
    Example 420 (lines 6984-6988) Emphasis and strong emphasis
    *foo **bar *baz* bim** bop*
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><em>foo <strong>bar <em>baz</em> bim</strong> bop</em></p>
    +<p><em>foo <strong>bar *baz</em> bim</strong> bop*</p>
    
    Example 427 (lines 7046-7050) Emphasis and strong emphasis
    __foo __bar__ baz__
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><strong>foo <strong>bar</strong> baz</strong></p>
    +<p><strong>foo __bar</strong> baz__</p>
    
    Example 428 (lines 7053-7057) Emphasis and strong emphasis
    ____foo__ bar__
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><strong><strong>foo</strong> bar</strong></p>
    +<p><strong>__foo</strong> bar__</p>
    
    Example 429 (lines 7060-7064) Emphasis and strong emphasis
    **foo **bar****
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><strong>foo <strong>bar</strong></strong></p>
    +<p><strong>foo *<em>bar</strong></em>*</p>
    
    Example 431 (lines 7074-7078) Emphasis and strong emphasis
    **foo*bar*baz**
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><strong>foo<em>bar</em>baz</strong></p>
    +<p><strong>foo*bar*baz</strong></p>
    
    Example 433 (lines 7088-7092) Emphasis and strong emphasis
    **foo *bar***
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><strong>foo <em>bar</em></strong></p>
    +<p><strong>foo <em>bar</strong></em></p>
    
    Example 434 (lines 7097-7103) Emphasis and strong emphasis
    **foo *bar **baz**
    bim* bop**
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><strong>foo <em>bar <strong>baz</strong> bim</em> bop</strong></p>
    +<p><strong>foo <em>bar *</em>baz</strong> bim* bop**</p>
    
    Example 440 (lines 7146-7150) Emphasis and strong emphasis
    foo *_*
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>foo <em>_</em></p>
    +<p>foo *_*</p>
    
    Example 443 (lines 7167-7171) Emphasis and strong emphasis
    foo **_**
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>foo <strong>_</strong></p>
    +<p>foo **_**</p>
    
    Example 446 (lines 7192-7196) Emphasis and strong emphasis
    ***foo**
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>*<strong>foo</strong></p>
    +<p><strong>*foo</strong></p>
    
    Example 452 (lines 7237-7241) Emphasis and strong emphasis
    foo _*_
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>foo <em>*</em></p>
    +<p>foo _*_</p>
    
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
    
    Example 458 (lines 7283-7287) Emphasis and strong emphasis
    ___foo__
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>_<strong>foo</strong></p>
    +<p><strong>_foo</strong></p>
    
    Example 459 (lines 7290-7294) Emphasis and strong emphasis
    ____foo_
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>___<em>foo</em></p>
    +<p>____foo_</p>
    
    Example 463 (lines 7321-7325) Emphasis and strong emphasis
    *_foo_*
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><em><em>foo</em></em></p>
    +<p>*<em>foo</em>*</p>
    
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
    +<p><strong>*<em>foo</strong></em>*</p>
    
    Example 467 (lines 7352-7356) Emphasis and strong emphasis
    ____foo____
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><strong><strong>foo</strong></strong></p>
    +<p><strong>__foo</strong>__</p>
    
    Example 468 (lines 7363-7367) Emphasis and strong emphasis
    ******foo******
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><strong><strong><strong>foo</strong></strong></strong></p>
    +<p><strong>*<em></strong>foo<strong></em>*</strong></p>
    
    Example 469 (lines 7372-7376) Emphasis and strong emphasis
    ***foo***
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><em><strong>foo</strong></em></p>
    +<p><strong><em>foo</strong></em></p>
    
    Example 470 (lines 7379-7383) Emphasis and strong emphasis
    _____foo_____
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><em><strong><strong>foo</strong></strong></em></p>
    +<p><strong>___foo</strong>___</p>
    
    Example 473 (lines 7404-7408) Emphasis and strong emphasis
    **foo **bar baz**
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>**foo <strong>bar baz</strong></p>
    +<p><strong>foo **bar baz</strong></p>
    
    Example 474 (lines 7411-7415) Emphasis and strong emphasis
    *foo *bar baz*
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>*foo <em>bar baz</em></p>
    +<p><em>foo *bar baz</em></p>
    
    Example 475 (lines 7420-7424) Emphasis and strong emphasis
    *[bar*](/url)
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>*<a href="/url">bar*</a></p>
    +<p><em><a href="/url">bar</em></a></p>
    
    Example 476 (lines 7427-7431) Emphasis and strong emphasis
    _foo [bar_](/url)
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>_foo <a href="/url">bar_</a></p>
    +<p><em>foo <a href="/url">bar</em></a></p>
    
    79 passed, 53 failed, 0 errored, 523 skipped
  stderr:
    Traceback (most recent call last):
      File "emphasis-nesting.py", line 10, in <module>
        assert result.returncode == 0
               ^^^^^^^^^^^^^^^^^^^^^^
    AssertionError

## Post-build programmatic acceptance
- PASS: emphasis-delimiters (FEATURE-INLINE-EMPHASIS.md)
  intent: The implementation passes delimiter-run, flanking, intraword, and modulo-three emphasis examples.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/.venv/bin/python3
  provisioning: not required
  return code: 0
  stdout:
    132 passed, 0 failed, 0 errored, 523 skipped
- PASS: emphasis-nesting (FEATURE-INLINE-EMPHASIS.md)
  intent: The implementation passes nested, overlapping, precedence, and unmatched delimiter examples.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/.venv/bin/python3
  provisioning: not required
  return code: 0
  stdout:
    132 passed, 0 failed, 0 errored, 523 skipped

## Build summary
RESULT: SUCCESS

FILES CHANGED:
- renderer/html.py
- test_inline_emphasis.py

SUMMARY:
Implemented delimiter-run emphasis and strong-emphasis parsing, including nesting, flanking, intraword rules, modulo-three constraints, and overlap precedence. Focused suite passes: 132/132 examples; regression tests pass.

BLOCKERS:
- Full suite still has pre-existing block-parser failures unrelated to emphasis.
