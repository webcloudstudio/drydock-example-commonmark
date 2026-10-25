# Evidence: Block 2 · Service (block-2)

- block type: block
- date: 2026-10-24
- resulting state: closed/failed
- story points (combined assembled cost): 60024
- execution id: 20261025.034642.361Z-1f8a7ec9

## Stories built
- Parse CommonMark block structure and collect link reference definitions. (block_parsing) [story]
- Parse CommonMark inline syntax and render inline HTML. (inline_parsing) [story]
- Provide the commonmark stdin/stdout executable. (executable) [story]
- Verify the completed parser against the full CommonMark suite. (full_conformance) [story]

## Stacked context
- stack: python_compact.md (SP 601)
- compass: COMPASS.md (SP 462)
- implements: FEATURE-Block-Parsing.md (SP 540)
- context: spec_tests.py (SP 1609)
- context: cmark.py (SP 339)
- context: normalize.py (SP 1631)
- context: spec.txt (SP 51527)
- context: ARCHITECTURE_compact.md (SP 204)
- stack: common_compact.md (SP 1079)
- implements: FEATURE-Inline-Parsing.md (SP 527)
- implements: FEATURE-Executable.md (SP 453)
- implements: VERIFICATION.md (SP 341)
- context: full_test.sh (SP 509)

## Build directory changes
- commonmark
- pyproject.toml
- src/commonmark/__init__.py
- src/commonmark/__main__.py
- src/commonmark/block_parser.py
- src/commonmark/cli.py
- src/commonmark/inline_parser.py
- src/commonmark/model.py
- src/commonmark/parser.py
- src/commonmark/renderer.py
- src/commonmark.egg-info/PKG-INFO
- src/commonmark.egg-info/SOURCES.txt
- src/commonmark.egg-info/dependency_links.txt
- src/commonmark.egg-info/entry_points.txt
- src/commonmark.egg-info/top_level.txt
- tests/test_parser_behavior.py
- commonmark/__init__.py
- commonmark/__main__.py
- commonmark/block_parser.py
- commonmark/cli.py
- commonmark/inline_parser.py
- commonmark/model.py
- commonmark/parser.py
- commonmark/renderer.py

## Pre-build acceptance observation
- RED: block-parsing-conformance (FEATURE-Block-Parsing.md)
  intent: All supplied cases in the block parsing sections pass (the complete block capability slice).
  return code: 1
  stderr:
    Traceback (most recent call last):
      File "/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261025.023211/build/commonmark/sources/spec_tests.py", line 164, in <module>
        result = do_test(test, args.normalize, previous.get(str(test['example'])))
                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
      File "/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261025.023211/build/commonmark/sources/spec_tests.py", line 44, in do_test
        [retcode, actual_html_bytes, err] = cmark.to_html(test['markdown'])
                                            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
      File "/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261025.023211/build/commonmark/sources/cmark.py", line 23, in <lambda>
        self.to_html = lambda x: pipe_through_prog(prog, x)
                                 ^^^^^^^^^^^^^^^^^^^^^^^^^^
      File "/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261025.023211/build/commonmark/sources/cmark.py", line 10, in pipe_through_prog
        p1 = Popen(prog.split(), stdout=PIPE, stdin=PIPE, stderr=PIPE)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
      File "/home/barlo/.local/share/uv/python/cpython-3.12.13-linux-x86_64-gnu/lib/python3.12/subprocess.py", line 1026, in __init__
        self._execute_child(args, executable, preexec_fn, close_fds,
      File "/home/barlo/.local/share/uv/python/cpython-3.12.13-linux-x86_64-gnu/lib/python3.12/subprocess.py", line 1955, in _execute_child
        raise child_exception_type(errno_num, err_msg, err_filename)
    PermissionError: [Errno 13] Permission denied: './commonmark'
    
    --- drydock: values at failure ---
      result = CompletedProcess(args=['/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261025.023211/build/commonmark/.venv/bin/python', 'sources/spec_tests.py', '--program', './commonmark', '--spec', 'sources/spec.txt', '--pattern', 'Thematic breaks|ATX headings|Setext headings|Indented code blocks|Fenced code blocks|HTML blocks|Link reference definitions|Paragraphs|Blank lines|Block quotes|List items… (+1677 chars)
    --- drydock: end values ---
    Traceback (most recent call last):
      File "block-parsing-conformance.py", line 18, in <module>
        assert result.returncode == 0
               ^^^^^^^^^^^^^^^^^^^^^^
    AssertionError
- RED: inline-parsing-conformance (FEATURE-Inline-Parsing.md)
  intent: All supplied cases in the inline parsing sections pass (the complete inline capability slice).
  return code: 1
  stderr:
    Traceback (most recent call last):
      File "/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261025.023211/build/commonmark/sources/spec_tests.py", line 164, in <module>
        result = do_test(test, args.normalize, previous.get(str(test['example'])))
                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
      File "/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261025.023211/build/commonmark/sources/spec_tests.py", line 44, in do_test
        [retcode, actual_html_bytes, err] = cmark.to_html(test['markdown'])
                                            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
      File "/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261025.023211/build/commonmark/sources/cmark.py", line 23, in <lambda>
        self.to_html = lambda x: pipe_through_prog(prog, x)
                                 ^^^^^^^^^^^^^^^^^^^^^^^^^^
      File "/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261025.023211/build/commonmark/sources/cmark.py", line 10, in pipe_through_prog
        p1 = Popen(prog.split(), stdout=PIPE, stdin=PIPE, stderr=PIPE)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
      File "/home/barlo/.local/share/uv/python/cpython-3.12.13-linux-x86_64-gnu/lib/python3.12/subprocess.py", line 1026, in __init__
        self._execute_child(args, executable, preexec_fn, close_fds,
      File "/home/barlo/.local/share/uv/python/cpython-3.12.13-linux-x86_64-gnu/lib/python3.12/subprocess.py", line 1955, in _execute_child
        raise child_exception_type(errno_num, err_msg, err_filename)
    PermissionError: [Errno 13] Permission denied: './commonmark'
    
    --- drydock: values at failure ---
      result = CompletedProcess(args=['/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261025.023211/build/commonmark/.venv/bin/python', 'sources/spec_tests.py', '--program', './commonmark', '--spec', 'sources/spec.txt', '--pattern', 'Backslash escapes|Entity and numeric character references|Code spans|Emphasis and strong emphasis|Links|Images|Autolinks|Raw HTML|Hard line breaks|Soft line breaks|Textua… (+1680 chars)
    --- drydock: end values ---
    Traceback (most recent call last):
      File "inline-parsing-conformance.py", line 18, in <module>
        assert result.returncode == 0
               ^^^^^^^^^^^^^^^^^^^^^^
    AssertionError
- RED: executable-stdin-stdout (FEATURE-Executable.md)
  intent: The root executable accepts Markdown on standard input and emits converted output on standard output.
  return code: 1
  stderr:
    --- drydock: values at failure ---
      errno_num = 13
      err_msg = 'Permission denied'
      err_filename = './commonmark'
    --- drydock: end values ---
    Traceback (most recent call last):
      File "executable-stdin-stdout.py", line 4, in <module>
        result = subprocess.run(
                 ^^^^^^^^^^^^^^^
      File "/home/barlo/.local/share/uv/python/cpython-3.12.13-linux-x86_64-gnu/lib/python3.12/subprocess.py", line 548, in run
        with Popen(*popenargs, **kwargs) as process:
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^
      File "/home/barlo/.local/share/uv/python/cpython-3.12.13-linux-x86_64-gnu/lib/python3.12/subprocess.py", line 1026, in __init__
        self._execute_child(args, executable, preexec_fn, close_fds,
      File "/home/barlo/.local/share/uv/python/cpython-3.12.13-linux-x86_64-gnu/lib/python3.12/subprocess.py", line 1955, in _execute_child
        raise child_exception_type(errno_num, err_msg, err_filename)
    PermissionError: [Errno 13] Permission denied: './commonmark'
- RED: executable-errors (FEATURE-Executable.md)
  intent: Invalid UTF-8 input is reported as an unsuccessful process invocation.
  return code: 1
  stderr:
    --- drydock: values at failure ---
      errno_num = 13
      err_msg = 'Permission denied'
      err_filename = './commonmark'
    --- drydock: end values ---
    Traceback (most recent call last):
      File "executable-errors.py", line 3, in <module>
        result = subprocess.run(
                 ^^^^^^^^^^^^^^^
      File "/home/barlo/.local/share/uv/python/cpython-3.12.13-linux-x86_64-gnu/lib/python3.12/subprocess.py", line 548, in run
        with Popen(*popenargs, **kwargs) as process:
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^
      File "/home/barlo/.local/share/uv/python/cpython-3.12.13-linux-x86_64-gnu/lib/python3.12/subprocess.py", line 1026, in __init__
        self._execute_child(args, executable, preexec_fn, close_fds,
      File "/home/barlo/.local/share/uv/python/cpython-3.12.13-linux-x86_64-gnu/lib/python3.12/subprocess.py", line 1955, in _execute_child
        raise child_exception_type(errno_num, err_msg, err_filename)
    PermissionError: [Errno 13] Permission denied: './commonmark'
- RED: full-commonmark-suite (VERIFICATION.md)
  intent: The supplied full CommonMark conformance suite completes successfully.
  return code: 1
  stdout:
    Traceback (most recent call last):
      File "/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261025.023211/build/commonmark/sources/spec_tests.py", line 164, in <module>
        result = do_test(test, args.normalize, previous.get(str(test['example'])))
                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
      File "/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261025.023211/build/commonmark/sources/spec_tests.py", line 44, in do_test
        [retcode, actual_html_bytes, err] = cmark.to_html(test['markdown'])
                                            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
      File "/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261025.023211/build/commonmark/sources/cmark.py", line 23, in <lambda>
        self.to_html = lambda x: pipe_through_prog(prog, x)
                                 ^^^^^^^^^^^^^^^^^^^^^^^^^^
      File "/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261025.023211/build/commonmark/sources/cmark.py", line 10, in pipe_through_prog
        p1 = Popen(prog.split(), stdout=PIPE, stdin=PIPE, stderr=PIPE)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
      File "/home/barlo/.local/share/uv/python/cpython-3.12.13-linux-x86_64-gnu/lib/python3.12/subprocess.py", line 1026, in __init__
        self._execute_child(args, executable, preexec_fn, close_fds,
      File "/home/barlo/.local/share/uv/python/cpython-3.12.13-linux-x86_64-gnu/lib/python3.12/subprocess.py", line 1955, in _execute_child
        raise child_exception_type(errno_num, err_msg, err_filename)
    PermissionError: [Errno 13] Permission denied: '/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261025.023211/build/commonmark/commonmark'
  stderr:
    --- drydock: values at failure ---
      result = CompletedProcess(args=['sh', 'sources/full_test.sh'], returncode=1, stdout='Traceback (most recent call last):\n  File "/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261025.023211/build/commonmark/sources/spec_tests.py", line 164, in <module>\n    result = do_test(test, args.normalize, previous.get(str(test[\'example\'])))\n             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^… (+1408 chars)
    --- drydock: end values ---
    Traceback (most recent call last):
      File "full-commonmark-suite.py", line 10, in <module>
        assert result.returncode == 0
               ^^^^^^^^^^^^^^^^^^^^^^
    AssertionError

## Post-build programmatic acceptance
- FAIL: block-parsing-conformance (FEATURE-Block-Parsing.md)
  intent: All supplied cases in the block parsing sections pass (the complete block capability slice).
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261025.023211/build/commonmark/.venv/bin/python
  provisioning: not required
  return code: 1
  stdout:
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
    +<h2>`Foo</h2><p>`</p><h2>&lt;a title="a lot</h2><p>of dashes"/&gt;</p>
    
    Example 93 (lines 1527-1537) Setext headings
    > foo
    bar
    ===
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<blockquote><p>foo bar ===</p></blockquote>
    +<blockquote><p>foo</p></blockquote><h1>bar</h1>
    
    Example 128 (lines 2091-2102) Fenced code blocks
    > ```
    > aaa
    
    bbb
    
    --- expected HTML
    +++ actual HTML
    @@ -1,2 +1,3 @@
     <blockquote><pre><code>aaa
    +
     </code></pre></blockquote><p>bbb</p>
    
    Example 138 (lines 2226-2232) Fenced code blocks
    ``` ```
    aaa
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1,2 @@
    -<p><code> </code> aaa</p>
    +<pre><code class="language-```">aaa
    +</code></pre>
    
    Example 145 (lines 2326-2332) Fenced code blocks
    ``` aa ```
    foo
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1,2 @@
    -<p><code>aa</code> foo</p>
    +<pre><code class="language-aa">foo
    +</code></pre>
    
    Example 168 (lines 2707-2717) HTML blocks
    <del>
    
    *foo*
    
    </del>
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<del><p><em>foo</em></p></del> 
    +<del><p><em>foo</em></p><p></del></p>
    
    Example 195 (lines 3210-3218) Link reference definitions
       [foo]: 
          /url  
               'the title'  
    
    [foo]
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><a href="/url" title="the title">foo</a></p>
    +<p>[foo]: /url<br>'the title'</p><p>[foo]</p>
    
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
    
    Example 203 (lines 3312-3319) Link reference definitions
    [foo]: <bar>(baz)
    
    [foo]
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>[foo]: <bar>(baz)</p><p>[foo]</p>
    +<p><a href="bar%3E(baz">foo</a></p>
    
    Example 204 (lines 3325-3331) Link reference definitions
    [foo]: /url\bar\*baz "foo\"bar\baz"
    
    [foo]
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><a href="/url%5Cbar*baz" title="foo&quot;bar\baz">foo</a></p>
    +<p>[foo]: /url\bar*baz "foo&quot;bar\baz"</p><p>[foo]</p>
    
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
    
    Example 211 (lines 3406-3410) Link reference definitions
    [foo]: /url "title" ok
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>[foo]: /url &quot;title&quot; ok</p>
    +<p>[foo]: /url "title" ok</p>
    
    Example 212 (lines 3415-3420) Link reference definitions
    [foo]: /url
    "title" ok
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>&quot;title&quot; ok</p>
    +<p>"title" ok</p>
    
    Example 213 (lines 3426-3434) Link reference definitions
        [foo]: /url "title"
    
    [foo]
    
    --- expected HTML
    +++ actual HTML
    @@ -1,2 +1,2 @@
    -<pre><code>[foo]: /url &quot;title&quot;
    +<pre><code>[foo]: /url "title"
     </code></pre><p>[foo]</p>
    
    Example 215 (lines 3455-3464) Link reference definitions
    Foo
    [bar]: /baz
    
    [bar]
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>Foo [bar]: /baz</p><p>[bar]</p>
    +<p>Foo</p><p><a href="/baz">bar</a></p>
    
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
    +<p>"bar"</p><p><a href="/foo-url" title="foo">foo</a>, <a href="/bar-url">bar</a>, <a href="/baz-url">baz</a></p>
    
    Example 234 (lines 3782-3792) Block quotes
    > # Foo
    > bar
    baz
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<blockquote><h1>Foo</h1><p>bar baz</p></blockquote>
    +<blockquote><h1>Foo</h1><p>bar</p></blockquote><p>baz</p>
    
    Example 235 (lines 3798-3808) Block quotes
    > bar
    baz
    > foo
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<blockquote><p>bar baz foo</p></blockquote>
    +<blockquote><p>bar</p></blockquote><p>baz</p><blockquote><p>foo</p></blockquote>
    
    Example 240 (lines 3889-3897) Block quotes
    > foo
        - bar
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1,2 @@
    -<blockquote><p>foo - bar</p></blockquote>
    +<blockquote><p>foo</p></blockquote><pre><code>- bar
    +</code></pre>
    
    Example 244 (lines 3946-3957) Block quotes
    > foo
    
    > bar
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<blockquote><p>foo</p></blockquote><blockquote><p>bar</p></blockquote>
    +<blockquote><p>foo</p><p>bar</p></blockquote>
    
    Example 249 (lines 4027-4035) Block quotes
    > bar
    baz
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<blockquote><p>bar baz</p></blockquote>
    +<blockquote><p>bar</p></blockquote><p>baz</p>
    
    Example 252 (lines 4066-4078) Block quotes
    > > > foo
    bar
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<blockquote><blockquote><blockquote><p>foo bar</p></blockquote></blockquote></blockquote>
    +<blockquote><blockquote><blockquote><p>foo</p></blockquote></blockquote></blockquote><p>bar</p>
    
    Example 253 (lines 4081-4095) Block quotes
    >>> foo
    > bar
    >>baz
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<blockquote><blockquote><blockquote><p>foo bar baz</p></blockquote></blockquote></blockquote>
    +<blockquote><blockquote><blockquote><p>foo</p></blockquote></blockquote><p>bar</p><blockquote><p>baz</p></blockquote></blockquote>
    
    Example 254 (lines 4103-4115) Block quotes
    >     code
    
    >    not code
    
    --- expected HTML
    +++ actual HTML
    @@ -1,2 +1,2 @@
     <blockquote><pre><code>code
    -</code></pre></blockquote><blockquote><p>not code</p></blockquote>
    +</code></pre><p>not code</p></blockquote>
    
    Example 259 (lines 4238-4248) List items
     -    one
    
         two
    
    --- expected HTML
    +++ actual HTML
    @@ -1,2 +1 @@
    -<ul><li>one</li></ul><pre><code> two
    -</code></pre>
    +<ul><li><p>one</p><p>two</p></li></ul>
    
    Example 264 (lines 4332-4344) List items
    - foo
    
    
      bar
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<ul><li><p>foo</p><p>bar</p></li></ul>
    +<ul><li>foo</li></ul><p>bar</p>
    
    Example 266 (lines 4377-4395) List items
    - Foo
    
          bar
    
    
          baz
    
    --- expected HTML
    +++ actual HTML
    @@ -1,5 +1,2 @@
    -<ul><li><p>Foo</p><pre><code>bar
    -
    -
    -baz
    -</code></pre></li></ul>
    +<ul><li><p>Foo</p><p>bar</p></li></ul><pre><code>  baz
    +</code></pre>
    
    Example 272 (lines 4460-4472) List items
    - foo
    
          bar
    
    --- expected HTML
    +++ actual HTML
    @@ -1,2 +1 @@
    -<ul><li><p>foo</p><pre><code>bar
    -</code></pre></li></ul>
    +<ul><li><p>foo</p><p>bar</p></li></ul>
    
    Example 273 (lines 4477-4489) List items
      10.  foo
    
               bar
    
    --- expected HTML
    +++ actual HTML
    @@ -1,2 +1,2 @@
    -<ol start="10"><li><p>foo</p><pre><code>bar
    +<ol start="10"><li><p>foo</p><pre><code>   bar
     </code></pre></li></ol>
    
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
    +<ol><li><p>indented code</p><p>paragraph</p><p>more code</p></li></ol>
    
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
    +<ol><li><p>indented code</p><p>paragraph</p><p>more code</p></li></ol>
    
    Example 278 (lines 4570-4579) List items
    -    foo
    
      bar
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<ul><li>foo</li></ul><p>bar</p>
    +<ul><li><p>foo</p><p>bar</p></li></ul>
    
    Example 282 (lines 4654-4663) List items
    -
    
      foo
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<ul><li></li></ul><p>foo</p>
    +<ul><li><p>foo</p></li></ul>
    
    Example 288 (lines 4745-4764) List items
     1.  A paragraph
         with two lines.
    
             indented code
    
         > A block quote.
    
    --- expected HTML
    +++ actual HTML
    @@ -1,2 +1,2 @@
    -<ol><li><p>A paragraph with two lines.</p><pre><code>indented code
    +<ol><li><p>A paragraph with two lines.</p><pre><code> indented code
     </code></pre><blockquote><p>A block quote.</p></blockquote></li></ol>
    
    Example 289 (lines 4769-4788) List items
      1.  A paragraph
          with two lines.
    
              indented code
    
          > A block quote.
    
    --- expected HTML
    +++ actual HTML
    @@ -1,2 +1,2 @@
    -<ol><li><p>A paragraph with two lines.</p><pre><code>indented code
    +<ol><li><p>A paragraph with two lines.</p><pre><code>  indented code
     </code></pre><blockquote><p>A block quote.</p></blockquote></li></ol>
    
    Example 290 (lines 4793-4812) List items
       1.  A paragraph
           with two lines.
    
               indented code
    
           > A block quote.
    
    --- expected HTML
    +++ actual HTML
    @@ -1,2 +1,2 @@
    -<ol><li><p>A paragraph with two lines.</p><pre><code>indented code
    +<ol><li><p>A paragraph with two lines.</p><pre><code>   indented code
     </code></pre><blockquote><p>A block quote.</p></blockquote></li></ol>
    
    Example 292 (lines 4847-4866) List items
      1.  A paragraph
    with two lines.
    
              indented code
    
          > A block quote.
    
    --- expected HTML
    +++ actual HTML
    @@ -1,2 +1,2 @@
    -<ol><li><p>A paragraph with two lines.</p><pre><code>indented code
    +<ol><li><p>A paragraph with two lines.</p><pre><code>  indented code
     </code></pre><blockquote><p>A block quote.</p></blockquote></li></ol>
    
    Example 294 (lines 4884-4898) List items
    > 1. > Blockquote
    continued here.
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<blockquote><ol><li><blockquote><p>Blockquote continued here.</p></blockquote></li></ol></blockquote>
    +<blockquote><ol><li><blockquote><p>Blockquote</p></blockquote></li></ol></blockquote><p>continued here.</p>
    
    Example 295 (lines 4901-4915) List items
    > 1. > Blockquote
    > continued here.
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<blockquote><ol><li><blockquote><p>Blockquote continued here.</p></blockquote></li></ol></blockquote>
    +<blockquote><ol><li><blockquote><p>Blockquote</p></blockquote>continued here.</li></ol></blockquote>
    
    Example 296 (lines 4929-4950) List items
    - foo
      - bar
        - baz
          - boo
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<ul><li>foo<ul><li>bar<ul><li>baz<ul><li>boo</li></ul></li></ul></li></ul></li></ul>
    +<ul><li>foo<ul><li>bar</li><li>baz<ul><li>boo</li></ul></li></ul></li></ul>
    
    Example 297 (lines 4955-4967) List items
    - foo
     - bar
      - baz
       - boo
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<ul><li>foo</li><li>bar</li><li>baz</li><li>boo</li></ul>
    +<ul><li>foo<ul><li>bar</li><li>baz</li><li>boo</li></ul></li></ul>
    
    Example 299 (lines 4988-4998) List items
    10) foo
       - bar
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<ol start="10"><li>foo</li></ol><ul><li>bar</li></ul>
    +<ol start="10"><li>foo<ul><li>bar</li></ul></li></ol>
    
    Example 302 (lines 5035-5049) List items
    - # Foo
    - Bar
      ---
      baz
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<ul><li><h1>Foo</h1></li><li><h2>Bar</h2>baz</li></ul>
    +<ul><li><h1>Foo</h1></li><li>Bar</li></ul><hr><p>baz</p>
    
    Example 308 (lines 5406-5425) Lists
    - foo
    
    - bar
    
    
    - baz
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<ul><li><p>foo</p></li><li><p>bar</p></li><li><p>baz</p></li></ul>
    +<ul><li><p>foo</p></li><li><p>bar</p></li></ul><ul><li>baz</li></ul>
    
    Example 309 (lines 5427-5449) Lists
    - foo
      - bar
        - baz
    
    
          bim
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1,2 @@
    -<ul><li>foo<ul><li>bar<ul><li><p>baz</p><p>bim</p></li></ul></li></ul></li></ul>
    +<ul><li>foo<ul><li>bar</li><li>baz</li></ul></li></ul><pre><code>  bim
    +</code></pre>
    
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
    +<ul><li>a<ul><li>b</li><li>c</li><li>d</li><li>e</li><li>f</li></ul></li><li>g</li></ul>
    
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
    +<ul><li>a<ul><li>b</li><li>c</li><li>d</li><li>e</li></ul></li></ul>
    
    Example 315 (lines 5574-5591) Lists
    1. a
    
      2. b
    
        3. c
    
    --- expected HTML
    +++ actual HTML
    @@ -1,2 +1 @@
    -<ol><li><p>a</p></li><li><p>b</p></li></ol><pre><code>3. c
    -</code></pre>
    +<ol><li><p>a</p></li><li><p>b</p><ol start="3"><li>c</li></ol></li></ol>
    
    Example 320 (lines 5686-5705) Lists
    - a
    - ```
      b
    
    
      ```
    - c
    
    --- expected HTML
    +++ actual HTML
    @@ -1,4 +1,3 @@
     <ul><li>a</li><li><pre><code>b
    -
    -
    -</code></pre></li><li>c</li></ul>
    +</code></pre></li></ul><pre><code>- c
    +</code></pre>
    
    Example 321 (lines 5712-5730) Lists
    - a
      - b
    
        c
    - d
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<ul><li>a<ul><li><p>b</p><p>c</p></li></ul></li><li>d</li></ul>
    +<ul><li><p>a</p><ul><li>b</li></ul><p>c</p></li><li><p>d</p></li></ul>
    
    Example 326 (lines 5805-5819) Lists
    1. ```
       foo
       ```
    
       bar
    
    --- expected HTML
    +++ actual HTML
    @@ -1,2 +1,2 @@
    -<ol><li><pre><code>foo
    +<ol><li><pre><code> foo
     </code></pre><p>bar</p></li></ol>
    
    232 passed, 54 failed, 0 errored, 369 skipped
  stderr:
    --- drydock: progress ---
    cases: pass=232 fail=54 error=0 skip=369 total=655 from=result.stdout
    --- drydock: end progress ---
    --- drydock: values at failure ---
      result = CompletedProcess(args=['/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261025.023211/build/commonmark/.venv/bin/python', 'sources/spec_tests.py', '--program', './commonmark', '--spec', 'sources/spec.txt', '--pattern', 'Thematic breaks|ATX headings|Setext headings|Indented code blocks|Fenced code blocks|HTML blocks|Link reference definitions|Paragraphs|Blank lines|Block quotes|List items… (+14443 chars)
    --- drydock: end values ---
    Traceback (most recent call last):
      File "block-parsing-conformance.py", line 18, in <module>
        assert result.returncode == 0
               ^^^^^^^^^^^^^^^^^^^^^^
    AssertionError
- FAIL: inline-parsing-conformance (FEATURE-Inline-Parsing.md)
  intent: All supplied cases in the inline parsing sections pass (the complete inline capability slice).
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261025.023211/build/commonmark/.venv/bin/python
  provisioning: not required
  return code: 1
  stdout:
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
    +<p>*not emphasized* &lt;br/&gt; not a tag [not a link](/foo) `not code` 1. not a list * not a list # not a heading [foo]: /url "not a reference" &amp;ouml; not a character entity</p>
    
    Example 23 (lines 604-610) Backslash escapes
    [foo]
    
    [foo]: /bar\* "ti\*tle"
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><a href="/bar*" title="ti*tle">foo</a></p>
    +<p><a href="/bar*" title="ti\*tle">foo</a></p>
    
    Example 24 (lines 613-620) Backslash escapes
    ``` foo\+bar
    foo
    ```
    
    --- expected HTML
    +++ actual HTML
    @@ -1,2 +1,2 @@
    -<pre><code class="language-foo+bar">foo
    +<pre><code class="language-foo\+bar">foo
     </code></pre>
    
    Example 34 (lines 751-758) Entity and numeric character references
    ``` f&ouml;&ouml;
    foo
    ```
    
    --- expected HTML
    +++ actual HTML
    @@ -1,2 +1,2 @@
    -<pre><code class="language-föö">foo
    +<pre><code class="language-f&amp;ouml;&amp;ouml;">foo
     </code></pre>
    
    Example 343 (lines 6041-6045) Code spans
    *foo`*`
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>*foo<code>*</code></p>
    +<p><em>foo`</em>`</p>
    
    Example 345 (lines 6060-6064) Code spans
    `<a href="`">`
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><code>&lt;a href=&quot;</code>&quot;&gt;`</p>
    +<p><code>&lt;a href="</code>"&gt;`</p>
    
    Example 349 (lines 6097-6101) Code spans
    ```foo``
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>```foo``</p>
    +<pre><code class="language-foo``"></code></pre>
    
    Example 354 (lines 6351-6355) Emphasis and strong emphasis
    a*"foo"*
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>a*&quot;foo&quot;*</p>
    +<p>a<em>"foo"</em></p>
    
    Example 358 (lines 6394-6398) Emphasis and strong emphasis
    5*6*78
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>5<em>6</em>78</p>
    +<p>5*6*78</p>
    
    Example 361 (lines 6423-6427) Emphasis and strong emphasis
    a_"foo"_
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>a_&quot;foo&quot;_</p>
    +<p>a_"foo"_</p>
    
    Example 365 (lines 6456-6460) Emphasis and strong emphasis
    aa_"bb"_cc
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>aa_&quot;bb&quot;_cc</p>
    +<p>aa_"bb"_cc</p>
    
    Example 371 (lines 6521-6525) Emphasis and strong emphasis
    *(*foo*)*
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><em>(<em>foo</em>)</em></p>
    +<p><em>(*foo</em>)*</p>
    
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
    +<p><em>(_foo</em>)_</p>
    
    Example 382 (lines 6626-6630) Emphasis and strong emphasis
    a**"foo"**
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>a**&quot;foo&quot;**</p>
    +<p>a<strong>"foo"</strong></p>
    
    Example 387 (lines 6674-6678) Emphasis and strong emphasis
    a__"foo"__
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>a__&quot;foo&quot;__</p>
    +<p>a_<em>"foo"</em>_</p>
    
    Example 388 (lines 6683-6687) Emphasis and strong emphasis
    foo__bar__
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>foo__bar__</p>
    +<p>foo_<em>bar</em>_</p>
    
    Example 390 (lines 6697-6701) Emphasis and strong emphasis
    пристаням__стремятся__
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>пристаням__стремятся__</p>
    +<p>пристаням_<em>стремятся</em>_</p>
    
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
    +<p><em>(**foo</em><em>)</em></p>
    
    Example 396 (lines 6758-6764) Emphasis and strong emphasis
    **Gomphocarpus (*Gomphocarpus physocarpus*, syn.
    *Asclepias physocarpa*)**
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><strong>Gomphocarpus (<em>Gomphocarpus physocarpus</em>, syn. <em>Asclepias physocarpa</em>)</strong></p>
    +<p><em>*Gomphocarpus (*Gomphocarpus physocarpus</em>, syn. <em>Asclepias physocarpa</em>)**</p>
    
    Example 397 (lines 6767-6771) Emphasis and strong emphasis
    **foo "*bar*" foo**
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><strong>foo &quot;<em>bar</em>&quot; foo</strong></p>
    +<p><em>*foo "*bar</em>" foo**</p>
    
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
    +<p><em>(__foo</em><em>)</em></p>
    
    Example 408 (lines 6873-6877) Emphasis and strong emphasis
    _foo __bar__ baz_
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><em>foo <strong>bar</strong> baz</em></p>
    +<p><em>foo __bar</em>_ baz_</p>
    
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
    +<p><em>_foo</em> bar_</p>
    
    Example 411 (lines 6894-6898) Emphasis and strong emphasis
    *foo *bar**
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><em>foo <em>bar</em></em></p>
    +<p><em>foo *bar</em>*</p>
    
    Example 412 (lines 6901-6905) Emphasis and strong emphasis
    *foo **bar** baz*
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><em>foo <strong>bar</strong> baz</em></p>
    +<p><em>foo **bar</em>* baz*</p>
    
    Example 413 (lines 6907-6911) Emphasis and strong emphasis
    *foo**bar**baz*
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><em>foo<strong>bar</strong>baz</em></p>
    +<p><em>foo**bar**baz</em></p>
    
    Example 415 (lines 6944-6948) Emphasis and strong emphasis
    ***foo** bar*
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><em><strong>foo</strong> bar</em></p>
    +<p><strong>*foo</strong> bar*</p>
    
    Example 416 (lines 6951-6955) Emphasis and strong emphasis
    *foo **bar***
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><em>foo <strong>bar</strong></em></p>
    +<p><em>foo **bar</em>**</p>
    
    Example 417 (lines 6958-6962) Emphasis and strong emphasis
    *foo**bar***
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><em>foo<strong>bar</strong></em></p>
    +<p><em>foo**bar</em>**</p>
    
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
    +<p><em>foo **bar *baz</em> bim** bop*</p>
    
    Example 421 (lines 6991-6995) Emphasis and strong emphasis
    *foo [*bar*](/url)*
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><em>foo <a href="/url"><em>bar</em></a></em></p>
    +<p><em>foo [*bar</em>](/url)*</p>
    
    Example 426 (lines 7039-7043) Emphasis and strong emphasis
    __foo _bar_ baz__
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><strong>foo <em>bar</em> baz</strong></p>
    +<p><em>_foo _bar</em> baz__</p>
    
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
    +<p><strong>foo **bar</strong>**</p>
    
    Example 430 (lines 7067-7071) Emphasis and strong emphasis
    **foo *bar* baz**
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><strong>foo <em>bar</em> baz</strong></p>
    +<p><em>*foo *bar</em> baz**</p>
    
    Example 431 (lines 7074-7078) Emphasis and strong emphasis
    **foo*bar*baz**
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><strong>foo<em>bar</em>baz</strong></p>
    +<p><strong>foo*bar*baz</strong></p>
    
    Example 432 (lines 7081-7085) Emphasis and strong emphasis
    ***foo* bar**
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><strong><em>foo</em> bar</strong></p>
    +<p><em>**foo</em> bar**</p>
    
    Example 433 (lines 7088-7092) Emphasis and strong emphasis
    **foo *bar***
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><strong>foo <em>bar</em></strong></p>
    +<p><strong>foo *bar</strong>*</p>
    
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
    +<p><em>*foo [*bar</em>](/url)**</p>
    
    Example 444 (lines 7178-7182) Emphasis and strong emphasis
    **foo*
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>*<em>foo</em></p>
    +<p><em>*foo</em></p>
    
    Example 446 (lines 7192-7196) Emphasis and strong emphasis
    ***foo**
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>*<strong>foo</strong></p>
    +<p><strong>*foo</strong></p>
    
    Example 447 (lines 7199-7203) Emphasis and strong emphasis
    ****foo*
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>***<em>foo</em></p>
    +<p><em>***foo</em></p>
    
    Example 456 (lines 7265-7269) Emphasis and strong emphasis
    __foo_
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>_<em>foo</em></p>
    +<p><em>_foo</em></p>
    
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
    +<p><em>___foo</em></p>
    
    Example 466 (lines 7345-7349) Emphasis and strong emphasis
    ****foo****
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><strong><strong>foo</strong></strong></p>
    +<p><strong>**foo</strong>**</p>
    
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
    +<p><strong>****foo</strong>****</p>
    
    Example 469 (lines 7372-7376) Emphasis and strong emphasis
    ***foo***
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><em><strong>foo</strong></em></p>
    +<p><strong>*foo</strong>*</p>
    
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
    +<p><em>[bar</em>](/url)</p>
    
    Example 476 (lines 7427-7431) Emphasis and strong emphasis
    _foo [bar_](/url)
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>_foo <a href="/url">bar_</a></p>
    +<p><em>foo [bar</em>](/url)</p>
    
    Example 477 (lines 7434-7438) Emphasis and strong emphasis
    *<img src="foo" title="*"/>
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>*<img src="foo" title="*"></p>
    +<p><em>&lt;img src="foo" title="</em>"/&gt;</p>
    
    Example 478 (lines 7441-7445) Emphasis and strong emphasis
    **<a href="**">
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>**<a href="**"></p>
    +<p><strong>&lt;a href="</strong>"&gt;</p>
    
    Example 479 (lines 7448-7452) Emphasis and strong emphasis
    __<a href="__">
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>__<a href="__"></p>
    +<p><strong>&lt;a href="</strong>"&gt;</p>
    
    Example 480 (lines 7455-7459) Emphasis and strong emphasis
    *a `*`*
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><em>a <code>*</code></em></p>
    +<p><em>a `</em>`*</p>
    
    Example 481 (lines 7462-7466) Emphasis and strong emphasis
    _a `_`_
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><em>a <code>_</code></em></p>
    +<p><em>a `</em>`_</p>
    
    Example 482 (lines 7469-7473) Emphasis and strong emphasis
    **a<https://foo.bar/?q=**>
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>**a<a href="https://foo.bar/?q=**">https://foo.bar/?q=**</a></p>
    +<p><strong>a&lt;https://foo.bar/?q=</strong>&gt;</p>
    
    Example 483 (lines 7476-7480) Emphasis and strong emphasis
    __a<https://foo.bar/?q=__>
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>__a<a href="https://foo.bar/?q=__">https://foo.bar/?q=__</a></p>
    +<p><strong>a&lt;https://foo.bar/?q=</strong>&gt;</p>
    
    Example 495 (lines 7652-7656) Links
    [link](<foo\>)
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>[link](&lt;foo&gt;)</p>
    +<p><a href="foo%5C">link</a></p>
    
    Example 509 (lines 7801-7805) Links
    [link](/url "title")
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><a href="/url%C2%A0%22title%22">link</a></p>
    +<p>[link](/url "title")</p>
    
    Example 510 (lines 7810-7814) Links
    [link](/url "title "and" title")
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>[link](/url &quot;title &quot;and&quot; title&quot;)</p>
    +<p>[link](/url "title "and" title")</p>
    
    Example 518 (lines 7895-7899) Links
    [link *foo **bar** `#`*](/uri)
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><a href="/uri">link <em>foo <strong>bar</strong> <code>#</code></em></a></p>
    +<p><a href="/uri">link <em>foo **bar</em>* <code>#</code>*</a></p>
    
    Example 520 (lines 7911-7915) Links
    [foo [bar](/uri)](/uri)
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>[foo <a href="/uri">bar</a>](/uri)</p>
    +<p><a href="/uri">foo <a href="/uri">bar</a></a></p>
    
    Example 521 (lines 7918-7922) Links
    [foo *[bar [baz](/uri)](/uri)*](/uri)
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>[foo <em>[bar <a href="/uri">baz</a>](/uri)</em>](/uri)</p>
    +<p><a href="/uri">foo <em><a href="/uri">bar <a href="/uri">baz</a></a></em></a></p>
    
    Example 522 (lines 7925-7929) Links
    ![[[foo](uri1)](uri2)](uri3)
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><img alt="[foo](uri2)" src="uri3"></p>
    +<p><img alt="[[foo](uri1)](uri2)" src="uri3"></p>
    
    Example 523 (lines 7935-7939) Links
    *[foo*](/uri)
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>*<a href="/uri">foo*</a></p>
    +<p><em>[foo</em>](/uri)</p>
    
    Example 526 (lines 7962-7966) Links
    [foo <bar attr="](baz)">
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>[foo <bar attr="](baz)"></p>
    +<p><a href="baz">foo &lt;bar attr="</a>"&gt;</p>
    
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
    +<p><a href="/uri">link <em>foo **bar</em>* <code>#</code>*</a></p>
    
    Example 534 (lines 8069-8075) Links
    [foo [bar](/uri)][ref]
    
    [ref]: /uri
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>[foo <a href="/uri">bar</a>]<a href="/uri">ref</a></p>
    +<p><a href="/uri">foo <a href="/uri">bar</a></a></p>
    
    Example 535 (lines 8078-8084) Links
    [foo *bar [baz][ref]*][ref]
    
    [ref]: /uri
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>[foo <em>bar <a href="/uri">baz</a></em>]<a href="/uri">ref</a></p>
    +<p><a href="/uri">foo <em>bar <a href="/uri">baz</a></em></a></p>
    
    Example 536 (lines 8093-8099) Links
    *[foo*][ref]
    
    [ref]: /uri
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>*<a href="/uri">foo*</a></p>
    +<p><em>[foo</em>]<a href="/uri">ref</a></p>
    
    Example 538 (lines 8114-8120) Links
    [foo <bar attr="][ref]">
    
    [ref]: /uri
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>[foo <bar attr="][ref]"></p>
    +<p><a href="/uri">foo &lt;bar attr="</a>"&gt;</p>
    
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
    
    Example 548 (lines 8256-8263) Links
    [foo][ref[]
    
    [ref[]: /uri
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>[foo][ref[]</p><p>[ref[]: /uri</p>
    +<p>[foo][ref[]</p>
    
    Example 566 (lines 8468-8474) Links
    [foo*]: /url
    
    *[foo*]
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>*<a href="/url">foo*</a></p>
    +<p><em>[foo</em>]</p>
    
    Example 576 (lines 8582-8586) Images
    ![foo ![bar](/url)](/url2)
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><img alt="foo bar" src="/url2"></p>
    +<p><img alt="foo ![bar](/url)" src="/url2"></p>
    
    Example 577 (lines 8589-8593) Images
    ![foo [bar](/url)](/url2)
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><img alt="foo bar" src="/url2"></p>
    +<p><img alt="foo [bar](/url)" src="/url2"></p>
    
    Example 592 (lines 8736-8743) Images
    ![[foo]]
    
    [[foo]]: /url "title"
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>![[foo]]</p><p>[[foo]]: /url &quot;title&quot;</p>
    +<p>![[foo]]</p><p>[[foo]]: /url "title"</p>
    
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
    +<p>&lt;a href="hi'&gt; &lt;a href=hi'&gt;</p>
    
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
    
    259 passed, 97 failed, 0 errored, 299 skipped
  stderr:
    --- drydock: progress ---
    cases: pass=259 fail=97 error=0 skip=299 total=655 from=result.stdout
    --- drydock: end progress ---
    --- drydock: values at failure ---
      result = CompletedProcess(args=['/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261025.023211/build/commonmark/.venv/bin/python', 'sources/spec_tests.py', '--program', './commonmark', '--spec', 'sources/spec.txt', '--pattern', 'Backslash escapes|Entity and numeric character references|Code spans|Emphasis and strong emphasis|Links|Images|Autolinks|Raw HTML|Hard line breaks|Soft line breaks|Textua… (+20991 chars)
    --- drydock: end values ---
    Traceback (most recent call last):
      File "inline-parsing-conformance.py", line 18, in <module>
        assert result.returncode == 0
               ^^^^^^^^^^^^^^^^^^^^^^
    AssertionError
- PASS: executable-stdin-stdout (FEATURE-Executable.md)
  intent: The root executable accepts Markdown on standard input and emits converted output on standard output.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261025.023211/build/commonmark/.venv/bin/python
  provisioning: not required
  return code: 0
- PASS: executable-errors (FEATURE-Executable.md)
  intent: Invalid UTF-8 input is reported as an unsuccessful process invocation.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261025.023211/build/commonmark/.venv/bin/python
  provisioning: not required
  return code: 0
  stdout:
    Traceback (most recent call last):
      File "<frozen runpy>", line 198, in _run_module_as_main
      File "<frozen runpy>", line 88, in _run_code
      File "/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261025.023211/build/commonmark/src/commonmark/cli.py", line 15, in <module>
        raise SystemExit(main())
                         ^^^^^^
      File "/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261025.023211/build/commonmark/src/commonmark/cli.py", line 10, in main
        source = sys.stdin.buffer.read().decode("utf-8")
                 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    UnicodeDecodeError: 'utf-8' codec can't decode byte 0xff in position 0: invalid start byte
- FAIL: full-commonmark-suite (VERIFICATION.md)
  intent: The supplied full CommonMark conformance suite completes successfully.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261025.023211/build/commonmark/.venv/bin/python
  provisioning: not required
  return code: 1
  stdout:
    Example 1 (lines 355-360) Tabs
    	foo	baz		bim
    
    --- expected HTML
    +++ actual HTML
    @@ -1,2 +1 @@
    -<pre><code>foo	baz		bim
    -</code></pre>
    +<p>foo baz bim</p>
    
    Example 2 (lines 362-367) Tabs
      	foo	baz		bim
    
    --- expected HTML
    +++ actual HTML
    @@ -1,2 +1 @@
    -<pre><code>foo	baz		bim
    -</code></pre>
    +<p>foo baz bim</p>
    
    Example 4 (lines 382-393) Tabs
      - foo
    
    	bar
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<ul><li><p>foo</p><p>bar</p></li></ul>
    +<ul><li>foo</li></ul><p>bar</p>
    
    Example 5 (lines 395-407) Tabs
    - foo
    
    		bar
    
    --- expected HTML
    +++ actual HTML
    @@ -1,2 +1 @@
    -<ul><li><p>foo</p><pre><code>  bar
    -</code></pre></li></ul>
    +<ul><li>foo</li></ul><p>bar</p>
    
    Example 6 (lines 418-425) Tabs
    >		foo
    
    --- expected HTML
    +++ actual HTML
    @@ -1,2 +1 @@
    -<blockquote><pre><code>  foo
    -</code></pre></blockquote>
    +<blockquote><p>foo</p></blockquote>
    
    Example 7 (lines 427-436) Tabs
    -		foo
    
    --- expected HTML
    +++ actual HTML
    @@ -1,2 +1 @@
    -<ul><li><pre><code>  foo
    -</code></pre></li></ul>
    +<ul><li>foo</li></ul>
    
    Example 8 (lines 439-446) Tabs
        foo
    	bar
    
    --- expected HTML
    +++ actual HTML
    @@ -1,3 +1,2 @@
     <pre><code>foo
    -bar
    -</code></pre>
    +</code></pre><p>bar</p>
    
    Example 9 (lines 448-464) Tabs
     - foo
       - bar
    	 - baz
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<ul><li>foo<ul><li>bar<ul><li>baz</li></ul></li></ul></li></ul>
    +<ul><li>foo<ul><li>bar - baz</li></ul></li></ul>
    
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
    +<p>*not emphasized* &lt;br/&gt; not a tag [not a link](/foo) `not code` 1. not a list * not a list # not a heading [foo]: /url "not a reference" &amp;ouml; not a character entity</p>
    
    Example 23 (lines 604-610) Backslash escapes
    [foo]
    
    [foo]: /bar\* "ti\*tle"
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><a href="/bar*" title="ti*tle">foo</a></p>
    +<p><a href="/bar*" title="ti\*tle">foo</a></p>
    
    Example 24 (lines 613-620) Backslash escapes
    ``` foo\+bar
    foo
    ```
    
    --- expected HTML
    +++ actual HTML
    @@ -1,2 +1,2 @@
    -<pre><code class="language-foo+bar">foo
    +<pre><code class="language-foo\+bar">foo
     </code></pre>
    
    Example 34 (lines 751-758) Entity and numeric character references
    ``` f&ouml;&ouml;
    foo
    ```
    
    --- expected HTML
    +++ actual HTML
    @@ -1,2 +1,2 @@
    -<pre><code class="language-föö">foo
    +<pre><code class="language-f&amp;ouml;&amp;ouml;">foo
     </code></pre>
    
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
    +<h2>`Foo</h2><p>`</p><h2>&lt;a title="a lot</h2><p>of dashes"/&gt;</p>
    
    Example 93 (lines 1527-1537) Setext headings
    > foo
    bar
    ===
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<blockquote><p>foo bar ===</p></blockquote>
    +<blockquote><p>foo</p></blockquote><h1>bar</h1>
    
    Example 128 (lines 2091-2102) Fenced code blocks
    > ```
    > aaa
    
    bbb
    
    --- expected HTML
    +++ actual HTML
    @@ -1,2 +1,3 @@
     <blockquote><pre><code>aaa
    +
     </code></pre></blockquote><p>bbb</p>
    
    Example 138 (lines 2226-2232) Fenced code blocks
    ``` ```
    aaa
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1,2 @@
    -<p><code> </code> aaa</p>
    +<pre><code class="language-```">aaa
    +</code></pre>
    
    Example 145 (lines 2326-2332) Fenced code blocks
    ``` aa ```
    foo
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1,2 @@
    -<p><code>aa</code> foo</p>
    +<pre><code class="language-aa">foo
    +</code></pre>
    
    Example 168 (lines 2707-2717) HTML blocks
    <del>
    
    *foo*
    
    </del>
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<del><p><em>foo</em></p></del> 
    +<del><p><em>foo</em></p><p></del></p>
    
    Example 195 (lines 3210-3218) Link reference definitions
       [foo]: 
          /url  
               'the title'  
    
    [foo]
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><a href="/url" title="the title">foo</a></p>
    +<p>[foo]: /url<br>'the title'</p><p>[foo]</p>
    
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
    
    Example 203 (lines 3312-3319) Link reference definitions
    [foo]: <bar>(baz)
    
    [foo]
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>[foo]: <bar>(baz)</p><p>[foo]</p>
    +<p><a href="bar%3E(baz">foo</a></p>
    
    Example 204 (lines 3325-3331) Link reference definitions
    [foo]: /url\bar\*baz "foo\"bar\baz"
    
    [foo]
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><a href="/url%5Cbar*baz" title="foo&quot;bar\baz">foo</a></p>
    +<p>[foo]: /url\bar*baz "foo&quot;bar\baz"</p><p>[foo]</p>
    
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
    
    Example 211 (lines 3406-3410) Link reference definitions
    [foo]: /url "title" ok
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>[foo]: /url &quot;title&quot; ok</p>
    +<p>[foo]: /url "title" ok</p>
    
    Example 212 (lines 3415-3420) Link reference definitions
    [foo]: /url
    "title" ok
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>&quot;title&quot; ok</p>
    +<p>"title" ok</p>
    
    Example 213 (lines 3426-3434) Link reference definitions
        [foo]: /url "title"
    
    [foo]
    
    --- expected HTML
    +++ actual HTML
    @@ -1,2 +1,2 @@
    -<pre><code>[foo]: /url &quot;title&quot;
    +<pre><code>[foo]: /url "title"
     </code></pre><p>[foo]</p>
    
    Example 215 (lines 3455-3464) Link reference definitions
    Foo
    [bar]: /baz
    
    [bar]
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>Foo [bar]: /baz</p><p>[bar]</p>
    +<p>Foo</p><p><a href="/baz">bar</a></p>
    
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
    +<p>"bar"</p><p><a href="/foo-url" title="foo">foo</a>, <a href="/bar-url">bar</a>, <a href="/baz-url">baz</a></p>
    
    Example 234 (lines 3782-3792) Block quotes
    > # Foo
    > bar
    baz
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<blockquote><h1>Foo</h1><p>bar baz</p></blockquote>
    +<blockquote><h1>Foo</h1><p>bar</p></blockquote><p>baz</p>
    
    Example 235 (lines 3798-3808) Block quotes
    > bar
    baz
    > foo
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<blockquote><p>bar baz foo</p></blockquote>
    +<blockquote><p>bar</p></blockquote><p>baz</p><blockquote><p>foo</p></blockquote>
    
    Example 240 (lines 3889-3897) Block quotes
    > foo
        - bar
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1,2 @@
    -<blockquote><p>foo - bar</p></blockquote>
    +<blockquote><p>foo</p></blockquote><pre><code>- bar
    +</code></pre>
    
    Example 244 (lines 3946-3957) Block quotes
    > foo
    
    > bar
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<blockquote><p>foo</p></blockquote><blockquote><p>bar</p></blockquote>
    +<blockquote><p>foo</p><p>bar</p></blockquote>
    
    Example 249 (lines 4027-4035) Block quotes
    > bar
    baz
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<blockquote><p>bar baz</p></blockquote>
    +<blockquote><p>bar</p></blockquote><p>baz</p>
    
    Example 252 (lines 4066-4078) Block quotes
    > > > foo
    bar
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<blockquote><blockquote><blockquote><p>foo bar</p></blockquote></blockquote></blockquote>
    +<blockquote><blockquote><blockquote><p>foo</p></blockquote></blockquote></blockquote><p>bar</p>
    
    Example 253 (lines 4081-4095) Block quotes
    >>> foo
    > bar
    >>baz
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<blockquote><blockquote><blockquote><p>foo bar baz</p></blockquote></blockquote></blockquote>
    +<blockquote><blockquote><blockquote><p>foo</p></blockquote></blockquote><p>bar</p><blockquote><p>baz</p></blockquote></blockquote>
    
    Example 254 (lines 4103-4115) Block quotes
    >     code
    
    >    not code
    
    --- expected HTML
    +++ actual HTML
    @@ -1,2 +1,2 @@
     <blockquote><pre><code>code
    -</code></pre></blockquote><blockquote><p>not code</p></blockquote>
    +</code></pre><p>not code</p></blockquote>
    
    Example 259 (lines 4238-4248) List items
     -    one
    
         two
    
    --- expected HTML
    +++ actual HTML
    @@ -1,2 +1 @@
    -<ul><li>one</li></ul><pre><code> two
    -</code></pre>
    +<ul><li><p>one</p><p>two</p></li></ul>
    
    Example 264 (lines 4332-4344) List items
    - foo
    
    
      bar
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<ul><li><p>foo</p><p>bar</p></li></ul>
    +<ul><li>foo</li></ul><p>bar</p>
    
    Example 266 (lines 4377-4395) List items
    - Foo
    
          bar
    
    
          baz
    
    --- expected HTML
    +++ actual HTML
    @@ -1,5 +1,2 @@
    -<ul><li><p>Foo</p><pre><code>bar
    -
    -
    -baz
    -</code></pre></li></ul>
    +<ul><li><p>Foo</p><p>bar</p></li></ul><pre><code>  baz
    +</code></pre>
    
    Example 272 (lines 4460-4472) List items
    - foo
    
          bar
    
    --- expected HTML
    +++ actual HTML
    @@ -1,2 +1 @@
    -<ul><li><p>foo</p><pre><code>bar
    -</code></pre></li></ul>
    +<ul><li><p>foo</p><p>bar</p></li></ul>
    
    Example 273 (lines 4477-4489) List items
      10.  foo
    
               bar
    
    --- expected HTML
    +++ actual HTML
    @@ -1,2 +1,2 @@
    -<ol start="10"><li><p>foo</p><pre><code>bar
    +<ol start="10"><li><p>foo</p><pre><code>   bar
     </code></pre></li></ol>
    
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
    +<ol><li><p>indented code</p><p>paragraph</p><p>more code</p></li></ol>
    
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
    +<ol><li><p>indented code</p><p>paragraph</p><p>more code</p></li></ol>
    
    Example 278 (lines 4570-4579) List items
    -    foo
    
      bar
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<ul><li>foo</li></ul><p>bar</p>
    +<ul><li><p>foo</p><p>bar</p></li></ul>
    
    Example 282 (lines 4654-4663) List items
    -
    
      foo
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<ul><li></li></ul><p>foo</p>
    +<ul><li><p>foo</p></li></ul>
    
    Example 288 (lines 4745-4764) List items
     1.  A paragraph
         with two lines.
    
             indented code
    
         > A block quote.
    
    --- expected HTML
    +++ actual HTML
    @@ -1,2 +1,2 @@
    -<ol><li><p>A paragraph with two lines.</p><pre><code>indented code
    +<ol><li><p>A paragraph with two lines.</p><pre><code> indented code
     </code></pre><blockquote><p>A block quote.</p></blockquote></li></ol>
    
    Example 289 (lines 4769-4788) List items
      1.  A paragraph
          with two lines.
    
              indented code
    
          > A block quote.
    
    --- expected HTML
    +++ actual HTML
    @@ -1,2 +1,2 @@
    -<ol><li><p>A paragraph with two lines.</p><pre><code>indented code
    +<ol><li><p>A paragraph with two lines.</p><pre><code>  indented code
     </code></pre><blockquote><p>A block quote.</p></blockquote></li></ol>
    
    Example 290 (lines 4793-4812) List items
       1.  A paragraph
           with two lines.
    
               indented code
    
           > A block quote.
    
    --- expected HTML
    +++ actual HTML
    @@ -1,2 +1,2 @@
    -<ol><li><p>A paragraph with two lines.</p><pre><code>indented code
    +<ol><li><p>A paragraph with two lines.</p><pre><code>   indented code
     </code></pre><blockquote><p>A block quote.</p></blockquote></li></ol>
    
    Example 292 (lines 4847-4866) List items
      1.  A paragraph
    with two lines.
    
              indented code
    
          > A block quote.
    
    --- expected HTML
    +++ actual HTML
    @@ -1,2 +1,2 @@
    -<ol><li><p>A paragraph with two lines.</p><pre><code>indented code
    +<ol><li><p>A paragraph with two lines.</p><pre><code>  indented code
     </code></pre><blockquote><p>A block quote.</p></blockquote></li></ol>
    
    Example 294 (lines 4884-4898) List items
    > 1. > Blockquote
    continued here.
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<blockquote><ol><li><blockquote><p>Blockquote continued here.</p></blockquote></li></ol></blockquote>
    +<blockquote><ol><li><blockquote><p>Blockquote</p></blockquote></li></ol></blockquote><p>continued here.</p>
    
    Example 295 (lines 4901-4915) List items
    > 1. > Blockquote
    > continued here.
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<blockquote><ol><li><blockquote><p>Blockquote continued here.</p></blockquote></li></ol></blockquote>
    +<blockquote><ol><li><blockquote><p>Blockquote</p></blockquote>continued here.</li></ol></blockquote>
    
    Example 296 (lines 4929-4950) List items
    - foo
      - bar
        - baz
          - boo
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<ul><li>foo<ul><li>bar<ul><li>baz<ul><li>boo</li></ul></li></ul></li></ul></li></ul>
    +<ul><li>foo<ul><li>bar</li><li>baz<ul><li>boo</li></ul></li></ul></li></ul>
    
    Example 297 (lines 4955-4967) List items
    - foo
     - bar
      - baz
       - boo
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<ul><li>foo</li><li>bar</li><li>baz</li><li>boo</li></ul>
    +<ul><li>foo<ul><li>bar</li><li>baz</li><li>boo</li></ul></li></ul>
    
    Example 299 (lines 4988-4998) List items
    10) foo
       - bar
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<ol start="10"><li>foo</li></ol><ul><li>bar</li></ul>
    +<ol start="10"><li>foo<ul><li>bar</li></ul></li></ol>
    
    Example 302 (lines 5035-5049) List items
    - # Foo
    - Bar
      ---
      baz
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<ul><li><h1>Foo</h1></li><li><h2>Bar</h2>baz</li></ul>
    +<ul><li><h1>Foo</h1></li><li>Bar</li></ul><hr><p>baz</p>
    
    Example 308 (lines 5406-5425) Lists
    - foo
    
    - bar
    
    
    - baz
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<ul><li><p>foo</p></li><li><p>bar</p></li><li><p>baz</p></li></ul>
    +<ul><li><p>foo</p></li><li><p>bar</p></li></ul><ul><li>baz</li></ul>
    
    Example 309 (lines 5427-5449) Lists
    - foo
      - bar
        - baz
    
    
          bim
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1,2 @@
    -<ul><li>foo<ul><li>bar<ul><li><p>baz</p><p>bim</p></li></ul></li></ul></li></ul>
    +<ul><li>foo<ul><li>bar</li><li>baz</li></ul></li></ul><pre><code>  bim
    +</code></pre>
    
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
    +<ul><li>a<ul><li>b</li><li>c</li><li>d</li><li>e</li><li>f</li></ul></li><li>g</li></ul>
    
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
    +<ul><li>a<ul><li>b</li><li>c</li><li>d</li><li>e</li></ul></li></ul>
    
    Example 315 (lines 5574-5591) Lists
    1. a
    
      2. b
    
        3. c
    
    --- expected HTML
    +++ actual HTML
    @@ -1,2 +1 @@
    -<ol><li><p>a</p></li><li><p>b</p></li></ol><pre><code>3. c
    -</code></pre>
    +<ol><li><p>a</p></li><li><p>b</p><ol start="3"><li>c</li></ol></li></ol>
    
    Example 320 (lines 5686-5705) Lists
    - a
    - ```
      b
    
    
      ```
    - c
    
    --- expected HTML
    +++ actual HTML
    @@ -1,4 +1,3 @@
     <ul><li>a</li><li><pre><code>b
    -
    -
    -</code></pre></li><li>c</li></ul>
    +</code></pre></li></ul><pre><code>- c
    +</code></pre>
    
    Example 321 (lines 5712-5730) Lists
    - a
      - b
    
        c
    - d
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<ul><li>a<ul><li><p>b</p><p>c</p></li></ul></li><li>d</li></ul>
    +<ul><li><p>a</p><ul><li>b</li></ul><p>c</p></li><li><p>d</p></li></ul>
    
    Example 326 (lines 5805-5819) Lists
    1. ```
       foo
       ```
    
       bar
    
    --- expected HTML
    +++ actual HTML
    @@ -1,2 +1,2 @@
    -<ol><li><pre><code>foo
    +<ol><li><pre><code> foo
     </code></pre><p>bar</p></li></ol>
    
    Example 343 (lines 6041-6045) Code spans
    *foo`*`
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>*foo<code>*</code></p>
    +<p><em>foo`</em>`</p>
    
    Example 345 (lines 6060-6064) Code spans
    `<a href="`">`
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><code>&lt;a href=&quot;</code>&quot;&gt;`</p>
    +<p><code>&lt;a href="</code>"&gt;`</p>
    
    Example 349 (lines 6097-6101) Code spans
    ```foo``
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>```foo``</p>
    +<pre><code class="language-foo``"></code></pre>
    
    Example 354 (lines 6351-6355) Emphasis and strong emphasis
    a*"foo"*
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>a*&quot;foo&quot;*</p>
    +<p>a<em>"foo"</em></p>
    
    Example 358 (lines 6394-6398) Emphasis and strong emphasis
    5*6*78
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>5<em>6</em>78</p>
    +<p>5*6*78</p>
    
    Example 361 (lines 6423-6427) Emphasis and strong emphasis
    a_"foo"_
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>a_&quot;foo&quot;_</p>
    +<p>a_"foo"_</p>
    
    Example 365 (lines 6456-6460) Emphasis and strong emphasis
    aa_"bb"_cc
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>aa_&quot;bb&quot;_cc</p>
    +<p>aa_"bb"_cc</p>
    
    Example 371 (lines 6521-6525) Emphasis and strong emphasis
    *(*foo*)*
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><em>(<em>foo</em>)</em></p>
    +<p><em>(*foo</em>)*</p>
    
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
    +<p><em>(_foo</em>)_</p>
    
    Example 382 (lines 6626-6630) Emphasis and strong emphasis
    a**"foo"**
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>a**&quot;foo&quot;**</p>
    +<p>a<strong>"foo"</strong></p>
    
    Example 387 (lines 6674-6678) Emphasis and strong emphasis
    a__"foo"__
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>a__&quot;foo&quot;__</p>
    +<p>a_<em>"foo"</em>_</p>
    
    Example 388 (lines 6683-6687) Emphasis and strong emphasis
    foo__bar__
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>foo__bar__</p>
    +<p>foo_<em>bar</em>_</p>
    
    Example 390 (lines 6697-6701) Emphasis and strong emphasis
    пристаням__стремятся__
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>пристаням__стремятся__</p>
    +<p>пристаням_<em>стремятся</em>_</p>
    
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
    +<p><em>(**foo</em><em>)</em></p>
    
    Example 396 (lines 6758-6764) Emphasis and strong emphasis
    **Gomphocarpus (*Gomphocarpus physocarpus*, syn.
    *Asclepias physocarpa*)**
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><strong>Gomphocarpus (<em>Gomphocarpus physocarpus</em>, syn. <em>Asclepias physocarpa</em>)</strong></p>
    +<p><em>*Gomphocarpus (*Gomphocarpus physocarpus</em>, syn. <em>Asclepias physocarpa</em>)**</p>
    
    Example 397 (lines 6767-6771) Emphasis and strong emphasis
    **foo "*bar*" foo**
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><strong>foo &quot;<em>bar</em>&quot; foo</strong></p>
    +<p><em>*foo "*bar</em>" foo**</p>
    
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
    +<p><em>(__foo</em><em>)</em></p>
    
    Example 408 (lines 6873-6877) Emphasis and strong emphasis
    _foo __bar__ baz_
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><em>foo <strong>bar</strong> baz</em></p>
    +<p><em>foo __bar</em>_ baz_</p>
    
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
    +<p><em>_foo</em> bar_</p>
    
    Example 411 (lines 6894-6898) Emphasis and strong emphasis
    *foo *bar**
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><em>foo <em>bar</em></em></p>
    +<p><em>foo *bar</em>*</p>
    
    Example 412 (lines 6901-6905) Emphasis and strong emphasis
    *foo **bar** baz*
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><em>foo <strong>bar</strong> baz</em></p>
    +<p><em>foo **bar</em>* baz*</p>
    
    Example 413 (lines 6907-6911) Emphasis and strong emphasis
    *foo**bar**baz*
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><em>foo<strong>bar</strong>baz</em></p>
    +<p><em>foo**bar**baz</em></p>
    
    Example 415 (lines 6944-6948) Emphasis and strong emphasis
    ***foo** bar*
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><em><strong>foo</strong> bar</em></p>
    +<p><strong>*foo</strong> bar*</p>
    
    Example 416 (lines 6951-6955) Emphasis and strong emphasis
    *foo **bar***
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><em>foo <strong>bar</strong></em></p>
    +<p><em>foo **bar</em>**</p>
    
    Example 417 (lines 6958-6962) Emphasis and strong emphasis
    *foo**bar***
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><em>foo<strong>bar</strong></em></p>
    +<p><em>foo**bar</em>**</p>
    
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
    +<p><em>foo **bar *baz</em> bim** bop*</p>
    
    Example 421 (lines 6991-6995) Emphasis and strong emphasis
    *foo [*bar*](/url)*
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><em>foo <a href="/url"><em>bar</em></a></em></p>
    +<p><em>foo [*bar</em>](/url)*</p>
    
    Example 426 (lines 7039-7043) Emphasis and strong emphasis
    __foo _bar_ baz__
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><strong>foo <em>bar</em> baz</strong></p>
    +<p><em>_foo _bar</em> baz__</p>
    
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
    +<p><strong>foo **bar</strong>**</p>
    
    Example 430 (lines 7067-7071) Emphasis and strong emphasis
    **foo *bar* baz**
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><strong>foo <em>bar</em> baz</strong></p>
    +<p><em>*foo *bar</em> baz**</p>
    
    Example 431 (lines 7074-7078) Emphasis and strong emphasis
    **foo*bar*baz**
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><strong>foo<em>bar</em>baz</strong></p>
    +<p><strong>foo*bar*baz</strong></p>
    
    Example 432 (lines 7081-7085) Emphasis and strong emphasis
    ***foo* bar**
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><strong><em>foo</em> bar</strong></p>
    +<p><em>**foo</em> bar**</p>
    
    Example 433 (lines 7088-7092) Emphasis and strong emphasis
    **foo *bar***
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><strong>foo <em>bar</em></strong></p>
    +<p><strong>foo *bar</strong>*</p>
    
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
    +<p><em>*foo [*bar</em>](/url)**</p>
    
    Example 444 (lines 7178-7182) Emphasis and strong emphasis
    **foo*
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>*<em>foo</em></p>
    +<p><em>*foo</em></p>
    
    Example 446 (lines 7192-7196) Emphasis and strong emphasis
    ***foo**
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>*<strong>foo</strong></p>
    +<p><strong>*foo</strong></p>
    
    Example 447 (lines 7199-7203) Emphasis and strong emphasis
    ****foo*
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>***<em>foo</em></p>
    +<p><em>***foo</em></p>
    
    Example 456 (lines 7265-7269) Emphasis and strong emphasis
    __foo_
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>_<em>foo</em></p>
    +<p><em>_foo</em></p>
    
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
    +<p><em>___foo</em></p>
    
    Example 466 (lines 7345-7349) Emphasis and strong emphasis
    ****foo****
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><strong><strong>foo</strong></strong></p>
    +<p><strong>**foo</strong>**</p>
    
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
    +<p><strong>****foo</strong>****</p>
    
    Example 469 (lines 7372-7376) Emphasis and strong emphasis
    ***foo***
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><em><strong>foo</strong></em></p>
    +<p><strong>*foo</strong>*</p>
    
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
    +<p><em>[bar</em>](/url)</p>
    
    Example 476 (lines 7427-7431) Emphasis and strong emphasis
    _foo [bar_](/url)
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>_foo <a href="/url">bar_</a></p>
    +<p><em>foo [bar</em>](/url)</p>
    
    Example 477 (lines 7434-7438) Emphasis and strong emphasis
    *<img src="foo" title="*"/>
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>*<img src="foo" title="*"></p>
    +<p><em>&lt;img src="foo" title="</em>"/&gt;</p>
    
    Example 478 (lines 7441-7445) Emphasis and strong emphasis
    **<a href="**">
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>**<a href="**"></p>
    +<p><strong>&lt;a href="</strong>"&gt;</p>
    
    Example 479 (lines 7448-7452) Emphasis and strong emphasis
    __<a href="__">
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>__<a href="__"></p>
    +<p><strong>&lt;a href="</strong>"&gt;</p>
    
    Example 480 (lines 7455-7459) Emphasis and strong emphasis
    *a `*`*
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><em>a <code>*</code></em></p>
    +<p><em>a `</em>`*</p>
    
    Example 481 (lines 7462-7466) Emphasis and strong emphasis
    _a `_`_
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><em>a <code>_</code></em></p>
    +<p><em>a `</em>`_</p>
    
    Example 482 (lines 7469-7473) Emphasis and strong emphasis
    **a<https://foo.bar/?q=**>
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>**a<a href="https://foo.bar/?q=**">https://foo.bar/?q=**</a></p>
    +<p><strong>a&lt;https://foo.bar/?q=</strong>&gt;</p>
    
    Example 483 (lines 7476-7480) Emphasis and strong emphasis
    __a<https://foo.bar/?q=__>
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>__a<a href="https://foo.bar/?q=__">https://foo.bar/?q=__</a></p>
    +<p><strong>a&lt;https://foo.bar/?q=</strong>&gt;</p>
    
    Example 495 (lines 7652-7656) Links
    [link](<foo\>)
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>[link](&lt;foo&gt;)</p>
    +<p><a href="foo%5C">link</a></p>
    
    Example 509 (lines 7801-7805) Links
    [link](/url "title")
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><a href="/url%C2%A0%22title%22">link</a></p>
    +<p>[link](/url "title")</p>
    
    Example 510 (lines 7810-7814) Links
    [link](/url "title "and" title")
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>[link](/url &quot;title &quot;and&quot; title&quot;)</p>
    +<p>[link](/url "title "and" title")</p>
    
    Example 518 (lines 7895-7899) Links
    [link *foo **bar** `#`*](/uri)
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><a href="/uri">link <em>foo <strong>bar</strong> <code>#</code></em></a></p>
    +<p><a href="/uri">link <em>foo **bar</em>* <code>#</code>*</a></p>
    
    Example 520 (lines 7911-7915) Links
    [foo [bar](/uri)](/uri)
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>[foo <a href="/uri">bar</a>](/uri)</p>
    +<p><a href="/uri">foo <a href="/uri">bar</a></a></p>
    
    Example 521 (lines 7918-7922) Links
    [foo *[bar [baz](/uri)](/uri)*](/uri)
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>[foo <em>[bar <a href="/uri">baz</a>](/uri)</em>](/uri)</p>
    +<p><a href="/uri">foo <em><a href="/uri">bar <a href="/uri">baz</a></a></em></a></p>
    
    Example 522 (lines 7925-7929) Links
    ![[[foo](uri1)](uri2)](uri3)
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><img alt="[foo](uri2)" src="uri3"></p>
    +<p><img alt="[[foo](uri1)](uri2)" src="uri3"></p>
    
    Example 523 (lines 7935-7939) Links
    *[foo*](/uri)
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>*<a href="/uri">foo*</a></p>
    +<p><em>[foo</em>](/uri)</p>
    
    Example 526 (lines 7962-7966) Links
    [foo <bar attr="](baz)">
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>[foo <bar attr="](baz)"></p>
    +<p><a href="baz">foo &lt;bar attr="</a>"&gt;</p>
    
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
    +<p><a href="/uri">link <em>foo **bar</em>* <code>#</code>*</a></p>
    
    Example 534 (lines 8069-8075) Links
    [foo [bar](/uri)][ref]
    
    [ref]: /uri
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>[foo <a href="/uri">bar</a>]<a href="/uri">ref</a></p>
    +<p><a href="/uri">foo <a href="/uri">bar</a></a></p>
    
    Example 535 (lines 8078-8084) Links
    [foo *bar [baz][ref]*][ref]
    
    [ref]: /uri
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>[foo <em>bar <a href="/uri">baz</a></em>]<a href="/uri">ref</a></p>
    +<p><a href="/uri">foo <em>bar <a href="/uri">baz</a></em></a></p>
    
    Example 536 (lines 8093-8099) Links
    *[foo*][ref]
    
    [ref]: /uri
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>*<a href="/uri">foo*</a></p>
    +<p><em>[foo</em>]<a href="/uri">ref</a></p>
    
    Example 538 (lines 8114-8120) Links
    [foo <bar attr="][ref]">
    
    [ref]: /uri
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>[foo <bar attr="][ref]"></p>
    +<p><a href="/uri">foo &lt;bar attr="</a>"&gt;</p>
    
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
    
    Example 548 (lines 8256-8263) Links
    [foo][ref[]
    
    [ref[]: /uri
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>[foo][ref[]</p><p>[ref[]: /uri</p>
    +<p>[foo][ref[]</p>
    
    Example 566 (lines 8468-8474) Links
    [foo*]: /url
    
    *[foo*]
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>*<a href="/url">foo*</a></p>
    +<p><em>[foo</em>]</p>
    
    Example 576 (lines 8582-8586) Images
    ![foo ![bar](/url)](/url2)
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><img alt="foo bar" src="/url2"></p>
    +<p><img alt="foo ![bar](/url)" src="/url2"></p>
    
    Example 577 (lines 8589-8593) Images
    ![foo [bar](/url)](/url2)
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><img alt="foo bar" src="/url2"></p>
    +<p><img alt="foo [bar](/url)" src="/url2"></p>
    
    Example 592 (lines 8736-8743) Images
    ![[foo]]
    
    [[foo]]: /url "title"
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>![[foo]]</p><p>[[foo]]: /url &quot;title&quot;</p>
    +<p>![[foo]]</p><p>[[foo]]: /url "title"</p>
    
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
    +<p>&lt;a href="hi'&gt; &lt;a href=hi'&gt;</p>
    
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
    
    496 passed, 159 failed, 0 errored, 0 skipped
  stderr:
    --- drydock: progress ---
    cases: pass=496 fail=159 error=0 skip=0 total=655 from=result.stdout
    --- drydock: end progress ---
    --- drydock: values at failure ---
      result = CompletedProcess(args=['sh', 'sources/full_test.sh'], returncode=1, stdout='Example 1 (lines 355-360) Tabs\n\tfoo\tbaz\t\tbim\n\n--- expected HTML\n+++ actual HTML\n@@ -1,2 +1 @@\n-<pre><code>foo\tbaz\t\tbim\n-</code></pre>\n+<p>foo baz bim</p>\n\nExample 2 (lines 362-367) Tabs\n  \tfoo\tbaz\t\tbim\n\n--- expected HTML\n+++ actual HTML\n@@ -1,2 +1 @@\n-<pre><code>foo\tbaz\t\tbim\n-</code></pre>\n+… (+36475 chars)
    --- drydock: end values ---
    Traceback (most recent call last):
      File "full-commonmark-suite.py", line 10, in <module>
        assert result.returncode == 0
               ^^^^^^^^^^^^^^^^^^^^^^
    AssertionError

## Repair attempts
- attempt 0 (initial build): failed; 2/5 checks; 865/1965 cases model=gpt-6-luna; execution 20261025.023605.681Z-de5167ab; reason: programmatic acceptance failed: block-parsing-conformance, inline-parsing-conformance, full-commonmark-suite
- attempt 1 (repair 1): failed; 2/5 checks; 869/1965 cases model=gpt-6-luna; execution 20261025.025556.110Z-3eb535c8; reason: programmatic acceptance failed: block-parsing-conformance, inline-parsing-conformance, full-commonmark-suite
- attempt 2 (repair 2): failed; 2/5 checks; 903/1965 cases model=gpt-6-luna; execution 20261025.030521.327Z-23a2bc97; reason: programmatic acceptance failed: block-parsing-conformance, inline-parsing-conformance, full-commonmark-suite
- attempt 3 (repair 3): failed; 2/5 checks; 915/1965 cases model=gpt-6-luna; execution 20261025.032110.944Z-ac3bab81; reason: programmatic acceptance failed: block-parsing-conformance, inline-parsing-conformance, full-commonmark-suite
- attempt 4 (repair 4): failed; 2/5 checks; 959/1965 cases model=gpt-6-luna; execution 20261025.033050.523Z-fd9650fa; reason: programmatic acceptance failed: block-parsing-conformance, inline-parsing-conformance, full-commonmark-suite
- attempt 5 (repair 5): failed; checks not executed (5 declared) model=gpt-6-luna; execution 20261025.034243.229Z-7d797458; reason: target verification interrupted by build agent
- attempt 6 (repair 6): failed; 2/5 checks; 987/1965 cases model=gpt-6-luna; execution 20261025.034642.361Z-1f8a7ec9; reason: programmatic acceptance failed: block-parsing-conformance, inline-parsing-conformance, full-commonmark-suite

## Agent self-report (advisory)
The build agent declared a failure. This report is advisory; Drydock's execution and deterministic checks determine the block's outcome.
- summary: CommonMark conformance checks remain failing
- detail:
    The declared block, inline, and full suite checks completed but reported failures. Fix the remaining general parsing behavior, then rerun all three checks. The pytest command also failed because pytest is unavailable in the available Python environments.

## Failure
- summary: programmatic acceptance failed: block-parsing-conformance, inline-parsing-conformance, full-commonmark-suite
- detail:
    Block "Block 2 · Service" [block-2] failed its acceptance criteria.
      Story "Parse CommonMark block structure and collect link reference definitions." [block_parsing] does not meet its own acceptance criteria:
        - AC block-parsing-conformance — All supplied cases in the block parsing sections pass (the complete block capability slice).
            assertion: assert result.returncode == 0 → AssertionError
            cases: pass=232 fail=54 error=0 skip=369 total=655 from=result.stdout
            raised at: block-parsing-conformance.py:18
            process exit code: 1
            values at failure:
              result = CompletedProcess(args=['/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261025.023211/build/commonmark/.venv/bin/python', 'sources/spec_tests.py', '--program', './commonmark', '--spec', 'sources/spec.txt', '--pattern', 'Thematic breaks|ATX headings|Setext headings|Indented code blocks|Fenced code blocks|HTML blocks|Link reference definitions|Paragraphs|Blank lines|Block quotes|List items… (+14443 chars)
            observed output:
              Example 326 (lines 5805-5819) Lists
              1. ```
                 foo
                 ```
                 bar
              --- expected HTML
              +++ actual HTML
              @@ -1,2 +1,2 @@
              -<ol><li><pre><code>foo
              +<ol><li><pre><code> foo
               </code></pre><p>bar</p></li></ol>
              232 passed, 54 failed, 0 errored, 369 skipped
              … 516 earlier line(s) omitted, --full for all
            check stderr:
              Traceback (most recent call last):
                File "block-parsing-conformance.py", line 18, in <module>
                  assert result.returncode == 0
                         ^^^^^^^^^^^^^^^^^^^^^^
              AssertionError
      Story "Parse CommonMark inline syntax and render inline HTML." [inline_parsing] does not meet its own acceptance criteria:
        - AC inline-parsing-conformance — All supplied cases in the inline parsing sections pass (the complete inline capability slice).
            assertion: assert result.returncode == 0 → AssertionError
            cases: pass=259 fail=97 error=0 skip=299 total=655 from=result.stdout
            raised at: inline-parsing-conformance.py:18
            process exit code: 1
            values at failure:
              result = CompletedProcess(args=['/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261025.023211/build/commonmark/.venv/bin/python', 'sources/spec_tests.py', '--program', './commonmark', '--spec', 'sources/spec.txt', '--pattern', 'Backslash escapes|Entity and numeric character references|Code spans|Emphasis and strong emphasis|Links|Images|Autolinks|Raw HTML|Hard line breaks|Soft line breaks|Textua… (+20991 chars)
            observed output:
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
              259 passed, 97 failed, 0 errored, 299 skipped
              … 697 earlier line(s) omitted, --full for all
            check stderr:
              Traceback (most recent call last):
                File "inline-parsing-conformance.py", line 18, in <module>
                  assert result.returncode == 0
                         ^^^^^^^^^^^^^^^^^^^^^^
              AssertionError
      Story "Verify the completed parser against the full CommonMark suite." [full_conformance] does not meet its own acceptance criteria:
        - AC full-commonmark-suite — The supplied full CommonMark conformance suite completes successfully.
            assertion: assert result.returncode == 0 → AssertionError
            cases: pass=496 fail=159 error=0 skip=0 total=655 from=result.stdout
            raised at: full-commonmark-suite.py:10
            process exit code: 1
            values at failure:
              result = CompletedProcess(args=['sh', 'sources/full_test.sh'], returncode=1, stdout='Example 1 (lines 355-360) Tabs\n\tfoo\tbaz\t\tbim\n\n--- expected HTML\n+++ actual HTML\n@@ -1,2 +1 @@\n-<pre><code>foo\tbaz\t\tbim\n-</code></pre>\n+<p>foo baz bim</p>\n\nExample 2 (lines 362-367) Tabs\n  \tfoo\tbaz\t\tbim\n\n--- expected HTML\n+++ actual HTML\n@@ -1,2 +1 @@\n-<pre><code>foo\tbaz\t\tbim\n-</code></pre>\n+… (+36475 chars)
            observed output:
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
              496 passed, 159 failed, 0 errored, 0 skipped
              … 1292 earlier line(s) omitted, --full for all
            check stderr:
              Traceback (most recent call last):
                File "full-commonmark-suite.py", line 10, in <module>
                  assert result.returncode == 0
                         ^^^^^^^^^^^^^^^^^^^^^^
              AssertionError

## Build summary
RESULT: FAILED

FILES CHANGED:
- src/commonmark/block_parser.py
- src/commonmark/inline_parser.py

SUMMARY:
Fixed several block and inline parsing issues, including empty ATX headings, HTML block boundaries, paragraph interruption, entity handling, and URL escaping. The scoped and full conformance checks still fail:

- Block parsing: 232 passed, 54 failed.
- Inline parsing: 259 passed, 97 failed.
- Full suite: 496 passed, 159 failed.

`pytest -q` could not collect tests because pytest is not installed in the available Python environments. The source compiled successfully with `python3 -m compileall`.

BLOCKERS:
- The parser still fails CommonMark cases involving list and container continuation, reference definitions, emphasis nesting, and raw HTML handling.
- pytest is unavailable in the configured environment.

FAILURE_SUMMARY: CommonMark conformance checks remain failing
FAILURE_DETAIL: The declared block, inline, and full suite checks completed but reported failures. Fix the remaining general parsing behavior, then rerun all three checks. The pytest command also failed because pytest is unavailable in the available Python environments.
