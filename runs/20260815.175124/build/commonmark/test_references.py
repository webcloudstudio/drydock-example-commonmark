import unittest

from commonmark import parse, render


class ReferenceDefinitionTests(unittest.TestCase):
    def test_labels_use_casefold_and_collapsed_whitespace(self):
        document = parse("[  FOO\n bar ]: /url\n\n[foo bar]\n")
        self.assertEqual(render(document), '<p><a href="/url">foo bar</a></p>\n')

    def test_definition_is_document_wide_and_first_wins(self):
        document = parse("[foo]\n\n> [foo]: /first\n> [foo]: /second\n")
        self.assertEqual(render(document), '<p><a href="/first">foo</a></p>\n<blockquote>\n\n</blockquote>\n')

    def test_invalid_definition_remains_visible(self):
        document = parse("[foo]: <bar>(baz)\n\n[foo]\n")
        self.assertEqual(render(document), '<p>[foo]: <bar>(baz)</p>\n<p>[foo]</p>\n')

    def test_multiline_title_is_preserved(self):
        document = parse("[foo]: /url '\ntitle\nline1\n'\n\n[foo]\n")
        self.assertIn('title="\ntitle\nline1\n"', render(document))

    def test_escaped_destination_parenthesis_is_not_structural(self):
        document = parse("[foo]: /url\\)\n\n[foo]\n")
        self.assertEqual(render(document), '<p><a href="/url)">foo</a></p>\n')

    def test_definition_inside_list_is_document_wide(self):
        document = parse("[foo]\n\n- [foo]: /url\n")
        self.assertEqual(render(document), '<p><a href="/url">foo</a></p>\n<ul>\n<li></li>\n</ul>\n')


if __name__ == "__main__":
    unittest.main()
