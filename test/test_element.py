import pytest

from decstro import Model, Element


class SimpleElement(Model):
    child: int = Element("child")


xml = "<root><child>42</child></root>"
xml_error = "<root><child>notAnInt</child></root>"


def test_simple_element():
    model = SimpleElement(xml)
    assert model.child == 42


def test_simple_element_error():
    with pytest.raises(ValueError):
        SimpleElement(xml_error)
