# Evidence: Block 6 · Service (block-6)

- block type: block
- date: 2026-08-15
- resulting state: closed/verified
- story points (combined assembled cost): 59861
- execution id: 20260815.212354.816Z-a92e138b

## Stories built
- Parse emphasis and strong emphasis with the delimiter-run algorithm. (inline-002) [story]

## Stacked context
- compass: COMPASS.md (SP 1455)
- implements: FEATURE-Inline-Emphasis.md (SP 419)
- context: spec.txt (SP 51527)
- context: spec_tests.py (SP 1609)
- context: cmark.py (SP 339)
- context: normalize.py (SP 1631)
- context: ARCHITECTURE_compact.md (SP 87)
- stack: common_compact.md (SP 1179)
- stack: python_compact.md (SP 1534)

## Build directory changes
- commonmark
- tests/test_interface.py

## Pre-build acceptance observation
- RED: emphasis-conformance (FEATURE-Inline-Emphasis.md)
  intent: The implementation passes every supplied conformance example owned by emphasis and strong emphasis.
  return code: 1
  stdout:
    Example 353 (lines 6340-6344) Emphasis and strong emphasis
    a * foo bar*
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>a * foo bar*</p>
    +<p>a <em> foo bar</em></p>
    
    Example 355 (lines 6360-6364) Emphasis and strong emphasis
    * a *
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>* a *</p>
    +<p><em> a </em></p>
    
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
    
    Example 360 (lines 6413-6417) Emphasis and strong emphasis
    _ foo bar_
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>_ foo bar_</p>
    +<p><em> foo bar</em></p>
    
    Example 368 (lines 6489-6493) Emphasis and strong emphasis
    *foo bar *
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>*foo bar *</p>
    +<p><em>foo bar </em></p>
    
    Example 369 (lines 6498-6504) Emphasis and strong emphasis
    *foo bar
    *
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>*foo bar *</p>
    +<p><em>foo bar </em></p>
    
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
    
    Example 373 (lines 6543-6547) Emphasis and strong emphasis
    _foo bar _
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>_foo bar _</p>
    +<p><em>foo bar </em></p>
    
    Example 375 (lines 6562-6566) Emphasis and strong emphasis
    _(_foo_)_
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><em>(<em>foo</em>)</em></p>
    +<p>_(<em>foo</em>)_</p>
    
    Example 378 (lines 6585-6589) Emphasis and strong emphasis
    _foo_bar_baz_
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><em>foo_bar_baz</em></p>
    +<p>_foo_bar_baz_</p>
    
    Example 381 (lines 6615-6619) Emphasis and strong emphasis
    ** foo bar**
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>** foo bar**</p>
    +<p><strong> foo bar</strong></p>
    
    Example 382 (lines 6626-6630) Emphasis and strong emphasis
    a**"foo"**
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>a**&quot;foo&quot;**</p>
    +<p>a<strong>&quot;foo&quot;</strong></p>
    
    Example 385 (lines 6654-6658) Emphasis and strong emphasis
    __ foo bar__
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>__ foo bar__</p>
    +<p><strong> foo bar</strong></p>
    
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
    
    Example 389 (lines 6690-6694) Emphasis and strong emphasis
    5__6__78
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>5__6__78</p>
    +<p>5<strong>6</strong>78</p>
    
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
    +<p><strong>foo, </strong>bar<strong>, baz</strong></p>
    
    Example 393 (lines 6728-6732) Emphasis and strong emphasis
    **foo bar **
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>**foo bar **</p>
    +<p><strong>foo bar </strong></p>
    
    Example 394 (lines 6741-6745) Emphasis and strong emphasis
    **(**foo)
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>**(**foo)</p>
    +<p><strong>(</strong>foo)</p>
    
    Example 396 (lines 6758-6764) Emphasis and strong emphasis
    **Gomphocarpus (*Gomphocarpus physocarpus*, syn.
    *Asclepias physocarpa*)**
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><strong>Gomphocarpus (<em>Gomphocarpus physocarpus</em>, syn. <em>Asclepias physocarpa</em>)</strong></p>
    +<p>**Gomphocarpus (<em>Gomphocarpus physocarpus</em>, syn. <em>Asclepias physocarpa</em>)**</p>
    
    Example 397 (lines 6767-6771) Emphasis and strong emphasis
    **foo "*bar*" foo**
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><strong>foo &quot;<em>bar</em>&quot; foo</strong></p>
    +<p>**foo &quot;<em>bar</em>&quot; foo**</p>
    
    Example 399 (lines 6788-6792) Emphasis and strong emphasis
    __foo bar __
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>__foo bar __</p>
    +<p><strong>foo bar </strong></p>
    
    Example 400 (lines 6798-6802) Emphasis and strong emphasis
    __(__foo)
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>__(__foo)</p>
    +<p><strong>(</strong>foo)</p>
    
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
    +<p>_foo <em>bar</em> baz_</p>
    
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
    +<p><em>foo </em>bar**</p>
    
    Example 414 (lines 6931-6935) Emphasis and strong emphasis
    *foo**bar*
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><em>foo**bar</em></p>
    +<p>*foo**bar*</p>
    
    Example 418 (lines 6969-6973) Emphasis and strong emphasis
    foo***bar***baz
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>foo<em><strong>bar</strong></em>baz</p>
    +<p>foo*<strong>bar</strong>*baz</p>
    
    Example 419 (lines 6975-6979) Emphasis and strong emphasis
    foo******bar*********baz
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>foo<strong><strong><strong>bar</strong></strong></strong>***baz</p>
    +<p>foo****<strong>bar</strong>*******baz</p>
    
    Example 420 (lines 6984-6988) Emphasis and strong emphasis
    *foo **bar *baz* bim** bop*
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><em>foo <strong>bar <em>baz</em> bim</strong> bop</em></p>
    +<p>*foo **bar <em>baz</em> bim** bop*</p>
    
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
    +<p>__foo <em>bar</em> baz__</p>
    
    Example 427 (lines 7046-7050) Emphasis and strong emphasis
    __foo __bar__ baz__
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><strong>foo <strong>bar</strong> baz</strong></p>
    +<p><strong>foo </strong>bar<strong> baz</strong></p>
    
    Example 428 (lines 7053-7057) Emphasis and strong emphasis
    ____foo__ bar__
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><strong><strong>foo</strong> bar</strong></p>
    +<p>__<strong>foo</strong> bar__</p>
    
    Example 429 (lines 7060-7064) Emphasis and strong emphasis
    **foo **bar****
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><strong>foo <strong>bar</strong></strong></p>
    +<p><strong>foo </strong>bar****</p>
    
    Example 430 (lines 7067-7071) Emphasis and strong emphasis
    **foo *bar* baz**
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><strong>foo <em>bar</em> baz</strong></p>
    +<p>**foo <em>bar</em> baz**</p>
    
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
    +<p>**foo <em>bar <strong>baz</strong> bim</em> bop**</p>
    
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
    
    Example 447 (lines 7199-7203) Emphasis and strong emphasis
    ****foo*
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>***<em>foo</em></p>
    +<p>****foo*</p>
    
    Example 449 (lines 7213-7217) Emphasis and strong emphasis
    *foo****
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><em>foo</em>***</p>
    +<p>*foo****</p>
    
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
    
    Example 459 (lines 7290-7294) Emphasis and strong emphasis
    ____foo_
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>___<em>foo</em></p>
    +<p>____foo_</p>
    
    Example 461 (lines 7304-7308) Emphasis and strong emphasis
    _foo____
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><em>foo</em>___</p>
    +<p>_foo____</p>
    
    Example 466 (lines 7345-7349) Emphasis and strong emphasis
    ****foo****
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><strong><strong>foo</strong></strong></p>
    +<p>**<strong>foo</strong>**</p>
    
    Example 467 (lines 7352-7356) Emphasis and strong emphasis
    ____foo____
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><strong><strong>foo</strong></strong></p>
    +<p>__<strong>foo</strong>__</p>
    
    Example 468 (lines 7363-7367) Emphasis and strong emphasis
    ******foo******
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><strong><strong><strong>foo</strong></strong></strong></p>
    +<p>****<strong>foo</strong>****</p>
    
    Example 470 (lines 7379-7383) Emphasis and strong emphasis
    _____foo_____
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><em><strong><strong>foo</strong></strong></em></p>
    +<p>___<strong>foo</strong>___</p>
    
    Example 472 (lines 7395-7399) Emphasis and strong emphasis
    *foo __bar *baz bim__ bam*
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><em>foo <strong>bar *baz bim</strong> bam</em></p>
    +<p><em>foo <strong>bar </em>baz bim</strong> bam*</p>
    
    Example 473 (lines 7404-7408) Emphasis and strong emphasis
    **foo **bar baz**
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>**foo <strong>bar baz</strong></p>
    +<p><strong>foo </strong>bar baz**</p>
    
    Example 474 (lines 7411-7415) Emphasis and strong emphasis
    *foo *bar baz*
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>*foo <em>bar baz</em></p>
    +<p><em>foo </em>bar baz*</p>
    
    70 passed, 62 failed, 0 errored, 523 skipped
  stderr:
    Traceback (most recent call last):
      File "emphasis-conformance.py", line 20, in <module>
        assert result.returncode == 0
               ^^^^^^^^^^^^^^^^^^^^^^
    AssertionError

## Post-build programmatic acceptance
- PASS: emphasis-conformance (FEATURE-Inline-Emphasis.md)
  intent: The implementation passes every supplied conformance example owned by emphasis and strong emphasis.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/.venv/bin/python3
  provisioning: not required
  return code: 0
  stdout:
    132 passed, 0 failed, 0 errored, 523 skipped

## Build summary
RESULT: SUCCESS

FILES CHANGED:
- commonmark
- tests/test_interface.py

SUMMARY:
Implemented delimiter-run emphasis parsing with nesting, Unicode flanking rules, unmatched markers, and multiple-of-three handling. Scoped conformance: 132 passed. Project tests: 7 passed.

BLOCKERS:
- None
