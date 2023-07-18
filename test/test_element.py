import pytest

from decstro import Model, Element


class SimpleElement(Model):
    child: int = Element("child")


xml_error = "<root><child>notAnInt</child></root>"


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
