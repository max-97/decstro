from typing import Union


class Element:
    def __init__(self, expression, /, default=None):
        self.expression = f"./{expression}"
        self.default = default

    def __set_name__(self, owner, name):
        self.attribute_name = name
        self.annotation = owner.__annotations__.get(name)

    def __get__(self, instance, owner):
        value = self.extract(instance.xml)
        instance.__dict__[self.attribute_name] = value
        return value

    def extract(self, xml):
        elements = xml.xpath(self.expression)
        if elements:
            if self._is_list_type(self.annotation):
                return [self.annotation.__args__[0](x) for x in elements]
            else:
                if len(elements) > 1:
                    raise ValueError(f"Multiple elements found for {self.expression} but only one expected.")
                if self._is_optional_type(self.annotation):
                    return self.annotation.__args__[0](elements[0])
                return self.annotation(elements[0])
        else:
            if not self._is_optional_type(self.annotation) and self.default is None:
                raise ValueError(f"""Element {self.expression} not found and no non-None default provided. Check the 
                XML definition or make the element optional.""")

            return self.default

    @staticmethod
    def _is_list_type(annotation):
        return hasattr(annotation, '__origin__') and annotation.__origin__ is list

    @staticmethod
    def _is_optional_type(annotation):
        return hasattr(annotation, '__origin__') and annotation.__origin__ is Union and \
            type(None) in annotation.__args__ and len(annotation.__args__) == 2
