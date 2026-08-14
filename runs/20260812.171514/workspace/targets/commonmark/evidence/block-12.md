# Evidence: Block 12 · Service (block-12)

- block type: block
- date: 2026-08-12
- resulting state: closed/verified
- story points (combined assembled cost): 59451
- execution id: 20260812.193447.205Z-ae61ce2f

## Stories built
- Render parsed block structure as CommonMark HTML. (render-blocks) [story]

## Acceptance tooling authorization
- FEATURE-RENDER-BLOCKS.md#render-blocks-suite: executable=python3; scope=test; authorization=existing Target environment
- FEATURE-RENDER-BLOCKS.md#render-blocks-escaping: executable=python3; scope=test; authorization=existing Target environment

## Reusable compacts
- normalize_compact.md

## Stacked context
- compass: COMPASS.md (SP 1263)
- implements: FEATURE-RENDER-BLOCKS.md (SP 551)
- context: spec.txt (SP 51527)
- context: spec_tests.py (SP 1609)
- context: normalize.py (SP 1631)
- context: ARCHITECTURE_compact.md (SP 116)
- stack: common_compact.md (SP 1179)
- stack: python_compact.md (SP 1534)

## Build directory changes
- parser/blocks.py
- renderer/html.py
- scoped-final.log
- test_render_blocks.py

## Pre-build acceptance observation
- RED: render-blocks-suite (FEATURE-RENDER-BLOCKS.md)
  intent: Block-level HTML rendering passes the complete owned conformance scope.
  return code: 1
  stdout:
    Example 56 (lines 1010-1014) Thematic breaks
     *-*
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><em>-</em></p>
    +<p><em&gt;-< em&gt;< p> 
    
    Example 57 (lines 1019-1031) Thematic breaks
    - foo
    ***
    - bar
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<ul><li>foo</li></ul><hr><ul><li>bar</li></ul>
    +<ul><li>foo<hr></li><li>bar</li></ul>
    
    Example 66 (lines 1167-1171) ATX headings
    # foo *bar* \*baz\*
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<h1>foo <em>bar</em> *baz*</h1>
    +<h1>foo <em&gt;bar< *baz*< em&gt; h1> 
    
    Example 80 (lines 1347-1356) Setext headings
    Foo *bar*
    =========
    
    Foo *bar*
    ---------
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<h1>Foo <em>bar</em></h1><h2>Foo <em>bar</em></h2>
    +<h1>Foo <em&gt;bar< em&gt;< h1><h2>Foo <em&gt;bar< em&gt;< h2> 
    
    Example 81 (lines 1361-1368) Setext headings
    Foo *bar
    baz*
    ====
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<h1>Foo <em>bar baz</em></h1>
    +<h1>Foo <em&gt;bar baz< em&gt;< h1> 
    
    Example 82 (lines 1375-1382) Setext headings
      Foo *bar
    baz*	
    ====
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<h1>Foo <em>bar baz</em></h1>
    +<h1>Foo <em&gt;bar baz< em&gt;< h1> 
    
    Example 94 (lines 1540-1548) Setext headings
    - Foo
    ---
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<ul><li>Foo</li></ul><hr>
    +<ul><li><h2>Foo</h2></li></ul>
    
    Example 99 (lines 1606-1614) Setext headings
    - foo
    -----
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<ul><li>foo</li></ul><hr>
    +<ul><li><h2>foo</h2></li></ul>
    
    Example 109 (lines 1777-1790) Indented code blocks
    1.  foo
    
        - bar
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<ol><li><p>foo</p><ul><li>bar</li></ul></li></ol>
    +<ol><li>foo<ul><li>bar</li></ul></li></ol>
    
    Example 148 (lines 2429-2444) HTML blocks
    <table><tr><td>
    <pre>
    **Hello**,
    
    _world_.
    </pre>
    </td></tr></table>
    
    --- expected HTML
    +++ actual HTML
    @@ -1,3 +1,3 @@
     <table><tr><td><pre>
    -**Hello**,<p><em>world</em>.
    -</pre></p></td></tr></table>
    +**Hello**,<p><em&gt;world< < em&gt;. pre></p></td></tr></table>
    +
    
    Example 152 (lines 2504-2514) HTML blocks
    <DIV CLASS="foo">
    
    *Markdown*
    
    </DIV>
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<div class="foo"><p><em>Markdown</em></p></div>
    +<div class="foo"><p><em&gt;markdown< em&gt;< p></div>
    
    Example 155 (lines 2543-2552) HTML blocks
    <div>
    *foo*
    
    *bar*
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<div>*foo*<p><em>bar</em></p>
    +<div>*foo*<p><em&gt;bar< em&gt;< p> 
    
    Example 162 (lines 2629-2635) HTML blocks
    <div
    > not quoted text
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<div>not quoted text 
    +<p>&lt;div</p><blockquote><p>not quoted text</p></blockquote>
    
    Example 168 (lines 2707-2717) HTML blocks
    <del>
    
    *foo*
    
    </del>
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<del><p><em>foo</em></p></del> 
    +<del><p><em&gt;foo< em&gt;< p> </del> 
    
    Example 169 (lines 2725-2729) HTML blocks
    <del>*foo*</del>
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><del><em>foo</em></del></p>
    +<p><del><em&gt;foo< del em&gt;<></p>
    
    Example 170 (lines 2731-2741) HTML blocks
    <del
    class="foo">
    *foo*
    </del>
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><del class="foo"> <em>foo</em> </del></p>
    +<p><del class="foo"> <em&gt;foo< < del em&gt;></p>
    
    Example 178 (lines 2878-2884) HTML blocks
    <style>p{color:red;}</style>
    *foo*
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<style>p{color:red;}</style><p><em>foo</em></p>
    +<style>p{color:red;}</style><p><em&gt;foo< em&gt;< p> 
    
    Example 179 (lines 2887-2893) HTML blocks
    <!-- foo -->*bar*
    *baz*
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<!-- foo -->*bar*<p><em>baz</em></p>
    +<!-- foo -->*bar*<p><em&gt;baz< em&gt;< p> 
    
    Example 190 (lines 3090-3100) HTML blocks
    <div>
    
    *Emphasized* text.
    
    </div>
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<div><p><em>Emphasized</em> text.</p></div>
    +<div><p><em&gt;emphasized< em&gt; p text.<></div>
    
    Example 228 (lines 3637-3643) Paragraphs
    aaa     
    bbb     
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>aaa<br>bbb</p>
    +<p>aaa<br &gt; bbb< p>
    
    239 passed, 20 failed, 0 errored, 396 skipped
  stderr:
    Traceback (most recent call last):
      File "render-blocks-suite.py", line 11, in <module>
        assert result.returncode == 0
               ^^^^^^^^^^^^^^^^^^^^^^
    AssertionError
- RED: render-blocks-escaping (FEATURE-RENDER-BLOCKS.md)
  intent: Block rendering preserves structural nesting and escapes literal code content.
  return code: 1
  stderr:
    Traceback (most recent call last):
      File "render-blocks-escaping.py", line 9, in <module>
        assert result.returncode == 0
               ^^^^^^^^^^^^^^^^^^^^^^
    AssertionError

## Post-build programmatic acceptance
- PASS: render-blocks-suite (FEATURE-RENDER-BLOCKS.md)
  intent: Block-level HTML rendering passes the complete owned conformance scope.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/.venv/bin/python3
  provisioning: not required
  return code: 0
  stdout:
    259 passed, 0 failed, 0 errored, 396 skipped
- PASS: render-blocks-escaping (FEATURE-RENDER-BLOCKS.md)
  intent: Block rendering preserves structural nesting and escapes literal code content.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/.venv/bin/python3
  provisioning: not required
  return code: 0

## Build summary
<reusable-compact filename="normalize.py">
Provides `normalize_html(html: str) -> str`, normalizing insignificant HTML whitespace, attribute ordering, self-closing tags, and entity references for conformance comparison. Uses only Python standard-library modules.
</reusable-compact>

RESULT: SUCCESS

FILES CHANGED:
- parser/blocks.py
- renderer/html.py
- test_render_blocks.py

SUMMARY:
Implemented block rendering fixes for raw HTML, thematic breaks, loose lists, headings, and escaped/generated HTML markup. Added regression tests. All 28 project tests pass; each declared block-scope section passes independently.

BLOCKERS:
- Full suite remains non-green due pre-existing inline-scope failures and timeout outside this build block.
