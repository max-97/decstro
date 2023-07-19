from typing import Optional

import pytest

from decstro import Model, Attribute


class SimpleAttribute(Model):
    id: int = Attribute("id")


def test_simple_attribute():
    xml = "<simple id='1' />"
    simple = SimpleAttribute(xml)
    assert simple.id == 1


def test_error_on_list_attribute():
    with pytest.raises(RuntimeError):
        class AttributeWithList(Model):
            ids: list[int] = Attribute("ids")


class OptionalAttribute(Model):
    id: Optional[int] = Attribute("id", default=1)


def test_optional_attribute():
    xml = "<optional />"
    optional = OptionalAttribute(xml)
    assert optional.id == 1
