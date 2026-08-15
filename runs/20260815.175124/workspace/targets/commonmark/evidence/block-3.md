# Evidence: Block 3 · Service (block-3)

- block type: block
- date: 2026-08-15
- resulting state: closed/verified
- story points (combined assembled cost): 59964
- execution id: 20260815.181303.870Z-771c26e6

## Stories built
- Parse CommonMark leaf blocks and render their structural content. (block-leaves) [story]

## Stacked context
- compass: COMPASS.md (SP 1237)
- implements: FEATURE-Block-Leaves.md (SP 682)
- context: spec.txt (SP 51527)
- context: spec_tests.py (SP 1609)
- context: cmark.py (SP 339)
- context: normalize.py (SP 1631)
- context: ARCHITECTURE_compact.md (SP 124)
- stack: common_compact.md (SP 1179)
- stack: python_compact.md (SP 1534)

## Build directory changes
- blocks.py
- renderer.py

## Pre-build acceptance observation
- RED: block-leaves-basic (FEATURE-Block-Leaves.md)
  intent: The implementation passes thematic-break, ATX-heading, and setext-heading conformance sections.
  return code: 1
  stdout:
    Example 44 (lines 892-896) Thematic breaks
    +++
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>+++</p>
    +<ul><li><ul><li><ul><li></li></ul></li></ul></li></ul>
    
    Example 46 (lines 908-916) Thematic breaks
    --
    **
    __
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>-- ** __</p>
    +<ul><li><ul><li></li></ul></li></ul><ul><li><ul><li>__</li></ul></li></ul>
    
    Example 48 (lines 934-939) Thematic breaks
        ***
    
    --- expected HTML
    +++ actual HTML
    @@ -1,2 +1 @@
    -<pre><code>***
    -</code></pre>
    +<hr>
    
    Example 49 (lines 942-948) Thematic breaks
    Foo
        ***
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>Foo ***</p>
    +<p>Foo</p><hr>
    
    Example 55 (lines 994-1004) Thematic breaks
    _ _ _ _ a
    
    a------
    
    ---a---
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>_ _ _ _ a</p><p>a------</p><p>---a---</p>
    +<p>_ _ _ _ a</p><p>a------</p><ul><li><ul><li><ul><li>a---</li></ul></li></ul></li></ul>
    
    Example 56 (lines 1010-1014) Thematic breaks
     *-*
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><em>-</em></p>
    +<ul><li><ul><li><ul><li></li></ul></li></ul></li></ul>
    
    Example 59 (lines 1053-1060) Thematic breaks
    Foo
    ---
    bar
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<h2>Foo</h2><p>bar</p>
    +<p>Foo</p><hr><p>bar</p>
    
    Example 60 (lines 1066-1078) Thematic breaks
    * Foo
    * * *
    * Bar
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<ul><li>Foo</li></ul><hr><ul><li>Bar</li></ul>
    +<ul><li>Foo</li><li><hr></li><li>Bar</li></ul>
    
    Example 65 (lines 1158-1162) ATX headings
    \## foo
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>## foo</p>
    +<p>\## foo</p>
    
    Example 66 (lines 1167-1171) ATX headings
    # foo *bar* \*baz\*
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<h1>foo <em>bar</em> *baz*</h1>
    +<h1>foo *bar* \*baz\*</h1>
    
    Example 71 (lines 1217-1223) ATX headings
    ## foo ##
      ###   bar    ###
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<h2>foo</h2><h3>bar</h3>
    +<h2>foo ##</h2><h3>bar ###</h3>
    
    Example 72 (lines 1228-1234) ATX headings
    # foo ##################################
    ##### foo ##
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<h1>foo</h1><h5>foo</h5>
    +<h1>foo ##################################</h1><h5>foo ##</h5>
    
    Example 73 (lines 1239-1243) ATX headings
    ### foo ###     
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<h3>foo</h3>
    +<h3>foo ###</h3>
    
    Example 76 (lines 1269-1277) ATX headings
    ### foo \###
    ## foo #\##
    # foo \#
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<h3>foo ###</h3><h2>foo ###</h2><h1>foo #</h1>
    +<h3>foo \###</h3><h2>foo #\##</h2><h1>foo \#</h1>
    
    Example 79 (lines 1307-1315) ATX headings
    ## 
    #
    ### ###
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<h2></h2><h1></h1><h3></h3>
    +<h2></h2><h1></h1><h3>###</h3>
    
    Example 80 (lines 1347-1356) Setext headings
    Foo *bar*
    =========
    
    Foo *bar*
    ---------
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<h1>Foo <em>bar</em></h1><h2>Foo <em>bar</em></h2>
    +<p>Foo *bar* =========</p><p>Foo *bar*</p><hr>
    
    Example 81 (lines 1361-1368) Setext headings
    Foo *bar
    baz*
    ====
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<h1>Foo <em>bar baz</em></h1>
    +<p>Foo *bar baz* ====</p>
    
    Example 82 (lines 1375-1382) Setext headings
      Foo *bar
    baz*	
    ====
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<h1>Foo <em>bar baz</em></h1>
    +<p>Foo *bar baz* ====</p>
    
    Example 83 (lines 1387-1396) Setext headings
    Foo
    -------------------------
    
    Foo
    =
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<h2>Foo</h2><h1>Foo</h1>
    +<p>Foo</p><hr><p>Foo =</p>
    
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
    +<p>Foo</p><hr><p>Foo</p><hr><p>Foo ===</p>
    
    Example 86 (lines 1439-1444) Setext headings
    Foo
       ----      
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<h2>Foo</h2>
    +<p>Foo</p><hr>
    
    Example 87 (lines 1449-1455) Setext headings
    Foo
        ---
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>Foo ---</p>
    +<p>Foo</p><hr>
    
    Example 89 (lines 1476-1481) Setext headings
    Foo  
    -----
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<h2>Foo</h2>
    +<p>Foo</p><hr>
    
    Example 90 (lines 1486-1491) Setext headings
    Foo\
    ----
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<h2>Foo\</h2>
    +<p>Foo\</p><hr>
    
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
    +<p>`Foo</p><hr><p>`</p><p>&lt;a title=&quot;a lot</p><hr><p>of dashes&quot;/&gt;</p>
    
    Example 93 (lines 1527-1537) Setext headings
    > foo
    bar
    ===
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<blockquote><p>foo bar ===</p></blockquote>
    +<blockquote><p>foo</p></blockquote><p>bar ===</p>
    
    Example 94 (lines 1540-1548) Setext headings
    - Foo
    ---
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<ul><li>Foo</li></ul><hr>
    +<ul><li>Foo</li><li><ul><li><ul><li></li></ul></li></ul></li></ul>
    
    Example 95 (lines 1555-1562) Setext headings
    Foo
    Bar
    ---
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<h2>Foo Bar</h2>
    +<p>Foo Bar</p><hr>
    
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
    +<hr><p>Foo</p><hr><p>Bar</p><hr><p>Baz</p>
    
    Example 99 (lines 1606-1614) Setext headings
    - foo
    -----
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<ul><li>foo</li></ul><hr>
    +<ul><li>foo</li><li><hr></li></ul>
    
    Example 102 (lines 1641-1646) Setext headings
    \> foo
    ------
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<h2>&gt; foo</h2>
    +<p>\&gt; foo</p><hr>
    
    Example 103 (lines 1672-1682) Setext headings
    Foo
    
    bar
    ---
    baz
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>Foo</p><h2>bar</h2><p>baz</p>
    +<p>Foo</p><p>bar</p><hr><p>baz</p>
    
    Example 106 (lines 1721-1731) Setext headings
    Foo
    bar
    \---
    baz
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>Foo bar --- baz</p>
    +<p>Foo bar \--- baz</p>
    
    31 passed, 33 failed, 0 errored, 591 skipped
  stderr:
    Traceback (most recent call last):
      File "block-leaves-basic.py", line 12, in <module>
        assert result.returncode == 0
               ^^^^^^^^^^^^^^^^^^^^^^
    AssertionError
- RED: block-leaves-code (FEATURE-Block-Leaves.md)
  intent: The implementation passes indented-code and fenced-code conformance sections.
  return code: 1
  stdout:
    Example 109 (lines 1777-1790) Indented code blocks
    1.  foo
    
        - bar
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<ol><li><p>foo</p><ul><li>bar</li></ul></li></ol>
    +<ol><li><ul><li>bar</li></ul></li></ol>
    
    Example 115 (lines 1878-1893) Indented code blocks
    # Heading
        foo
    Heading
    ------
        foo
    ----
    
    --- expected HTML
    +++ actual HTML
    @@ -1,3 +1,3 @@
     <h1>Heading</h1><pre><code>foo
    -</code></pre><h2>Heading</h2><pre><code>foo
    +</code></pre><p>Heading</p><hr><pre><code>foo
     </code></pre><hr>
    
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
    +<p>``` &lt; &gt; ```</p>
    
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
    +<p>~~~ &lt; &gt; ~~~</p>
    
    Example 121 (lines 2007-2013) Fenced code blocks
    ``
    foo
    ``
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><code>foo</code></p>
    +<p>`` foo ``</p>
    
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
    +<p>``` aaa ~~~ ```</p>
    
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
    +<p>~~~ aaa ``` ~~~</p>
    
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
    +<p>```` aaa ``` ``````</p>
    
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
    +<p>~~~~ aaa ~~~ ~~~~</p>
    
    Example 126 (lines 2071-2075) Fenced code blocks
    ```
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<pre><code></code></pre>
    +<p>```</p>
    
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
    +<p>`````</p><p>``` aaa</p>
    
    Example 128 (lines 2091-2102) Fenced code blocks
    > ```
    > aaa
    
    bbb
    
    --- expected HTML
    +++ actual HTML
    @@ -1,2 +1 @@
    -<blockquote><pre><code>aaa
    -</code></pre></blockquote><p>bbb</p>
    +<blockquote><p>``` aaa</p></blockquote><p>bbb</p>
    
    Example 129 (lines 2107-2116) Fenced code blocks
    ```
    
      
    ```
    
    --- expected HTML
    +++ actual HTML
    @@ -1,3 +1 @@
    -<pre><code>
    -  
    -</code></pre>
    +<p>```</p><p>```</p>
    
    Example 130 (lines 2121-2126) Fenced code blocks
    ```
    ```
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<pre><code></code></pre>
    +<p>``` ```</p>
    
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
    +<p>``` aaa aaa ```</p>
    
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
    +<p>``` aaa aaa aaa ```</p>
    
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
    +<p>``` aaa aaa aaa ```</p>
    
    Example 135 (lines 2190-2197) Fenced code blocks
    ```
    aaa
      ```
    
    --- expected HTML
    +++ actual HTML
    @@ -1,2 +1 @@
    -<pre><code>aaa
    -</code></pre>
    +<p>``` aaa ```</p>
    
    Example 136 (lines 2200-2207) Fenced code blocks
       ```
    aaa
      ```
    
    --- expected HTML
    +++ actual HTML
    @@ -1,2 +1 @@
    -<pre><code>aaa
    -</code></pre>
    +<p>``` aaa ```</p>
    
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
    +<p>``` aaa ```</p>
    
    Example 138 (lines 2226-2232) Fenced code blocks
    ``` ```
    aaa
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><code> </code> aaa</p>
    +<p>``` ``` aaa</p>
    
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
    +<p>~~~~~~ aaa ~~~ ~~</p>
    
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
    +<p>foo ``` bar ``` baz</p>
    
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
    +<p>foo</p><hr><p>~~~ bar ~~~</p><h1>baz</h1>
    
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
    +<p>```ruby def foo(x) return 3 end ```</p>
    
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
    +<p>~~~~ ruby startline=3 $%@#$ def foo(x) return 3 end ~~~~~~~</p>
    
    Example 144 (lines 2316-2321) Fenced code blocks
    ````;
    ````
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<pre><code class="language-;"></code></pre>
    +<p>````; ````</p>
    
    Example 145 (lines 2326-2332) Fenced code blocks
    ``` aa ```
    foo
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><code>aa</code> foo</p>
    +<p>``` aa ``` foo</p>
    
    Example 146 (lines 2337-2344) Fenced code blocks
    ~~~ aa ``` ~~~
    foo
    ~~~
    
    --- expected HTML
    +++ actual HTML
    @@ -1,2 +1 @@
    -<pre><code class="language-aa">foo
    -</code></pre>
    +<p>~~~ aa ``` ~~~ foo ~~~</p>
    
    Example 147 (lines 2349-2356) Fenced code blocks
    ```
    ``` aaa
    ```
    
    --- expected HTML
    +++ actual HTML
    @@ -1,2 +1 @@
    -<pre><code>``` aaa
    -</code></pre>
    +<p>``` ``` aaa ```</p>
    
    11 passed, 30 failed, 0 errored, 614 skipped
  stderr:
    Traceback (most recent call last):
      File "block-leaves-code.py", line 12, in <module>
        assert result.returncode == 0
               ^^^^^^^^^^^^^^^^^^^^^^
    AssertionError
- RED: block-leaves-html (FEATURE-Block-Leaves.md)
  intent: The implementation passes the complete HTML-block conformance section.
  return code: 1
  stdout:
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
    +<p>&lt;table&gt;&lt;tr&gt;&lt;td&gt; &lt;pre&gt;</p><ul><li><ul><li><p>Hello**,</p><p>_world_. &lt;/pre&gt; &lt;/td&gt;&lt;/tr&gt;&lt;/table&gt;</p></li></ul></li></ul>
    
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
    +<p>&lt;table&gt; &lt;tr&gt; &lt;td&gt; hi &lt;/td&gt; &lt;/tr&gt; &lt;/table&gt;</p><p>okay.</p>
    
    Example 150 (lines 2480-2488) HTML blocks
     <div>
      *hello*
             <foo><a>
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<div>*hello* <foo><a> 
    +<p>&lt;div&gt;</p><ul><li>hello* &lt;foo&gt;&lt;a&gt;</li></ul>
    
    Example 151 (lines 2493-2499) HTML blocks
    </div>
    *foo*
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -</div>*foo*
    +<p>&lt;/div&gt;</p><ul><li>foo*</li></ul>
    
    Example 152 (lines 2504-2514) HTML blocks
    <DIV CLASS="foo">
    
    *Markdown*
    
    </DIV>
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<div class="foo"><p><em>Markdown</em></p></div>
    +<p>&lt;DIV CLASS=&quot;foo&quot;&gt;</p><ul><li><p>Markdown*</p><p>&lt;/DIV&gt;</p></li></ul>
    
    Example 153 (lines 2520-2528) HTML blocks
    <div id="foo"
      class="bar">
    </div>
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<div class="bar" id="foo"></div>
    +<p>&lt;div id=&quot;foo&quot; class=&quot;bar&quot;&gt; &lt;/div&gt;</p>
    
    Example 154 (lines 2531-2539) HTML blocks
    <div id="foo" class="bar
      baz">
    </div>
    
    --- expected HTML
    +++ actual HTML
    @@ -1,2 +1 @@
    -<div class="bar
    -  baz" id="foo"></div>
    +<p>&lt;div id=&quot;foo&quot; class=&quot;bar baz&quot;&gt; &lt;/div&gt;</p>
    
    Example 155 (lines 2543-2552) HTML blocks
    <div>
    *foo*
    
    *bar*
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<div>*foo*<p><em>bar</em></p>
    +<p>&lt;div&gt;</p><ul><li><p>foo*</p></li><li><p>bar*</p></li></ul>
    
    Example 156 (lines 2559-2565) HTML blocks
    <div id="foo"
    *hi*
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -div id="foo" *hi* 
    +<p>&lt;div id=&quot;foo&quot;</p><ul><li>hi*</li></ul>
    
    Example 157 (lines 2568-2574) HTML blocks
    <div class
    foo
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -div class foo 
    +<p>&lt;div class foo</p>
    
    Example 158 (lines 2580-2586) HTML blocks
    <div *???-&&&-<---
    *foo*
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -div *???-&&&---- *foo* 
    +<p>&lt;div *???-&amp;&amp;&amp;-&lt;---</p><ul><li>foo*</li></ul>
    
    Example 159 (lines 2592-2596) HTML blocks
    <div><a href="bar">*foo*</a></div>
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<div><a href="bar">*foo*</a></div>
    +<p>&lt;div&gt;&lt;a href=&quot;bar&quot;&gt;*foo*&lt;/a&gt;&lt;/div&gt;</p>
    
    Example 160 (lines 2599-2607) HTML blocks
    <table><tr><td>
    foo
    </td></tr></table>
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<table><tr><td>foo</td></tr></table>
    +<p>&lt;table&gt;&lt;tr&gt;&lt;td&gt; foo &lt;/td&gt;&lt;/tr&gt;&lt;/table&gt;</p>
    
    Example 161 (lines 2616-2626) HTML blocks
    <div></div>
    ``` c
    int x = 33;
    ```
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<div></div>``` c int x = 33; ```
    +<p>&lt;div&gt;&lt;/div&gt; ``` c int x = 33; ```</p>
    
    Example 162 (lines 2629-2635) HTML blocks
    <div
    > not quoted text
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<div>not quoted text 
    +<p>&lt;div &gt; not quoted text</p>
    
    Example 163 (lines 2642-2650) HTML blocks
    <a href="foo">
    *bar*
    </a>
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<a href="foo"> *bar* </a> 
    +<p>&lt;a href=&quot;foo&quot;&gt;</p><ul><li>bar* &lt;/a&gt;</li></ul>
    
    Example 164 (lines 2655-2663) HTML blocks
    <Warning>
    *bar*
    </Warning>
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<warning> *bar* </warning> 
    +<p>&lt;Warning&gt;</p><ul><li>bar* &lt;/Warning&gt;</li></ul>
    
    Example 165 (lines 2666-2674) HTML blocks
    <i class="foo">
    *bar*
    </i>
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<i class="foo"> *bar* </i> 
    +<p>&lt;i class=&quot;foo&quot;&gt;</p><ul><li>bar* &lt;/i&gt;</li></ul>
    
    Example 166 (lines 2677-2683) HTML blocks
    </ins>
    *bar*
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -</ins> *bar* 
    +<p>&lt;/ins&gt;</p><ul><li>bar*</li></ul>
    
    Example 167 (lines 2692-2700) HTML blocks
    <del>
    *foo*
    </del>
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<del> *foo* </del> 
    +<p>&lt;del&gt;</p><ul><li>foo* &lt;/del&gt;</li></ul>
    
    Example 168 (lines 2707-2717) HTML blocks
    <del>
    
    *foo*
    
    </del>
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<del><p><em>foo</em></p></del> 
    +<p>&lt;del&gt;</p><ul><li><p>foo*</p><p>&lt;/del&gt;</p></li></ul>
    
    Example 169 (lines 2725-2729) HTML blocks
    <del>*foo*</del>
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><del><em>foo</em></del></p>
    +<p>&lt;del&gt;*foo*&lt;/del&gt;</p>
    
    Example 170 (lines 2731-2741) HTML blocks
    <del
    class="foo">
    *foo*
    </del>
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><del class="foo"> <em>foo</em> </del></p>
    +<p>&lt;del class=&quot;foo&quot;&gt;</p><ul><li>foo* &lt;/del&gt;</li></ul>
    
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
    -
    -main :: IO ()
    -main = print $ parseTags tags
    -</code></pre><p>okay</p>
    +<p>&lt;pre language=&quot;haskell&quot;&gt;&lt;code&gt; import Text.HTML.TagSoup</p><p>main :: IO () main = print $ parseTags tags &lt;/code&gt;&lt;/pre&gt; okay</p>
    
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
    +<p>&lt;script type=&quot;text/javascript&quot;&gt; // JavaScript example</p><p>document.getElementById(&quot;demo&quot;).innerHTML = &quot;Hello JavaScript!&quot;; &lt;/script&gt; okay</p>
    
    Example 173 (lines 2793-2809) HTML blocks
    <textarea>
    
    *foo*
    
    _bar_
    
    </textarea>
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<textarea>*foo* _bar_</textarea>
    +<p>&lt;textarea&gt;</p><ul><li><p>foo*</p><p>_bar_</p><p>&lt;/textarea&gt;</p></li></ul>
    
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
    +<p>&lt;style type=&quot;text/css&quot;&gt; h1 {color:red;}</p><p>p {color:blue;} &lt;/style&gt; okay</p>
    
    Example 175 (lines 2836-2846) HTML blocks
    <style
      type="text/css">
    
    foo
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<style type="text/css">foo 
    +<p>&lt;style type=&quot;text/css&quot;&gt;</p><p>foo</p>
    
    Example 176 (lines 2849-2860) HTML blocks
    > <div>
    > foo
    
    bar
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<blockquote><div>foo</blockquote><p>bar</p>
    +<blockquote><p>&lt;div&gt; foo</p></blockquote><p>bar</p>
    
    Example 177 (lines 2863-2873) HTML blocks
    - <div>
    - foo
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<ul><li><div></li><li>foo</li></ul>
    +<ul><li>&lt;div&gt;</li><li>foo</li></ul>
    
    Example 178 (lines 2878-2884) HTML blocks
    <style>p{color:red;}</style>
    *foo*
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<style>p{color:red;}</style><p><em>foo</em></p>
    +<p>&lt;style&gt;p{color:red;}&lt;/style&gt;</p><ul><li>foo*</li></ul>
    
    Example 179 (lines 2887-2893) HTML blocks
    <!-- foo -->*bar*
    *baz*
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<!-- foo -->*bar*<p><em>baz</em></p>
    +<p>&lt;!-- foo --&gt;*bar*</p><ul><li>baz*</li></ul>
    
    Example 180 (lines 2899-2907) HTML blocks
    <script>
    foo
    </script>1. *bar*
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<script>foo</script>1. *bar*
    +<p>&lt;script&gt; foo &lt;/script&gt;1. *bar*</p>
    
    Example 181 (lines 2912-2924) HTML blocks
    <!-- Foo
    
    bar
       baz -->
    okay
    
    --- expected HTML
    +++ actual HTML
    @@ -1,4 +1 @@
    -<!-- Foo
    -
    -bar
    -   baz --><p>okay</p>
    +<p>&lt;!-- Foo</p><p>bar baz --&gt; okay</p>
    
    Example 182 (lines 2930-2944) HTML blocks
    <?php
    
      echo '>';
    
    ?>
    okay
    
    --- expected HTML
    +++ actual HTML
    @@ -1,3 +1 @@
    -<?php
    -
    -  echo '>'; ?><p>okay</p>
    +<p>&lt;?php</p><p>echo '&gt;';</p><p>?&gt; okay</p>
    
    Example 183 (lines 2949-2953) HTML blocks
    <!DOCTYPE html>
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<!DOCTYPE html> 
    +<p>&lt;!DOCTYPE html&gt;</p>
    
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
    @@ -1,12 +1,2 @@
    -<![CDATA[
    -function matchwo(a,b)
    -{
    -  if (a < b && a < 0) then {
    -    return 1;
    -
    -  } else {
    -
    -    return 0;
    -  }
    -}
    -]]><p>okay</p>
    +<p>&lt;![CDATA[ function matchwo(a,b) { if (a &lt; b &amp;&amp; a &lt; 0) then { return 1;</p><p>} else {</p><pre><code>return 0;
    +</code></pre><p>} } ]]&gt; okay</p>
    
    Example 185 (lines 2992-3000) HTML blocks
      <!-- foo -->
    
        <!-- foo -->
    
    --- expected HTML
    +++ actual HTML
    @@ -1,2 +1,2 @@
    - <!-- foo --><pre><code>&lt;!-- foo --&gt;
    +<p>&lt;!-- foo --&gt;</p><pre><code>&lt;!-- foo --&gt;
     </code></pre>
    
    Example 186 (lines 3003-3011) HTML blocks
      <div>
    
        <div>
    
    --- expected HTML
    +++ actual HTML
    @@ -1,2 +1,2 @@
    -<div><pre><code>&lt;div&gt;
    +<p>&lt;div&gt;</p><pre><code>&lt;div&gt;
     </code></pre>
    
    Example 187 (lines 3017-3027) HTML blocks
    Foo
    <div>
    bar
    </div>
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>Foo</p><div>bar</div>
    +<p>Foo &lt;div&gt; bar &lt;/div&gt;</p>
    
    Example 188 (lines 3034-3044) HTML blocks
    <div>
    bar
    </div>
    *foo*
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<div>bar</div>*foo*
    +<p>&lt;div&gt; bar &lt;/div&gt;</p><ul><li>foo*</li></ul>
    
    Example 189 (lines 3049-3057) HTML blocks
    Foo
    <a href="bar">
    baz
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>Foo <a href="bar"> baz</p>
    +<p>Foo &lt;a href=&quot;bar&quot;&gt; baz</p>
    
    Example 190 (lines 3090-3100) HTML blocks
    <div>
    
    *Emphasized* text.
    
    </div>
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<div><p><em>Emphasized</em> text.</p></div>
    +<p>&lt;div&gt;</p><ul><li><p>Emphasized* text.</p><p>&lt;/div&gt;</p></li></ul>
    
    Example 191 (lines 3103-3111) HTML blocks
    <div>
    *Emphasized* text.
    </div>
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<div>*Emphasized* text.</div>
    +<p>&lt;div&gt;</p><ul><li>Emphasized* text. &lt;/div&gt;</li></ul>
    
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
    +<p>&lt;table&gt;</p><p>&lt;tr&gt;</p><p>&lt;td&gt; Hi &lt;/td&gt;</p><p>&lt;/tr&gt;</p><p>&lt;/table&gt;</p>
    
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
    @@ -1,4 +1,4 @@
    -<table><tr><pre><code>&lt;td&gt;
    +<p>&lt;table&gt;</p><p>&lt;tr&gt;</p><pre><code>&lt;td&gt;
       Hi
     &lt;/td&gt;
    -</code></pre></tr></table>
    +</code></pre><p>&lt;/tr&gt;</p><p>&lt;/table&gt;</p>
    
    0 passed, 46 failed, 0 errored, 609 skipped
  stderr:
    Traceback (most recent call last):
      File "block-leaves-html.py", line 11, in <module>
        assert result.returncode == 0
               ^^^^^^^^^^^^^^^^^^^^^^
    AssertionError

## Post-build programmatic acceptance
- PASS: block-leaves-basic (FEATURE-Block-Leaves.md)
  intent: The implementation passes thematic-break, ATX-heading, and setext-heading conformance sections.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/.venv/bin/python3
  provisioning: not required
  return code: 0
  stdout:
    64 passed, 0 failed, 0 errored, 591 skipped
- PASS: block-leaves-code (FEATURE-Block-Leaves.md)
  intent: The implementation passes indented-code and fenced-code conformance sections.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/.venv/bin/python3
  provisioning: not required
  return code: 0
  stdout:
    41 passed, 0 failed, 0 errored, 614 skipped
- PASS: block-leaves-html (FEATURE-Block-Leaves.md)
  intent: The implementation passes the complete HTML-block conformance section.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/.venv/bin/python3
  provisioning: not required
  return code: 0
  stdout:
    46 passed, 0 failed, 0 errored, 609 skipped

## Repair attempts
- attempt 0 (initial build): failed; 0/3 checks; 133/151 cases model=gpt-5.6-luna; execution 20260815.180703.199Z-7fd0a843
- attempt 1 (repair 1): built; 3/3 checks; 151/151 cases model=gpt-5.6-luna; execution 20260815.181303.870Z-771c26e6

## Build summary
RESULT: SUCCESS

FILES CHANGED:
- blocks.py
- renderer.py

SUMMARY:
Fixed leaf parsing and rendering for thematic breaks, headings, code fences, indentation, raw HTML, escaping, and inline emphasis.

Scoped conformance checks passed:

- 64/64 leaf heading/thematic-break tests
- 41/41 code-block tests
- 46/46 HTML-block tests

BLOCKERS:
- None
