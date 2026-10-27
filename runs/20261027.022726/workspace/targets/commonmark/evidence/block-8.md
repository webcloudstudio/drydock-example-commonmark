# Evidence: Block 8 · Service (block-8)

- block type: block
- date: 2026-10-26
- resulting state: closed/verified
- story points (combined assembled cost): 2952
- execution id: 20261027.024747.108Z-a4f84c25

## Stories built
- Parse and normalize backtick code spans. (code-spans) [story]

## Acceptance tooling authorization
- FEATURE-CodeSpans.md#code-spans-conformance: executable=python3; scope=test; authorization=existing Target environment

## Stacked context
- stack: python_compact.md (SP 601)
- compass: COMPASS.md (SP 512)
- implements: FEATURE-CodeSpans.md (SP 478)
- context: ARCHITECTURE_compact.md (SP 211)
- stack: common_compact.md (SP 1079)

## Build directory changes
- commonmark_parser/inline.py
- commonmark_parser/stages.py
- tests/test_escapes_and_entities.py

## Pre-build acceptance observation
- RED: code-spans-conformance (FEATURE-CodeSpans.md)
  intent: The completed inline parser passes every authoritative code-span example, including precedence interactions.
  return code: 1
  stdout:
    Example 330 (lines 5908-5912) Code spans
    `foo`
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><code>foo</code></p>
    +<p>`foo`</p>
    
    Example 331 (lines 5919-5923) Code spans
    `` foo ` bar ``
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><code>foo ` bar</code></p>
    +<p>`` foo ` bar ``</p>
    
    Example 332 (lines 5929-5933) Code spans
    ` `` `
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><code>``</code></p>
    +<p>` `` `</p>
    
    Example 333 (lines 5937-5941) Code spans
    `  ``  `
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><code> `` </code></p>
    +<p>` `` `</p>
    
    Example 334 (lines 5946-5950) Code spans
    ` a`
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><code> a</code></p>
    +<p>` a`</p>
    
    Example 335 (lines 5955-5959) Code spans
    ` b `
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><code> b </code></p>
    +<p>` b `</p>
    
    Example 336 (lines 5963-5969) Code spans
    ` `
    `  `
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><code> </code> <code> </code></p>
    +<p>` ` ` `</p>
    
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
    +<p>`` foo bar baz ``</p>
    
    Example 338 (lines 5984-5990) Code spans
    ``
    foo 
    ``
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><code>foo </code></p>
    +<p>`` foo ``</p>
    
    Example 339 (lines 5995-6000) Code spans
    `foo   bar 
    baz`
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><code>foo bar baz</code></p>
    +<p>`foo bar baz`</p>
    
    Example 340 (lines 6012-6016) Code spans
    `foo\`bar`
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><code>foo\</code>bar`</p>
    +<p>`foo`bar`</p>
    
    Example 341 (lines 6023-6027) Code spans
    ``foo`bar``
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><code>foo`bar</code></p>
    +<p>``foo`bar``</p>
    
    Example 342 (lines 6029-6033) Code spans
    ` foo `` bar `
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><code>foo `` bar</code></p>
    +<p>` foo `` bar `</p>
    
    Example 343 (lines 6041-6045) Code spans
    *foo`*`
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>*foo<code>*</code></p>
    +<p>*foo`*`</p>
    
    Example 344 (lines 6050-6054) Code spans
    [not a `link](/foo`)
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>[not a <code>link](/foo</code>)</p>
    +<p>[not a `link](/foo`)</p>
    
    Example 345 (lines 6060-6064) Code spans
    `<a href="`">`
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><code>&lt;a href=&quot;</code>&quot;&gt;`</p>
    +<p>`&lt;a href=&quot;`&quot;&gt;`</p>
    
    Example 346 (lines 6069-6073) Code spans
    <a href="`">`
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><a href="`">`</p>
    +<p>&lt;a href=&quot;`&quot;&gt;`</p>
    
    Example 347 (lines 6078-6082) Code spans
    `<https://foo.bar.`baz>`
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><code>&lt;https://foo.bar.</code>baz&gt;`</p>
    +<p>`&lt;https://foo.bar.`baz&gt;`</p>
    
    Example 348 (lines 6087-6091) Code spans
    <https://foo.bar.`baz>`
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p><a href="https://foo.bar.%60baz">https://foo.bar.`baz</a>`</p>
    +<p>&lt;https://foo.bar.`baz&gt;`</p>
    
    Example 351 (lines 6113-6117) Code spans
    `foo``bar``
    
    --- expected HTML
    +++ actual HTML
    @@ -1 +1 @@
    -<p>`foo<code>bar</code></p>
    +<p>`foo``bar``</p>
    
    2 passed, 20 failed, 0 errored, 633 skipped
  stderr:
    --- drydock: progress ---
    cases: pass=2 fail=20 error=0 skip=633 total=655 from=result.stdout
    --- drydock: end progress ---
    --- drydock: values at failure ---
      result = CompletedProcess(args=['/mnt/c/Users/barlo/projects/drydock/.venv/bin/python', 'sources/spec_tests.py', '--program', '/mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261027.022726/build/commonmark/commonmark', '--spec', 'sources/spec.txt', '--pattern', '^Code spans$'], returncode=20, stdout='Example 330 (lines 5908-5912) Code spans\n`foo`\n\n--- expected HTML\n+++ actual HTML\n@@ -1 +1 @… (+3321 chars)
    --- drydock: end values ---
    Traceback (most recent call last):
      File "code-spans-conformance.py", line 12, in <module>
        assert result.returncode == 0
               ^^^^^^^^^^^^^^^^^^^^^^
    AssertionError

## Post-build programmatic acceptance
- PASS: code-spans-conformance (FEATURE-CodeSpans.md)
  intent: The completed inline parser passes every authoritative code-span example, including precedence interactions.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/.venv/bin/python
  provisioning: not required
  return code: 0
  stdout:
    22 passed, 0 failed, 0 errored, 633 skipped

## Repair attempts
- attempt 0 (initial build): failed; 0/1 checks; 19/22 cases model=gpt-6-luna; execution 20261027.024646.442Z-8a54751a; reason: programmatic acceptance failed: code-spans-conformance
- attempt 1 (repair 1): built; 1/1 checks; 22/22 cases model=gpt-6-luna; execution 20261027.024747.108Z-a4f84c25

## Build summary
RESULT: SUCCESS

FILES CHANGED:
- commonmark_parser/inline.py
- commonmark_parser/stages.py

SUMMARY:
Preserved trailing paragraph spaces needed by code spans and added left to right handling for inline HTML tags and autolinks. Scoped Code spans conformance passed: 22 passed, 0 failed. Related tests passed: 20 passed.

BLOCKERS:
- None
