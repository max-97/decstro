import pytest

from decstro import Model, ListElement


class TestListElement(Model):
    list_valued_element: list[int] = ListElement("someList", delimiter=",")


def test_list_element_int():
    xml = "<root><someList>1,2,3,4</someList></root>"
    model = TestListElement(xml)
    assert model.list_valued_element == [1, 2, 3, 4]
