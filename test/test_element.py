from typing import Optional

import pytest

from decstro import Model, Element


class SimpleElement(Model):
    child: int = Element("child")


def test_simple_element():
    xml = "<root><child>42</child></root>"
    model = SimpleElement(xml)
    assert model.child == 42


def test_error_on_mismatch_type():
    xml = "<root><child>notAnInt</child></root>"
    with pytest.raises(ValueError):
        SimpleElement(xml)


def test_error_on_too_many_elements():
    xml = "<root><child>42</child><child>43</child></root>"
    with pytest.raises(ValueError):
        SimpleElement(xml)


class ManyElements(Model):
    a: str = Element("a")
    b: int = Element("b")
    c: float = Element("c")


def test_many_elements():
    xml = "<root><a>foo</a><b>42</b><c>3.14</c></root>"
    model = ManyElements(xml)
    assert model.a == "foo"
    assert model.b == 42
    assert model.c == 3.14


class MultipleElement(Model):
    children: list[int] = Element("child")


def test_multiple_element():
    xml = "<root><child>42</child><child>43</child></root>"
    model = MultipleElement(xml)
    assert model.children == [42, 43]


def test_element_without_annotation_errors():
    with pytest.raises(RuntimeError):
        class ElementWithoutAnnotation(Model):
            child = Element("child")


class OptionalElement(Model):
    child: Optional[int] = Element("child", default=42)


def test_optional_element():
    xml = "<root></root>"
    model = OptionalElement(xml)
    assert model.child == 42
