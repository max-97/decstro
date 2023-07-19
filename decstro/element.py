from decstro import XPath


class Element(XPath):

    def __init__(self, expression, /, default=None):
        super().__init__(f"./{expression}", default=default)
