# Evidence: Block 11 · Service (block-11)

- block type: block
- date: 2026-08-12
- resulting state: closed/verified
- story points (combined assembled cost): 57747
- execution id: 20260812.192510.439Z-440a9e4a

## Stories built
- Parse autolinks and raw HTML. (inline-html) [story]

## Acceptance tooling authorization
- FEATURE-INLINE-HTML.md#inline-html-suite: executable=python3; scope=test; authorization=existing Target environment
- FEATURE-INLINE-HTML.md#inline-html-malformed: executable=python3; scope=test; authorization=existing Target environment

## Stacked context
- compass: COMPASS.md (SP 1263)
- implements: FEATURE-INLINE-HTML.md (SP 483)
- context: spec.txt (SP 51527)
- context: spec_tests.py (SP 1609)
- context: ARCHITECTURE_compact.md (SP 116)
- stack: common_compact.md (SP 1179)
- stack: python_compact.md (SP 1534)

## Build directory changes
- parser/blocks.py
- renderer/html.py

## Pre-build acceptance observation
- RED: inline-html-suite (FEATURE-INLINE-HTML.md)
  intent: The autolink and raw HTML syntax passes its complete owned conformance scope.
  return code: 1
  stdout:
    Example 598 (lines 8819-8823) Autolinks
    <irc://foo.bar:2233/baz>
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><a href="irc://foo.bar:2233/baz">irc://foo.bar:2233/baz</a></p>
    +<p>&lt;irc://foo.bar:2233/baz&gt;</p>
    
    Example 599 (lines 8828-8832) Autolinks
    <MAILTO:FOO@BAR.BAZ>
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><a href="MAILTO:FOO@BAR.BAZ">MAILTO:FOO@BAR.BAZ</a></p>
    +<mailto:foo@bar.baz> 
    
    Example 600 (lines 8840-8844) Autolinks
    <a+b+c:d>
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><a href="a+b+c:d">a+b+c:d</a></p>
    +<a+b+c:d> 
    
    Example 601 (lines 8847-8851) Autolinks
    <made-up-scheme://foo,bar>
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><a href="made-up-scheme://foo,bar">made-up-scheme://foo,bar</a></p>
    +<p>&lt;made-up-scheme://foo,bar&gt;</p>
    
    Example 603 (lines 8861-8865) Autolinks
    <localhost:5001/foo>
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><a href="localhost:5001/foo">localhost:5001/foo</a></p>
    +<localhost:5001 foo> 
    
    Example 604 (lines 8870-8874) Autolinks
    <https://foo.bar/baz bim>
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>&lt;https://foo.bar/baz bim&gt;</p>
    +<p><a href="https://foo.bar/baz%20bim">https://foo.bar/baz bim</a></p>
    
    Example 605 (lines 8879-8883) Autolinks
    <https://example.com/\[\>
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><a href="https://example.com/%5C%5B%5C">https://example.com/\[\</a></p>
    +<p>&lt;https://example.com/[&gt;</p>
    
    Example 606 (lines 8901-8905) Autolinks
    <foo@bar.example.com>
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><a href="mailto:foo@bar.example.com">foo@bar.example.com</a></p>
    +<foo@bar.example.com> 
    
    Example 607 (lines 8908-8912) Autolinks
    <foo+special@Bar.baz-bar0.com>
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><a href="mailto:foo+special@Bar.baz-bar0.com">foo+special@Bar.baz-bar0.com</a></p>
    +<foo+special@bar.baz-bar0.com> 
    
    Example 608 (lines 8917-8921) Autolinks
    <foo\+@bar.example.com>
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>&lt;foo+@bar.example.com&gt;</p>
    +<foo\+@bar.example.com> 
    
    Example 611 (lines 8940-8944) Autolinks
    <m:abc>
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>&lt;m:abc&gt;</p>
    +<m:abc> 
    
    Example 612 (lines 8947-8951) Autolinks
    <foo.bar.baz>
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>&lt;foo.bar.baz&gt;</p>
    +<foo.bar.baz> 
    
    Example 618 (lines 9070-9076) Raw HTML
    <a foo="bar" bam = 'baz <em>"</em>'
    _boolean zoop:33=zoop:33 />
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><a 'baz <em bam="" foo="bar">"</em>' _boolean zoop:33=zoop:33 /></p>
    +<p>&lt;a foo=&quot;bar&quot; bam = 'baz <em>&quot;</em>' _boolean zoop:33=zoop:33 /&gt;</p>
    
    Example 621 (lines 9099-9103) Raw HTML
    <a h*#ref="hi">
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>&lt;a h*#ref=&quot;hi&quot;&gt;</p>
    +<a h*#ref="hi"> 
    
    Example 622 (lines 9108-9112) Raw HTML
    <a href="hi'> <a href=hi'>
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>&lt;a href=&quot;hi'&gt; &lt;a href=hi'&gt;</p>
    +<p>
    
    Example 623 (lines 9117-9127) Raw HTML
    < a><
    foo><bar/ >
    <foo bar=baz
    bim!bop />
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>&lt; a&gt;&lt; foo&gt;&lt;bar/ &gt; &lt;foo bar=baz bim!bop /&gt;</p>
    +<p>&lt; a&gt;&lt; foo&gt;&lt;bar/ &gt; <foo bar="baz" bim!bop></p>
    
    Example 624 (lines 9132-9136) Raw HTML
    <a href='bar'title=title>
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>&lt;a href='bar'title=title&gt;</p>
    +<a href="bar" title="title"> 
    
    Example 626 (lines 9150-9154) Raw HTML
    </a href="foo">
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>&lt;/a href=&quot;foo&quot;&gt;</p>
    +</a> 
    
    Example 627 (lines 9159-9165) Raw HTML
    foo <!-- this is a --
    comment - with hyphens -->
    
    --- expected HTML
    +++ actual HTML
    @@ -1,2 +1 @@
    -<p>foo <!-- this is a --
    -comment - with hyphens --></p>
    +<p>foo &lt;!-- this is a -- comment - with hyphens --&gt;</p>
    
    Example 628 (lines 9167-9174) Raw HTML
    foo <!--> foo -->
    
    foo <!---> foo -->
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>foo <!----> foo --&gt;</p><p>foo <!----> foo --&gt;</p>
    +<p>foo &lt;!--&gt; foo --&gt;</p><p>foo &lt;!---&gt; foo --&gt;</p>
    
    Example 629 (lines 9179-9183) Raw HTML
    foo <?php echo $a; ?>
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>foo <?php echo $a; ?></p>
    +<p>foo &lt;?php echo $a; ?&gt;</p>
    
    Example 630 (lines 9188-9192) Raw HTML
    foo <!ELEMENT br EMPTY>
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>foo <!--ELEMENT br EMPTY--></p>
    +<p>foo &lt;!ELEMENT br EMPTY&gt;</p>
    
    Example 631 (lines 9197-9201) Raw HTML
    foo <![CDATA[>&<]]>
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>foo <![CDATA[>&<]]></p>
    +<p>foo &lt;![CDATA[&gt;&amp;&lt;]]&gt;</p>
    
    Example 632 (lines 9207-9211) Raw HTML
    foo <a href="&ouml;">
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>foo <a href="ö"></p>
    +<p>foo <a href="0"></p>
    
    Example 633 (lines 9216-9220) Raw HTML
    foo <a href="\*">
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>foo <a href="\*"></p>
    +<p>foo <a href="0"></p>
    
    Example 634 (lines 9223-9227) Raw HTML
    <a href="\"">
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>&lt;a href=&quot;&quot;&quot;&gt;</p>
    +<a " href="\"> 
    
    Example 635 (lines 9233-9241) Raw HTML
    <a
    > quoted text
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>&lt;a</p><blockquote><p>quoted text</p></blockquote>
    +<a> quoted text 
    
    13 passed, 27 failed, 0 errored, 615 skipped
  stderr:
    Traceback (most recent call last):
      File "inline-html-suite.py", line 11, in <module>
        assert result.returncode == 0
               ^^^^^^^^^^^^^^^^^^^^^^
    AssertionError
- RED: inline-html-malformed (FEATURE-INLINE-HTML.md)
  intent: Invalid autolinks and malformed HTML remain ordinary escaped content.
  return code: 1
  stderr:
    Traceback (most recent call last):
      File "inline-html-malformed.py", line 9, in <module>
        assert result.returncode == 0
               ^^^^^^^^^^^^^^^^^^^^^^
    AssertionError

## Post-build programmatic acceptance
- PASS: inline-html-suite (FEATURE-INLINE-HTML.md)
  intent: The autolink and raw HTML syntax passes its complete owned conformance scope.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/.venv/bin/python3
  provisioning: not required
  return code: 0
  stdout:
    40 passed, 0 failed, 0 errored, 615 skipped
- PASS: inline-html-malformed (FEATURE-INLINE-HTML.md)
  intent: Invalid autolinks and malformed HTML remain ordinary escaped content.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/.venv/bin/python3
  provisioning: not required
  return code: 0

## Repair attempts
- attempt 0 (initial build): failed; 0/2 checks; 29/40 cases model=gpt-5.6-luna; execution 20260812.191803.834Z-4159ca9f
- attempt 1 (repair 1): built; 2/2 checks; 40/40 cases model=gpt-5.6-luna; execution 20260812.192510.439Z-440a9e4a

## Build summary
RESULT: SUCCESS

FILES CHANGED:
- renderer/html.py

SUMMARY:
Fixed inline autolinks, raw HTML validation, malformed markup escaping, attribute scanning, and special HTML comments. Both acceptance checks pass: 40 passed, 0 failed.

BLOCKERS:
- None
