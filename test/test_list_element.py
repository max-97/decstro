from typing import Optional

import pytest

from decstro import Model, ListElement


class TestListElement(Model):
    list_valued_element: list[int] = ListElement("someList", delimiter=",")


def test_list_element_int():
    xml = "<root><someList>1,2,3,4</someList></root>"
    model = TestListElement(xml)
    assert model.list_valued_element == [1, 2, 3, 4]


def test_empty_list_element_without_default_errors():
    xml = "<root></root>"
    with pytest.raises(ValueError):
        TestListElement(xml)


class ListElementString(Model):
    list_valued_element: list[str] = ListElement("someList", delimiter=",")


def test_list_element_string():
    xml = "<root><someList>1,2,3,4</someList></root>"
    model = ListElementString(xml)
    assert model.list_valued_element == ["1", "2", "3", "4"]


class ListElementWithDefault(Model):
    list_valued_element: list[int] = ListElement("someList", delimiter=",", default=[])


def test_optional_list_element():
    xml = "<root></root>"
    model = ListElementWithDefault(xml)
    assert model.list_valued_element == []


class OptionalListElementWithoutDefault(Model):
    list_valued_element: Optional[list[int]] = ListElement("someList", delimiter=",")


def test_optional_list_element_empty_xml():
    xml = "<root></root>"
    model = OptionalListElementWithoutDefault(xml)
    assert model.list_valued_element is None


def test_optional_list_element_with_value():
    xml = "<root><someList>1,2,3,4</someList></root>"
    model = OptionalListElementWithoutDefault(xml)
    assert model.list_valued_element == [1, 2, 3, 4]
