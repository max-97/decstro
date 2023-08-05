from decstro import XPath
from decstro.xpath import _is_list_type, _is_optional_type


class ListElement(XPath):

    def __init__(self, expression, /, delimiter: str = ";", default=None):
        self.delimiter = delimiter
        super().__init__(expression, default=default)

    def __set_name__(self, owner, name):
        self.attribute_name = name
        self.annotation = owner.__annotations__.get(name)

        if _is_optional_type(self.annotation):
            if not _is_list_type(self.annotation.__args__[0]):
                raise AttributeError("Attribute must be a list or optional list.")
        elif not _is_list_type(self.annotation):
            raise AttributeError("Attribute must be a list.")

    def extract(self, xml):
        elements = xml.xpath(self.expression)
        if elements:
            if _is_optional_type(self.annotation):
                return [self.annotation.__args__[0].__args__[0](x) for x in elements[0].text.split(self.delimiter)]
            return [self.annotation.__args__[0](x) for x in elements[0].text.split(self.delimiter)]
        else:
            if not _is_optional_type(self.annotation) and self.default is None:
                raise ValueError(f"""Element {self.expression} not found and no non-None default provided. Check the 
                XML definition or make the element optional.""")
            return self.default
