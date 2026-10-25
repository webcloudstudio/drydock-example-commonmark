"""Foundation contract checks for the parser package and phase flow."""

import importlib.util

from commonmark.parser import parse


def test_parser_is_an_importable_package():
    spec = importlib.util.find_spec("commonmark")
    assert spec is not None
    assert spec.submodule_search_locations is not None


def test_empty_document_flows_through_parser():
    assert parse("") == ""
