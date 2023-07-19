from decstro import XPath
from decstro.xpath import _is_list_type


class Attribute(XPath):

    def __init__(self, expression, /, default=None):
        super().__init__(f"./@{expression}", default=default)

    def __set_name__(self, owner, name):
        self.attribute_name = name
        self.annotation = owner.__annotations__.get(name)
        if _is_list_type(self.annotation):
            raise AttributeError("Attribute cannot be a list.")
