from decstro import XPath
from decstro.xpath import _is_list_type


class ListElement(XPath):

    def __init__(self, expression, /, delimiter: str = ";", default=None):
        self.delimiter = delimiter
        super().__init__(expression, default=default)

    def __set_name__(self, owner, name):
        self.attribute_name = name
        self.annotation = owner.__annotations__.get(name)
        if not _is_list_type(self.annotation):
            raise AttributeError("Attribute must be a list.")

    def extract(self, xml):
        elements = xml.xpath(self.expression)
        if elements:
            return [self.annotation.__args__[0](x) for x in elements[0].text.split(self.delimiter)]
        else:
            return self.default
