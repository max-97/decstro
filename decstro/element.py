class Element:
    def __init__(self, expression, /, default=None, multiple=False):
        self.expression = f"./{expression}"
        self.default = default
        self.multiple = multiple

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
            if self.multiple:
                if self.annotation:
                    return [self.annotation(x) for x in elements]
                else:
                    return elements
            else:
                first = elements[0]
                if self.annotation:
                    return self.annotation(first)
                else:
                    return first
        else:
            return self.default
