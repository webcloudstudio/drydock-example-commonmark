# Evidence: Block 5 · Service (block-5)

- block type: block
- date: 2026-10-14
- resulting state: closed/verified
- story points (combined assembled cost): 4942
- execution id: 20261014.060510.463Z-6890125c

## Stories built
- Parse raw inline HTML tags, comments, processing instructions, declarations and CDATA. (raw-html-inline) [story]

## Stacked context
- compass: COMPASS.md (SP 1072)
- implements: FEATURE-Raw-HTML.md (SP 1719)
- context: ARCHITECTURE_compact.md (SP 335)
- stack: common_compact.md (SP 1199)
- stack: python_compact.md (SP 390)

## Build directory changes
- mdparser/inlines.py
- tests/test_autolinks.py
- tests/test_raw_html.py
- tests/test_render.py

## Pre-build acceptance observation
- RED: rawhtml-open-and-close-tags (FEATURE-Raw-HTML.md)
  intent: Valid open, self-closing and closing tags in a paragraph pass through verbatim.
  return code: 1
  stdout:
    <p>Foo &lt;a&gt;&lt;bab&gt;&lt;c2c&gt; &lt;a href=&quot;x&quot; data-k=v /&gt; &lt;/a&gt;&lt;/foo &gt;</p>
  stderr:
    --- drydock: values at failure ---
      tags = '<a><bab><c2c> <a href="x" data-k=v /> </a></foo >'
      result = CompletedProcess(args=['./commonmark'], returncode=0, stdout='<p>Foo &lt;a&gt;&lt;bab&gt;&lt;c2c&gt; &lt;a href=&quot;x&quot; data-k=v /&gt; &lt;/a&gt;&lt;/foo &gt;</p>\n', stderr='')
    --- drydock: end values ---
    Traceback (most recent call last):
      File "rawhtml-open-and-close-tags.py", line 7, in <module>
        assert tags in result.stdout
               ^^^^^^^^^^^^^^^^^^^^^
    AssertionError
- RED: rawhtml-comment-pi-declaration-cdata (FEATURE-Raw-HTML.md)
  intent: Inline comments, processing instructions, declarations and CDATA pass through verbatim.
  return code: 1
  stdout:
    <p>foo &lt;!-- a comment --&gt; bar</p>
  stderr:
    --- drydock: values at failure ---
      fragment = '<!-- a comment -->'
      result = CompletedProcess(args=['./commonmark'], returncode=0, stdout='<p>foo &lt;!-- a comment --&gt; bar</p>\n', stderr='')
    --- drydock: end values ---
    Traceback (most recent call last):
      File "rawhtml-comment-pi-declaration-cdata.py", line 7, in <module>
        assert fragment in result.stdout
               ^^^^^^^^^^^^^^^^^^^^^^^^^
    AssertionError
- GREEN (prepassed): rawhtml-illegal-forms-escaped (FEATURE-Raw-HTML.md)
  intent: Illegal tag names are not raw HTML, so only the paragraph tags contribute angle brackets.
  return code: 0
  stdout:
    <p>&lt;33&gt; &lt;__&gt;</p>
- GREEN (prepassed): rawhtml-closing-tag-with-attributes (FEATURE-Raw-HTML.md)
  intent: A closing tag with attributes is not raw HTML, so no extra angle brackets appear in the output.
  return code: 0
  stdout:
    <p>&lt;/a href=&quot;foo&quot;&gt;</p>
- RED: rawhtml-backslash-inert (FEATURE-Raw-HTML.md)
  intent: A backslash inside a tag attribute value is preserved and not treated as an escape.
  return code: 1
  stdout:
    <p>foo &lt;a href=&quot;*&quot;&gt;</p>
  stderr:
    --- drydock: values at failure ---
      tag = '<a href="\\*">'
      result = CompletedProcess(args=['./commonmark'], returncode=0, stdout='<p>foo &lt;a href=&quot;*&quot;&gt;</p>\n', stderr='')
    --- drydock: end values ---
    Traceback (most recent call last):
      File "rawhtml-backslash-inert.py", line 7, in <module>
        assert tag in result.stdout
               ^^^^^^^^^^^^^^^^^^^^
    AssertionError

## Post-build programmatic acceptance
- PASS: rawhtml-open-and-close-tags (FEATURE-Raw-HTML.md)
  intent: Valid open, self-closing and closing tags in a paragraph pass through verbatim.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261014.053711/build/commonmark/.venv/bin/python
  provisioning: not required
  return code: 0
  stdout:
    <p>Foo <a><bab><c2c> <a href="x" data-k=v /> </a></foo ></p>
- PASS: rawhtml-comment-pi-declaration-cdata (FEATURE-Raw-HTML.md)
  intent: Inline comments, processing instructions, declarations and CDATA pass through verbatim.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261014.053711/build/commonmark/.venv/bin/python
  provisioning: not required
  return code: 0
  stdout:
    <p>foo <!-- a comment --> bar</p>
    
    <p>foo <?php echo $a; ?> bar</p>
    
    <p>foo <!ELEMENT br EMPTY> bar</p>
    
    <p>foo <![CDATA[>&<]]> bar</p>
- PASS: rawhtml-illegal-forms-escaped (FEATURE-Raw-HTML.md)
  intent: Illegal tag names are not raw HTML, so only the paragraph tags contribute angle brackets.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261014.053711/build/commonmark/.venv/bin/python
  provisioning: not required
  return code: 0
  stdout:
    <p>&lt;33&gt; &lt;__&gt;</p>
- PASS: rawhtml-closing-tag-with-attributes (FEATURE-Raw-HTML.md)
  intent: A closing tag with attributes is not raw HTML, so no extra angle brackets appear in the output.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261014.053711/build/commonmark/.venv/bin/python
  provisioning: not required
  return code: 0
  stdout:
    <p>&lt;/a href=&quot;foo&quot;&gt;</p>
- PASS: rawhtml-backslash-inert (FEATURE-Raw-HTML.md)
  intent: A backslash inside a tag attribute value is preserved and not treated as an escape.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261014.053711/build/commonmark/.venv/bin/python
  provisioning: not required
  return code: 0
  stdout:
    <p>foo <a href="\*"></p>

## Build summary
I'll start by inspecting the build directory to see what earlier blocks already produced.The autolink block is the closest precedent for this step. I'll read its tests, the conftest, and the spec's raw HTML section before writing anything.Tests in this project compare exact returned strings and executable stdout. Before writing the grammar, I'll confirm two things: the spec's exact comment and declaration wording, and how `blocks.py` joins paragraph lines, since raw HTML can span a line ending.The spec confirms the grammar in `FEATURE-Raw-HTML.md`, and paragraph content is joined with `\n`, so a raw tag can span lines. No block-level rule in `blocks.py` claims a `<` line, so the acceptance inputs reach the inline hook as paragraphs. Next I'll add the raw HTML matcher to the inline scanner, ahead of the escape fallback and after autolinks.Now the test file. It follows `test_autolinks.py`: the declared acceptance checks first, then finer grammar tests, each comparing an exact returned string or exact stdout bytes.Before running anything, I want to fix one weakness in what I just wrote. The illegal-form tests compute their expected value with `inlines.escape_html`, which is the code under test. That makes the oracle circular. I'll replace each with a literal expected string.Now I'll remove the `_escaped` helper, which no test uses any more, and run the new file together with the existing suite.One failure, and the mistake is in my expected value, not the code. In `<a b=c<d>` the trailing `<d>` is itself a valid open tag, so only the leading `<a b=c` is escaped. The output is correct under the spec. I'll fix the expectation and keep the case.The new file is green. Next I'll run the rest of the project suite to confirm the inline change didn't break the earlier blocks. The autolinks file has a test that invokes the staged `spec_tests.py`. This step declares no staged-suite criterion, so I'll deselect those corpus-section tests rather than run the staged suite early.Two existing tests now fail, and both fail for the same reason. `<b>` and `<a>` are valid raw HTML tags under the spec, and the earlier blocks' tests assumed they would be escaped. The new output is what the spec requires. I'll update those two expectations and keep each test's input unchanged, so the cases still exercise what they were written to exercise.Re-running the project suite with the same corpus deselection, plus the executable's behavior on the declared acceptance inputs:The inline change is complete and the project suite is green at 262 passed. I'll confirm the set of files written.Raw inline HTML is implemented in `mdparser/inlines.py`. The four declared acceptance checks pass, and the project's pytest suite is green at 262 passed.

I did not run `sources/full_test.sh` or the staged `spec_tests.py`. This step declares no criterion that invokes the staged suite, so I left it alone. The autolinks corpus test, which runs the staged suite scoped to Autolinks, is deselected from my runs for the same reason.

Two earlier tests encoded behavior the spec overrides, so I changed their expectations. Their inputs are unchanged:
- `tests/test_render.py`: `a<b>&"c"` now expects `a<b>&amp;&quot;c&quot;`, because `<b>` is a valid raw tag.
- `tests/test_autolinks.py`: `<http://e.com/<a>` now expects `&lt;http://e.com/<a>`, because `<a>` is a valid raw tag. Only the leading `<` is escaped.

Choices I made where the spec left room:
- A tag needs whitespace before each attribute name, so `<a b="x"c>` is escaped text.
- Each construct is tried in order after autolinks, so a `<` that opens nothing falls through to escaping.

RESULT: SUCCESS

FILES CHANGED:
- mdparser/inlines.py
- tests/test_raw_html.py
- tests/test_render.py
- tests/test_autolinks.py

SUMMARY:
- `inlines.py`: added the raw HTML grammars (open and closing tags, comments including `<!-->` and `<!--->`, processing instructions, declarations, CDATA). `parse_inline` tries autolinks first, then raw HTML, and passes a match through byte for byte. Backslashes and entities inside a match are not processed.
- `tests/test_raw_html.py` (new): the four declared acceptance checks plus the backslash-inert check, transcribed from `FEATURE-Raw-HTML.md`. Also grammar tests for legal and illegal forms of every construct, including line endings inside tags and the escaping of a backslash before `<`. Every test compares exact output.
- Test runs: `tests/test_raw_html.py` alone passed 81 of 81 after the fix. The full project suite, with the staged-suite corpus test deselected, passed 262 of 262.
- The staged `sources/` files are unchanged.

<blueprint-decisions>
[{"spec":"FEATURE-Raw-HTML.md","severity":"Material","subject":"Two earlier-block test expectations updated for raw HTML","decision":"tests/test_render.py expected 'a&lt;b&gt;...' for input 'a<b>&\"c\"', and tests/test_autolinks.py expected '&lt;http://e.com/&lt;a&gt;' for input '<http://e.com/<a>'. Both inputs are valid raw HTML open tags (<b>, <a>), which the spec now passes through. I kept the inputs and changed only the expected values, so each test still checks its original escaping of &, \", and the leading <. Is that acceptable, or should these tests change their inputs instead?"}]
</blueprint-decisions>

RESULT: SUCCESS
