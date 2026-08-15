# Evidence: Block 9 · Service (block-9)

- block type: block
- date: 2026-08-15
- resulting state: closed/verified
- story points (combined assembled cost): 60337
- execution id: 20260815.213833.039Z-c3a972ed

## Stories built
- Run the complete supplied CommonMark conformance suite. (verify-001) [story]

## Stacked context
- compass: COMPASS.md (SP 1455)
- implements: FEATURE-Conformance-Verification.md (SP 404)
- context: spec.txt (SP 51527)
- context: spec_tests.py (SP 1609)
- context: cmark.py (SP 339)
- context: normalize.py (SP 1631)
- context: full_test.sh (SP 509)
- context: ARCHITECTURE_compact.md (SP 87)
- stack: common_compact.md (SP 1179)
- stack: python_compact.md (SP 1534)

## Build directory changes
- commonmark

## Pre-build acceptance observation
- UNVERIFIED: complete-conformance (FEATURE-Conformance-Verification.md)
  intent: The completed parser passes the complete unfiltered supplied CommonMark conformance suite.
  return code: 1
  error: malformed check: the assertion itself raised NameError (name 'sys' is not defined. Did you forget to import 'sys'?) in its own frame, before reaching the code under test. No implementation can satisfy it. Each check runs as its own script in its own process, so a name bound by another check is not in scope. Repair the assertion in the Blueprint specification.
  stdout:
    Example 1 (lines 355-360) Tabs
    	foo	baz		bim
    
    --- expected HTML
    +++ actual HTML
    @@ -1,2 +1,2 @@
    -<pre><code>foo	baz		bim
    +<pre><code>foo baz  bim
     </code></pre>
    
    Example 2 (lines 362-367) Tabs
      	foo	baz		bim
    
    --- expected HTML
    +++ actual HTML
    @@ -1,2 +1,2 @@
    -<pre><code>foo	baz		bim
    +<pre><code>foo baz  bim
     </code></pre>
    
    Example 3 (lines 369-376) Tabs
        a	a
        ὐ	a
    
    --- expected HTML
    +++ actual HTML
    @@ -1,3 +1,3 @@
    -<pre><code>a	a
    -ὐ	a
    +<pre><code>a a
    +ὐ a
     </code></pre>
    
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
    
    Example 93 (lines 1527-1537) Setext headings
    > foo
    bar
    ===
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<blockquote><p>foo bar ===</p></blockquote>
    +<blockquote><p>foo bar</p></blockquote><p>===</p>
    
    649 passed, 6 failed, 0 errored, 0 skipped
  stderr:
    Traceback (most recent call last):
      File "complete-conformance.py", line 9, in <module>
        print(result.stderr, file=sys.stderr)
                                  ^^^
    NameError: name 'sys' is not defined. Did you forget to import 'sys'?

## Post-build programmatic acceptance
- UNVERIFIED: complete-conformance (FEATURE-Conformance-Verification.md)
  intent: The completed parser passes the complete unfiltered supplied CommonMark conformance suite.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/.venv/bin/python3
  provisioning: not required
  return code: 1
  error: malformed check: the assertion itself raised NameError (name 'sys' is not defined. Did you forget to import 'sys'?) in its own frame, before reaching the code under test. No implementation can satisfy it. Each check runs as its own script in its own process, so a name bound by another check is not in scope. Repair the assertion in the Blueprint specification.
  stdout:
    655 passed, 0 failed, 0 errored, 0 skipped
  stderr:
    Traceback (most recent call last):
      File "complete-conformance.py", line 9, in <module>
        print(result.stderr, file=sys.stderr)
                                  ^^^
    NameError: name 'sys' is not defined. Did you forget to import 'sys'?

## Build summary
RESULT: SUCCESS

FILES CHANGED:
- commonmark

SUMMARY:
Fixed tab preservation and block-quote lazy continuation handling. Full suite: 655 passed, 0 failed, 0 errored, 0 skipped.

BLOCKERS:
- Supplemental pytest directory was unavailable; conformance verification passed.
