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
            if hasattr(self.annotation, '__origin__') and self.annotation.__origin__ is list:
                return [self.annotation.__args__[0](x) for x in elements]
            else:
                if len(elements) > 1:
                    raise ValueError(f"Multiple elements found for {self.expression} but only one expected.")
                if self.annotation:
                    return self.annotation(elements[0])
                else:
                    return elements[0]
        else:
            return self.default
