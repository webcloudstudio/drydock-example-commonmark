# Evidence: Block 13 · Service (block-13)

- block type: block
- date: 2026-10-27
- resulting state: closed/failed
- story points (combined assembled cost): 3737
- execution id: 20261028.001809.125Z-549378e5

## Stories built
- Exercise all scoped CommonMark examples against the integrated parser. (conformance-integration) [story]

## Acceptance tooling authorization
- FEATURE-ConformanceIntegration.md#conformance-preliminaries: executable=python3; scope=test; authorization=existing Target environment
- FEATURE-ConformanceIntegration.md#conformance-blocks: executable=python3; scope=test; authorization=existing Target environment
- FEATURE-ConformanceIntegration.md#conformance-containers: executable=python3; scope=test; authorization=existing Target environment
- FEATURE-ConformanceIntegration.md#conformance-inlines: executable=python3; scope=test; authorization=existing Target environment

## Stacked context
- stack: python_compact.md (SP 654)
- compass: COMPASS.md (SP 548)
- implements: FEATURE-ConformanceIntegration.md (SP 1037)
- context: ARCHITECTURE_compact.md (SP 304)
- stack: common_compact.md (SP 1079)

## Build directory changes
- commonmark_parser/__init__.py
- commonmark_parser/autolinks.py
- commonmark_parser/blocks.py
- commonmark_parser/fenced_code.py
- commonmark_parser/html_blocks.py
- commonmark_parser/images.py
- commonmark_parser/indented_code.py
- commonmark_parser/inline_html_breaks.py
- commonmark_parser/inlines.py
- commonmark_parser/links.py
- commonmark_parser/references.py
- tests/test_block_quotes.py
- tests/test_fenced_code_indent.py
- tests/test_inline_providers.py
- tests/test_inline_text.py
- tests/test_links.py
- tests/test_lists.py
- tests/test_render_integration.py
- tests/test_service_blocks.py
- tests/test_setext.py

## Pre-build acceptance observation
- RED: conformance-preliminaries (FEATURE-ConformanceIntegration.md)
  intent: The integrated parser passes every supplied Tabs and Precedence example.
  return code: 1
  stdout:
    Example 1 (lines 355-360) Tabs
    	foo	baz		bim
    
    --- expected HTML
    +++ actual HTML
    @@ -1,2 +1 @@
    -<pre><code>foo	baz		bim
    -</code></pre>
    +
    
    Example 2 (lines 362-367) Tabs
      	foo	baz		bim
    
    --- expected HTML
    +++ actual HTML
    @@ -1,2 +1 @@
    -<pre><code>foo	baz		bim
    -</code></pre>
    +
    
    Example 3 (lines 369-376) Tabs
        a	a
        ὐ	a
    
    --- expected HTML
    +++ actual HTML
    @@ -1,3 +1 @@
    -<pre><code>a	a
    -ὐ	a
    -</code></pre>
    +
    
    Example 4 (lines 382-393) Tabs
      - foo
    
    	bar
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<ul><li><p>foo</p><p>bar</p></li></ul>
    +
    
    Example 5 (lines 395-407) Tabs
    - foo
    
    		bar
    
    --- expected HTML
    +++ actual HTML
    @@ -1,2 +1 @@
    -<ul><li><p>foo</p><pre><code>  bar
    -</code></pre></li></ul>
    +
    
    Example 6 (lines 418-425) Tabs
    >		foo
    
    --- expected HTML
    +++ actual HTML
    @@ -1,2 +1 @@
    -<blockquote><pre><code>  foo
    -</code></pre></blockquote>
    +
    
    Example 7 (lines 427-436) Tabs
    -		foo
    
    --- expected HTML
    +++ actual HTML
    @@ -1,2 +1 @@
    -<ul><li><pre><code>  foo
    -</code></pre></li></ul>
    +
    
    Example 8 (lines 439-446) Tabs
        foo
    	bar
    
    --- expected HTML
    +++ actual HTML
    @@ -1,3 +1 @@
    -<pre><code>foo
    -bar
    -</code></pre>
    +
    
    Example 9 (lines 448-464) Tabs
     - foo
       - bar
    	 - baz
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<ul><li>foo<ul><li>bar<ul><li>baz</li></ul></li></ul></li></ul>
    +
    
    Example 10 (lines 466-470) Tabs
    #	Foo
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<h1>Foo</h1>
    +
    
    Example 11 (lines 472-476) Tabs
    *	*	*	
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<hr>
    +
    
    Example 42 (lines 840-848) Precedence
    - `one
    - two`
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<ul><li>`one</li><li>two`</li></ul>
    +
    
    0 passed, 12 failed, 0 errored, 643 skipped
  stderr:
    --- drydock: progress ---
    cases: pass=0 fail=12 error=0 skip=643 total=655 from=result.stdout
    --- drydock: end progress ---
    --- drydock: values at failure ---
      result = CompletedProcess(args=['/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/.venv/bin/python', 'sources/spec_tests.py', '--program', '/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/commonmark', '--spec', 'sources/spec.txt', '--pattern', '^(Tabs|Precedence)$'], returncode=12, stdout='Example 1 (lines 355-360) Tabs\n\tfoo… (+1808 chars)
    --- drydock: end values ---
    Traceback (most recent call last):
      File "conformance-preliminaries.py", line 12, in <module>
        assert result.returncode == 0
               ^^^^^^^^^^^^^^^^^^^^^^
    AssertionError
- RED: conformance-blocks (FEATURE-ConformanceIntegration.md)
  intent: The integrated parser passes every example in the supplied leaf block sections.
  return code: 1
  stdout:
    Example 43 (lines 879-887) Thematic breaks
    ***
    ---
    ___
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<hr><hr><hr>
    +
    
    Example 44 (lines 892-896) Thematic breaks
    +++
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>+++</p>
    +
    
    Example 45 (lines 899-903) Thematic breaks
    ===
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>===</p>
    +
    
    Example 46 (lines 908-916) Thematic breaks
    --
    **
    __
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>-- ** __</p>
    +
    
    Example 47 (lines 921-929) Thematic breaks
     ***
      ***
       ***
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<hr><hr><hr>
    +
    
    Example 48 (lines 934-939) Thematic breaks
        ***
    
    --- expected HTML
    +++ actual HTML
    @@ -1,2 +1 @@
    -<pre><code>***
    -</code></pre>
    +
    
    Example 49 (lines 942-948) Thematic breaks
    Foo
        ***
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>Foo ***</p>
    +
    
    Example 50 (lines 953-957) Thematic breaks
    _____________________________________
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<hr>
    +
    
    Example 51 (lines 962-966) Thematic breaks
     - - -
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<hr>
    +
    
    Example 52 (lines 969-973) Thematic breaks
     **  * ** * ** * **
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<hr>
    +
    
    Example 53 (lines 976-980) Thematic breaks
    -     -      -      -
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<hr>
    +
    
    Example 54 (lines 985-989) Thematic breaks
    - - - -    
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<hr>
    +
    
    Example 55 (lines 994-1004) Thematic breaks
    _ _ _ _ a
    
    a------
    
    ---a---
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>_ _ _ _ a</p><p>a------</p><p>---a---</p>
    +
    
    Example 56 (lines 1010-1014) Thematic breaks
     *-*
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><em>-</em></p>
    +
    
    Example 57 (lines 1019-1031) Thematic breaks
    - foo
    ***
    - bar
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<ul><li>foo</li></ul><hr><ul><li>bar</li></ul>
    +
    
    Example 58 (lines 1036-1044) Thematic breaks
    Foo
    ***
    bar
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>Foo</p><hr><p>bar</p>
    +
    
    Example 59 (lines 1053-1060) Thematic breaks
    Foo
    ---
    bar
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<h2>Foo</h2><p>bar</p>
    +
    
    Example 60 (lines 1066-1078) Thematic breaks
    * Foo
    * * *
    * Bar
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<ul><li>Foo</li></ul><hr><ul><li>Bar</li></ul>
    +
    
    Example 61 (lines 1083-1093) Thematic breaks
    - Foo
    - * * *
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<ul><li>Foo</li><li><hr></li></ul>
    +
    
    Example 62 (lines 1112-1126) ATX headings
    # foo
    ## foo
    ### foo
    #### foo
    ##### foo
    ###### foo
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<h1>foo</h1><h2>foo</h2><h3>foo</h3><h4>foo</h4><h5>foo</h5><h6>foo</h6>
    +
    
    Example 63 (lines 1131-1135) ATX headings
    ####### foo
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>####### foo</p>
    +
    
    Example 64 (lines 1146-1153) ATX headings
    #5 bolt
    
    #hashtag
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>#5 bolt</p><p>#hashtag</p>
    +
    
    Example 65 (lines 1158-1162) ATX headings
    \## foo
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>## foo</p>
    +
    
    Example 66 (lines 1167-1171) ATX headings
    # foo *bar* \*baz\*
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<h1>foo <em>bar</em> *baz*</h1>
    +
    
    Example 67 (lines 1176-1180) ATX headings
    #                  foo                     
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<h1>foo</h1>
    +
    
    Example 68 (lines 1185-1193) ATX headings
     ### foo
      ## foo
       # foo
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<h3>foo</h3><h2>foo</h2><h1>foo</h1>
    +
    
    Example 69 (lines 1198-1203) ATX headings
        # foo
    
    --- expected HTML
    +++ actual HTML
    @@ -1,2 +1 @@
    -<pre><code># foo
    -</code></pre>
    +
    
    Example 70 (lines 1206-1212) ATX headings
    foo
        # bar
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>foo # bar</p>
    +
    
    Example 71 (lines 1217-1223) ATX headings
    ## foo ##
      ###   bar    ###
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<h2>foo</h2><h3>bar</h3>
    +
    
    Example 72 (lines 1228-1234) ATX headings
    # foo ##################################
    ##### foo ##
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<h1>foo</h1><h5>foo</h5>
    +
    
    Example 73 (lines 1239-1243) ATX headings
    ### foo ###     
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<h3>foo</h3>
    +
    
    Example 74 (lines 1250-1254) ATX headings
    ### foo ### b
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<h3>foo ### b</h3>
    +
    
    Example 75 (lines 1259-1263) ATX headings
    # foo#
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<h1>foo#</h1>
    +
    
    Example 76 (lines 1269-1277) ATX headings
    ### foo \###
    ## foo #\##
    # foo \#
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<h3>foo ###</h3><h2>foo ###</h2><h1>foo #</h1>
    +
    
    Example 77 (lines 1283-1291) ATX headings
    ****
    ## foo
    ****
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<hr><h2>foo</h2><hr>
    +
    
    Example 78 (lines 1294-1302) ATX headings
    Foo bar
    # baz
    Bar foo
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>Foo bar</p><h1>baz</h1><p>Bar foo</p>
    +
    
    Example 79 (lines 1307-1315) ATX headings
    ## 
    #
    ### ###
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<h2></h2><h1></h1><h3></h3>
    +
    
    Example 80 (lines 1347-1356) Setext headings
    Foo *bar*
    =========
    
    Foo *bar*
    ---------
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<h1>Foo <em>bar</em></h1><h2>Foo <em>bar</em></h2>
    +
    
    Example 81 (lines 1361-1368) Setext headings
    Foo *bar
    baz*
    ====
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<h1>Foo <em>bar baz</em></h1>
    +
    
    Example 82 (lines 1375-1382) Setext headings
      Foo *bar
    baz*	
    ====
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<h1>Foo <em>bar baz</em></h1>
    +
    
    Example 83 (lines 1387-1396) Setext headings
    Foo
    -------------------------
    
    Foo
    =
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<h2>Foo</h2><h1>Foo</h1>
    +
    
    Example 84 (lines 1402-1415) Setext headings
       Foo
    ---
    
      Foo
    -----
    
      Foo
      ===
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<h2>Foo</h2><h2>Foo</h2><h1>Foo</h1>
    +
    
    Example 85 (lines 1420-1433) Setext headings
        Foo
        ---
    
        Foo
    ---
    
    --- expected HTML
    +++ actual HTML
    @@ -1,5 +1 @@
    -<pre><code>Foo
    ----
     
    -Foo
    -</code></pre><hr>
    
    Example 86 (lines 1439-1444) Setext headings
    Foo
       ----      
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<h2>Foo</h2>
    +
    
    Example 87 (lines 1449-1455) Setext headings
    Foo
        ---
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>Foo ---</p>
    +
    
    Example 88 (lines 1460-1471) Setext headings
    Foo
    = =
    
    Foo
    --- -
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>Foo = =</p><p>Foo</p><hr>
    +
    
    Example 89 (lines 1476-1481) Setext headings
    Foo  
    -----
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<h2>Foo</h2>
    +
    
    Example 90 (lines 1486-1491) Setext headings
    Foo\
    ----
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<h2>Foo\</h2>
    +
    
    Example 91 (lines 1497-1510) Setext headings
    `Foo
    ----
    `
    
    <a title="a lot
    ---
    of dashes"/>
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<h2>`Foo</h2><p>`</p><h2>&lt;a title=&quot;a lot</h2><p>of dashes&quot;/&gt;</p>
    +
    
    Example 92 (lines 1516-1524) Setext headings
    > Foo
    ---
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<blockquote><p>Foo</p></blockquote><hr>
    +
    
    Example 93 (lines 1527-1537) Setext headings
    > foo
    bar
    ===
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<blockquote><p>foo bar ===</p></blockquote>
    +
    
    Example 94 (lines 1540-1548) Setext headings
    - Foo
    ---
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<ul><li>Foo</li></ul><hr>
    +
    
    Example 95 (lines 1555-1562) Setext headings
    Foo
    Bar
    ---
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<h2>Foo Bar</h2>
    +
    
    Example 96 (lines 1568-1580) Setext headings
    ---
    Foo
    ---
    Bar
    ---
    Baz
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<hr><h2>Foo</h2><h2>Bar</h2><p>Baz</p>
    +
    
    Example 97 (lines 1585-1590) Setext headings
    
    ====
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>====</p>
    +
    
    Example 98 (lines 1597-1603) Setext headings
    ---
    ---
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<hr><hr>
    +
    
    Example 99 (lines 1606-1614) Setext headings
    - foo
    -----
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<ul><li>foo</li></ul><hr>
    +
    
    Example 100 (lines 1617-1624) Setext headings
        foo
    ---
    
    --- expected HTML
    +++ actual HTML
    @@ -1,2 +1 @@
    -<pre><code>foo
    -</code></pre><hr>
    +
    
    Example 101 (lines 1627-1635) Setext headings
    > foo
    -----
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<blockquote><p>foo</p></blockquote><hr>
    +
    
    Example 102 (lines 1641-1646) Setext headings
    \> foo
    ------
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<h2>&gt; foo</h2>
    +
    
    Example 103 (lines 1672-1682) Setext headings
    Foo
    
    bar
    ---
    baz
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>Foo</p><h2>bar</h2><p>baz</p>
    +
    
    Example 104 (lines 1688-1700) Setext headings
    Foo
    bar
    
    ---
    
    baz
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>Foo bar</p><hr><p>baz</p>
    +
    
    Example 105 (lines 1706-1716) Setext headings
    Foo
    bar
    * * *
    baz
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>Foo bar</p><hr><p>baz</p>
    +
    
    Example 106 (lines 1721-1731) Setext headings
    Foo
    bar
    \---
    baz
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>Foo bar --- baz</p>
    +
    
    Example 107 (lines 1749-1756) Indented code blocks
        a simple
          indented code block
    
    --- expected HTML
    +++ actual HTML
    @@ -1,3 +1 @@
    -<pre><code>a simple
    -  indented code block
    -</code></pre>
    +
    
    Example 108 (lines 1763-1774) Indented code blocks
      - foo
    
        bar
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<ul><li><p>foo</p><p>bar</p></li></ul>
    +
    
    Example 109 (lines 1777-1790) Indented code blocks
    1.  foo
    
        - bar
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<ol><li><p>foo</p><ul><li>bar</li></ul></li></ol>
    +
    
    Example 110 (lines 1797-1808) Indented code blocks
        <a/>
        *hi*
    
        - one
    
    --- expected HTML
    +++ actual HTML
    @@ -1,5 +1 @@
    -<pre><code>&lt;a/&gt;
    -*hi*
     
    -- one
    -</code></pre>
    
    Example 111 (lines 1813-1830) Indented code blocks
        chunk1
    
        chunk2
      
     
     
        chunk3
    
    --- expected HTML
    +++ actual HTML
    @@ -1,8 +1 @@
    -<pre><code>chunk1
     
    -chunk2
    -
    -
    -
    -chunk3
    -</code></pre>
    
    Example 112 (lines 1836-1845) Indented code blocks
        chunk1
          
          chunk2
    
    --- expected HTML
    +++ actual HTML
    @@ -1,4 +1 @@
    -<pre><code>chunk1
    -  
    -  chunk2
    -</code></pre>
    +
    
    Example 113 (lines 1851-1858) Indented code blocks
    Foo
        bar
    
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>Foo bar</p>
    +
    
    Example 114 (lines 1865-1872) Indented code blocks
        foo
    bar
    
    --- expected HTML
    +++ actual HTML
    @@ -1,2 +1 @@
    -<pre><code>foo
    -</code></pre><p>bar</p>
    +
    
    Example 115 (lines 1878-1893) Indented code blocks
    # Heading
        foo
    Heading
    ------
        foo
    ----
    
    --- expected HTML
    +++ actual HTML
    @@ -1,3 +1 @@
    -<h1>Heading</h1><pre><code>foo
    -</code></pre><h2>Heading</h2><pre><code>foo
    -</code></pre><hr>
    +
    
    Example 116 (lines 1898-1905) Indented code blocks
            foo
        bar
    
    --- expected HTML
    +++ actual HTML
    @@ -1,3 +1 @@
    -<pre><code>    foo
    -bar
    -</code></pre>
    +
    
    Example 117 (lines 1911-1920) Indented code blocks
    
        
        foo
        
    
    
    --- expected HTML
    +++ actual HTML
    @@ -1,2 +1 @@
    -<pre><code>foo
    -</code></pre>
    +
    
    Example 118 (lines 1925-1930) Indented code blocks
        foo  
    
    --- expected HTML
    +++ actual HTML
    @@ -1,2 +1 @@
    -<pre><code>foo  
    -</code></pre>
    +
    
    Example 119 (lines 1980-1989) Fenced code blocks
    ```
    <
     >
    ```
    
    --- expected HTML
    +++ actual HTML
    @@ -1,3 +1 @@
    -<pre><code>&lt;
    - &gt;
    -</code></pre>
    +
    
    Example 120 (lines 1994-2003) Fenced code blocks
    ~~~
    <
     >
    ~~~
    
    --- expected HTML
    +++ actual HTML
    @@ -1,3 +1 @@
    -<pre><code>&lt;
    - &gt;
    -</code></pre>
    +
    
    Example 121 (lines 2007-2013) Fenced code blocks
    ``
    foo
    ``
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><code>foo</code></p>
    +
    
    Example 122 (lines 2018-2027) Fenced code blocks
    ```
    aaa
    ~~~
    ```
    
    --- expected HTML
    +++ actual HTML
    @@ -1,3 +1 @@
    -<pre><code>aaa
    -~~~
    -</code></pre>
    +
    
    Example 123 (lines 2030-2039) Fenced code blocks
    ~~~
    aaa
    ```
    ~~~
    
    --- expected HTML
    +++ actual HTML
    @@ -1,3 +1 @@
    -<pre><code>aaa
    -```
    -</code></pre>
    +
    
    Example 124 (lines 2044-2053) Fenced code blocks
    ````
    aaa
    ```
    ``````
    
    --- expected HTML
    +++ actual HTML
    @@ -1,3 +1 @@
    -<pre><code>aaa
    -```
    -</code></pre>
    +
    
    Example 125 (lines 2056-2065) Fenced code blocks
    ~~~~
    aaa
    ~~~
    ~~~~
    
    --- expected HTML
    +++ actual HTML
    @@ -1,3 +1 @@
    -<pre><code>aaa
    -~~~
    -</code></pre>
    +
    
    Example 126 (lines 2071-2075) Fenced code blocks
    ```
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<pre><code></code></pre>
    +
    
    Example 127 (lines 2078-2088) Fenced code blocks
    `````
    
    ```
    aaa
    
    --- expected HTML
    +++ actual HTML
    @@ -1,4 +1 @@
    -<pre><code>
    -```
    -aaa
    -</code></pre>
    +
    
    Example 128 (lines 2091-2102) Fenced code blocks
    > ```
    > aaa
    
    bbb
    
    --- expected HTML
    +++ actual HTML
    @@ -1,2 +1 @@
    -<blockquote><pre><code>aaa
    -</code></pre></blockquote><p>bbb</p>
    +
    
    Example 129 (lines 2107-2116) Fenced code blocks
    ```
    
      
    ```
    
    --- expected HTML
    +++ actual HTML
    @@ -1,3 +1 @@
    -<pre><code>
    -  
    -</code></pre>
    +
    
    Example 130 (lines 2121-2126) Fenced code blocks
    ```
    ```
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<pre><code></code></pre>
    +
    
    Example 131 (lines 2133-2142) Fenced code blocks
     ```
     aaa
    aaa
    ```
    
    --- expected HTML
    +++ actual HTML
    @@ -1,3 +1 @@
    -<pre><code>aaa
    -aaa
    -</code></pre>
    +
    
    Example 132 (lines 2145-2156) Fenced code blocks
      ```
    aaa
      aaa
    aaa
      ```
    
    --- expected HTML
    +++ actual HTML
    @@ -1,4 +1 @@
    -<pre><code>aaa
    -aaa
    -aaa
    -</code></pre>
    +
    
    Example 133 (lines 2159-2170) Fenced code blocks
       ```
       aaa
        aaa
      aaa
       ```
    
    --- expected HTML
    +++ actual HTML
    @@ -1,4 +1 @@
    -<pre><code>aaa
    - aaa
    -aaa
    -</code></pre>
    +
    
    Example 134 (lines 2175-2184) Fenced code blocks
        ```
        aaa
        ```
    
    --- expected HTML
    +++ actual HTML
    @@ -1,4 +1 @@
    -<pre><code>```
    -aaa
    -```
    -</code></pre>
    +
    
    Example 135 (lines 2190-2197) Fenced code blocks
    ```
    aaa
      ```
    
    --- expected HTML
    +++ actual HTML
    @@ -1,2 +1 @@
    -<pre><code>aaa
    -</code></pre>
    +
    
    Example 136 (lines 2200-2207) Fenced code blocks
       ```
    aaa
      ```
    
    --- expected HTML
    +++ actual HTML
    @@ -1,2 +1 @@
    -<pre><code>aaa
    -</code></pre>
    +
    
    Example 137 (lines 2212-2220) Fenced code blocks
    ```
    aaa
        ```
    
    --- expected HTML
    +++ actual HTML
    @@ -1,3 +1 @@
    -<pre><code>aaa
    -    ```
    -</code></pre>
    +
    
    Example 138 (lines 2226-2232) Fenced code blocks
    ``` ```
    aaa
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><code> </code> aaa</p>
    +
    
    Example 139 (lines 2235-2243) Fenced code blocks
    ~~~~~~
    aaa
    ~~~ ~~
    
    --- expected HTML
    +++ actual HTML
    @@ -1,3 +1 @@
    -<pre><code>aaa
    -~~~ ~~
    -</code></pre>
    +
    
    Example 140 (lines 2249-2260) Fenced code blocks
    foo
    ```
    bar
    ```
    baz
    
    --- expected HTML
    +++ actual HTML
    @@ -1,2 +1 @@
    -<p>foo</p><pre><code>bar
    -</code></pre><p>baz</p>
    +
    
    Example 141 (lines 2266-2278) Fenced code blocks
    foo
    ---
    ~~~
    bar
    ~~~
    # baz
    
    --- expected HTML
    +++ actual HTML
    @@ -1,2 +1 @@
    -<h2>foo</h2><pre><code>bar
    -</code></pre><h1>baz</h1>
    +
    
    Example 142 (lines 2288-2299) Fenced code blocks
    ```ruby
    def foo(x)
      return 3
    end
    ```
    
    --- expected HTML
    +++ actual HTML
    @@ -1,4 +1 @@
    -<pre><code class="language-ruby">def foo(x)
    -  return 3
    -end
    -</code></pre>
    +
    
    Example 143 (lines 2302-2313) Fenced code blocks
    ~~~~    ruby startline=3 $%@#$
    def foo(x)
      return 3
    end
    ~~~~~~~
    
    --- expected HTML
    +++ actual HTML
    @@ -1,4 +1 @@
    -<pre><code class="language-ruby">def foo(x)
    -  return 3
    -end
    -</code></pre>
    +
    
    Example 144 (lines 2316-2321) Fenced code blocks
    ````;
    ````
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<pre><code class="language-;"></code></pre>
    +
    
    Example 145 (lines 2326-2332) Fenced code blocks
    ``` aa ```
    foo
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><code>aa</code> foo</p>
    +
    
    Example 146 (lines 2337-2344) Fenced code blocks
    ~~~ aa ``` ~~~
    foo
    ~~~
    
    --- expected HTML
    +++ actual HTML
    @@ -1,2 +1 @@
    -<pre><code class="language-aa">foo
    -</code></pre>
    +
    
    Example 147 (lines 2349-2356) Fenced code blocks
    ```
    ``` aaa
    ```
    
    --- expected HTML
    +++ actual HTML
    @@ -1,2 +1 @@
    -<pre><code>``` aaa
    -</code></pre>
    +
    
    Example 148 (lines 2429-2444) HTML blocks
    <table><tr><td>
    <pre>
    **Hello**,
    
    _world_.
    </pre>
    </td></tr></table>
    
    --- expected HTML
    +++ actual HTML
    @@ -1,3 +1 @@
    -<table><tr><td><pre>
    -**Hello**,<p><em>world</em>.
    -</pre></p></td></tr></table>
    +
    
    Example 149 (lines 2458-2477) HTML blocks
    <table>
      <tr>
        <td>
               hi
        </td>
      </tr>
    </table>
    
    okay.
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<table><tr><td>hi</td></tr></table><p>okay.</p>
    +
    
    Example 150 (lines 2480-2488) HTML blocks
     <div>
      *hello*
             <foo><a>
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<div>*hello* <foo><a> 
    +
    
    Example 151 (lines 2493-2499) HTML blocks
    </div>
    *foo*
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -</div>*foo*
    +
    
    Example 152 (lines 2504-2514) HTML blocks
    <DIV CLASS="foo">
    
    *Markdown*
    
    </DIV>
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<div class="foo"><p><em>Markdown</em></p></div>
    +
    
    Example 153 (lines 2520-2528) HTML blocks
    <div id="foo"
      class="bar">
    </div>
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<div class="bar" id="foo"></div>
    +
    
    Example 154 (lines 2531-2539) HTML blocks
    <div id="foo" class="bar
      baz">
    </div>
    
    --- expected HTML
    +++ actual HTML
    @@ -1,2 +1 @@
    -<div class="bar
    -  baz" id="foo"></div>
    +
    
    Example 155 (lines 2543-2552) HTML blocks
    <div>
    *foo*
    
    *bar*
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<div>*foo*<p><em>bar</em></p>
    +
    
    Example 156 (lines 2559-2565) HTML blocks
    <div id="foo"
    *hi*
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -div id="foo" *hi* 
    +
    
    Example 157 (lines 2568-2574) HTML blocks
    <div class
    foo
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -div class foo 
    +
    
    Example 158 (lines 2580-2586) HTML blocks
    <div *???-&&&-<---
    *foo*
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -div *???-&&&---- *foo* 
    +
    
    Example 159 (lines 2592-2596) HTML blocks
    <div><a href="bar">*foo*</a></div>
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<div><a href="bar">*foo*</a></div>
    +
    
    Example 160 (lines 2599-2607) HTML blocks
    <table><tr><td>
    foo
    </td></tr></table>
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<table><tr><td>foo</td></tr></table>
    +
    
    Example 161 (lines 2616-2626) HTML blocks
    <div></div>
    ``` c
    int x = 33;
    ```
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<div></div>``` c int x = 33; ```
    +
    
    Example 162 (lines 2629-2635) HTML blocks
    <div
    > not quoted text
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<div>not quoted text 
    +
    
    Example 163 (lines 2642-2650) HTML blocks
    <a href="foo">
    *bar*
    </a>
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<a href="foo"> *bar* </a> 
    +
    
    Example 164 (lines 2655-2663) HTML blocks
    <Warning>
    *bar*
    </Warning>
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<warning> *bar* </warning> 
    +
    
    Example 165 (lines 2666-2674) HTML blocks
    <i class="foo">
    *bar*
    </i>
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<i class="foo"> *bar* </i> 
    +
    
    Example 166 (lines 2677-2683) HTML blocks
    </ins>
    *bar*
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -</ins> *bar* 
    +
    
    Example 167 (lines 2692-2700) HTML blocks
    <del>
    *foo*
    </del>
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<del> *foo* </del> 
    +
    
    Example 168 (lines 2707-2717) HTML blocks
    <del>
    
    *foo*
    
    </del>
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<del><p><em>foo</em></p></del> 
    +
    
    Example 169 (lines 2725-2729) HTML blocks
    <del>*foo*</del>
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><del><em>foo</em></del></p>
    +
    
    Example 170 (lines 2731-2741) HTML blocks
    <del
    class="foo">
    *foo*
    </del>
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><del class="foo"> <em>foo</em> </del></p>
    +
    
    Example 171 (lines 2753-2769) HTML blocks
    <pre language="haskell"><code>
    import Text.HTML.TagSoup
    
    main :: IO ()
    main = print $ parseTags tags
    </code></pre>
    okay
    
    --- expected HTML
    +++ actual HTML
    @@ -1,6 +1 @@
    -<pre language="haskell"><code>
    -import Text.HTML.TagSoup
     
    -main :: IO ()
    -main = print $ parseTags tags
    -</code></pre><p>okay</p>
    
    Example 172 (lines 2774-2788) HTML blocks
    <script type="text/javascript">
    // JavaScript example
    
    document.getElementById("demo").innerHTML = "Hello JavaScript!";
    </script>
    okay
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<script type="text/javascript">// JavaScript example document.getElementById("demo").innerHTML = "Hello JavaScript!";</script><p>okay</p>
    +
    
    Example 173 (lines 2793-2809) HTML blocks
    <textarea>
    
    *foo*
    
    _bar_
    
    </textarea>
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<textarea>*foo* _bar_</textarea>
    +
    
    Example 174 (lines 2813-2829) HTML blocks
    <style
      type="text/css">
    h1 {color:red;}
    
    p {color:blue;}
    </style>
    okay
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<style type="text/css">h1 {color:red;} p {color:blue;}</style><p>okay</p>
    +
    
    Example 175 (lines 2836-2846) HTML blocks
    <style
      type="text/css">
    
    foo
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<style type="text/css">foo 
    +
    
    Example 176 (lines 2849-2860) HTML blocks
    > <div>
    > foo
    
    bar
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<blockquote><div>foo</blockquote><p>bar</p>
    +
    
    Example 177 (lines 2863-2873) HTML blocks
    - <div>
    - foo
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<ul><li><div></li><li>foo</li></ul>
    +
    
    Example 178 (lines 2878-2884) HTML blocks
    <style>p{color:red;}</style>
    *foo*
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<style>p{color:red;}</style><p><em>foo</em></p>
    +
    
    Example 179 (lines 2887-2893) HTML blocks
    <!-- foo -->*bar*
    *baz*
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<!-- foo -->*bar*<p><em>baz</em></p>
    +
    
    Example 180 (lines 2899-2907) HTML blocks
    <script>
    foo
    </script>1. *bar*
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<script>foo</script>1. *bar*
    +
    
    Example 181 (lines 2912-2924) HTML blocks
    <!-- Foo
    
    bar
       baz -->
    okay
    
    --- expected HTML
    +++ actual HTML
    @@ -1,4 +1 @@
    -<!-- Foo
     
    -bar
    -   baz --><p>okay</p>
    
    Example 182 (lines 2930-2944) HTML blocks
    <?php
    
      echo '>';
    
    ?>
    okay
    
    --- expected HTML
    +++ actual HTML
    @@ -1,3 +1 @@
    -<?php
     
    -  echo '>'; ?><p>okay</p>
    
    Example 183 (lines 2949-2953) HTML blocks
    <!DOCTYPE html>
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<!DOCTYPE html> 
    +
    
    Example 184 (lines 2958-2986) HTML blocks
    <![CDATA[
    function matchwo(a,b)
    {
      if (a < b && a < 0) then {
        return 1;
    
      } else {
    
        return 0;
      }
    }
    ]]>
    okay
    
    --- expected HTML
    +++ actual HTML
    @@ -1,12 +1 @@
    -<![CDATA[
    -function matchwo(a,b)
    -{
    -  if (a < b && a < 0) then {
    -    return 1;
     
    -  } else {
    -
    -    return 0;
    -  }
    -}
    -]]><p>okay</p>
    
    Example 185 (lines 2992-3000) HTML blocks
      <!-- foo -->
    
        <!-- foo -->
    
    --- expected HTML
    +++ actual HTML
    @@ -1,2 +1 @@
    - <!-- foo --><pre><code>&lt;!-- foo --&gt;
    -</code></pre>
    +
    
    Example 186 (lines 3003-3011) HTML blocks
      <div>
    
        <div>
    
    --- expected HTML
    +++ actual HTML
    @@ -1,2 +1 @@
    -<div><pre><code>&lt;div&gt;
    -</code></pre>
    +
    
    Example 187 (lines 3017-3027) HTML blocks
    Foo
    <div>
    bar
    </div>
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>Foo</p><div>bar</div>
    +
    
    Example 188 (lines 3034-3044) HTML blocks
    <div>
    bar
    </div>
    *foo*
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<div>bar</div>*foo*
    +
    
    Example 189 (lines 3049-3057) HTML blocks
    Foo
    <a href="bar">
    baz
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>Foo <a href="bar"> baz</p>
    +
    
    Example 190 (lines 3090-3100) HTML blocks
    <div>
    
    *Emphasized* text.
    
    </div>
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<div><p><em>Emphasized</em> text.</p></div>
    +
    
    Example 191 (lines 3103-3111) HTML blocks
    <div>
    *Emphasized* text.
    </div>
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<div>*Emphasized* text.</div>
    +
    
    Example 192 (lines 3125-3145) HTML blocks
    <table>
    
    <tr>
    
    <td>
    Hi
    </td>
    
    </tr>
    
    </table>
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<table><tr><td>Hi</td></tr></table>
    +
    
    Example 193 (lines 3152-3173) HTML blocks
    <table>
    
      <tr>
    
        <td>
          Hi
        </td>
    
      </tr>
    
    </table>
    
    --- expected HTML
    +++ actual HTML
    @@ -1,4 +1 @@
    -<table><tr><pre><code>&lt;td&gt;
    -  Hi
    -&lt;/td&gt;
    -</code></pre></tr></table>
    +
    
    Example 194 (lines 3201-3207) Link reference definitions
    [foo]: /url "title"
    
    [foo]
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><a href="/url" title="title">foo</a></p>
    +
    
    Example 195 (lines 3210-3218) Link reference definitions
       [foo]: 
          /url  
               'the title'  
    
    [foo]
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><a href="/url" title="the title">foo</a></p>
    +
    
    Example 196 (lines 3221-3227) Link reference definitions
    [Foo*bar\]]:my_(url) 'title (with parens)'
    
    [Foo*bar\]]
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><a href="my_(url)" title="title (with parens)">Foo*bar]</a></p>
    +
    
    Example 197 (lines 3230-3238) Link reference definitions
    [Foo bar]:
    <my url>
    'title'
    
    [Foo bar]
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><a href="my%20url" title="title">Foo bar</a></p>
    +
    
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
    +
    
    Example 199 (lines 3262-3272) Link reference definitions
    [foo]: /url 'title
    
    with blank line'
    
    [foo]
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>[foo]: /url 'title</p><p>with blank line'</p><p>[foo]</p>
    +
    
    Example 200 (lines 3277-3284) Link reference definitions
    [foo]:
    /url
    
    [foo]
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><a href="/url">foo</a></p>
    +
    
    Example 201 (lines 3289-3296) Link reference definitions
    [foo]:
    
    [foo]
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>[foo]:</p><p>[foo]</p>
    +
    
    Example 202 (lines 3301-3307) Link reference definitions
    [foo]: <>
    
    [foo]
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><a href="">foo</a></p>
    +
    
    Example 203 (lines 3312-3319) Link reference definitions
    [foo]: <bar>(baz)
    
    [foo]
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>[foo]: <bar>(baz)</p><p>[foo]</p>
    +
    
    Example 204 (lines 3325-3331) Link reference definitions
    [foo]: /url\bar\*baz "foo\"bar\baz"
    
    [foo]
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><a href="/url%5Cbar*baz" title="foo&quot;bar\baz">foo</a></p>
    +
    
    Example 205 (lines 3336-3342) Link reference definitions
    [foo]
    
    [foo]: url
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><a href="url">foo</a></p>
    +
    
    Example 206 (lines 3348-3355) Link reference definitions
    [foo]
    
    [foo]: first
    [foo]: second
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><a href="first">foo</a></p>
    +
    
    Example 207 (lines 3361-3367) Link reference definitions
    [FOO]: /url
    
    [Foo]
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><a href="/url">Foo</a></p>
    +
    
    Example 208 (lines 3370-3376) Link reference definitions
    [ΑΓΩ]: /φου
    
    [αγω]
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><a href="/%CF%86%CE%BF%CF%85">αγω</a></p>
    +
    
    Example 210 (lines 3393-3400) Link reference definitions
    [
    foo
    ]: /url
    bar
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>bar</p>
    +
    
    Example 211 (lines 3406-3410) Link reference definitions
    [foo]: /url "title" ok
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>[foo]: /url &quot;title&quot; ok</p>
    +
    
    Example 212 (lines 3415-3420) Link reference definitions
    [foo]: /url
    "title" ok
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>&quot;title&quot; ok</p>
    +
    
    Example 213 (lines 3426-3434) Link reference definitions
        [foo]: /url "title"
    
    [foo]
    
    --- expected HTML
    +++ actual HTML
    @@ -1,2 +1 @@
    -<pre><code>[foo]: /url &quot;title&quot;
    -</code></pre><p>[foo]</p>
    +
    
    Example 214 (lines 3440-3450) Link reference definitions
    ```
    [foo]: /url
    ```
    
    [foo]
    
    --- expected HTML
    +++ actual HTML
    @@ -1,2 +1 @@
    -<pre><code>[foo]: /url
    -</code></pre><p>[foo]</p>
    +
    
    Example 215 (lines 3455-3464) Link reference definitions
    Foo
    [bar]: /baz
    
    [bar]
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>Foo [bar]: /baz</p><p>[bar]</p>
    +
    
    Example 216 (lines 3470-3479) Link reference definitions
    # [Foo]
    [foo]: /url
    > bar
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<h1><a href="/url">Foo</a></h1><blockquote><p>bar</p></blockquote>
    +
    
    Example 217 (lines 3481-3489) Link reference definitions
    [foo]: /url
    bar
    ===
    [foo]
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<h1>bar</h1><p><a href="/url">foo</a></p>
    +
    
    Example 218 (lines 3491-3498) Link reference definitions
    [foo]: /url
    ===
    [foo]
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>=== <a href="/url">foo</a></p>
    +
    
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
    +
    
    Example 220 (lines 3525-3533) Link reference definitions
    [foo]
    
    > [foo]: /url
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><a href="/url">foo</a></p><blockquote></blockquote>
    +
    
    Example 221 (lines 3547-3554) Paragraphs
    aaa
    
    bbb
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>aaa</p><p>bbb</p>
    +
    
    Example 222 (lines 3559-3570) Paragraphs
    aaa
    bbb
    
    ccc
    ddd
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>aaa bbb</p><p>ccc ddd</p>
    +
    
    Example 223 (lines 3575-3583) Paragraphs
    aaa
    
    
    bbb
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>aaa</p><p>bbb</p>
    +
    
    Example 224 (lines 3588-3594) Paragraphs
      aaa
     bbb
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>aaa bbb</p>
    +
    
    Example 225 (lines 3600-3608) Paragraphs
    aaa
                 bbb
                                           ccc
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>aaa bbb ccc</p>
    +
    
    Example 226 (lines 3614-3620) Paragraphs
       aaa
    bbb
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>aaa bbb</p>
    +
    
    Example 227 (lines 3623-3630) Paragraphs
        aaa
    bbb
    
    --- expected HTML
    +++ actual HTML
    @@ -1,2 +1 @@
    -<pre><code>aaa
    -</code></pre><p>bbb</p>
    +
    
    Example 228 (lines 3637-3643) Paragraphs
    aaa     
    bbb     
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>aaa<br>bbb</p>
    +
    
    Example 229 (lines 3654-3666) Blank lines
      
    
    aaa
      
    
    # aaa
    
      
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>aaa</p><h1>aaa</h1>
    +
    
    1 passed, 186 failed, 0 errored, 468 skipped
  stderr:
    --- drydock: progress ---
    cases: pass=1 fail=186 error=0 skip=468 total=655 from=result.stdout
    --- drydock: end progress ---
    --- drydock: values at failure ---
      result = CompletedProcess(args=['/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/.venv/bin/python', 'sources/spec_tests.py', '--program', '/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/commonmark', '--spec', 'sources/spec.txt', '--pattern', '^(Thematic breaks|ATX headings|Setext headings|Indented code blocks|Fenced code blo… (+32023 chars)
    --- drydock: end values ---
    Traceback (most recent call last):
      File "conformance-blocks.py", line 12, in <module>
        assert result.returncode == 0
               ^^^^^^^^^^^^^^^^^^^^^^
    AssertionError
- RED: conformance-containers (FEATURE-ConformanceIntegration.md)
  intent: The integrated parser passes every supplied block quote, list item, and list example.
  return code: 1
  stdout:
    Example 230 (lines 3722-3732) Block quotes
    > # Foo
    > bar
    > baz
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<blockquote><h1>Foo</h1><p>bar baz</p></blockquote>
    +
    
    Example 231 (lines 3737-3747) Block quotes
    ># Foo
    >bar
    > baz
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<blockquote><h1>Foo</h1><p>bar baz</p></blockquote>
    +
    
    Example 232 (lines 3752-3762) Block quotes
       > # Foo
       > bar
     > baz
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<blockquote><h1>Foo</h1><p>bar baz</p></blockquote>
    +
    
    Example 233 (lines 3767-3776) Block quotes
        > # Foo
        > bar
        > baz
    
    --- expected HTML
    +++ actual HTML
    @@ -1,4 +1 @@
    -<pre><code>&gt; # Foo
    -&gt; bar
    -&gt; baz
    -</code></pre>
    +
    
    Example 234 (lines 3782-3792) Block quotes
    > # Foo
    > bar
    baz
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<blockquote><h1>Foo</h1><p>bar baz</p></blockquote>
    +
    
    Example 235 (lines 3798-3808) Block quotes
    > bar
    baz
    > foo
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<blockquote><p>bar baz foo</p></blockquote>
    +
    
    Example 236 (lines 3822-3830) Block quotes
    > foo
    ---
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<blockquote><p>foo</p></blockquote><hr>
    +
    
    Example 237 (lines 3842-3854) Block quotes
    > - foo
    - bar
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<blockquote><ul><li>foo</li></ul></blockquote><ul><li>bar</li></ul>
    +
    
    Example 238 (lines 3860-3870) Block quotes
    >     foo
        bar
    
    --- expected HTML
    +++ actual HTML
    @@ -1,3 +1 @@
    -<blockquote><pre><code>foo
    -</code></pre></blockquote><pre><code>bar
    -</code></pre>
    +
    
    Example 239 (lines 3873-3883) Block quotes
    > ```
    foo
    ```
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<blockquote><pre><code></code></pre></blockquote><p>foo</p><pre><code></code></pre>
    +
    
    Example 240 (lines 3889-3897) Block quotes
    > foo
        - bar
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<blockquote><p>foo - bar</p></blockquote>
    +
    
    Example 241 (lines 3913-3918) Block quotes
    >
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<blockquote></blockquote>
    +
    
    Example 242 (lines 3921-3928) Block quotes
    >
    >  
    > 
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<blockquote></blockquote>
    +
    
    Example 243 (lines 3933-3941) Block quotes
    >
    > foo
    >  
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<blockquote><p>foo</p></blockquote>
    +
    
    Example 244 (lines 3946-3957) Block quotes
    > foo
    
    > bar
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<blockquote><p>foo</p></blockquote><blockquote><p>bar</p></blockquote>
    +
    
    Example 245 (lines 3968-3976) Block quotes
    > foo
    > bar
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<blockquote><p>foo bar</p></blockquote>
    +
    
    Example 246 (lines 3981-3990) Block quotes
    > foo
    >
    > bar
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<blockquote><p>foo</p><p>bar</p></blockquote>
    +
    
    Example 247 (lines 3995-4003) Block quotes
    foo
    > bar
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>foo</p><blockquote><p>bar</p></blockquote>
    +
    
    Example 248 (lines 4009-4021) Block quotes
    > aaa
    ***
    > bbb
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<blockquote><p>aaa</p></blockquote><hr><blockquote><p>bbb</p></blockquote>
    +
    
    Example 249 (lines 4027-4035) Block quotes
    > bar
    baz
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<blockquote><p>bar baz</p></blockquote>
    +
    
    Example 250 (lines 4038-4047) Block quotes
    > bar
    
    baz
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<blockquote><p>bar</p></blockquote><p>baz</p>
    +
    
    Example 251 (lines 4050-4059) Block quotes
    > bar
    >
    baz
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<blockquote><p>bar</p></blockquote><p>baz</p>
    +
    
    Example 252 (lines 4066-4078) Block quotes
    > > > foo
    bar
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<blockquote><blockquote><blockquote><p>foo bar</p></blockquote></blockquote></blockquote>
    +
    
    Example 253 (lines 4081-4095) Block quotes
    >>> foo
    > bar
    >>baz
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<blockquote><blockquote><blockquote><p>foo bar baz</p></blockquote></blockquote></blockquote>
    +
    
    Example 254 (lines 4103-4115) Block quotes
    >     code
    
    >    not code
    
    --- expected HTML
    +++ actual HTML
    @@ -1,2 +1 @@
    -<blockquote><pre><code>code
    -</code></pre></blockquote><blockquote><p>not code</p></blockquote>
    +
    
    Example 255 (lines 4157-4172) List items
    A paragraph
    with two lines.
    
        indented code
    
    > A block quote.
    
    --- expected HTML
    +++ actual HTML
    @@ -1,2 +1 @@
    -<p>A paragraph with two lines.</p><pre><code>indented code
    -</code></pre><blockquote><p>A block quote.</p></blockquote>
    +
    
    Example 256 (lines 4179-4198) List items
    1.  A paragraph
        with two lines.
    
            indented code
    
        > A block quote.
    
    --- expected HTML
    +++ actual HTML
    @@ -1,2 +1 @@
    -<ol><li><p>A paragraph with two lines.</p><pre><code>indented code
    -</code></pre><blockquote><p>A block quote.</p></blockquote></li></ol>
    +
    
    Example 257 (lines 4212-4221) List items
    - one
    
     two
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<ul><li>one</li></ul><p>two</p>
    +
    
    Example 258 (lines 4224-4235) List items
    - one
    
      two
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<ul><li><p>one</p><p>two</p></li></ul>
    +
    
    Example 259 (lines 4238-4248) List items
     -    one
    
         two
    
    --- expected HTML
    +++ actual HTML
    @@ -1,2 +1 @@
    -<ul><li>one</li></ul><pre><code> two
    -</code></pre>
    +
    
    Example 260 (lines 4251-4262) List items
     -    one
    
          two
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<ul><li><p>one</p><p>two</p></li></ul>
    +
    
    Example 261 (lines 4273-4288) List items
       > > 1.  one
    >>
    >>     two
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<blockquote><blockquote><ol><li><p>one</p><p>two</p></li></ol></blockquote></blockquote>
    +
    
    Example 262 (lines 4300-4313) List items
    >>- one
    >>
      >  > two
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<blockquote><blockquote><ul><li>one</li></ul><p>two</p></blockquote></blockquote>
    +
    
    Example 263 (lines 4319-4326) List items
    -one
    
    2.two
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>-one</p><p>2.two</p>
    +
    
    Example 264 (lines 4332-4344) List items
    - foo
    
    
      bar
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<ul><li><p>foo</p><p>bar</p></li></ul>
    +
    
    Example 265 (lines 4349-4371) List items
    1.  foo
    
        ```
        bar
        ```
    
        baz
    
        > bam
    
    --- expected HTML
    +++ actual HTML
    @@ -1,2 +1 @@
    -<ol><li><p>foo</p><pre><code>bar
    -</code></pre><p>baz</p><blockquote><p>bam</p></blockquote></li></ol>
    +
    
    Example 266 (lines 4377-4395) List items
    - Foo
    
          bar
    
    
          baz
    
    --- expected HTML
    +++ actual HTML
    @@ -1,5 +1 @@
    -<ul><li><p>Foo</p><pre><code>bar
     
    -
    -baz
    -</code></pre></li></ul>
    
    Example 267 (lines 4399-4405) List items
    123456789. ok
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<ol start="123456789"><li>ok</li></ol>
    +
    
    Example 268 (lines 4408-4412) List items
    1234567890. not ok
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>1234567890. not ok</p>
    +
    
    Example 269 (lines 4417-4423) List items
    0. ok
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<ol start="0"><li>ok</li></ol>
    +
    
    Example 270 (lines 4426-4432) List items
    003. ok
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<ol start="3"><li>ok</li></ol>
    +
    
    Example 271 (lines 4437-4441) List items
    -1. not ok
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>-1. not ok</p>
    +
    
    Example 272 (lines 4460-4472) List items
    - foo
    
          bar
    
    --- expected HTML
    +++ actual HTML
    @@ -1,2 +1 @@
    -<ul><li><p>foo</p><pre><code>bar
    -</code></pre></li></ul>
    +
    
    Example 273 (lines 4477-4489) List items
      10.  foo
    
               bar
    
    --- expected HTML
    +++ actual HTML
    @@ -1,2 +1 @@
    -<ol start="10"><li><p>foo</p><pre><code>bar
    -</code></pre></li></ol>
    +
    
    Example 274 (lines 4496-4508) List items
        indented code
    
    paragraph
    
        more code
    
    --- expected HTML
    +++ actual HTML
    @@ -1,3 +1 @@
    -<pre><code>indented code
    -</code></pre><p>paragraph</p><pre><code>more code
    -</code></pre>
    +
    
    Example 275 (lines 4511-4527) List items
    1.     indented code
    
       paragraph
    
           more code
    
    --- expected HTML
    +++ actual HTML
    @@ -1,3 +1 @@
    -<ol><li><pre><code>indented code
    -</code></pre><p>paragraph</p><pre><code>more code
    -</code></pre></li></ol>
    +
    
    Example 276 (lines 4533-4549) List items
    1.      indented code
    
       paragraph
    
           more code
    
    --- expected HTML
    +++ actual HTML
    @@ -1,3 +1 @@
    -<ol><li><pre><code> indented code
    -</code></pre><p>paragraph</p><pre><code>more code
    -</code></pre></li></ol>
    +
    
    Example 277 (lines 4560-4567) List items
       foo
    
    bar
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>foo</p><p>bar</p>
    +
    
    Example 278 (lines 4570-4579) List items
    -    foo
    
      bar
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<ul><li>foo</li></ul><p>bar</p>
    +
    
    Example 279 (lines 4587-4598) List items
    -  foo
    
       bar
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<ul><li><p>foo</p><p>bar</p></li></ul>
    +
    
    Example 280 (lines 4614-4635) List items
    -
      foo
    -
      ```
      bar
      ```
    -
          baz
    
    --- expected HTML
    +++ actual HTML
    @@ -1,3 +1 @@
    -<ul><li>foo</li><li><pre><code>bar
    -</code></pre></li><li><pre><code>baz
    -</code></pre></li></ul>
    +
    
    Example 281 (lines 4640-4647) List items
    -   
      foo
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<ul><li>foo</li></ul>
    +
    
    Example 282 (lines 4654-4663) List items
    -
    
      foo
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<ul><li></li></ul><p>foo</p>
    +
    
    Example 283 (lines 4668-4678) List items
    - foo
    -
    - bar
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<ul><li>foo</li><li></li><li>bar</li></ul>
    +
    
    Example 284 (lines 4683-4693) List items
    - foo
    -   
    - bar
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<ul><li>foo</li><li></li><li>bar</li></ul>
    +
    
    Example 285 (lines 4698-4708) List items
    1. foo
    2.
    3. bar
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<ol><li>foo</li><li></li><li>bar</li></ol>
    +
    
    Example 286 (lines 4713-4719) List items
    *
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<ul><li></li></ul>
    +
    
    Example 287 (lines 4723-4734) List items
    foo
    *
    
    foo
    1.
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>foo *</p><p>foo 1.</p>
    +
    
    Example 288 (lines 4745-4764) List items
     1.  A paragraph
         with two lines.
    
             indented code
    
         > A block quote.
    
    --- expected HTML
    +++ actual HTML
    @@ -1,2 +1 @@
    -<ol><li><p>A paragraph with two lines.</p><pre><code>indented code
    -</code></pre><blockquote><p>A block quote.</p></blockquote></li></ol>
    +
    
    Example 289 (lines 4769-4788) List items
      1.  A paragraph
          with two lines.
    
              indented code
    
          > A block quote.
    
    --- expected HTML
    +++ actual HTML
    @@ -1,2 +1 @@
    -<ol><li><p>A paragraph with two lines.</p><pre><code>indented code
    -</code></pre><blockquote><p>A block quote.</p></blockquote></li></ol>
    +
    
    Example 290 (lines 4793-4812) List items
       1.  A paragraph
           with two lines.
    
               indented code
    
           > A block quote.
    
    --- expected HTML
    +++ actual HTML
    @@ -1,2 +1 @@
    -<ol><li><p>A paragraph with two lines.</p><pre><code>indented code
    -</code></pre><blockquote><p>A block quote.</p></blockquote></li></ol>
    +
    
    Example 291 (lines 4817-4832) List items
        1.  A paragraph
            with two lines.
    
                indented code
    
            > A block quote.
    
    --- expected HTML
    +++ actual HTML
    @@ -1,7 +1 @@
    -<pre><code>1.  A paragraph
    -    with two lines.
     
    -        indented code
    -
    -    &gt; A block quote.
    -</code></pre>
    
    Example 292 (lines 4847-4866) List items
      1.  A paragraph
    with two lines.
    
              indented code
    
          > A block quote.
    
    --- expected HTML
    +++ actual HTML
    @@ -1,2 +1 @@
    -<ol><li><p>A paragraph with two lines.</p><pre><code>indented code
    -</code></pre><blockquote><p>A block quote.</p></blockquote></li></ol>
    +
    
    Example 293 (lines 4871-4879) List items
      1.  A paragraph
        with two lines.
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<ol><li>A paragraph with two lines.</li></ol>
    +
    
    Example 294 (lines 4884-4898) List items
    > 1. > Blockquote
    continued here.
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<blockquote><ol><li><blockquote><p>Blockquote continued here.</p></blockquote></li></ol></blockquote>
    +
    
    Example 295 (lines 4901-4915) List items
    > 1. > Blockquote
    > continued here.
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<blockquote><ol><li><blockquote><p>Blockquote continued here.</p></blockquote></li></ol></blockquote>
    +
    
    Example 296 (lines 4929-4950) List items
    - foo
      - bar
        - baz
          - boo
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<ul><li>foo<ul><li>bar<ul><li>baz<ul><li>boo</li></ul></li></ul></li></ul></li></ul>
    +
    
    Example 297 (lines 4955-4967) List items
    - foo
     - bar
      - baz
       - boo
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<ul><li>foo</li><li>bar</li><li>baz</li><li>boo</li></ul>
    +
    
    Example 298 (lines 4972-4983) List items
    10) foo
        - bar
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<ol start="10"><li>foo<ul><li>bar</li></ul></li></ol>
    +
    
    Example 299 (lines 4988-4998) List items
    10) foo
       - bar
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<ol start="10"><li>foo</li></ol><ul><li>bar</li></ul>
    +
    
    Example 300 (lines 5003-5013) List items
    - - foo
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<ul><li><ul><li>foo</li></ul></li></ul>
    +
    
    Example 301 (lines 5016-5030) List items
    1. - 2. foo
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<ol><li><ul><li><ol start="2"><li>foo</li></ol></li></ul></li></ol>
    +
    
    Example 302 (lines 5035-5049) List items
    - # Foo
    - Bar
      ---
      baz
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<ul><li><h1>Foo</h1></li><li><h2>Bar</h2>baz</li></ul>
    +
    
    Example 303 (lines 5271-5283) Lists
    - foo
    - bar
    + baz
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<ul><li>foo</li><li>bar</li></ul><ul><li>baz</li></ul>
    +
    
    Example 304 (lines 5286-5298) Lists
    1. foo
    2. bar
    3) baz
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<ol><li>foo</li><li>bar</li></ol><ol start="3"><li>baz</li></ol>
    +
    
    Example 305 (lines 5305-5315) Lists
    Foo
    - bar
    - baz
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>Foo</p><ul><li>bar</li><li>baz</li></ul>
    +
    
    Example 306 (lines 5382-5388) Lists
    The number of windows in my house is
    14.  The number of doors is 6.
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>The number of windows in my house is 14. The number of doors is 6.</p>
    +
    
    Example 307 (lines 5392-5400) Lists
    The number of windows in my house is
    1.  The number of doors is 6.
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>The number of windows in my house is</p><ol><li>The number of doors is 6.</li></ol>
    +
    
    Example 308 (lines 5406-5425) Lists
    - foo
    
    - bar
    
    
    - baz
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<ul><li><p>foo</p></li><li><p>bar</p></li><li><p>baz</p></li></ul>
    +
    
    Example 309 (lines 5427-5449) Lists
    - foo
      - bar
        - baz
    
    
          bim
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<ul><li>foo<ul><li>bar<ul><li><p>baz</p><p>bim</p></li></ul></li></ul></li></ul>
    +
    
    Example 310 (lines 5457-5475) Lists
    - foo
    - bar
    
    <!-- -->
    
    - baz
    - bim
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<ul><li>foo</li><li>bar</li></ul><!-- --><ul><li>baz</li><li>bim</li></ul>
    +
    
    Example 311 (lines 5478-5501) Lists
    -   foo
    
        notcode
    
    -   foo
    
    <!-- -->
    
        code
    
    --- expected HTML
    +++ actual HTML
    @@ -1,2 +1 @@
    -<ul><li><p>foo</p><p>notcode</p></li><li><p>foo</p></li></ul><!-- --><pre><code>code
    -</code></pre>
    +
    
    Example 312 (lines 5509-5527) Lists
    - a
     - b
      - c
       - d
      - e
     - f
    - g
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<ul><li>a</li><li>b</li><li>c</li><li>d</li><li>e</li><li>f</li><li>g</li></ul>
    +
    
    Example 313 (lines 5530-5548) Lists
    1. a
    
      2. b
    
       3. c
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<ol><li><p>a</p></li><li><p>b</p></li><li><p>c</p></li></ol>
    +
    
    Example 314 (lines 5554-5568) Lists
    - a
     - b
      - c
       - d
        - e
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<ul><li>a</li><li>b</li><li>c</li><li>d - e</li></ul>
    +
    
    Example 315 (lines 5574-5591) Lists
    1. a
    
      2. b
    
        3. c
    
    --- expected HTML
    +++ actual HTML
    @@ -1,2 +1 @@
    -<ol><li><p>a</p></li><li><p>b</p></li></ol><pre><code>3. c
    -</code></pre>
    +
    
    Example 316 (lines 5597-5614) Lists
    - a
    - b
    
    - c
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<ul><li><p>a</p></li><li><p>b</p></li><li><p>c</p></li></ul>
    +
    
    Example 317 (lines 5619-5634) Lists
    * a
    *
    
    * c
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<ul><li><p>a</p></li><li></li><li><p>c</p></li></ul>
    +
    
    Example 318 (lines 5641-5660) Lists
    - a
    - b
    
      c
    - d
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<ul><li><p>a</p></li><li><p>b</p><p>c</p></li><li><p>d</p></li></ul>
    +
    
    Example 319 (lines 5663-5681) Lists
    - a
    - b
    
      [ref]: /url
    - d
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<ul><li><p>a</p></li><li><p>b</p></li><li><p>d</p></li></ul>
    +
    
    Example 320 (lines 5686-5705) Lists
    - a
    - ```
      b
    
    
      ```
    - c
    
    --- expected HTML
    +++ actual HTML
    @@ -1,4 +1 @@
    -<ul><li>a</li><li><pre><code>b
     
    -
    -</code></pre></li><li>c</li></ul>
    
    Example 321 (lines 5712-5730) Lists
    - a
      - b
    
        c
    - d
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<ul><li>a<ul><li><p>b</p><p>c</p></li></ul></li><li>d</li></ul>
    +
    
    Example 322 (lines 5736-5750) Lists
    * a
      > b
      >
    * c
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<ul><li>a<blockquote><p>b</p></blockquote></li><li>c</li></ul>
    +
    
    Example 323 (lines 5756-5774) Lists
    - a
      > b
      ```
      c
      ```
    - d
    
    --- expected HTML
    +++ actual HTML
    @@ -1,2 +1 @@
    -<ul><li>a<blockquote><p>b</p></blockquote><pre><code>c
    -</code></pre></li><li>d</li></ul>
    +
    
    Example 324 (lines 5779-5785) Lists
    - a
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<ul><li>a</li></ul>
    +
    
    Example 325 (lines 5788-5799) Lists
    - a
      - b
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<ul><li>a<ul><li>b</li></ul></li></ul>
    +
    
    Example 326 (lines 5805-5819) Lists
    1. ```
       foo
       ```
    
       bar
    
    --- expected HTML
    +++ actual HTML
    @@ -1,2 +1 @@
    -<ol><li><pre><code>foo
    -</code></pre><p>bar</p></li></ol>
    +
    
    Example 327 (lines 5824-5839) Lists
    * foo
      * bar
    
      baz
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<ul><li><p>foo</p><ul><li>bar</li></ul><p>baz</p></li></ul>
    +
    
    Example 328 (lines 5842-5867) Lists
    - a
      - b
      - c
    
    - d
      - e
      - f
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<ul><li><p>a</p><ul><li>b</li><li>c</li></ul></li><li><p>d</p><ul><li>e</li><li>f</li></ul></li></ul>
    +
    
    0 passed, 99 failed, 0 errored, 556 skipped
  stderr:
    --- drydock: progress ---
    cases: pass=0 fail=99 error=0 skip=556 total=655 from=result.stdout
    --- drydock: end progress ---
    --- drydock: values at failure ---
      result = CompletedProcess(args=['/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/.venv/bin/python', 'sources/spec_tests.py', '--program', '/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/commonmark', '--spec', 'sources/spec.txt', '--pattern', '^(Block quotes|List items|Lists)$'], returncode=99, stdout='Example 230 (lines 3722… (+19156 chars)
    --- drydock: end values ---
    Traceback (most recent call last):
      File "conformance-containers.py", line 12, in <module>
        assert result.returncode == 0
               ^^^^^^^^^^^^^^^^^^^^^^
    AssertionError
- RED: conformance-inlines (FEATURE-ConformanceIntegration.md)
  intent: The integrated parser passes every example in the supplied inline and text sections.
  return code: 1
  stdout:
    Example 12 (lines 489-493) Backslash escapes
    \!\"\#\$\%\&\'\(\)\*\+\,\-\.\/\:\;\<\=\>\?\@\[\\\]\^\_\`\{\|\}\~
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>!&quot;#$%&amp;'()*+,-./:;&lt;=&gt;?@[\]^_`{|}~</p>
    +
    
    Example 13 (lines 499-503) Backslash escapes
    \	\A\a\ \3\φ\«
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>\ \A\a\ \3\φ\«</p>
    +
    
    Example 14 (lines 509-529) Backslash escapes
    \*not emphasized*
    \<br/> not a tag
    \[not a link](/foo)
    \`not code`
    1\. not a list
    \* not a list
    \# not a heading
    \[foo]: /url "not a reference"
    \&ouml; not a character entity
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>*not emphasized* &lt;br/&gt; not a tag [not a link](/foo) `not code` 1. not a list * not a list # not a heading [foo]: /url &quot;not a reference&quot; &amp;ouml; not a character entity</p>
    +
    
    Example 15 (lines 534-538) Backslash escapes
    \\*emphasis*
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>\<em>emphasis</em></p>
    +
    
    Example 16 (lines 543-549) Backslash escapes
    foo\
    bar
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>foo<br>bar</p>
    +
    
    Example 17 (lines 555-559) Backslash escapes
    `` \[\` ``
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><code>\[\`</code></p>
    +
    
    Example 18 (lines 562-567) Backslash escapes
        \[\]
    
    --- expected HTML
    +++ actual HTML
    @@ -1,2 +1 @@
    -<pre><code>\[\]
    -</code></pre>
    +
    
    Example 19 (lines 570-577) Backslash escapes
    ~~~
    \[\]
    ~~~
    
    --- expected HTML
    +++ actual HTML
    @@ -1,2 +1 @@
    -<pre><code>\[\]
    -</code></pre>
    +
    
    Example 20 (lines 580-584) Backslash escapes
    <https://example.com?find=\*>
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><a href="https://example.com?find=%5C*">https://example.com?find=\*</a></p>
    +
    
    Example 21 (lines 587-591) Backslash escapes
    <a href="/bar\/)">
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<a href="/bar\/)"> 
    +
    
    Example 22 (lines 597-601) Backslash escapes
    [foo](/bar\* "ti\*tle")
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><a href="/bar*" title="ti*tle">foo</a></p>
    +
    
    Example 23 (lines 604-610) Backslash escapes
    [foo]
    
    [foo]: /bar\* "ti\*tle"
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><a href="/bar*" title="ti*tle">foo</a></p>
    +
    
    Example 24 (lines 613-620) Backslash escapes
    ``` foo\+bar
    foo
    ```
    
    --- expected HTML
    +++ actual HTML
    @@ -1,2 +1 @@
    -<pre><code class="language-foo+bar">foo
    -</code></pre>
    +
    
    Example 25 (lines 649-657) Entity and numeric character references
    &nbsp; &amp; &copy; &AElig; &Dcaron;
    &frac34; &HilbertSpace; &DifferentialD;
    &ClockwiseContourIntegral; &ngE;
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>&amp; © Æ Ď ¾ ℋ ⅆ ∲ ≧̸</p>
    +
    
    Example 26 (lines 668-672) Entity and numeric character references
    &#35; &#1234; &#992; &#0;
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p># Ӓ Ϡ �</p>
    +
    
    Example 27 (lines 681-685) Entity and numeric character references
    &#X22; &#XD06; &#xcab;
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>&quot; ആ ಫ</p>
    +
    
    Example 28 (lines 690-700) Entity and numeric character references
    &nbsp &x; &#; &#x;
    &#87654321;
    &#abcdef0;
    &ThisIsNotDefined; &hi?;
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>&amp;nbsp &amp;x; &amp;#; &amp;#x; &amp;#87654321; &amp;#abcdef0; &amp;ThisIsNotDefined; &amp;hi?;</p>
    +
    
    Example 29 (lines 707-711) Entity and numeric character references
    &copy
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>&amp;copy</p>
    +
    
    Example 30 (lines 717-721) Entity and numeric character references
    &MadeUpEntity;
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>&amp;MadeUpEntity;</p>
    +
    
    Example 31 (lines 728-732) Entity and numeric character references
    <a href="&ouml;&ouml;.html">
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<a href="öö.html"> 
    +
    
    Example 32 (lines 735-739) Entity and numeric character references
    [foo](/f&ouml;&ouml; "f&ouml;&ouml;")
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><a href="/f%C3%B6%C3%B6" title="föö">foo</a></p>
    +
    
    Example 33 (lines 742-748) Entity and numeric character references
    [foo]
    
    [foo]: /f&ouml;&ouml; "f&ouml;&ouml;"
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><a href="/f%C3%B6%C3%B6" title="föö">foo</a></p>
    +
    
    Example 34 (lines 751-758) Entity and numeric character references
    ``` f&ouml;&ouml;
    foo
    ```
    
    --- expected HTML
    +++ actual HTML
    @@ -1,2 +1 @@
    -<pre><code class="language-föö">foo
    -</code></pre>
    +
    
    Example 35 (lines 764-768) Entity and numeric character references
    `f&ouml;&ouml;`
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><code>f&amp;ouml;&amp;ouml;</code></p>
    +
    
    Example 36 (lines 771-776) Entity and numeric character references
        f&ouml;f&ouml;
    
    --- expected HTML
    +++ actual HTML
    @@ -1,2 +1 @@
    -<pre><code>f&amp;ouml;f&amp;ouml;
    -</code></pre>
    +
    
    Example 37 (lines 783-789) Entity and numeric character references
    &#42;foo&#42;
    *foo*
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>*foo* <em>foo</em></p>
    +
    
    Example 38 (lines 791-800) Entity and numeric character references
    &#42; foo
    
    * foo
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>* foo</p><ul><li>foo</li></ul>
    +
    
    Example 39 (lines 802-808) Entity and numeric character references
    foo&#10;&#10;bar
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>foo bar</p>
    +
    
    Example 40 (lines 810-814) Entity and numeric character references
    &#9;foo
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>foo</p>
    +
    
    Example 41 (lines 817-821) Entity and numeric character references
    [a](url &quot;tit&quot;)
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>[a](url &quot;tit&quot;)</p>
    +
    
    Example 330 (lines 5908-5912) Code spans
    `foo`
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><code>foo</code></p>
    +
    
    Example 331 (lines 5919-5923) Code spans
    `` foo ` bar ``
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><code>foo ` bar</code></p>
    +
    
    Example 332 (lines 5929-5933) Code spans
    ` `` `
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><code>``</code></p>
    +
    
    Example 333 (lines 5937-5941) Code spans
    `  ``  `
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><code> `` </code></p>
    +
    
    Example 334 (lines 5946-5950) Code spans
    ` a`
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><code> a</code></p>
    +
    
    Example 335 (lines 5955-5959) Code spans
    ` b `
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><code> b </code></p>
    +
    
    Example 336 (lines 5963-5969) Code spans
    ` `
    `  `
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><code> </code> <code> </code></p>
    +
    
    Example 337 (lines 5974-5982) Code spans
    ``
    foo
    bar  
    baz
    ``
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><code>foo bar baz</code></p>
    +
    
    Example 338 (lines 5984-5990) Code spans
    ``
    foo 
    ``
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><code>foo </code></p>
    +
    
    Example 339 (lines 5995-6000) Code spans
    `foo   bar 
    baz`
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><code>foo bar baz</code></p>
    +
    
    Example 340 (lines 6012-6016) Code spans
    `foo\`bar`
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><code>foo\</code>bar`</p>
    +
    
    Example 341 (lines 6023-6027) Code spans
    ``foo`bar``
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><code>foo`bar</code></p>
    +
    
    Example 342 (lines 6029-6033) Code spans
    ` foo `` bar `
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><code>foo `` bar</code></p>
    +
    
    Example 343 (lines 6041-6045) Code spans
    *foo`*`
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>*foo<code>*</code></p>
    +
    
    Example 344 (lines 6050-6054) Code spans
    [not a `link](/foo`)
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>[not a <code>link](/foo</code>)</p>
    +
    
    Example 345 (lines 6060-6064) Code spans
    `<a href="`">`
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><code>&lt;a href=&quot;</code>&quot;&gt;`</p>
    +
    
    Example 346 (lines 6069-6073) Code spans
    <a href="`">`
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><a href="`">`</p>
    +
    
    Example 347 (lines 6078-6082) Code spans
    `<https://foo.bar.`baz>`
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><code>&lt;https://foo.bar.</code>baz&gt;`</p>
    +
    
    Example 348 (lines 6087-6091) Code spans
    <https://foo.bar.`baz>`
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><a href="https://foo.bar.%60baz">https://foo.bar.`baz</a>`</p>
    +
    
    Example 349 (lines 6097-6101) Code spans
    ```foo``
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>```foo``</p>
    +
    
    Example 350 (lines 6104-6108) Code spans
    `foo
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>`foo</p>
    +
    
    Example 351 (lines 6113-6117) Code spans
    `foo``bar``
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>`foo<code>bar</code></p>
    +
    
    Example 352 (lines 6330-6334) Emphasis and strong emphasis
    *foo bar*
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><em>foo bar</em></p>
    +
    
    Example 353 (lines 6340-6344) Emphasis and strong emphasis
    a * foo bar*
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>a * foo bar*</p>
    +
    
    Example 354 (lines 6351-6355) Emphasis and strong emphasis
    a*"foo"*
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>a*&quot;foo&quot;*</p>
    +
    
    Example 355 (lines 6360-6364) Emphasis and strong emphasis
    * a *
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>* a *</p>
    +
    
    Example 356 (lines 6369-6382) Emphasis and strong emphasis
    *$*alpha.
    
    *£*bravo.
    
    *€*charlie.
    
    *𞋿*delta.
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>*$*alpha.</p><p>*£*bravo.</p><p>*€*charlie.</p><p>*𞋿*delta.</p>
    +
    
    Example 357 (lines 6387-6391) Emphasis and strong emphasis
    foo*bar*
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>foo<em>bar</em></p>
    +
    
    Example 358 (lines 6394-6398) Emphasis and strong emphasis
    5*6*78
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>5<em>6</em>78</p>
    +
    
    Example 359 (lines 6403-6407) Emphasis and strong emphasis
    program returned error code 1
    Traceback (most recent call last):
      File "/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/commonmark", line 15, in <module>
        raise SystemExit(main())
                         ^^^^^^
      File "/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/commonmark", line 10, in main
        sys.stdout.write(render(sys.stdin.read()))
                         ^^^^^^^^^^^^^^^^^^^^^^^^
      File "/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/commonmark_parser/__init__.py", line 16, in render
        parse_inlines(block.literal, document.references)
      File "/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/commonmark_parser/inlines.py", line 115, in parse_inlines
        return _parse_emphasis(nodes)
               ^^^^^^^^^^^^^^^^^^^^^^
      File "/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/commonmark_parser/inlines.py", line 163, in _parse_emphasis
        can_close = can_close and (not (not cright and (not cleft or _punct(ca))) or _punct(ca))
                                            ^^^^^^
    NameError: name 'cright' is not defined. Did you mean: 'copyright'?
    Example 360 (lines 6413-6417) Emphasis and strong emphasis
    _ foo bar_
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>_ foo bar_</p>
    +
    
    Example 361 (lines 6423-6427) Emphasis and strong emphasis
    a_"foo"_
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>a_&quot;foo&quot;_</p>
    +
    
    Example 362 (lines 6432-6436) Emphasis and strong emphasis
    foo_bar_
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>foo_bar_</p>
    +
    
    Example 363 (lines 6439-6443) Emphasis and strong emphasis
    5_6_78
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>5_6_78</p>
    +
    
    Example 364 (lines 6446-6450) Emphasis and strong emphasis
    пристаням_стремятся_
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>пристаням_стремятся_</p>
    +
    
    Example 365 (lines 6456-6460) Emphasis and strong emphasis
    aa_"bb"_cc
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>aa_&quot;bb&quot;_cc</p>
    +
    
    Example 366 (lines 6467-6471) Emphasis and strong emphasis
    program returned error code 1
    Traceback (most recent call last):
      File "/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/commonmark", line 15, in <module>
        raise SystemExit(main())
                         ^^^^^^
      File "/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/commonmark", line 10, in main
        sys.stdout.write(render(sys.stdin.read()))
                         ^^^^^^^^^^^^^^^^^^^^^^^^
      File "/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/commonmark_parser/__init__.py", line 16, in render
        parse_inlines(block.literal, document.references)
      File "/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/commonmark_parser/inlines.py", line 115, in parse_inlines
        return _parse_emphasis(nodes)
               ^^^^^^^^^^^^^^^^^^^^^^
      File "/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/commonmark_parser/inlines.py", line 163, in _parse_emphasis
        can_close = can_close and (not (not cright and (not cleft or _punct(ca))) or _punct(ca))
                                            ^^^^^^
    NameError: name 'cright' is not defined. Did you mean: 'copyright'?
    Example 367 (lines 6479-6483) Emphasis and strong emphasis
    _foo*
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>_foo*</p>
    +
    
    Example 368 (lines 6489-6493) Emphasis and strong emphasis
    *foo bar *
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>*foo bar *</p>
    +
    
    Example 369 (lines 6498-6504) Emphasis and strong emphasis
    *foo bar
    *
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>*foo bar *</p>
    +
    
    Example 370 (lines 6511-6515) Emphasis and strong emphasis
    *(*foo)
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>*(*foo)</p>
    +
    
    Example 371 (lines 6521-6525) Emphasis and strong emphasis
    *(*foo*)*
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><em>(<em>foo</em>)</em></p>
    +
    
    Example 372 (lines 6530-6534) Emphasis and strong emphasis
    *foo*bar
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><em>foo</em>bar</p>
    +
    
    Example 373 (lines 6543-6547) Emphasis and strong emphasis
    _foo bar _
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>_foo bar _</p>
    +
    
    Example 374 (lines 6553-6557) Emphasis and strong emphasis
    _(_foo)
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>_(_foo)</p>
    +
    
    Example 375 (lines 6562-6566) Emphasis and strong emphasis
    program returned error code 1
    Traceback (most recent call last):
      File "/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/commonmark", line 15, in <module>
        raise SystemExit(main())
                         ^^^^^^
      File "/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/commonmark", line 10, in main
        sys.stdout.write(render(sys.stdin.read()))
                         ^^^^^^^^^^^^^^^^^^^^^^^^
      File "/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/commonmark_parser/__init__.py", line 16, in render
        parse_inlines(block.literal, document.references)
      File "/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/commonmark_parser/inlines.py", line 115, in parse_inlines
        return _parse_emphasis(nodes)
               ^^^^^^^^^^^^^^^^^^^^^^
      File "/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/commonmark_parser/inlines.py", line 163, in _parse_emphasis
        can_close = can_close and (not (not cright and (not cleft or _punct(ca))) or _punct(ca))
                                            ^^^^^^
    NameError: name 'cright' is not defined. Did you mean: 'copyright'?
    Example 376 (lines 6571-6575) Emphasis and strong emphasis
    program returned error code 1
    Traceback (most recent call last):
      File "/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/commonmark", line 15, in <module>
        raise SystemExit(main())
                         ^^^^^^
      File "/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/commonmark", line 10, in main
        sys.stdout.write(render(sys.stdin.read()))
                         ^^^^^^^^^^^^^^^^^^^^^^^^
      File "/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/commonmark_parser/__init__.py", line 16, in render
        parse_inlines(block.literal, document.references)
      File "/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/commonmark_parser/inlines.py", line 115, in parse_inlines
        return _parse_emphasis(nodes)
               ^^^^^^^^^^^^^^^^^^^^^^
      File "/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/commonmark_parser/inlines.py", line 163, in _parse_emphasis
        can_close = can_close and (not (not cright and (not cleft or _punct(ca))) or _punct(ca))
                                            ^^^^^^
    NameError: name 'cright' is not defined. Did you mean: 'copyright'?
    Example 377 (lines 6578-6582) Emphasis and strong emphasis
    program returned error code 1
    Traceback (most recent call last):
      File "/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/commonmark", line 15, in <module>
        raise SystemExit(main())
                         ^^^^^^
      File "/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/commonmark", line 10, in main
        sys.stdout.write(render(sys.stdin.read()))
                         ^^^^^^^^^^^^^^^^^^^^^^^^
      File "/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/commonmark_parser/__init__.py", line 16, in render
        parse_inlines(block.literal, document.references)
      File "/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/commonmark_parser/inlines.py", line 115, in parse_inlines
        return _parse_emphasis(nodes)
               ^^^^^^^^^^^^^^^^^^^^^^
      File "/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/commonmark_parser/inlines.py", line 163, in _parse_emphasis
        can_close = can_close and (not (not cright and (not cleft or _punct(ca))) or _punct(ca))
                                            ^^^^^^
    NameError: name 'cright' is not defined. Did you mean: 'copyright'?
    Example 378 (lines 6585-6589) Emphasis and strong emphasis
    program returned error code 1
    Traceback (most recent call last):
      File "/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/commonmark", line 15, in <module>
        raise SystemExit(main())
                         ^^^^^^
      File "/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/commonmark", line 10, in main
        sys.stdout.write(render(sys.stdin.read()))
                         ^^^^^^^^^^^^^^^^^^^^^^^^
      File "/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/commonmark_parser/__init__.py", line 16, in render
        parse_inlines(block.literal, document.references)
      File "/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/commonmark_parser/inlines.py", line 115, in parse_inlines
        return _parse_emphasis(nodes)
               ^^^^^^^^^^^^^^^^^^^^^^
      File "/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/commonmark_parser/inlines.py", line 163, in _parse_emphasis
        can_close = can_close and (not (not cright and (not cleft or _punct(ca))) or _punct(ca))
                                            ^^^^^^
    NameError: name 'cright' is not defined. Did you mean: 'copyright'?
    Example 379 (lines 6596-6600) Emphasis and strong emphasis
    program returned error code 1
    Traceback (most recent call last):
      File "/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/commonmark", line 15, in <module>
        raise SystemExit(main())
                         ^^^^^^
      File "/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/commonmark", line 10, in main
        sys.stdout.write(render(sys.stdin.read()))
                         ^^^^^^^^^^^^^^^^^^^^^^^^
      File "/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/commonmark_parser/__init__.py", line 16, in render
        parse_inlines(block.literal, document.references)
      File "/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/commonmark_parser/inlines.py", line 115, in parse_inlines
        return _parse_emphasis(nodes)
               ^^^^^^^^^^^^^^^^^^^^^^
      File "/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/commonmark_parser/inlines.py", line 163, in _parse_emphasis
        can_close = can_close and (not (not cright and (not cleft or _punct(ca))) or _punct(ca))
                                            ^^^^^^
    NameError: name 'cright' is not defined. Did you mean: 'copyright'?
    Example 380 (lines 6605-6609) Emphasis and strong emphasis
    **foo bar**
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><strong>foo bar</strong></p>
    +
    
    Example 381 (lines 6615-6619) Emphasis and strong emphasis
    ** foo bar**
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>** foo bar**</p>
    +
    
    Example 382 (lines 6626-6630) Emphasis and strong emphasis
    a**"foo"**
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>a**&quot;foo&quot;**</p>
    +
    
    Example 383 (lines 6635-6639) Emphasis and strong emphasis
    foo**bar**
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>foo<strong>bar</strong></p>
    +
    
    Example 384 (lines 6644-6648) Emphasis and strong emphasis
    program returned error code 1
    Traceback (most recent call last):
      File "/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/commonmark", line 15, in <module>
        raise SystemExit(main())
                         ^^^^^^
      File "/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/commonmark", line 10, in main
        sys.stdout.write(render(sys.stdin.read()))
                         ^^^^^^^^^^^^^^^^^^^^^^^^
      File "/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/commonmark_parser/__init__.py", line 16, in render
        parse_inlines(block.literal, document.references)
      File "/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/commonmark_parser/inlines.py", line 115, in parse_inlines
        return _parse_emphasis(nodes)
               ^^^^^^^^^^^^^^^^^^^^^^
      File "/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/commonmark_parser/inlines.py", line 163, in _parse_emphasis
        can_close = can_close and (not (not cright and (not cleft or _punct(ca))) or _punct(ca))
                                            ^^^^^^
    NameError: name 'cright' is not defined. Did you mean: 'copyright'?
    Example 385 (lines 6654-6658) Emphasis and strong emphasis
    __ foo bar__
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>__ foo bar__</p>
    +
    
    Example 386 (lines 6662-6668) Emphasis and strong emphasis
    __
    foo bar__
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>__ foo bar__</p>
    +
    
    Example 387 (lines 6674-6678) Emphasis and strong emphasis
    a__"foo"__
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>a__&quot;foo&quot;__</p>
    +
    
    Example 388 (lines 6683-6687) Emphasis and strong emphasis
    foo__bar__
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>foo__bar__</p>
    +
    
    Example 389 (lines 6690-6694) Emphasis and strong emphasis
    5__6__78
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>5__6__78</p>
    +
    
    Example 390 (lines 6697-6701) Emphasis and strong emphasis
    пристаням__стремятся__
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>пристаням__стремятся__</p>
    +
    
    Example 391 (lines 6704-6708) Emphasis and strong emphasis
    program returned error code 1
    Traceback (most recent call last):
      File "/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/commonmark", line 15, in <module>
        raise SystemExit(main())
                         ^^^^^^
      File "/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/commonmark", line 10, in main
        sys.stdout.write(render(sys.stdin.read()))
                         ^^^^^^^^^^^^^^^^^^^^^^^^
      File "/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/commonmark_parser/__init__.py", line 16, in render
        parse_inlines(block.literal, document.references)
      File "/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/commonmark_parser/inlines.py", line 115, in parse_inlines
        return _parse_emphasis(nodes)
               ^^^^^^^^^^^^^^^^^^^^^^
      File "/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/commonmark_parser/inlines.py", line 163, in _parse_emphasis
        can_close = can_close and (not (not cright and (not cleft or _punct(ca))) or _punct(ca))
                                            ^^^^^^
    NameError: name 'cright' is not defined. Did you mean: 'copyright'?
    Example 392 (lines 6715-6719) Emphasis and strong emphasis
    program returned error code 1
    Traceback (most recent call last):
      File "/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/commonmark", line 15, in <module>
        raise SystemExit(main())
                         ^^^^^^
      File "/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/commonmark", line 10, in main
        sys.stdout.write(render(sys.stdin.read()))
                         ^^^^^^^^^^^^^^^^^^^^^^^^
      File "/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/commonmark_parser/__init__.py", line 16, in render
        parse_inlines(block.literal, document.references)
      File "/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/commonmark_parser/inlines.py", line 115, in parse_inlines
        return _parse_emphasis(nodes)
               ^^^^^^^^^^^^^^^^^^^^^^
      File "/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/commonmark_parser/inlines.py", line 163, in _parse_emphasis
        can_close = can_close and (not (not cright and (not cleft or _punct(ca))) or _punct(ca))
                                            ^^^^^^
    NameError: name 'cright' is not defined. Did you mean: 'copyright'?
    Example 393 (lines 6728-6732) Emphasis and strong emphasis
    **foo bar **
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>**foo bar **</p>
    +
    
    Example 394 (lines 6741-6745) Emphasis and strong emphasis
    **(**foo)
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>**(**foo)</p>
    +
    
    Example 395 (lines 6751-6755) Emphasis and strong emphasis
    *(**foo**)*
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><em>(<strong>foo</strong>)</em></p>
    +
    
    Example 396 (lines 6758-6764) Emphasis and strong emphasis
    **Gomphocarpus (*Gomphocarpus physocarpus*, syn.
    *Asclepias physocarpa*)**
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><strong>Gomphocarpus (<em>Gomphocarpus physocarpus</em>, syn. <em>Asclepias physocarpa</em>)</strong></p>
    +
    
    Example 397 (lines 6767-6771) Emphasis and strong emphasis
    **foo "*bar*" foo**
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><strong>foo &quot;<em>bar</em>&quot; foo</strong></p>
    +
    
    Example 398 (lines 6776-6780) Emphasis and strong emphasis
    **foo**bar
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><strong>foo</strong>bar</p>
    +
    
    Example 399 (lines 6788-6792) Emphasis and strong emphasis
    __foo bar __
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>__foo bar __</p>
    +
    
    Example 400 (lines 6798-6802) Emphasis and strong emphasis
    __(__foo)
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>__(__foo)</p>
    +
    
    Example 401 (lines 6808-6812) Emphasis and strong emphasis
    program returned error code 1
    Traceback (most recent call last):
      File "/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/commonmark", line 15, in <module>
        raise SystemExit(main())
                         ^^^^^^
      File "/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/commonmark", line 10, in main
        sys.stdout.write(render(sys.stdin.read()))
                         ^^^^^^^^^^^^^^^^^^^^^^^^
      File "/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/commonmark_parser/__init__.py", line 16, in render
        parse_inlines(block.literal, document.references)
      File "/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/commonmark_parser/inlines.py", line 115, in parse_inlines
        return _parse_emphasis(nodes)
               ^^^^^^^^^^^^^^^^^^^^^^
      File "/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/commonmark_parser/inlines.py", line 163, in _parse_emphasis
        can_close = can_close and (not (not cright and (not cleft or _punct(ca))) or _punct(ca))
                                            ^^^^^^
    NameError: name 'cright' is not defined. Did you mean: 'copyright'?
    Example 402 (lines 6817-6821) Emphasis and strong emphasis
    program returned error code 1
    Traceback (most recent call last):
      File "/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/commonmark", line 15, in <module>
        raise SystemExit(main())
                         ^^^^^^
      File "/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/commonmark", line 10, in main
        sys.stdout.write(render(sys.stdin.read()))
                         ^^^^^^^^^^^^^^^^^^^^^^^^
      File "/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/commonmark_parser/__init__.py", line 16, in render
        parse_inlines(block.literal, document.references)
      File "/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/commonmark_parser/inlines.py", line 115, in parse_inlines
        return _parse_emphasis(nodes)
               ^^^^^^^^^^^^^^^^^^^^^^
      File "/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/commonmark_parser/inlines.py", line 163, in _parse_emphasis
        can_close = can_close and (not (not cright and (not cleft or _punct(ca))) or _punct(ca))
                                            ^^^^^^
    NameError: name 'cright' is not defined. Did you mean: 'copyright'?
    Example 403 (lines 6824-6828) Emphasis and strong emphasis
    program returned error code 1
    Traceback (most recent call last):
      File "/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/commonmark", line 15, in <module>
        raise SystemExit(main())
                         ^^^^^^
      File "/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/commonmark", line 10, in main
        sys.stdout.write(render(sys.stdin.read()))
                         ^^^^^^^^^^^^^^^^^^^^^^^^
      File "/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/commonmark_parser/__init__.py", line 16, in render
        parse_inlines(block.literal, document.references)
      File "/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/commonmark_parser/inlines.py", line 115, in parse_inlines
        return _parse_emphasis(nodes)
               ^^^^^^^^^^^^^^^^^^^^^^
      File "/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/commonmark_parser/inlines.py", line 163, in _parse_emphasis
        can_close = can_close and (not (not cright and (not cleft or _punct(ca))) or _punct(ca))
                                            ^^^^^^
    NameError: name 'cright' is not defined. Did you mean: 'copyright'?
    Example 404 (lines 6831-6835) Emphasis and strong emphasis
    program returned error code 1
    Traceback (most recent call last):
      File "/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/commonmark", line 15, in <module>
        raise SystemExit(main())
                         ^^^^^^
      File "/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/commonmark", line 10, in main
        sys.stdout.write(render(sys.stdin.read()))
                         ^^^^^^^^^^^^^^^^^^^^^^^^
      File "/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/commonmark_parser/__init__.py", line 16, in render
        parse_inlines(block.literal, document.references)
      File "/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/commonmark_parser/inlines.py", line 115, in parse_inlines
        return _parse_emphasis(nodes)
               ^^^^^^^^^^^^^^^^^^^^^^
      File "/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/commonmark_parser/inlines.py", line 163, in _parse_emphasis
        can_close = can_close and (not (not cright and (not cleft or _punct(ca))) or _punct(ca))
                                            ^^^^^^
    NameError: name 'cright' is not defined. Did you mean: 'copyright'?
    Example 405 (lines 6842-6846) Emphasis and strong emphasis
    program returned error code 1
    Traceback (most recent call last):
      File "/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/commonmark", line 15, in <module>
        raise SystemExit(main())
                         ^^^^^^
      File "/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/commonmark", line 10, in main
        sys.stdout.write(render(sys.stdin.read()))
                         ^^^^^^^^^^^^^^^^^^^^^^^^
      File "/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/commonmark_parser/__init__.py", line 16, in render
        parse_inlines(block.literal, document.references)
      File "/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/commonmark_parser/inlines.py", line 115, in parse_inlines
        return _parse_emphasis(nodes)
               ^^^^^^^^^^^^^^^^^^^^^^
      File "/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/commonmark_parser/inlines.py", line 163, in _parse_emphasis
        can_close = can_close and (not (not cright and (not cleft or _punct(ca))) or _punct(ca))
                                            ^^^^^^
    NameError: name 'cright' is not defined. Did you mean: 'copyright'?
    Example 406 (lines 6854-6858) Emphasis and strong emphasis
    *foo [bar](/url)*
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><em>foo <a href="/url">bar</a></em></p>
    +
    
    Example 407 (lines 6861-6867) Emphasis and strong emphasis
    *foo
    bar*
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><em>foo bar</em></p>
    +
    
    Example 408 (lines 6873-6877) Emphasis and strong emphasis
    program returned error code 1
    Traceback (most recent call last):
      File "/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/commonmark", line 15, in <module>
        raise SystemExit(main())
                         ^^^^^^
      File "/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/commonmark", line 10, in main
        sys.stdout.write(render(sys.stdin.read()))
                         ^^^^^^^^^^^^^^^^^^^^^^^^
      File "/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/commonmark_parser/__init__.py", line 16, in render
        parse_inlines(block.literal, document.references)
      File "/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/commonmark_parser/inlines.py", line 115, in parse_inlines
        return _parse_emphasis(nodes)
               ^^^^^^^^^^^^^^^^^^^^^^
      File "/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/commonmark_parser/inlines.py", line 163, in _parse_emphasis
        can_close = can_close and (not (not cright and (not cleft or _punct(ca))) or _punct(ca))
                                            ^^^^^^
    NameError: name 'cright' is not defined. Did you mean: 'copyright'?
    Example 409 (lines 6880-6884) Emphasis and strong emphasis
    program returned error code 1
    Traceback (most recent call last):
      File "/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/commonmark", line 15, in <module>
        raise SystemExit(main())
                         ^^^^^^
      File "/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/commonmark", line 10, in main
        sys.stdout.write(render(sys.stdin.read()))
                         ^^^^^^^^^^^^^^^^^^^^^^^^
      File "/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/commonmark_parser/__init__.py", line 16, in render
        parse_inlines(block.literal, document.references)
      File "/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/commonmark_parser/inlines.py", line 115, in parse_inlines
        return _parse_emphasis(nodes)
               ^^^^^^^^^^^^^^^^^^^^^^
      File "/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/commonmark_parser/inlines.py", line 163, in _parse_emphasis
        can_close = can_close and (not (not cright and (not cleft or _punct(ca))) or _punct(ca))
                                            ^^^^^^
    NameError: name 'cright' is not defined. Did you mean: 'copyright'?
    Example 410 (lines 6887-6891) Emphasis and strong emphasis
    program returned error code 1
    Traceback (most recent call last):
      File "/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/commonmark", line 15, in <module>
        raise SystemExit(main())
                         ^^^^^^
      File "/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/commonmark", line 10, in main
        sys.stdout.write(render(sys.stdin.read()))
                         ^^^^^^^^^^^^^^^^^^^^^^^^
      File "/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/commonmark_parser/__init__.py", line 16, in render
        parse_inlines(block.literal, document.references)
      File "/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/commonmark_parser/inlines.py", line 115, in parse_inlines
        return _parse_emphasis(nodes)
               ^^^^^^^^^^^^^^^^^^^^^^
      File "/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/commonmark_parser/inlines.py", line 163, in _parse_emphasis
        can_close = can_close and (not (not cright and (not cleft or _punct(ca))) or _punct(ca))
                                            ^^^^^^
    NameError: name 'cright' is not defined. Did you mean: 'copyright'?
    Example 411 (lines 6894-6898) Emphasis and strong emphasis
    *foo *bar**
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><em>foo <em>bar</em></em></p>
    +
    
    Example 412 (lines 6901-6905) Emphasis and strong emphasis
    *foo **bar** baz*
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><em>foo <strong>bar</strong> baz</em></p>
    +
    
    Example 413 (lines 6907-6911) Emphasis and strong emphasis
    *foo**bar**baz*
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><em>foo<strong>bar</strong>baz</em></p>
    +
    
    Example 414 (lines 6931-6935) Emphasis and strong emphasis
    *foo**bar*
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><em>foo**bar</em></p>
    +
    
    Example 415 (lines 6944-6948) Emphasis and strong emphasis
    ***foo** bar*
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><em><strong>foo</strong> bar</em></p>
    +
    
    Example 416 (lines 6951-6955) Emphasis and strong emphasis
    *foo **bar***
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><em>foo <strong>bar</strong></em></p>
    +
    
    Example 417 (lines 6958-6962) Emphasis and strong emphasis
    *foo**bar***
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><em>foo<strong>bar</strong></em></p>
    +
    
    Example 418 (lines 6969-6973) Emphasis and strong emphasis
    foo***bar***baz
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>foo<em><strong>bar</strong></em>baz</p>
    +
    
    Example 419 (lines 6975-6979) Emphasis and strong emphasis
    foo******bar*********baz
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>foo<strong><strong><strong>bar</strong></strong></strong>***baz</p>
    +
    
    Example 420 (lines 6984-6988) Emphasis and strong emphasis
    *foo **bar *baz* bim** bop*
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><em>foo <strong>bar <em>baz</em> bim</strong> bop</em></p>
    +
    
    Example 421 (lines 6991-6995) Emphasis and strong emphasis
    *foo [*bar*](/url)*
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><em>foo <a href="/url"><em>bar</em></a></em></p>
    +
    
    Example 422 (lines 7000-7004) Emphasis and strong emphasis
    ** is not an empty emphasis
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>** is not an empty emphasis</p>
    +
    
    Example 423 (lines 7007-7011) Emphasis and strong emphasis
    **** is not an empty strong emphasis
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>**** is not an empty strong emphasis</p>
    +
    
    Example 424 (lines 7020-7024) Emphasis and strong emphasis
    **foo [bar](/url)**
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><strong>foo <a href="/url">bar</a></strong></p>
    +
    
    Example 425 (lines 7027-7033) Emphasis and strong emphasis
    **foo
    bar**
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><strong>foo bar</strong></p>
    +
    
    Example 426 (lines 7039-7043) Emphasis and strong emphasis
    program returned error code 1
    Traceback (most recent call last):
      File "/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/commonmark", line 15, in <module>
        raise SystemExit(main())
                         ^^^^^^
      File "/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/commonmark", line 10, in main
        sys.stdout.write(render(sys.stdin.read()))
                         ^^^^^^^^^^^^^^^^^^^^^^^^
      File "/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/commonmark_parser/__init__.py", line 16, in render
        parse_inlines(block.literal, document.references)
      File "/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/commonmark_parser/inlines.py", line 115, in parse_inlines
        return _parse_emphasis(nodes)
               ^^^^^^^^^^^^^^^^^^^^^^
      File "/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/commonmark_parser/inlines.py", line 163, in _parse_emphasis
        can_close = can_close and (not (not cright and (not cleft or _punct(ca))) or _punct(ca))
                                            ^^^^^^
    NameError: name 'cright' is not defined. Did you mean: 'copyright'?
    Example 427 (lines 7046-7050) Emphasis and strong emphasis
    program returned error code 1
    Traceback (most recent call last):
      File "/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/commonmark", line 15, in <module>
        raise SystemExit(main())
                         ^^^^^^
      File "/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/commonmark", line 10, in main
        sys.stdout.write(render(sys.stdin.read()))
                         ^^^^^^^^^^^^^^^^^^^^^^^^
      File "/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/commonmark_parser/__init__.py", line 16, in render
        parse_inlines(block.literal, document.references)
      File "/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/commonmark_parser/inlines.py", line 115, in parse_inlines
        return _parse_emphasis(nodes)
               ^^^^^^^^^^^^^^^^^^^^^^
      File "/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/commonmark_parser/inlines.py", line 163, in _parse_emphasis
        can_close = can_close and (not (not cright and (not cleft or _punct(ca))) or _punct(ca))
                                            ^^^^^^
    NameError: name 'cright' is not defined. Did you mean: 'copyright'?
    Example 428 (lines 7053-7057) Emphasis and strong emphasis
    program returned error code 1
    Traceback (most recent call last):
      File "/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/commonmark", line 15, in <module>
        raise SystemExit(main())
                         ^^^^^^
      File "/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/commonmark", line 10, in main
        sys.stdout.write(render(sys.stdin.read()))
                         ^^^^^^^^^^^^^^^^^^^^^^^^
      File "/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/commonmark_parser/__init__.py", line 16, in render
        parse_inlines(block.literal, document.references)
      File "/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/commonmark_parser/inlines.py", line 115, in parse_inlines
        return _parse_emphasis(nodes)
               ^^^^^^^^^^^^^^^^^^^^^^
      File "/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/commonmark_parser/inlines.py", line 163, in _parse_emphasis
        can_close = can_close and (not (not cright and (not cleft or _punct(ca))) or _punct(ca))
                                            ^^^^^^
    NameError: name 'cright' is not defined. Did you mean: 'copyright'?
    Example 429 (lines 7060-7064) Emphasis and strong emphasis
    **foo **bar****
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><strong>foo <strong>bar</strong></strong></p>
    +
    
    Example 430 (lines 7067-7071) Emphasis and strong emphasis
    **foo *bar* baz**
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><strong>foo <em>bar</em> baz</strong></p>
    +
    
    Example 431 (lines 7074-7078) Emphasis and strong emphasis
    **foo*bar*baz**
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><strong>foo<em>bar</em>baz</strong></p>
    +
    
    Example 432 (lines 7081-7085) Emphasis and strong emphasis
    ***foo* bar**
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><strong><em>foo</em> bar</strong></p>
    +
    
    Example 433 (lines 7088-7092) Emphasis and strong emphasis
    **foo *bar***
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><strong>foo <em>bar</em></strong></p>
    +
    
    Example 434 (lines 7097-7103) Emphasis and strong emphasis
    **foo *bar **baz**
    bim* bop**
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><strong>foo <em>bar <strong>baz</strong> bim</em> bop</strong></p>
    +
    
    Example 435 (lines 7106-7110) Emphasis and strong emphasis
    **foo [*bar*](/url)**
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><strong>foo <a href="/url"><em>bar</em></a></strong></p>
    +
    
    Example 436 (lines 7115-7119) Emphasis and strong emphasis
    __ is not an empty emphasis
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>__ is not an empty emphasis</p>
    +
    
    Example 437 (lines 7122-7126) Emphasis and strong emphasis
    ____ is not an empty strong emphasis
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>____ is not an empty strong emphasis</p>
    +
    
    Example 438 (lines 7132-7136) Emphasis and strong emphasis
    foo ***
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>foo ***</p>
    +
    
    Example 439 (lines 7139-7143) Emphasis and strong emphasis
    foo *\**
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>foo <em>*</em></p>
    +
    
    Example 440 (lines 7146-7150) Emphasis and strong emphasis
    foo *_*
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>foo <em>_</em></p>
    +
    
    Example 441 (lines 7153-7157) Emphasis and strong emphasis
    foo *****
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>foo *****</p>
    +
    
    Example 442 (lines 7160-7164) Emphasis and strong emphasis
    foo **\***
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>foo <strong>*</strong></p>
    +
    
    Example 443 (lines 7167-7171) Emphasis and strong emphasis
    foo **_**
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>foo <strong>_</strong></p>
    +
    
    Example 444 (lines 7178-7182) Emphasis and strong emphasis
    **foo*
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>*<em>foo</em></p>
    +
    
    Example 445 (lines 7185-7189) Emphasis and strong emphasis
    *foo**
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><em>foo</em>*</p>
    +
    
    Example 446 (lines 7192-7196) Emphasis and strong emphasis
    ***foo**
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>*<strong>foo</strong></p>
    +
    
    Example 447 (lines 7199-7203) Emphasis and strong emphasis
    ****foo*
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>***<em>foo</em></p>
    +
    
    Example 448 (lines 7206-7210) Emphasis and strong emphasis
    **foo***
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><strong>foo</strong>*</p>
    +
    
    Example 449 (lines 7213-7217) Emphasis and strong emphasis
    *foo****
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><em>foo</em>***</p>
    +
    
    Example 450 (lines 7223-7227) Emphasis and strong emphasis
    foo ___
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>foo ___</p>
    +
    
    Example 451 (lines 7230-7234) Emphasis and strong emphasis
    foo _\__
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>foo <em>_</em></p>
    +
    
    Example 452 (lines 7237-7241) Emphasis and strong emphasis
    program returned error code 1
    Traceback (most recent call last):
      File "/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/commonmark", line 15, in <module>
        raise SystemExit(main())
                         ^^^^^^
      File "/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/commonmark", line 10, in main
        sys.stdout.write(render(sys.stdin.read()))
                         ^^^^^^^^^^^^^^^^^^^^^^^^
      File "/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/commonmark_parser/__init__.py", line 16, in render
        parse_inlines(block.literal, document.references)
      File "/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/commonmark_parser/inlines.py", line 115, in parse_inlines
        return _parse_emphasis(nodes)
               ^^^^^^^^^^^^^^^^^^^^^^
      File "/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/commonmark_parser/inlines.py", line 163, in _parse_emphasis
        can_close = can_close and (not (not cright and (not cleft or _punct(ca))) or _punct(ca))
                                            ^^^^^^
    NameError: name 'cright' is not defined. Did you mean: 'copyright'?
    Example 453 (lines 7244-7248) Emphasis and strong emphasis
    foo _____
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>foo _____</p>
    +
    
    Example 454 (lines 7251-7255) Emphasis and strong emphasis
    foo __\___
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>foo <strong>_</strong></p>
    +
    
    Example 455 (lines 7258-7262) Emphasis and strong emphasis
    program returned error code 1
    Traceback (most recent call last):
      File "/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/commonmark", line 15, in <module>
        raise SystemExit(main())
                         ^^^^^^
      File "/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/commonmark", line 10, in main
        sys.stdout.write(render(sys.stdin.read()))
                         ^^^^^^^^^^^^^^^^^^^^^^^^
      File "/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/commonmark_parser/__init__.py", line 16, in render
        parse_inlines(block.literal, document.references)
      File "/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/commonmark_parser/inlines.py", line 115, in parse_inlines
        return _parse_emphasis(nodes)
               ^^^^^^^^^^^^^^^^^^^^^^
      File "/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/commonmark_parser/inlines.py", line 163, in _parse_emphasis
        can_close = can_close and (not (not cright and (not cleft or _punct(ca))) or _punct(ca))
                                            ^^^^^^
    NameError: name 'cright' is not defined. Did you mean: 'copyright'?
    Example 456 (lines 7265-7269) Emphasis and strong emphasis
    program returned error code 1
    Traceback (most recent call last):
      File "/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/commonmark", line 15, in <module>
        raise SystemExit(main())
                         ^^^^^^
      File "/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/commonmark", line 10, in main
        sys.stdout.write(render(sys.stdin.read()))
                         ^^^^^^^^^^^^^^^^^^^^^^^^
      File "/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/commonmark_parser/__init__.py", line 16, in render
        parse_inlines(block.literal, document.references)
      File "/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/commonmark_parser/inlines.py", line 115, in parse_inlines
        return _parse_emphasis(nodes)
               ^^^^^^^^^^^^^^^^^^^^^^
      File "/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/commonmark_parser/inlines.py", line 163, in _parse_emphasis
        can_close = can_close and (not (not cright and (not cleft or _punct(ca))) or _punct(ca))
                                            ^^^^^^
    NameError: name 'cright' is not defined. Did you mean: 'copyright'?
    Example 457 (lines 7276-7280) Emphasis and strong emphasis
    program returned error code 1
    Traceback (most recent call last):
      File "/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/commonmark", line 15, in <module>
        raise SystemExit(main())
                         ^^^^^^
      File "/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/commonmark", line 10, in main
        sys.stdout.write(render(sys.stdin.read()))
                         ^^^^^^^^^^^^^^^^^^^^^^^^
      File "/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/commonmark_parser/__init__.py", line 16, in render
        parse_inlines(block.literal, document.references)
      File "/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/commonmark_parser/inlines.py", line 115, in parse_inlines
        return _parse_emphasis(nodes)
               ^^^^^^^^^^^^^^^^^^^^^^
      File "/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/commonmark_parser/inlines.py", line 163, in _parse_emphasis
        can_close = can_close and (not (not cright and (not cleft or _punct(ca))) or _punct(ca))
                                            ^^^^^^
    NameError: name 'cright' is not defined. Did you mean: 'copyright'?
    Example 458 (lines 7283-7287) Emphasis and strong emphasis
    program returned error code 1
    Traceback (most recent call last):
      File "/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/commonmark", line 15, in <module>
        raise SystemExit(main())
                         ^^^^^^
      File "/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/commonmark", line 10, in main
        sys.stdout.write(render(sys.stdin.read()))
                         ^^^^^^^^^^^^^^^^^^^^^^^^
      File "/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/commonmark_parser/__init__.py", line 16, in render
        parse_inlines(block.literal, document.references)
      File "/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/commonmark_parser/inlines.py", line 115, in parse_inlines
        return _parse_emphasis(nodes)
               ^^^^^^^^^^^^^^^^^^^^^^
      File "/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/commonmark_parser/inlines.py", line 163, in _parse_emphasis
        can_close = can_close and (not (not cright and (not cleft or _punct(ca))) or _punct(ca))
                                            ^^^^^^
    NameError: name 'cright' is not defined. Did you mean: 'copyright'?
    Example 459 (lines 7290-7294) Emphasis and strong emphasis
    program returned error code 1
    Traceback (most recent call last):
      File "/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/commonmark", line 15, in <module>
        raise SystemExit(main())
                         ^^^^^^
      File "/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/commonmark", line 10, in main
        sys.stdout.write(render(sys.stdin.read()))
                         ^^^^^^^^^^^^^^^^^^^^^^^^
      File "/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/commonmark_parser/__init__.py", line 16, in render
        parse_inlines(block.literal, document.references)
      File "/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/commonmark_parser/inlines.py", line 115, in parse_inlines
        return _parse_emphasis(nodes)
               ^^^^^^^^^^^^^^^^^^^^^^
      File "/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/commonmark_parser/inlines.py", line 163, in _parse_emphasis
        can_close = can_close and (not (not cright and (not cleft or _punct(ca))) or _punct(ca))
                                            ^^^^^^
    NameError: name 'cright' is not defined. Did you mean: 'copyright'?
    Example 460 (lines 7297-7301) Emphasis and strong emphasis
    program returned error code 1
    Traceback (most recent call last):
      File "/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/commonmark", line 15, in <module>
        raise SystemExit(main())
                         ^^^^^^
      File "/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/commonmark", line 10, in main
        sys.stdout.write(render(sys.stdin.read()))
                         ^^^^^^^^^^^^^^^^^^^^^^^^
      File "/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/commonmark_parser/__init__.py", line 16, in render
        parse_inlines(block.literal, document.references)
      File "/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/commonmark_parser/inlines.py", line 115, in parse_inlines
        return _parse_emphasis(nodes)
               ^^^^^^^^^^^^^^^^^^^^^^
      File "/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/commonmark_parser/inlines.py", line 163, in _parse_emphasis
        can_close = can_close and (not (not cright and (not cleft or _punct(ca))) or _punct(ca))
                                            ^^^^^^
    NameError: name 'cright' is not defined. Did you mean: 'copyright'?
    Example 461 (lines 7304-7308) Emphasis and strong emphasis
    program returned error code 1
    Traceback (most recent call last):
      File "/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/commonmark", line 15, in <module>
        raise SystemExit(main())
                         ^^^^^^
      File "/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/commonmark", line 10, in main
        sys.stdout.write(render(sys.stdin.read()))
                         ^^^^^^^^^^^^^^^^^^^^^^^^
      File "/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/commonmark_parser/__init__.py", line 16, in render
        parse_inlines(block.literal, document.references)
      File "/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/commonmark_parser/inlines.py", line 115, in parse_inlines
        return _parse_emphasis(nodes)
               ^^^^^^^^^^^^^^^^^^^^^^
      File "/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/commonmark_parser/inlines.py", line 163, in _parse_emphasis
        can_close = can_close and (not (not cright and (not cleft or _punct(ca))) or _punct(ca))
                                            ^^^^^^
    NameError: name 'cright' is not defined. Did you mean: 'copyright'?
    Example 462 (lines 7314-7318) Emphasis and strong emphasis
    **foo**
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><strong>foo</strong></p>
    +
    
    Example 463 (lines 7321-7325) Emphasis and strong emphasis
    program returned error code 1
    Traceback (most recent call last):
      File "/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/commonmark", line 15, in <module>
        raise SystemExit(main())
                         ^^^^^^
      File "/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/commonmark", line 10, in main
        sys.stdout.write(render(sys.stdin.read()))
                         ^^^^^^^^^^^^^^^^^^^^^^^^
      File "/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/commonmark_parser/__init__.py", line 16, in render
        parse_inlines(block.literal, document.references)
      File "/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/commonmark_parser/inlines.py", line 115, in parse_inlines
        return _parse_emphasis(nodes)
               ^^^^^^^^^^^^^^^^^^^^^^
      File "/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/commonmark_parser/inlines.py", line 176, in _parse_emphasis
        inner = _parse_emphasis([Inline("text", source[end:a])])
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
      File "/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/commonmark_parser/inlines.py", line 163, in _parse_emphasis
        can_close = can_close and (not (not cright and (not cleft or _punct(ca))) or _punct(ca))
                                            ^^^^^^
    NameError: name 'cright' is not defined. Did you mean: 'copyright'?
    Example 464 (lines 7328-7332) Emphasis and strong emphasis
    program returned error code 1
    Traceback (most recent call last):
      File "/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/commonmark", line 15, in <module>
        raise SystemExit(main())
                         ^^^^^^
      File "/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/commonmark", line 10, in main
        sys.stdout.write(render(sys.stdin.read()))
                         ^^^^^^^^^^^^^^^^^^^^^^^^
      File "/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/commonmark_parser/__init__.py", line 16, in render
        parse_inlines(block.literal, document.references)
      File "/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/commonmark_parser/inlines.py", line 115, in parse_inlines
        return _parse_emphasis(nodes)
               ^^^^^^^^^^^^^^^^^^^^^^
      File "/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/commonmark_parser/inlines.py", line 163, in _parse_emphasis
        can_close = can_close and (not (not cright and (not cleft or _punct(ca))) or _punct(ca))
                                            ^^^^^^
    NameError: name 'cright' is not defined. Did you mean: 'copyright'?
    Example 465 (lines 7335-7339) Emphasis and strong emphasis
    program returned error code 1
    Traceback (most recent call last):
      File "/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/commonmark", line 15, in <module>
        raise SystemExit(main())
                         ^^^^^^
      File "/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/commonmark", line 10, in main
        sys.stdout.write(render(sys.stdin.read()))
                         ^^^^^^^^^^^^^^^^^^^^^^^^
      File "/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/commonmark_parser/__init__.py", line 16, in render
        parse_inlines(block.literal, document.references)
      File "/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/commonmark_parser/inlines.py", line 115, in parse_inlines
        return _parse_emphasis(nodes)
               ^^^^^^^^^^^^^^^^^^^^^^
      File "/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/commonmark_parser/inlines.py", line 163, in _parse_emphasis
        can_close = can_close and (not (not cright and (not cleft or _punct(ca))) or _punct(ca))
                                            ^^^^^^
    NameError: name 'cright' is not defined. Did you mean: 'copyright'?
    Example 466 (lines 7345-7349) Emphasis and strong emphasis
    ****foo****
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><strong><strong>foo</strong></strong></p>
    +
    
    Example 467 (lines 7352-7356) Emphasis and strong emphasis
    program returned error code 1
    Traceback (most recent call last):
      File "/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/commonmark", line 15, in <module>
        raise SystemExit(main())
                         ^^^^^^
      File "/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/commonmark", line 10, in main
        sys.stdout.write(render(sys.stdin.read()))
                         ^^^^^^^^^^^^^^^^^^^^^^^^
      File "/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/commonmark_parser/__init__.py", line 16, in render
        parse_inlines(block.literal, document.references)
      File "/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/commonmark_parser/inlines.py", line 115, in parse_inlines
        return _parse_emphasis(nodes)
               ^^^^^^^^^^^^^^^^^^^^^^
      File "/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/commonmark_parser/inlines.py", line 163, in _parse_emphasis
        can_close = can_close and (not (not cright and (not cleft or _punct(ca))) or _punct(ca))
                                            ^^^^^^
    NameError: name 'cright' is not defined. Did you mean: 'copyright'?
    Example 468 (lines 7363-7367) Emphasis and strong emphasis
    ******foo******
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><strong><strong><strong>foo</strong></strong></strong></p>
    +
    
    Example 469 (lines 7372-7376) Emphasis and strong emphasis
    ***foo***
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><em><strong>foo</strong></em></p>
    +
    
    Example 470 (lines 7379-7383) Emphasis and strong emphasis
    program returned error code 1
    Traceback (most recent call last):
      File "/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/commonmark", line 15, in <module>
        raise SystemExit(main())
                         ^^^^^^
      File "/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/commonmark", line 10, in main
        sys.stdout.write(render(sys.stdin.read()))
                         ^^^^^^^^^^^^^^^^^^^^^^^^
      File "/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/commonmark_parser/__init__.py", line 16, in render
        parse_inlines(block.literal, document.references)
      File "/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/commonmark_parser/inlines.py", line 115, in parse_inlines
        return _parse_emphasis(nodes)
               ^^^^^^^^^^^^^^^^^^^^^^
      File "/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/commonmark_parser/inlines.py", line 163, in _parse_emphasis
        can_close = can_close and (not (not cright and (not cleft or _punct(ca))) or _punct(ca))
                                            ^^^^^^
    NameError: name 'cright' is not defined. Did you mean: 'copyright'?
    Example 471 (lines 7388-7392) Emphasis and strong emphasis
    *foo _bar* baz_
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><em>foo _bar</em> baz_</p>
    +
    
    Example 472 (lines 7395-7399) Emphasis and strong emphasis
    program returned error code 1
    Traceback (most recent call last):
      File "/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/commonmark", line 15, in <module>
        raise SystemExit(main())
                         ^^^^^^
      File "/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/commonmark", line 10, in main
        sys.stdout.write(render(sys.stdin.read()))
                         ^^^^^^^^^^^^^^^^^^^^^^^^
      File "/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/commonmark_parser/__init__.py", line 16, in render
        parse_inlines(block.literal, document.references)
      File "/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/commonmark_parser/inlines.py", line 115, in parse_inlines
        return _parse_emphasis(nodes)
               ^^^^^^^^^^^^^^^^^^^^^^
      File "/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/commonmark_parser/inlines.py", line 176, in _parse_emphasis
        inner = _parse_emphasis([Inline("text", source[end:a])])
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
      File "/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/commonmark_parser/inlines.py", line 163, in _parse_emphasis
        can_close = can_close and (not (not cright and (not cleft or _punct(ca))) or _punct(ca))
                                            ^^^^^^
    NameError: name 'cright' is not defined. Did you mean: 'copyright'?
    Example 473 (lines 7404-7408) Emphasis and strong emphasis
    **foo **bar baz**
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>**foo <strong>bar baz</strong></p>
    +
    
    Example 474 (lines 7411-7415) Emphasis and strong emphasis
    *foo *bar baz*
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>*foo <em>bar baz</em></p>
    +
    
    Example 475 (lines 7420-7424) Emphasis and strong emphasis
    *[bar*](/url)
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>*<a href="/url">bar*</a></p>
    +
    
    Example 476 (lines 7427-7431) Emphasis and strong emphasis
    program returned error code 1
    Traceback (most recent call last):
      File "/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/commonmark", line 15, in <module>
        raise SystemExit(main())
                         ^^^^^^
      File "/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/commonmark", line 10, in main
        sys.stdout.write(render(sys.stdin.read()))
                         ^^^^^^^^^^^^^^^^^^^^^^^^
      File "/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/commonmark_parser/__init__.py", line 16, in render
        parse_inlines(block.literal, document.references)
      File "/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/commonmark_parser/inlines.py", line 115, in parse_inlines
        return _parse_emphasis(nodes)
               ^^^^^^^^^^^^^^^^^^^^^^
      File "/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/commonmark_parser/inlines.py", line 163, in _parse_emphasis
        can_close = can_close and (not (not cright and (not cleft or _punct(ca))) or _punct(ca))
                                            ^^^^^^
    NameError: name 'cright' is not defined. Did you mean: 'copyright'?
    Example 477 (lines 7434-7438) Emphasis and strong emphasis
    *<img src="foo" title="*"/>
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>*<img src="foo" title="*"></p>
    +
    
    Example 478 (lines 7441-7445) Emphasis and strong emphasis
    **<a href="**">
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>**<a href="**"></p>
    +
    
    Example 479 (lines 7448-7452) Emphasis and strong emphasis
    program returned error code 1
    Traceback (most recent call last):
      File "/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/commonmark", line 15, in <module>
        raise SystemExit(main())
                         ^^^^^^
      File "/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/commonmark", line 10, in main
        sys.stdout.write(render(sys.stdin.read()))
                         ^^^^^^^^^^^^^^^^^^^^^^^^
      File "/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/commonmark_parser/__init__.py", line 16, in render
        parse_inlines(block.literal, document.references)
      File "/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/commonmark_parser/inlines.py", line 115, in parse_inlines
        return _parse_emphasis(nodes)
               ^^^^^^^^^^^^^^^^^^^^^^
      File "/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/commonmark_parser/inlines.py", line 163, in _parse_emphasis
        can_close = can_close and (not (not cright and (not cleft or _punct(ca))) or _punct(ca))
                                            ^^^^^^
    NameError: name 'cright' is not defined. Did you mean: 'copyright'?
    Example 480 (lines 7455-7459) Emphasis and strong emphasis
    *a `*`*
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><em>a <code>*</code></em></p>
    +
    
    Example 481 (lines 7462-7466) Emphasis and strong emphasis
    _a `_`_
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><em>a <code>_</code></em></p>
    +
    
    Example 482 (lines 7469-7473) Emphasis and strong emphasis
    **a<https://foo.bar/?q=**>
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>**a<a href="https://foo.bar/?q=**">https://foo.bar/?q=**</a></p>
    +
    
    Example 483 (lines 7476-7480) Emphasis and strong emphasis
    program returned error code 1
    Traceback (most recent call last):
      File "/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/commonmark", line 15, in <module>
        raise SystemExit(main())
                         ^^^^^^
      File "/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/commonmark", line 10, in main
        sys.stdout.write(render(sys.stdin.read()))
                         ^^^^^^^^^^^^^^^^^^^^^^^^
      File "/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/commonmark_parser/__init__.py", line 16, in render
        parse_inlines(block.literal, document.references)
      File "/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/commonmark_parser/inlines.py", line 115, in parse_inlines
        return _parse_emphasis(nodes)
               ^^^^^^^^^^^^^^^^^^^^^^
      File "/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/commonmark_parser/inlines.py", line 163, in _parse_emphasis
        can_close = can_close and (not (not cright and (not cleft or _punct(ca))) or _punct(ca))
                                            ^^^^^^
    NameError: name 'cright' is not defined. Did you mean: 'copyright'?
    Example 484 (lines 7564-7568) Links
    [link](/uri "title")
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><a href="/uri" title="title">link</a></p>
    +
    
    Example 485 (lines 7574-7578) Links
    [link](/uri)
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><a href="/uri">link</a></p>
    +
    
    Example 486 (lines 7580-7584) Links
    [](./target.md)
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><a href="./target.md"></a></p>
    +
    
    Example 487 (lines 7587-7591) Links
    [link]()
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><a href="">link</a></p>
    +
    
    Example 488 (lines 7594-7598) Links
    [link](<>)
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><a href="">link</a></p>
    +
    
    Example 489 (lines 7601-7605) Links
    []()
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><a href=""></a></p>
    +
    
    Example 490 (lines 7610-7614) Links
    [link](/my uri)
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>[link](/my uri)</p>
    +
    
    Example 491 (lines 7616-7620) Links
    [link](</my uri>)
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><a href="/my%20uri">link</a></p>
    +
    
    Example 492 (lines 7625-7631) Links
    [link](foo
    bar)
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>[link](foo bar)</p>
    +
    
    Example 493 (lines 7633-7639) Links
    [link](<foo
    bar>)
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>[link](<foo bar>)</p>
    +
    
    Example 494 (lines 7644-7648) Links
    [a](<b)c>)
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><a href="b)c">a</a></p>
    +
    
    Example 495 (lines 7652-7656) Links
    [link](<foo\>)
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>[link](&lt;foo&gt;)</p>
    +
    
    Example 496 (lines 7661-7669) Links
    [a](<b)c
    [a](<b)c>
    [a](<b>c)
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>[a](&lt;b)c [a](&lt;b)c&gt; [a](<b>c)</p>
    +
    
    Example 497 (lines 7673-7677) Links
    [link](\(foo\))
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><a href="(foo)">link</a></p>
    +
    
    Example 498 (lines 7682-7686) Links
    [link](foo(and(bar)))
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><a href="foo(and(bar))">link</a></p>
    +
    
    Example 499 (lines 7691-7695) Links
    [link](foo(and(bar))
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>[link](foo(and(bar))</p>
    +
    
    Example 500 (lines 7698-7702) Links
    [link](foo\(and\(bar\))
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><a href="foo(and(bar)">link</a></p>
    +
    
    Example 501 (lines 7705-7709) Links
    [link](<foo(and(bar)>)
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><a href="foo(and(bar)">link</a></p>
    +
    
    Example 502 (lines 7715-7719) Links
    [link](foo\)\:)
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><a href="foo):">link</a></p>
    +
    
    Example 503 (lines 7724-7734) Links
    [link](#fragment)
    
    [link](https://example.com#fragment)
    
    [link](https://example.com?foo=3#frag)
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><a href="#fragment">link</a></p><p><a href="https://example.com#fragment">link</a></p><p><a href="https://example.com?foo=3#frag">link</a></p>
    +
    
    Example 504 (lines 7740-7744) Links
    [link](foo\bar)
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><a href="foo%5Cbar">link</a></p>
    +
    
    Example 505 (lines 7756-7760) Links
    [link](foo%20b&auml;)
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><a href="foo%20b%C3%A4">link</a></p>
    +
    
    Example 506 (lines 7767-7771) Links
    [link]("title")
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><a href="%22title%22">link</a></p>
    +
    
    Example 507 (lines 7776-7784) Links
    [link](/url "title")
    [link](/url 'title')
    [link](/url (title))
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><a href="/url" title="title">link</a> <a href="/url" title="title">link</a> <a href="/url" title="title">link</a></p>
    +
    
    Example 508 (lines 7790-7794) Links
    [link](/url "title \"&quot;")
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><a href="/url" title="title &quot;&quot;">link</a></p>
    +
    
    Example 509 (lines 7801-7805) Links
    [link](/url "title")
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><a href="/url%C2%A0%22title%22">link</a></p>
    +
    
    Example 510 (lines 7810-7814) Links
    [link](/url "title "and" title")
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>[link](/url &quot;title &quot;and&quot; title&quot;)</p>
    +
    
    Example 511 (lines 7819-7823) Links
    [link](/url 'title "and" title')
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><a href="/url" title="title &quot;and&quot; title">link</a></p>
    +
    
    Example 512 (lines 7844-7849) Links
    [link](   /uri
      "title"  )
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><a href="/uri" title="title">link</a></p>
    +
    
    Example 513 (lines 7855-7859) Links
    [link] (/uri)
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>[link] (/uri)</p>
    +
    
    Example 514 (lines 7865-7869) Links
    [link [foo [bar]]](/uri)
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><a href="/uri">link [foo [bar]]</a></p>
    +
    
    Example 515 (lines 7872-7876) Links
    [link] bar](/uri)
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>[link] bar](/uri)</p>
    +
    
    Example 516 (lines 7879-7883) Links
    [link [bar](/uri)
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>[link <a href="/uri">bar</a></p>
    +
    
    Example 517 (lines 7886-7890) Links
    [link \[bar](/uri)
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><a href="/uri">link [bar</a></p>
    +
    
    Example 518 (lines 7895-7899) Links
    [link *foo **bar** `#`*](/uri)
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><a href="/uri">link <em>foo <strong>bar</strong> <code>#</code></em></a></p>
    +
    
    Example 519 (lines 7902-7906) Links
    [![moon](moon.jpg)](/uri)
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><a href="/uri"><img alt="moon" src="moon.jpg"></a></p>
    +
    
    Example 520 (lines 7911-7915) Links
    [foo [bar](/uri)](/uri)
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>[foo <a href="/uri">bar</a>](/uri)</p>
    +
    
    Example 521 (lines 7918-7922) Links
    [foo *[bar [baz](/uri)](/uri)*](/uri)
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>[foo <em>[bar <a href="/uri">baz</a>](/uri)</em>](/uri)</p>
    +
    
    Example 522 (lines 7925-7929) Links
    ![[[foo](uri1)](uri2)](uri3)
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><img alt="[foo](uri2)" src="uri3"></p>
    +
    
    Example 523 (lines 7935-7939) Links
    *[foo*](/uri)
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>*<a href="/uri">foo*</a></p>
    +
    
    Example 524 (lines 7942-7946) Links
    [foo *bar](baz*)
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><a href="baz*">foo *bar</a></p>
    +
    
    Example 525 (lines 7952-7956) Links
    *foo [bar* baz]
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><em>foo [bar</em> baz]</p>
    +
    
    Example 526 (lines 7962-7966) Links
    [foo <bar attr="](baz)">
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>[foo <bar attr="](baz)"></p>
    +
    
    Example 527 (lines 7969-7973) Links
    [foo`](/uri)`
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>[foo<code>](/uri)</code></p>
    +
    
    Example 528 (lines 7976-7980) Links
    [foo<https://example.com/?search=](uri)>
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>[foo<a href="https://example.com/?search=%5D(uri)">https://example.com/?search=](uri)</a></p>
    +
    
    Example 529 (lines 8014-8020) Links
    [foo][bar]
    
    [bar]: /url "title"
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><a href="/url" title="title">foo</a></p>
    +
    
    Example 530 (lines 8029-8035) Links
    [link [foo [bar]]][ref]
    
    [ref]: /uri
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><a href="/uri">link [foo [bar]]</a></p>
    +
    
    Example 531 (lines 8038-8044) Links
    [link \[bar][ref]
    
    [ref]: /uri
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><a href="/uri">link [bar</a></p>
    +
    
    Example 532 (lines 8049-8055) Links
    [link *foo **bar** `#`*][ref]
    
    [ref]: /uri
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><a href="/uri">link <em>foo <strong>bar</strong> <code>#</code></em></a></p>
    +
    
    Example 533 (lines 8058-8064) Links
    [![moon](moon.jpg)][ref]
    
    [ref]: /uri
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><a href="/uri"><img alt="moon" src="moon.jpg"></a></p>
    +
    
    Example 534 (lines 8069-8075) Links
    [foo [bar](/uri)][ref]
    
    [ref]: /uri
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>[foo <a href="/uri">bar</a>]<a href="/uri">ref</a></p>
    +
    
    Example 535 (lines 8078-8084) Links
    [foo *bar [baz][ref]*][ref]
    
    [ref]: /uri
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>[foo <em>bar <a href="/uri">baz</a></em>]<a href="/uri">ref</a></p>
    +
    
    Example 536 (lines 8093-8099) Links
    *[foo*][ref]
    
    [ref]: /uri
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>*<a href="/uri">foo*</a></p>
    +
    
    Example 537 (lines 8102-8108) Links
    [foo *bar][ref]*
    
    [ref]: /uri
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><a href="/uri">foo *bar</a>*</p>
    +
    
    Example 538 (lines 8114-8120) Links
    [foo <bar attr="][ref]">
    
    [ref]: /uri
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>[foo <bar attr="][ref]"></p>
    +
    
    Example 539 (lines 8123-8129) Links
    [foo`][ref]`
    
    [ref]: /uri
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>[foo<code>][ref]</code></p>
    +
    
    Example 540 (lines 8132-8138) Links
    [foo<https://example.com/?search=][ref]>
    
    [ref]: /uri
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>[foo<a href="https://example.com/?search=%5D%5Bref%5D">https://example.com/?search=][ref]</a></p>
    +
    
    Example 541 (lines 8143-8149) Links
    [foo][BaR]
    
    [bar]: /url "title"
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><a href="/url" title="title">foo</a></p>
    +
    
    Example 542 (lines 8154-8160) Links
    [ẞ]
    
    [SS]: /url
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><a href="/url">ẞ</a></p>
    +
    
    Example 543 (lines 8166-8173) Links
    [Foo
      bar]: /url
    
    [Baz][Foo bar]
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><a href="/url">Baz</a></p>
    +
    
    Example 544 (lines 8179-8185) Links
    [foo] [bar]
    
    [bar]: /url "title"
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>[foo] <a href="/url" title="title">bar</a></p>
    +
    
    Example 545 (lines 8188-8196) Links
    [foo]
    [bar]
    
    [bar]: /url "title"
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>[foo] <a href="/url" title="title">bar</a></p>
    +
    
    Example 546 (lines 8229-8237) Links
    [foo]: /url1
    
    [foo]: /url2
    
    [bar][foo]
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><a href="/url1">bar</a></p>
    +
    
    Example 547 (lines 8244-8250) Links
    [bar][foo\!]
    
    [foo!]: /url
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>[bar][foo!]</p>
    +
    
    Example 548 (lines 8256-8263) Links
    [foo][ref[]
    
    [ref[]: /uri
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>[foo][ref[]</p><p>[ref[]: /uri</p>
    +
    
    Example 549 (lines 8266-8273) Links
    [foo][ref[bar]]
    
    [ref[bar]]: /uri
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>[foo][ref[bar]]</p><p>[ref[bar]]: /uri</p>
    +
    
    Example 550 (lines 8276-8283) Links
    [[[foo]]]
    
    [[[foo]]]: /url
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>[[[foo]]]</p><p>[[[foo]]]: /url</p>
    +
    
    Example 551 (lines 8286-8292) Links
    [foo][ref\[]
    
    [ref\[]: /uri
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><a href="/uri">foo</a></p>
    +
    
    Example 552 (lines 8297-8303) Links
    [bar\\]: /uri
    
    [bar\\]
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><a href="/uri">bar\</a></p>
    +
    
    Example 553 (lines 8309-8316) Links
    []
    
    []: /uri
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>[]</p><p>[]: /uri</p>
    +
    
    Example 554 (lines 8319-8330) Links
    [
     ]
    
    [
     ]: /uri
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>[ ]</p><p>[ ]: /uri</p>
    +
    
    Example 555 (lines 8342-8348) Links
    [foo][]
    
    [foo]: /url "title"
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><a href="/url" title="title">foo</a></p>
    +
    
    Example 556 (lines 8351-8357) Links
    [*foo* bar][]
    
    [*foo* bar]: /url "title"
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><a href="/url" title="title"><em>foo</em> bar</a></p>
    +
    
    Example 557 (lines 8362-8368) Links
    [Foo][]
    
    [foo]: /url "title"
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><a href="/url" title="title">Foo</a></p>
    +
    
    Example 558 (lines 8375-8383) Links
    [foo] 
    []
    
    [foo]: /url "title"
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><a href="/url" title="title">foo</a> []</p>
    +
    
    Example 559 (lines 8395-8401) Links
    [foo]
    
    [foo]: /url "title"
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><a href="/url" title="title">foo</a></p>
    +
    
    Example 560 (lines 8404-8410) Links
    [*foo* bar]
    
    [*foo* bar]: /url "title"
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><a href="/url" title="title"><em>foo</em> bar</a></p>
    +
    
    Example 561 (lines 8413-8419) Links
    [[*foo* bar]]
    
    [*foo* bar]: /url "title"
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>[<a href="/url" title="title"><em>foo</em> bar</a>]</p>
    +
    
    Example 562 (lines 8422-8428) Links
    [[bar [foo]
    
    [foo]: /url
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>[[bar <a href="/url">foo</a></p>
    +
    
    Example 563 (lines 8433-8439) Links
    [Foo]
    
    [foo]: /url "title"
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><a href="/url" title="title">Foo</a></p>
    +
    
    Example 564 (lines 8444-8450) Links
    [foo] bar
    
    [foo]: /url
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><a href="/url">foo</a> bar</p>
    +
    
    Example 565 (lines 8456-8462) Links
    \[foo]
    
    [foo]: /url "title"
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>[foo]</p>
    +
    
    Example 566 (lines 8468-8474) Links
    [foo*]: /url
    
    *[foo*]
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>*<a href="/url">foo*</a></p>
    +
    
    Example 567 (lines 8480-8487) Links
    [foo][bar]
    
    [foo]: /url1
    [bar]: /url2
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><a href="/url2">foo</a></p>
    +
    
    Example 568 (lines 8489-8495) Links
    [foo][]
    
    [foo]: /url1
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><a href="/url1">foo</a></p>
    +
    
    Example 569 (lines 8499-8505) Links
    [foo]()
    
    [foo]: /url1
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><a href="">foo</a></p>
    +
    
    Example 570 (lines 8507-8513) Links
    [foo](not a link)
    
    [foo]: /url1
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><a href="/url1">foo</a>(not a link)</p>
    +
    
    Example 571 (lines 8518-8524) Links
    [foo][bar][baz]
    
    [baz]: /url
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>[foo]<a href="/url">bar</a></p>
    +
    
    Example 572 (lines 8530-8537) Links
    [foo][bar][baz]
    
    [baz]: /url1
    [bar]: /url2
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><a href="/url2">foo</a><a href="/url1">baz</a></p>
    +
    
    Example 573 (lines 8543-8550) Links
    [foo][bar][baz]
    
    [baz]: /url1
    [foo]: /url2
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>[foo]<a href="/url1">bar</a></p>
    +
    
    Example 574 (lines 8566-8570) Images
    ![foo](/url "title")
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><img alt="foo" src="/url" title="title"></p>
    +
    
    Example 575 (lines 8573-8579) Images
    ![foo *bar*]
    
    [foo *bar*]: train.jpg "train & tracks"
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><img alt="foo bar" src="train.jpg" title="train &amp; tracks"></p>
    +
    
    Example 576 (lines 8582-8586) Images
    ![foo ![bar](/url)](/url2)
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><img alt="foo bar" src="/url2"></p>
    +
    
    Example 577 (lines 8589-8593) Images
    ![foo [bar](/url)](/url2)
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><img alt="foo bar" src="/url2"></p>
    +
    
    Example 578 (lines 8603-8609) Images
    ![foo *bar*][]
    
    [foo *bar*]: train.jpg "train & tracks"
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><img alt="foo bar" src="train.jpg" title="train &amp; tracks"></p>
    +
    
    Example 579 (lines 8612-8618) Images
    ![foo *bar*][foobar]
    
    [FOOBAR]: train.jpg "train & tracks"
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><img alt="foo bar" src="train.jpg" title="train &amp; tracks"></p>
    +
    
    Example 580 (lines 8621-8625) Images
    ![foo](train.jpg)
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><img alt="foo" src="train.jpg"></p>
    +
    
    Example 581 (lines 8628-8632) Images
    My ![foo bar](/path/to/train.jpg  "title"   )
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>My <img alt="foo bar" src="/path/to/train.jpg" title="title"></p>
    +
    
    Example 582 (lines 8635-8639) Images
    ![foo](<url>)
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><img alt="foo" src="url"></p>
    +
    
    Example 583 (lines 8642-8646) Images
    ![](/url)
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><img alt="" src="/url"></p>
    +
    
    Example 584 (lines 8651-8657) Images
    ![foo][bar]
    
    [bar]: /url
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><img alt="foo" src="/url"></p>
    +
    
    Example 585 (lines 8660-8666) Images
    ![foo][bar]
    
    [BAR]: /url
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><img alt="foo" src="/url"></p>
    +
    
    Example 586 (lines 8671-8677) Images
    ![foo][]
    
    [foo]: /url "title"
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><img alt="foo" src="/url" title="title"></p>
    +
    
    Example 587 (lines 8680-8686) Images
    ![*foo* bar][]
    
    [*foo* bar]: /url "title"
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><img alt="foo bar" src="/url" title="title"></p>
    +
    
    Example 588 (lines 8691-8697) Images
    ![Foo][]
    
    [foo]: /url "title"
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><img alt="Foo" src="/url" title="title"></p>
    +
    
    Example 589 (lines 8703-8711) Images
    ![foo] 
    []
    
    [foo]: /url "title"
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><img alt="foo" src="/url" title="title"> []</p>
    +
    
    Example 590 (lines 8716-8722) Images
    ![foo]
    
    [foo]: /url "title"
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><img alt="foo" src="/url" title="title"></p>
    +
    
    Example 591 (lines 8725-8731) Images
    ![*foo* bar]
    
    [*foo* bar]: /url "title"
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><img alt="foo bar" src="/url" title="title"></p>
    +
    
    Example 592 (lines 8736-8743) Images
    ![[foo]]
    
    [[foo]]: /url "title"
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>![[foo]]</p><p>[[foo]]: /url &quot;title&quot;</p>
    +
    
    Example 593 (lines 8748-8754) Images
    ![Foo]
    
    [foo]: /url "title"
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><img alt="Foo" src="/url" title="title"></p>
    +
    
    Example 594 (lines 8760-8766) Images
    !\[foo]
    
    [foo]: /url "title"
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>![foo]</p>
    +
    
    Example 595 (lines 8772-8778) Images
    \![foo]
    
    [foo]: /url "title"
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>!<a href="/url" title="title">foo</a></p>
    +
    
    Example 596 (lines 8805-8809) Autolinks
    <http://foo.bar.baz>
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><a href="http://foo.bar.baz">http://foo.bar.baz</a></p>
    +
    
    Example 597 (lines 8812-8816) Autolinks
    <https://foo.bar.baz/test?q=hello&id=22&boolean>
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><a href="https://foo.bar.baz/test?q=hello&amp;id=22&amp;boolean">https://foo.bar.baz/test?q=hello&amp;id=22&amp;boolean</a></p>
    +
    
    Example 598 (lines 8819-8823) Autolinks
    <irc://foo.bar:2233/baz>
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><a href="irc://foo.bar:2233/baz">irc://foo.bar:2233/baz</a></p>
    +
    
    Example 599 (lines 8828-8832) Autolinks
    <MAILTO:FOO@BAR.BAZ>
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><a href="MAILTO:FOO@BAR.BAZ">MAILTO:FOO@BAR.BAZ</a></p>
    +
    
    Example 600 (lines 8840-8844) Autolinks
    <a+b+c:d>
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><a href="a+b+c:d">a+b+c:d</a></p>
    +
    
    Example 601 (lines 8847-8851) Autolinks
    <made-up-scheme://foo,bar>
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><a href="made-up-scheme://foo,bar">made-up-scheme://foo,bar</a></p>
    +
    
    Example 602 (lines 8854-8858) Autolinks
    <https://../>
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><a href="https://../">https://../</a></p>
    +
    
    Example 603 (lines 8861-8865) Autolinks
    <localhost:5001/foo>
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><a href="localhost:5001/foo">localhost:5001/foo</a></p>
    +
    
    Example 604 (lines 8870-8874) Autolinks
    <https://foo.bar/baz bim>
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>&lt;https://foo.bar/baz bim&gt;</p>
    +
    
    Example 605 (lines 8879-8883) Autolinks
    <https://example.com/\[\>
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><a href="https://example.com/%5C%5B%5C">https://example.com/\[\</a></p>
    +
    
    Example 606 (lines 8901-8905) Autolinks
    <foo@bar.example.com>
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><a href="mailto:foo@bar.example.com">foo@bar.example.com</a></p>
    +
    
    Example 607 (lines 8908-8912) Autolinks
    <foo+special@Bar.baz-bar0.com>
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><a href="mailto:foo+special@Bar.baz-bar0.com">foo+special@Bar.baz-bar0.com</a></p>
    +
    
    Example 608 (lines 8917-8921) Autolinks
    <foo\+@bar.example.com>
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>&lt;foo+@bar.example.com&gt;</p>
    +
    
    Example 609 (lines 8926-8930) Autolinks
    <>
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>&lt;&gt;</p>
    +
    
    Example 610 (lines 8933-8937) Autolinks
    < https://foo.bar >
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>&lt; https://foo.bar &gt;</p>
    +
    
    Example 611 (lines 8940-8944) Autolinks
    <m:abc>
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>&lt;m:abc&gt;</p>
    +
    
    Example 612 (lines 8947-8951) Autolinks
    <foo.bar.baz>
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>&lt;foo.bar.baz&gt;</p>
    +
    
    Example 613 (lines 8954-8958) Autolinks
    https://example.com
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>https://example.com</p>
    +
    
    Example 614 (lines 8961-8965) Autolinks
    foo@bar.example.com
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>foo@bar.example.com</p>
    +
    
    Example 615 (lines 9041-9045) Raw HTML
    <a><bab><c2c>
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><a><bab><c2c></p>
    +
    
    Example 616 (lines 9050-9054) Raw HTML
    <a/><b2/>
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><a><b2></p>
    +
    
    Example 617 (lines 9059-9065) Raw HTML
    <a  /><b2
    data="foo" >
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><a><b2 data="foo"></p>
    +
    
    Example 618 (lines 9070-9076) Raw HTML
    <a foo="bar" bam = 'baz <em>"</em>'
    _boolean zoop:33=zoop:33 />
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><a 'baz <em bam="" foo="bar">"</em>' _boolean zoop:33=zoop:33 /></p>
    +
    
    Example 619 (lines 9081-9085) Raw HTML
    Foo <responsive-image src="foo.jpg" />
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>Foo <responsive-image src="foo.jpg"></p>
    +
    
    Example 620 (lines 9090-9094) Raw HTML
    <33> <__>
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>&lt;33&gt; &lt;__&gt;</p>
    +
    
    Example 621 (lines 9099-9103) Raw HTML
    <a h*#ref="hi">
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>&lt;a h*#ref=&quot;hi&quot;&gt;</p>
    +
    
    Example 622 (lines 9108-9112) Raw HTML
    <a href="hi'> <a href=hi'>
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>&lt;a href=&quot;hi'&gt; &lt;a href=hi'&gt;</p>
    +
    
    Example 623 (lines 9117-9127) Raw HTML
    < a><
    foo><bar/ >
    <foo bar=baz
    bim!bop />
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>&lt; a&gt;&lt; foo&gt;&lt;bar/ &gt; &lt;foo bar=baz bim!bop /&gt;</p>
    +
    
    Example 624 (lines 9132-9136) Raw HTML
    <a href='bar'title=title>
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>&lt;a href='bar'title=title&gt;</p>
    +
    
    Example 625 (lines 9141-9145) Raw HTML
    </a></foo >
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p></a></foo></p>
    +
    
    Example 626 (lines 9150-9154) Raw HTML
    </a href="foo">
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>&lt;/a href=&quot;foo&quot;&gt;</p>
    +
    
    Example 627 (lines 9159-9165) Raw HTML
    foo <!-- this is a --
    comment - with hyphens -->
    
    --- expected HTML
    +++ actual HTML
    @@ -1,2 +1 @@
    -<p>foo <!-- this is a --
    -comment - with hyphens --></p>
    +
    
    Example 628 (lines 9167-9174) Raw HTML
    foo <!--> foo -->
    
    foo <!---> foo -->
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>foo <!----> foo --&gt;</p><p>foo <!----> foo --&gt;</p>
    +
    
    Example 629 (lines 9179-9183) Raw HTML
    foo <?php echo $a; ?>
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>foo <?php echo $a; ?></p>
    +
    
    Example 630 (lines 9188-9192) Raw HTML
    foo <!ELEMENT br EMPTY>
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>foo <!--ELEMENT br EMPTY--></p>
    +
    
    Example 631 (lines 9197-9201) Raw HTML
    foo <![CDATA[>&<]]>
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>foo <![CDATA[>&<]]></p>
    +
    
    Example 632 (lines 9207-9211) Raw HTML
    foo <a href="&ouml;">
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>foo <a href="ö"></p>
    +
    
    Example 633 (lines 9216-9220) Raw HTML
    foo <a href="\*">
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>foo <a href="\*"></p>
    +
    
    Example 634 (lines 9223-9227) Raw HTML
    <a href="\"">
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>&lt;a href=&quot;&quot;&quot;&gt;</p>
    +
    
    Example 635 (lines 9233-9241) Raw HTML
    <a
    > quoted text
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>&lt;a</p><blockquote><p>quoted text</p></blockquote>
    +
    
    Example 636 (lines 9251-9257) Hard line breaks
    foo  
    baz
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>foo<br>baz</p>
    +
    
    Example 637 (lines 9263-9269) Hard line breaks
    foo\
    baz
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>foo<br>baz</p>
    +
    
    Example 638 (lines 9274-9280) Hard line breaks
    foo       
    baz
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>foo<br>baz</p>
    +
    
    Example 639 (lines 9285-9291) Hard line breaks
    foo  
         bar
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>foo<br>bar</p>
    +
    
    Example 640 (lines 9294-9300) Hard line breaks
    foo\
         bar
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>foo<br>bar</p>
    +
    
    Example 641 (lines 9306-9312) Hard line breaks
    *foo  
    bar*
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><em>foo<br>bar</em></p>
    +
    
    Example 642 (lines 9315-9321) Hard line breaks
    *foo\
    bar*
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><em>foo<br>bar</em></p>
    +
    
    Example 643 (lines 9326-9331) Hard line breaks
    `code  
    span`
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><code>code span</code></p>
    +
    
    Example 644 (lines 9334-9339) Hard line breaks
    `code\
    span`
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><code>code\ span</code></p>
    +
    
    Example 645 (lines 9344-9350) Hard line breaks
    <a href="foo  
    bar">
    
    --- expected HTML
    +++ actual HTML
    @@ -1,2 +1 @@
    -<p><a href="foo  
    -bar"></p>
    +
    
    Example 646 (lines 9353-9359) Hard line breaks
    <a href="foo\
    bar">
    
    --- expected HTML
    +++ actual HTML
    @@ -1,2 +1 @@
    -<p><a href="foo\
    -bar"></p>
    +
    
    Example 647 (lines 9366-9370) Hard line breaks
    foo\
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>foo\</p>
    +
    
    Example 648 (lines 9373-9377) Hard line breaks
    foo  
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>foo</p>
    +
    
    Example 649 (lines 9380-9384) Hard line breaks
    ### foo\
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<h3>foo\</h3>
    +
    
    Example 650 (lines 9387-9391) Hard line breaks
    ### foo  
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<h3>foo</h3>
    +
    
    Example 651 (lines 9402-9408) Soft line breaks
    foo
    baz
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>foo baz</p>
    +
    
    Example 652 (lines 9414-9420) Soft line breaks
    foo 
     baz
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>foo baz</p>
    +
    
    Example 653 (lines 9434-9438) Textual content
    hello $.;'there
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>hello $.;'there</p>
    +
    
    Example 654 (lines 9441-9445) Textual content
    Foo χρῆν
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>Foo χρῆν</p>
    +
    
    Example 655 (lines 9450-9454) Textual content
    Multiple     spaces
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>Multiple spaces</p>
    +
    
    0 passed, 318 failed, 38 errored, 299 skipped
  stderr:
    --- drydock: progress ---
    cases: pass=0 fail=318 error=38 skip=299 total=655 from=result.stdout
    --- drydock: end progress ---
    --- drydock: values at failure ---
      result = CompletedProcess(args=['/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/.venv/bin/python', 'sources/spec_tests.py', '--program', '/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/commonmark', '--spec', 'sources/spec.txt', '--pattern', '^(Backslash escapes|Entity and numeric character references|Code spans|Emphasis and… (+105009 chars)
    --- drydock: end values ---
    Traceback (most recent call last):
      File "conformance-inlines.py", line 12, in <module>
        assert result.returncode == 0
               ^^^^^^^^^^^^^^^^^^^^^^
    AssertionError

## Post-build programmatic acceptance
- PASS: conformance-preliminaries (FEATURE-ConformanceIntegration.md)
  intent: The integrated parser passes every supplied Tabs and Precedence example.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/.venv/bin/python
  provisioning: not required
  return code: 0
  stdout:
    12 passed, 0 failed, 0 errored, 643 skipped
- FAIL: conformance-blocks (FEATURE-ConformanceIntegration.md)
  intent: The integrated parser passes every example in the supplied leaf block sections.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/.venv/bin/python
  provisioning: not required
  return code: 1
  stdout:
    Example 196 (lines 3221-3227) Link reference definitions
    [Foo*bar\]]:my_(url) 'title (with parens)'
    
    [Foo*bar\]]
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><a href="my_(url)" title="title (with parens)">Foo*bar]</a></p>
    +<p>[Foo*bar]]:my_(url) 'title (with parens)'</p><p>[Foo*bar]]</p>
    
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
    +<p>title line1 line2 '</p><p><a href="/url" title="">foo</a></p>
    
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
    
    184 passed, 3 failed, 0 errored, 468 skipped
  stderr:
    --- drydock: progress ---
    cases: pass=184 fail=3 error=0 skip=468 total=655 from=result.stdout
    --- drydock: end progress ---
    --- drydock: values at failure ---
      result = CompletedProcess(args=['/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/.venv/bin/python', 'sources/spec_tests.py', '--program', '/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/commonmark', '--spec', 'sources/spec.txt', '--pattern', '^(Thematic breaks|ATX headings|Setext headings|Indented code blocks|Fenced code blo… (+937 chars)
    --- drydock: end values ---
    Traceback (most recent call last):
      File "conformance-blocks.py", line 12, in <module>
        assert result.returncode == 0
               ^^^^^^^^^^^^^^^^^^^^^^
    AssertionError
- PASS: conformance-containers (FEATURE-ConformanceIntegration.md)
  intent: The integrated parser passes every supplied block quote, list item, and list example.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/.venv/bin/python
  provisioning: not required
  return code: 0
  stdout:
    99 passed, 0 failed, 0 errored, 556 skipped
- FAIL: conformance-inlines (FEATURE-ConformanceIntegration.md)
  intent: The integrated parser passes every example in the supplied inline and text sections.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/.venv/bin/python
  provisioning: not required
  return code: 1
  stdout:
    Example 371 (lines 6521-6525) Emphasis and strong emphasis
    *(*foo*)*
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><em>(<em>foo</em>)</em></p>
    +<p><em>(*foo</em>)*</p>
    
    Example 375 (lines 6562-6566) Emphasis and strong emphasis
    _(_foo_)_
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><em>(<em>foo</em>)</em></p>
    +<p><em>(_foo</em>)_</p>
    
    Example 391 (lines 6704-6708) Emphasis and strong emphasis
    __foo, __bar__, baz__
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><strong>foo, <strong>bar</strong>, baz</strong></p>
    +<p><strong>foo, __bar</strong>, baz__</p>
    
    Example 395 (lines 6751-6755) Emphasis and strong emphasis
    *(**foo**)*
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><em>(<strong>foo</strong>)</em></p>
    +<p><em>(**foo</em>)*</p>
    
    Example 396 (lines 6758-6764) Emphasis and strong emphasis
    **Gomphocarpus (*Gomphocarpus physocarpus*, syn.
    *Asclepias physocarpa*)**
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><strong>Gomphocarpus (<em>Gomphocarpus physocarpus</em>, syn. <em>Asclepias physocarpa</em>)</strong></p>
    +<p>*<em>Gomphocarpus (*Gomphocarpus physocarpus</em>, syn. <em>Asclepias physocarpa</em>)**</p>
    
    Example 397 (lines 6767-6771) Emphasis and strong emphasis
    **foo "*bar*" foo**
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><strong>foo &quot;<em>bar</em>&quot; foo</strong></p>
    +<p>*<em>foo &quot;*bar</em>&quot; foo**</p>
    
    Example 401 (lines 6808-6812) Emphasis and strong emphasis
    _(__foo__)_
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><em>(<strong>foo</strong>)</em></p>
    +<p><em>(__foo</em>)_</p>
    
    Example 406 (lines 6854-6858) Emphasis and strong emphasis
    *foo [bar](/url)*
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><em>foo <a href="/url">bar</a></em></p>
    +<p>*foo <a href="/url">bar</a>*</p>
    
    Example 408 (lines 6873-6877) Emphasis and strong emphasis
    _foo __bar__ baz_
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><em>foo <strong>bar</strong> baz</em></p>
    +<p><em>foo __bar</em> baz_</p>
    
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
    +<p>_<em>foo</em> bar_</p>
    
    Example 411 (lines 6894-6898) Emphasis and strong emphasis
    *foo *bar**
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><em>foo <em>bar</em></em></p>
    +<p><em>foo *bar</em></p>
    
    Example 412 (lines 6901-6905) Emphasis and strong emphasis
    *foo **bar** baz*
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><em>foo <strong>bar</strong> baz</em></p>
    +<p><em>foo **bar</em> baz*</p>
    
    Example 413 (lines 6907-6911) Emphasis and strong emphasis
    *foo**bar**baz*
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><em>foo<strong>bar</strong>baz</em></p>
    +<p><em>foo</em>bar*<em>baz</em></p>
    
    Example 414 (lines 6931-6935) Emphasis and strong emphasis
    *foo**bar*
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><em>foo**bar</em></p>
    +<p><em>foo</em>bar*</p>
    
    Example 415 (lines 6944-6948) Emphasis and strong emphasis
    ***foo** bar*
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><em><strong>foo</strong> bar</em></p>
    +<p>*<strong>foo</strong> bar*</p>
    
    Example 416 (lines 6951-6955) Emphasis and strong emphasis
    *foo **bar***
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><em>foo <strong>bar</strong></em></p>
    +<p><em>foo **bar</em></p>
    
    Example 417 (lines 6958-6962) Emphasis and strong emphasis
    *foo**bar***
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><em>foo<strong>bar</strong></em></p>
    +<p><em>foo</em>bar***</p>
    
    Example 418 (lines 6969-6973) Emphasis and strong emphasis
    foo***bar***baz
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>foo<em><strong>bar</strong></em>baz</p>
    +<p>foo*<strong>bar</strong>baz</p>
    
    Example 419 (lines 6975-6979) Emphasis and strong emphasis
    foo******bar*********baz
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>foo<strong><strong><strong>bar</strong></strong></strong>***baz</p>
    +<p>foo****<strong>bar</strong>baz</p>
    
    Example 420 (lines 6984-6988) Emphasis and strong emphasis
    *foo **bar *baz* bim** bop*
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><em>foo <strong>bar <em>baz</em> bim</strong> bop</em></p>
    +<p><em>foo **bar *baz</em> bim** bop*</p>
    
    Example 421 (lines 6991-6995) Emphasis and strong emphasis
    *foo [*bar*](/url)*
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><em>foo <a href="/url"><em>bar</em></a></em></p>
    +<p>*foo <a href="/url"><em>bar</em></a>*</p>
    
    Example 424 (lines 7020-7024) Emphasis and strong emphasis
    **foo [bar](/url)**
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><strong>foo <a href="/url">bar</a></strong></p>
    +<p>**foo <a href="/url">bar</a>**</p>
    
    Example 426 (lines 7039-7043) Emphasis and strong emphasis
    __foo _bar_ baz__
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><strong>foo <em>bar</em> baz</strong></p>
    +<p>_<em>foo _bar</em> baz__</p>
    
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
    +<p>__<strong>foo</strong> bar__</p>
    
    Example 429 (lines 7060-7064) Emphasis and strong emphasis
    **foo **bar****
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><strong>foo <strong>bar</strong></strong></p>
    +<p><strong>foo **bar</strong></p>
    
    Example 430 (lines 7067-7071) Emphasis and strong emphasis
    **foo *bar* baz**
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><strong>foo <em>bar</em> baz</strong></p>
    +<p>*<em>foo *bar</em> baz**</p>
    
    Example 431 (lines 7074-7078) Emphasis and strong emphasis
    **foo*bar*baz**
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><strong>foo<em>bar</em>baz</strong></p>
    +<p>*<em>foo</em>bar<em>baz</em></p>
    
    Example 432 (lines 7081-7085) Emphasis and strong emphasis
    ***foo* bar**
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><strong><em>foo</em> bar</strong></p>
    +<p>**<em>foo</em> bar**</p>
    
    Example 433 (lines 7088-7092) Emphasis and strong emphasis
    **foo *bar***
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><strong>foo <em>bar</em></strong></p>
    +<p><strong>foo *bar</strong></p>
    
    Example 434 (lines 7097-7103) Emphasis and strong emphasis
    **foo *bar **baz**
    bim* bop**
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><strong>foo <em>bar <strong>baz</strong> bim</em> bop</strong></p>
    +<p><strong>foo *bar **baz</strong> bim* bop**</p>
    
    Example 435 (lines 7106-7110) Emphasis and strong emphasis
    **foo [*bar*](/url)**
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><strong>foo <a href="/url"><em>bar</em></a></strong></p>
    +<p>**foo <a href="/url"><em>bar</em></a>**</p>
    
    Example 439 (lines 7139-7143) Emphasis and strong emphasis
    foo *\**
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>foo <em>*</em></p>
    +<p>foo ***</p>
    
    Example 442 (lines 7160-7164) Emphasis and strong emphasis
    foo **\***
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>foo <strong>*</strong></p>
    +<p>foo *****</p>
    
    Example 445 (lines 7185-7189) Emphasis and strong emphasis
    *foo**
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><em>foo</em>*</p>
    +<p><em>foo</em></p>
    
    Example 448 (lines 7206-7210) Emphasis and strong emphasis
    **foo***
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><strong>foo</strong>*</p>
    +<p><strong>foo</strong></p>
    
    Example 449 (lines 7213-7217) Emphasis and strong emphasis
    *foo****
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><em>foo</em>***</p>
    +<p><em>foo</em></p>
    
    Example 451 (lines 7230-7234) Emphasis and strong emphasis
    foo _\__
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>foo <em>_</em></p>
    +<p>foo ___</p>
    
    Example 454 (lines 7251-7255) Emphasis and strong emphasis
    foo __\___
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>foo <strong>_</strong></p>
    +<p>foo _____</p>
    
    Example 457 (lines 7276-7280) Emphasis and strong emphasis
    _foo__
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><em>foo</em>_</p>
    +<p><em>foo</em></p>
    
    Example 460 (lines 7297-7301) Emphasis and strong emphasis
    __foo___
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><strong>foo</strong>_</p>
    +<p><strong>foo</strong></p>
    
    Example 461 (lines 7304-7308) Emphasis and strong emphasis
    _foo____
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><em>foo</em>___</p>
    +<p><em>foo</em></p>
    
    Example 466 (lines 7345-7349) Emphasis and strong emphasis
    ****foo****
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><strong><strong>foo</strong></strong></p>
    +<p>**<strong>foo</strong></p>
    
    Example 467 (lines 7352-7356) Emphasis and strong emphasis
    ____foo____
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><strong><strong>foo</strong></strong></p>
    +<p>__<strong>foo</strong></p>
    
    Example 468 (lines 7363-7367) Emphasis and strong emphasis
    ******foo******
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><strong><strong><strong>foo</strong></strong></strong></p>
    +<p>****<strong>foo</strong></p>
    
    Example 469 (lines 7372-7376) Emphasis and strong emphasis
    ***foo***
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><em><strong>foo</strong></em></p>
    +<p>*<strong>foo</strong></p>
    
    Example 470 (lines 7379-7383) Emphasis and strong emphasis
    _____foo_____
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><em><strong><strong>foo</strong></strong></em></p>
    +<p>___<strong>foo</strong></p>
    
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
    
    Example 491 (lines 7616-7620) Links
    [link](</my uri>)
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><a href="/my%20uri">link</a></p>
    +<p>[link](</my>)</p>
    
    Example 518 (lines 7895-7899) Links
    [link *foo **bar** `#`*](/uri)
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><a href="/uri">link <em>foo <strong>bar</strong> <code>#</code></em></a></p>
    +<p><a href="/uri">link <em>foo **bar</em> <code>#</code>*</a></p>
    
    Example 519 (lines 7902-7906) Links
    [![moon](moon.jpg)](/uri)
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><a href="/uri"><img alt="moon" src="moon.jpg"></a></p>
    +<p><a href="/uri">![moon](moon.jpg)</a></p>
    
    Example 520 (lines 7911-7915) Links
    [foo [bar](/uri)](/uri)
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>[foo <a href="/uri">bar</a>](/uri)</p>
    +<p><a href="/uri">foo [bar](/uri)</a></p>
    
    Example 521 (lines 7918-7922) Links
    [foo *[bar [baz](/uri)](/uri)*](/uri)
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>[foo <em>[bar <a href="/uri">baz</a>](/uri)</em>](/uri)</p>
    +<p><a href="/uri">foo <em>[bar [baz](/uri)](/uri)</em></a></p>
    
    Example 522 (lines 7925-7929) Links
    ![[[foo](uri1)](uri2)](uri3)
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><img alt="[foo](uri2)" src="uri3"></p>
    +<p>![<a href="uri2">[foo](uri1)</a>](uri3)</p>
    
    Example 528 (lines 7976-7980) Links
    [foo<https://example.com/?search=](uri)>
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>[foo<a href="https://example.com/?search=%5D(uri)">https://example.com/?search=](uri)</a></p>
    +<p><a href="uri">foo&lt;https://example.com/?search=</a>&gt;</p>
    
    Example 532 (lines 8049-8055) Links
    [link *foo **bar** `#`*][ref]
    
    [ref]: /uri
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><a href="/uri">link <em>foo <strong>bar</strong> <code>#</code></em></a></p>
    +<p><a href="/uri">link <em>foo **bar</em> <code>#</code>*</a></p>
    
    Example 533 (lines 8058-8064) Links
    [![moon](moon.jpg)][ref]
    
    [ref]: /uri
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><a href="/uri"><img alt="moon" src="moon.jpg"></a></p>
    +<p><a href="/uri">![moon](moon.jpg)</a></p>
    
    Example 534 (lines 8069-8075) Links
    [foo [bar](/uri)][ref]
    
    [ref]: /uri
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>[foo <a href="/uri">bar</a>]<a href="/uri">ref</a></p>
    +<p><a href="/uri">foo [bar](/uri)</a></p>
    
    Example 535 (lines 8078-8084) Links
    [foo *bar [baz][ref]*][ref]
    
    [ref]: /uri
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>[foo <em>bar <a href="/uri">baz</a></em>]<a href="/uri">ref</a></p>
    +<p><a href="/uri">foo <em>bar [baz][ref]</em></a></p>
    
    Example 540 (lines 8132-8138) Links
    [foo<https://example.com/?search=][ref]>
    
    [ref]: /uri
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>[foo<a href="https://example.com/?search=%5D%5Bref%5D">https://example.com/?search=][ref]</a></p>
    +<p><a href="/uri">foo&lt;https://example.com/?search=</a>&gt;</p>
    
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
    
    Example 551 (lines 8286-8292) Links
    [foo][ref\[]
    
    [ref\[]: /uri
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><a href="/uri">foo</a></p>
    +<p>[foo][ref[]</p><p>[ref[]: /uri</p>
    
    Example 552 (lines 8297-8303) Links
    [bar\\]: /uri
    
    [bar\\]
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><a href="/uri">bar\</a></p>
    +<p>[bar\]</p>
    
    Example 577 (lines 8589-8593) Images
    ![foo [bar](/url)](/url2)
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><img alt="foo bar" src="/url2"></p>
    +<p>![foo <a href="/url">bar</a>](/url2)</p>
    
    Example 579 (lines 8612-8618) Images
    ![foo *bar*][foobar]
    
    [FOOBAR]: train.jpg "train & tracks"
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><img alt="foo bar" src="train.jpg" title="train &amp; tracks"></p>
    +<p>![foo <em>bar</em>]<a href="train.jpg" title="train &amp; tracks">foobar</a></p>
    
    Example 582 (lines 8635-8639) Images
    ![foo](<url>)
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><img alt="foo" src="url"></p>
    +<p>![foo](<url>)</p>
    
    Example 584 (lines 8651-8657) Images
    ![foo][bar]
    
    [bar]: /url
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><img alt="foo" src="/url"></p>
    +<p>![foo]<a href="/url">bar</a></p>
    
    Example 585 (lines 8660-8666) Images
    ![foo][bar]
    
    [BAR]: /url
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><img alt="foo" src="/url"></p>
    +<p>![foo]<a href="/url">bar</a></p>
    
    Example 595 (lines 8772-8778) Images
    \![foo]
    
    [foo]: /url "title"
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>!<a href="/url" title="title">foo</a></p>
    +<p>\<img alt="foo" src="/url" title="title"></p>
    
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
    
    Example 631 (lines 9197-9201) Raw HTML
    foo <![CDATA[>&<]]>
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>foo <![CDATA[>&<]]></p>
    +<p>foo <![CDATA[>&amp;&lt;]]&gt;</p>
    
    Example 634 (lines 9223-9227) Raw HTML
    <a href="\"">
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>&lt;a href=&quot;&quot;&quot;&gt;</p>
    +<a " href="\"> 
    
    Example 641 (lines 9306-9312) Hard line breaks
    *foo  
    bar*
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><em>foo<br>bar</em></p>
    +<p>*foo<br>bar*</p>
    
    Example 642 (lines 9315-9321) Hard line breaks
    *foo\
    bar*
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><em>foo<br>bar</em></p>
    +<p>*foo<br>bar*</p>
    
    273 passed, 83 failed, 0 errored, 299 skipped
  stderr:
    --- drydock: progress ---
    cases: pass=273 fail=83 error=0 skip=299 total=655 from=result.stdout
    --- drydock: end progress ---
    --- drydock: values at failure ---
      result = CompletedProcess(args=['/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/.venv/bin/python', 'sources/spec_tests.py', '--program', '/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/commonmark', '--spec', 'sources/spec.txt', '--pattern', '^(Backslash escapes|Entity and numeric character references|Code spans|Emphasis and… (+17815 chars)
    --- drydock: end values ---
    Traceback (most recent call last):
      File "conformance-inlines.py", line 12, in <module>
        assert result.returncode == 0
               ^^^^^^^^^^^^^^^^^^^^^^
    AssertionError

## Repair attempts
- attempt 0 (initial build): failed; 0/4 checks; 455/654 cases model=gpt-6-luna; execution 20261027.214041.152Z-e0b02b41; reason: programmatic acceptance failed: conformance-preliminaries, conformance-blocks, conformance-containers, conformance-inlines
- attempt 1 (repair 1): failed; 0/4 checks; 457/654 cases model=gpt-6-luna; execution 20261027.215141.573Z-12306cc0; reason: programmatic acceptance failed: conformance-preliminaries, conformance-blocks, conformance-containers, conformance-inlines
- attempt 2 (repair 2): failed; 0/4 checks; 458/654 cases model=gpt-6-luna; execution 20261027.215758.604Z-9b352a29; reason: programmatic acceptance failed: conformance-preliminaries, conformance-blocks, conformance-containers, conformance-inlines
- attempt 3 (repair 3): failed; 0/4 checks; 459/654 cases model=gpt-6-luna; execution 20261027.220435.183Z-10a1b99b; reason: programmatic acceptance failed: conformance-preliminaries, conformance-blocks, conformance-containers, conformance-inlines
- attempt 4 (repair 4): failed; 1/4 checks; 460/654 cases model=gpt-6-luna; execution 20261027.221052.921Z-c2aa11a1; reason: programmatic acceptance failed: conformance-blocks, conformance-containers, conformance-inlines
- attempt 5 (repair 5): failed; 1/4 checks; 462/654 cases model=gpt-6-luna; execution 20261027.221721.508Z-00266f46; reason: programmatic acceptance failed: conformance-blocks, conformance-containers, conformance-inlines
- attempt 6 (repair 6): failed; 1/4 checks; 478/654 cases model=gpt-6-luna; execution 20261027.222333.407Z-bb94d2af; reason: programmatic acceptance failed: conformance-blocks, conformance-containers, conformance-inlines
- attempt 7 (repair 7): failed; 1/4 checks; 481/654 cases model=gpt-6-luna; execution 20261027.223003.829Z-584b4ebc; reason: programmatic acceptance failed: conformance-blocks, conformance-containers, conformance-inlines
- attempt 8 (repair 8): failed; 1/4 checks; 485/654 cases model=gpt-6-luna; execution 20261027.223755.609Z-1ffd60d1; reason: programmatic acceptance failed: conformance-blocks, conformance-containers, conformance-inlines
- attempt 9 (repair 9): failed; 1/4 checks; 486/654 cases model=gpt-6-luna; execution 20261027.224405.804Z-d128a5ec; reason: programmatic acceptance failed: conformance-blocks, conformance-containers, conformance-inlines
- attempt 10 (repair 10): failed; 1/4 checks; 487/654 cases model=gpt-6-luna; execution 20261027.225013.563Z-275e7bc1; reason: programmatic acceptance failed: conformance-blocks, conformance-containers, conformance-inlines
- attempt 11 (repair 11): failed; 1/4 checks; 491/654 cases model=gpt-6-luna; execution 20261027.225636.219Z-4495cc75; reason: programmatic acceptance failed: conformance-blocks, conformance-containers, conformance-inlines
- attempt 12 (repair 12): failed; 1/4 checks; 503/654 cases model=gpt-6-luna; execution 20261027.230244.943Z-668c9082; reason: programmatic acceptance failed: conformance-blocks, conformance-containers, conformance-inlines
- attempt 13 (repair 13): failed; 1/4 checks; 514/654 cases model=gpt-6-luna; execution 20261027.230841.955Z-f5e414d2; reason: programmatic acceptance failed: conformance-blocks, conformance-containers, conformance-inlines
- attempt 14 (repair 14): failed; 1/4 checks; 516/654 cases model=gpt-6-luna; execution 20261027.231816.873Z-3a7606a2; reason: programmatic acceptance failed: conformance-blocks, conformance-containers, conformance-inlines
- attempt 15 (repair 15): failed; 1/4 checks; 533/654 cases model=gpt-6-luna; execution 20261027.232420.880Z-86d4b0ae; reason: programmatic acceptance failed: conformance-blocks, conformance-containers, conformance-inlines
- attempt 16 (repair 16): failed; 2/4 checks; 561/654 cases model=gpt-6-luna; execution 20261027.233350.892Z-9ef6a2c5; reason: programmatic acceptance failed: conformance-blocks, conformance-inlines
- attempt 17 (repair 17): failed; 1/4 checks; 561/654 cases model=gpt-6-luna; execution 20261027.235013.184Z-ad447d68; reason: programmatic acceptance failed: conformance-blocks, conformance-containers, conformance-inlines
- attempt 18 (repair 18): failed; 2/4 checks; 562/654 cases model=gpt-6-luna; execution 20261027.235859.179Z-e95527d0; reason: programmatic acceptance failed: conformance-blocks, conformance-inlines
- attempt 19 (repair 19): failed; 2/4 checks; 565/654 cases model=gpt-6-luna; execution 20261028.000242.550Z-037c88aa; reason: programmatic acceptance failed: conformance-blocks, conformance-inlines
- attempt 20 (repair 20): failed; 2/4 checks; 567/654 cases model=gpt-6-luna; execution 20261028.000834.048Z-36ed2d30; reason: programmatic acceptance failed: conformance-blocks, conformance-inlines
- attempt 21 (repair 21): failed; 2/4 checks; 568/654 cases model=gpt-6-luna; execution 20261028.001809.125Z-549378e5; reason: programmatic acceptance failed: conformance-blocks, conformance-inlines

## Agent self-report (advisory)
The build agent declared a failure. This report is advisory; Drydock's execution and deterministic checks determine the block's outcome.
- summary: Scoped CommonMark conformance remains incomplete
- detail:
    The symbol-flanking fix resolves example 356, but the existing inline delimiter and reference parsing implementations still fail other staged examples. Repair those parser paths and rerun the affected scoped selectors before retrying this block.

## Failure
- summary: programmatic acceptance failed: conformance-blocks, conformance-inlines
- detail:
    Block "Block 13 · Service" [block-13] failed its acceptance criteria.
      Story "Exercise all scoped CommonMark examples against the integrated parser." [conformance-integration] does not meet its own acceptance criteria:
        - AC conformance-blocks — The integrated parser passes every example in the supplied leaf block sections.
            assertion: assert result.returncode == 0 → AssertionError
            cases: pass=184 fail=3 error=0 skip=468 total=655 from=result.stdout
            raised at: conformance-blocks.py:12
            process exit code: 1
            values at failure:
              result = CompletedProcess(args=['/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/.venv/bin/python', 'sources/spec_tests.py', '--program', '/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/commonmark', '--spec', 'sources/spec.txt', '--pattern', '^(Thematic breaks|ATX headings|Setext headings|Indented code blocks|Fenced code blo… (+937 chars)
            observed output:
              +<p>title line1 line2 '</p><p><a href="/url" title="">foo</a></p>
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
              184 passed, 3 failed, 0 errored, 468 skipped
              … 23 earlier line(s) omitted, --full for all
            check stderr:
              Traceback (most recent call last):
                File "conformance-blocks.py", line 12, in <module>
                  assert result.returncode == 0
                         ^^^^^^^^^^^^^^^^^^^^^^
              AssertionError
        - AC conformance-inlines — The integrated parser passes every example in the supplied inline and text sections.
            assertion: assert result.returncode == 0 → AssertionError
            cases: pass=273 fail=83 error=0 skip=299 total=655 from=result.stdout
            raised at: conformance-inlines.py:12
            process exit code: 1
            values at failure:
              result = CompletedProcess(args=['/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/.venv/bin/python', 'sources/spec_tests.py', '--program', '/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.211306/build/commonmark/commonmark', '--spec', 'sources/spec.txt', '--pattern', '^(Backslash escapes|Entity and numeric character references|Code spans|Emphasis and… (+17815 chars)
            observed output:
              @@ -1 +1 @@
              -<p><em>foo<br>bar</em></p>
              +<p>*foo<br>bar*</p>
              Example 642 (lines 9315-9321) Hard line breaks
              *foo\
              bar*
              --- expected HTML
              +++ actual HTML
              @@ -1 +1 @@
              -<p><em>foo<br>bar</em></p>
              +<p>*foo<br>bar*</p>
              273 passed, 83 failed, 0 errored, 299 skipped
              … 592 earlier line(s) omitted, --full for all
            check stderr:
              Traceback (most recent call last):
                File "conformance-inlines.py", line 12, in <module>
                  assert result.returncode == 0
                         ^^^^^^^^^^^^^^^^^^^^^^
              AssertionError

## Build summary
RESULT: FAILED

FILES CHANGED:
- commonmark_parser/inlines.py
- tests/test_inline_providers.py

SUMMARY:
Fixed Unicode symbol flanking for emphasis and added a regression for the representative currency symbol case. The focused regression and conformance examples 356 and 357 pass; `pytest -q` passes (103 tests).

BLOCKERS:
- The saved failures show broader unresolved reference definition, delimiter, link, image, and HTML parsing failures. The focused emphasis section still fails on other examples; the declared conformance checks are not yet satisfied.

FAILURE_SUMMARY: Scoped CommonMark conformance remains incomplete
FAILURE_DETAIL: The symbol-flanking fix resolves example 356, but the existing inline delimiter and reference parsing implementations still fail other staged examples. Repair those parser paths and rerun the affected scoped selectors before retrying this block.
