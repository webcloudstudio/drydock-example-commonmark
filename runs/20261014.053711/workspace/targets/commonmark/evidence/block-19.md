# Evidence: Block 19 · Service (block-19)

- block type: block
- date: 2026-10-14
- resulting state: closed/verified
- story points (combined assembled cost): 5295
- execution id: 20261014.074416.111Z-9e39bf16

## Stories built
- Parse block quotes with laziness and consecutiveness rules. (block-quotes) [story]

## Stacked context
- compass: COMPASS.md (SP 1072)
- implements: FEATURE-Block-Quotes.md (SP 2119)
- context: ARCHITECTURE_compact.md (SP 335)
- stack: common_compact.md (SP 1199)
- stack: python_compact.md (SP 390)

## Build directory changes
- mdparser/blocks.py
- mdparser/render.py
- tests/test_block_quotes.py
- tests/test_blocks.py

## Pre-build acceptance observation
- RED: quote-basic-content (FEATURE-Block-Quotes.md)
  intent: A quote with a heading and paragraph lines renders one blockquote containing one h1 and one paragraph.
  return code: 1
  stdout:
    <p>&gt; # Foo
    &gt; bar
    &gt; baz</p>
  stderr:
    --- drydock: values at failure ---
      result = CompletedProcess(args=['./commonmark'], returncode=0, stdout='<p>&gt; # Foo\n&gt; bar\n&gt; baz</p>\n', stderr='')
    --- drydock: end values ---
    Traceback (most recent call last):
      File "quote-basic-content.py", line 6, in <module>
        assert result.stdout.count("<blockquote>") == 1
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    AssertionError
- RED: quote-marker-space-optional (FEATURE-Block-Quotes.md)
  intent: The space after the marker is optional, and up to three spaces of indentation are allowed.
  return code: 1
  stdout:
    <p>&gt;# Foo
    &gt;bar</p>
  stderr:
    --- drydock: values at failure ---
      result = CompletedProcess(args=['./commonmark'], returncode=0, stdout='<p>&gt;# Foo\n&gt;bar</p>\n', stderr='')
    --- drydock: end values ---
    Traceback (most recent call last):
      File "quote-marker-space-optional.py", line 7, in <module>
        assert result.stdout.count("<blockquote>") == 1
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    AssertionError
- RED: quote-lazy-continuation (FEATURE-Block-Quotes.md)
  intent: An unmarked paragraph continuation line stays in the quote's paragraph.
  return code: 1
  stdout:
    <p>&gt; bar
    baz</p>
  stderr:
    --- drydock: values at failure ---
      result = CompletedProcess(args=['./commonmark'], returncode=0, stdout='<p>&gt; bar\nbaz</p>\n', stderr='')
    --- drydock: end values ---
    Traceback (most recent call last):
      File "quote-lazy-continuation.py", line 6, in <module>
        assert result.stdout.count("<blockquote>") == 1
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    AssertionError
- RED: quote-nested-lazy (FEATURE-Block-Quotes.md)
  intent: Omitted markers on a nested quote's continuation line still keep three nesting levels and one paragraph.
  return code: 1
  stdout:
    <p>&gt; &gt; &gt; foo
    bar</p>
  stderr:
    --- drydock: values at failure ---
      result = CompletedProcess(args=['./commonmark'], returncode=0, stdout='<p>&gt; &gt; &gt; foo\nbar</p>\n', stderr='')
    --- drydock: end values ---
    Traceback (most recent call last):
      File "quote-nested-lazy.py", line 6, in <module>
        assert result.stdout.count("<blockquote>") == 3
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    AssertionError
- RED: quote-blank-line-separates (FEATURE-Block-Quotes.md)
  intent: A blank line separates two quotes, and adjacent marked lines form one quote.
  return code: 1
  stdout:
    <p>&gt; foo</p>
    <p>&gt; bar</p>
    
    <p>&gt; foo
    &gt; bar</p>
  stderr:
    --- drydock: values at failure ---
      separated = CompletedProcess(args=['./commonmark'], returncode=0, stdout='<p>&gt; foo</p>\n<p>&gt; bar</p>\n', stderr='')
    --- drydock: end values ---
    Traceback (most recent call last):
      File "quote-blank-line-separates.py", line 9, in <module>
        assert separated.stdout.count("<blockquote>") == 2
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    AssertionError
- RED: quote-interrupts-paragraph (FEATURE-Block-Quotes.md)
  intent: A quote interrupts a paragraph, leaving one paragraph before it and one inside it.
  return code: 1
  stdout:
    <p>foo
    &gt; bar</p>
  stderr:
    --- drydock: values at failure ---
      result = CompletedProcess(args=['./commonmark'], returncode=0, stdout='<p>foo\n&gt; bar</p>\n', stderr='')
    --- drydock: end values ---
    Traceback (most recent call last):
      File "quote-interrupts-paragraph.py", line 6, in <module>
        assert result.stdout.count("<blockquote>") == 1
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    AssertionError
- GREEN (prepassed): quote-four-spaces-is-code (FEATURE-Block-Quotes.md)
  intent: Four spaces before the marker make an indented code block, not a quote.
  return code: 0
  stdout:
    <pre><code>&gt; foo
    </code></pre>
- RED: quote-no-lazy-code (FEATURE-Block-Quotes.md)
  intent: Laziness does not apply to indented code, so the unmarked indented line becomes its own code block.
  return code: 1
  stdout:
    <p>&gt;     foo
    bar</p>
  stderr:
    --- drydock: values at failure ---
      result = CompletedProcess(args=['./commonmark'], returncode=0, stdout='<p>&gt;     foo\nbar</p>\n', stderr='')
    --- drydock: end values ---
    Traceback (most recent call last):
      File "quote-no-lazy-code.py", line 6, in <module>
        assert result.stdout.count("<blockquote>") == 1
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    AssertionError

## Post-build programmatic acceptance
- PASS: quote-basic-content (FEATURE-Block-Quotes.md)
  intent: A quote with a heading and paragraph lines renders one blockquote containing one h1 and one paragraph.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261014.053711/build/commonmark/.venv/bin/python
  provisioning: not required
  return code: 0
  stdout:
    <blockquote>
    <h1>Foo</h1>
    <p>bar
    baz</p>
    </blockquote>
- PASS: quote-marker-space-optional (FEATURE-Block-Quotes.md)
  intent: The space after the marker is optional, and up to three spaces of indentation are allowed.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261014.053711/build/commonmark/.venv/bin/python
  provisioning: not required
  return code: 0
  stdout:
    <blockquote>
    <h1>Foo</h1>
    <p>bar</p>
    </blockquote>
    
    <blockquote>
    <h1>Foo</h1>
    <p>bar</p>
    </blockquote>
- PASS: quote-lazy-continuation (FEATURE-Block-Quotes.md)
  intent: An unmarked paragraph continuation line stays in the quote's paragraph.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261014.053711/build/commonmark/.venv/bin/python
  provisioning: not required
  return code: 0
  stdout:
    <blockquote>
    <p>bar
    baz</p>
    </blockquote>
- PASS: quote-nested-lazy (FEATURE-Block-Quotes.md)
  intent: Omitted markers on a nested quote's continuation line still keep three nesting levels and one paragraph.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261014.053711/build/commonmark/.venv/bin/python
  provisioning: not required
  return code: 0
  stdout:
    <blockquote>
    <blockquote>
    <blockquote>
    <p>foo
    bar</p>
    </blockquote>
    </blockquote>
    </blockquote>
- PASS: quote-blank-line-separates (FEATURE-Block-Quotes.md)
  intent: A blank line separates two quotes, and adjacent marked lines form one quote.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261014.053711/build/commonmark/.venv/bin/python
  provisioning: not required
  return code: 0
  stdout:
    <blockquote>
    <p>foo</p>
    </blockquote>
    <blockquote>
    <p>bar</p>
    </blockquote>
    
    <blockquote>
    <p>foo
    bar</p>
    </blockquote>
- PASS: quote-interrupts-paragraph (FEATURE-Block-Quotes.md)
  intent: A quote interrupts a paragraph, leaving one paragraph before it and one inside it.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261014.053711/build/commonmark/.venv/bin/python
  provisioning: not required
  return code: 0
  stdout:
    <p>foo</p>
    <blockquote>
    <p>bar</p>
    </blockquote>
- PASS: quote-four-spaces-is-code (FEATURE-Block-Quotes.md)
  intent: Four spaces before the marker make an indented code block, not a quote.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261014.053711/build/commonmark/.venv/bin/python
  provisioning: not required
  return code: 0
  stdout:
    <pre><code>&gt; foo
    </code></pre>
- PASS: quote-no-lazy-code (FEATURE-Block-Quotes.md)
  intent: Laziness does not apply to indented code, so the unmarked indented line becomes its own code block.
  target interpreter: /mnt/c/Users/barlo/projects/drydock/uat/CommonMark/runs/20261014.053711/build/commonmark/.venv/bin/python
  provisioning: not required
  return code: 0
  stdout:
    <blockquote>
    <pre><code>foo
    </code></pre>
    </blockquote>
    <pre><code>bar
    </code></pre>

## Build summary
I'll start by inspecting the build directory and the staged sources.The project already has an `mdparser` package, tests, and a launcher from earlier blocks. I'll read those before changing anything.The block parser is the core of this change, so I'll read it in full.The engine is a registry of block types with start, continue, and lazy rules, which fits block quotes well. Before I write anything, I'll check how the existing tests exercise `Cursor` and the registry, since I plan to touch both.Two existing tests touch what I plan to change: a test asserts the whole-tab overshoot behaviour, and another pins the default registry's start-rule tuple. I'll read both before deciding how to handle them.The suite run exceeded the foreground timeout and moved to the background. I'll read the test sections directly while it finishes.I have what I need. The plan, and the reasoning behind it:

- **Engine:** a `BLOCK_QUOTE` container with a `>` marker rule, registered in `DEFAULT_REGISTRY`. Lazy continuation already exists for paragraphs, so the quote only needs to match its marker.
- **Laziness:** a line that can only lazily continue an open paragraph must not start indented code or a type-7 HTML block. Right now those start rules check only the matched container, so I'll add a line-level flag on the cursor.
- **Tabs:** the spec requires a partly consumed tab to leave its remaining columns as content. The existing `advance_columns` consumes straddling tabs whole, and an existing test asserts that. I'll add a separate `consume_columns` method instead of changing that behaviour.

I'll start with the cursor.The background baseline run has finished. I'll check its result against the pre-change state before going further.The baseline is 948 passed and 1 skipped, which is green. Now I'll finish the engine: the lazy-paragraph check in step 2, the start-rule guards, and the block quote type.Next, the block quote type itself, placed after the HTML block and registered in the default registry.Now the renderer: a block quote renders its children between `<blockquote>` tags, and the top-level walk shares the same child-rendering helper.Before writing tests, I'll run the executable on the spec-style inputs, including the tab and laziness cases, to see the actual output.All of these match CommonMark: including `>\t\tfoo` → `  foo` inside `<pre>`, and the lazy `    bar` continuation. The tab splitting, the lazy rules, and the tree shape are right.

Now the tests. I'll transcribe the eight declared acceptance checks with their assertions unchanged, then add tests for the rest of the behaviour. I'll also update one existing registry test whose expected start-rule tuple now legitimately includes the block quote.The file is written, but I spotted three things to fix before running it: a wrong comment on the two-tab case (the arithmetic is six columns of indentation, not what I wrote), a misleading test name, and a duplicate indented-code test.Now I'll run the new block quote tests and the closely related block-engine tests, which are the ones most likely to be affected by the cursor and laziness changes.All 430 pass. Next, the full project suite, since earlier blocks' tests also exercise the block engine. The previous run took about two minutes, so I'll give it a longer timeout.The full suite is green: 991 passed (the earlier 948 plus 43 new), with the same single pre-existing skip. I'll confirm which files changed so the report matches the working tree.Block quotes are implemented. All eight declared acceptance checks pass, and the project suite is green at 991 passed with 1 skipped (the skip was already there before this block).

<blueprint-decisions>
[{"spec":"FEATURE-Block-Quotes.md","severity":"Low","subject":"Partly consumed tab after the quote marker","decision":"The spec requires a tab that is only partly consumed to leave its remaining columns as content indentation. I added a separate Cursor.consume_columns method for this and left advance_columns unchanged, because an existing unit test pins its whole-tab overshoot. Indented code's start and continue rules now use consume_columns so that the spec's >\\t\\tfoo example renders as two spaces inside pre. Fenced-code indentation removal still uses advance_columns, so a tab straddling a fence's indentation is still consumed whole. Is that acceptable, or should fenced code move to consume_columns on replan?"}]
</blueprint-decisions>

RESULT: SUCCESS

FILES CHANGED:
- mdparser/blocks.py
- mdparser/render.py
- tests/test_blocks.py
- tests/test_block_quotes.py

SUMMARY:
- **Block quote container** (`mdparser/blocks.py`): a `BLOCK_QUOTE` container type, registered last in `DEFAULT_REGISTRY`. It starts and continues on a `>` with up to three columns of indentation and one optional column. Nested quotes work, and a blank line ends a quote.
- **Laziness**: a line that can only lazily continue an open paragraph now sees a `cursor.lazy_paragraph` flag. Indented code and type-7 HTML blocks cannot start on such a line, so `> foo` followed by `    bar` stays paragraph text. Headings, fences, thematic breaks and type-6 HTML still close the quote.
- **Tabs**: `Cursor.consume_columns` splits a straddling tab and reports the remaining columns through `rest` as spaces. Indented code uses it too.
- **Rendering** (`mdparser/render.py`): `<blockquote>\n…</blockquote>\n`, recursive through a shared `_render_children` helper. An empty quote renders as two lines.
- **Tests**:
  - `tests/test_block_quotes.py` (new): the eight declared checks, transcribed with their assertions unchanged. Also exact-output tests, block-tree tests, lazy-rule tests and cursor tests.
  - `tests/test_blocks.py`: the default registry test's expected start-rule tuple now includes `BLOCK_QUOTE`. This is the only existing assertion I changed, and only because the registry legitimately grew.
- **Verification**:
  - The eight declared checks: pass (430 passed across the block-quote and related block-engine test files).
  - Full project pytest: 991 passed, 1 skipped (the skip predates this block). Before this block the count was 948 passed, 1 skipped.
  - I did not run `sources/full_test.sh`. No criterion in this step declares it, and the corpus examples that use lists are gated to the lists story.
- `sources/` is untouched, and I did not run any git add or commit.
