import importlib
import subprocess
import sys
import unittest

import commonmark


class ArchitectureTests(unittest.TestCase):
    def test_public_input_boundary_exists(self):
        self.assertTrue(callable(getattr(importlib.import_module("commonmark"), "parse", None)))

    def test_public_render_boundary_round_trips_document(self):
        document = commonmark.parse("hello")
        self.assertEqual(commonmark.render(document), "<p>hello</p>\n")

    def test_public_cli_boundary_uses_stdin_and_stdout(self):
        result = subprocess.run(
            [sys.executable, "commonmark.py"],
            input="# title\n",
            text=True,
            capture_output=True,
            check=False,
        )
        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stdout, "<h1>title</h1>\n")

    def test_input_normalization_replaces_null_and_line_endings(self):
        self.assertEqual(commonmark.render(commonmark.parse("a\x00\r\nb")), "<p>a�\nb</p>\n")
