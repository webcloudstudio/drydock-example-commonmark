# Evidence: Block 16 · Service (block-16)

- block type: block
- date: 2026-08-12
- resulting state: closed/verified
- story points (combined assembled cost): 59659
- execution id: 20260812.203419.805Z-d8525ecc

## Stories built
- Run the complete supplied CommonMark conformance suite. (conformance-full) [story]

## Stacked context
- compass: COMPASS.md (SP 1263)
- implements: FEATURE-CONFORMANCE-FULL.md (SP 397)
- context: spec.txt (SP 51527)
- context: spec_tests.py (SP 1609)
- context: cmark.py (SP 339)
- context: normalize.py (SP 1631)
- context: ARCHITECTURE_compact.md (SP 116)
- stack: common_compact.md (SP 1179)
- stack: python_compact.md (SP 1534)

## Build directory changes
- full_test.sh
- parser/blocks.py

## Pre-build acceptance observation
- RED: complete-conformance-suite (FEATURE-CONFORMANCE-FULL.md)
  intent: The complete supplied CommonMark conformance suite passes through the required wrapper.
  return code: 1
  stdout:
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
    +<ul><li>foo</li></ul>
    
    Example 5 (lines 395-407) Tabs
    - foo
    
    		bar
    
    --- expected HTML
    +++ actual HTML
    @@ -1,2 +1 @@
    -<ul><li><p>foo</p><pre><code>  bar
    -</code></pre></li></ul>
    +<ul><li><p>foo</p><p>bar</p></li></ul>
    
    Example 6 (lines 418-425) Tabs
    >		foo
    
    --- expected HTML
    +++ actual HTML
    @@ -1,2 +1,2 @@
    -<blockquote><pre><code>  foo
    +<blockquote><pre><code>foo
     </code></pre></blockquote>
    
    Example 7 (lines 427-436) Tabs
    -		foo
    
    --- expected HTML
    +++ actual HTML
    @@ -1,2 +1,2 @@
    -<ul><li><pre><code>  foo
    +<ul><li><pre><code>   foo
     </code></pre></li></ul>
    
    Example 9 (lines 448-464) Tabs
     - foo
       - bar
    	 - baz
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<ul><li>foo<ul><li>bar<ul><li>baz</li></ul></li></ul></li></ul>
    +<ul><li>foo<ul><li>bar baz</li></ul></li></ul>
    
    649 passed, 6 failed, 0 errored, 0 skipped
  stderr:
    Traceback (most recent call last):
      File "complete-conformance-suite.py", line 10, in <module>
        assert result.returncode == 0
               ^^^^^^^^^^^^^^^^^^^^^^
    AssertionError

## Post-build programmatic acceptance
- PASS: complete-conformance-suite (FEATURE-CONFORMANCE-FULL.md)
  intent: The complete supplied CommonMark conformance suite passes through the required wrapper.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/.venv/bin/python3
  provisioning: not required
  return code: 0
  stdout:
    655 passed, 0 failed, 0 errored, 0 skipped

## Build summary
RESULT: SUCCESS

FILES CHANGED:
- full_test.sh
- parser/blocks.py

SUMMARY:
Added the complete-suite wrapper and fixed tab-stop handling. The full CommonMark conformance suite passes.

BLOCKERS:
- None
