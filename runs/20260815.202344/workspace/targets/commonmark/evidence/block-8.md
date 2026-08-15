# Evidence: Block 8 · Service (block-8)

- block type: block
- date: 2026-08-15
- resulting state: closed/verified
- story points (combined assembled cost): 59901
- execution id: 20260815.213333.614Z-4f0372e7

## Stories built
- Parse autolinks and raw HTML inline constructs. (inline-004) [story]

## Stacked context
- compass: COMPASS.md (SP 1455)
- implements: FEATURE-Inline-HTML-Autolinks.md (SP 466)
- context: spec.txt (SP 51527)
- context: spec_tests.py (SP 1609)
- context: cmark.py (SP 339)
- context: normalize.py (SP 1631)
- context: ARCHITECTURE_compact.md (SP 87)
- stack: common_compact.md (SP 1179)
- stack: python_compact.md (SP 1534)

## Build directory changes
- commonmark
- tests/test_inline_html.py

## Pre-build acceptance observation
- RED: html-autolinks-conformance (FEATURE-Inline-HTML-Autolinks.md)
  intent: The implementation passes every supplied conformance example owned by autolinks and raw HTML.
  return code: 1
  stdout:
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
    
    Example 612 (lines 8947-8951) Autolinks
    <foo.bar.baz>
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>&lt;foo.bar.baz&gt;</p>
    +<foo.bar.baz> 
    
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
    
    Example 628 (lines 9167-9174) Raw HTML
    foo <!--> foo -->
    
    foo <!---> foo -->
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>foo <!----> foo --&gt;</p><p>foo <!----> foo --&gt;</p>
    +<p>foo <!----> foo --></p><p>foo <!----> foo --></p>
    
    Example 634 (lines 9223-9227) Raw HTML
    <a href="\"">
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>&lt;a href=&quot;&quot;&quot;&gt;</p>
    +<a " href="\"> 
    
    29 passed, 11 failed, 0 errored, 615 skipped
  stderr:
    Traceback (most recent call last):
      File "html-autolinks-conformance.py", line 20, in <module>
        assert result.returncode == 0
               ^^^^^^^^^^^^^^^^^^^^^^
    AssertionError

## Post-build programmatic acceptance
- PASS: html-autolinks-conformance (FEATURE-Inline-HTML-Autolinks.md)
  intent: The implementation passes every supplied conformance example owned by autolinks and raw HTML.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/.venv/bin/python3
  provisioning: not required
  return code: 0
  stdout:
    40 passed, 0 failed, 0 errored, 615 skipped

## Build summary
RESULT: SUCCESS

FILES CHANGED:
- commonmark
- tests/test_inline_html.py

SUMMARY:
Implemented strict URI/email autolinks and raw HTML parsing. Scoped suite: 40 passed. Full conformance harness and focused tests passed.

BLOCKERS:
- None
