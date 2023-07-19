from decstro import XPath


class Element(XPath):

    def __init__(self, expression, /, default=None):
        self.expression = f"./{expression}"
        self.default = default
