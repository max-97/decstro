import lxml.objectify


class Model:
    """Abstract base class for your models."""
    def __init__(self, data):
        if isinstance(data, str):
            self.xml = lxml.objectify.fromstring(data)
        elif isinstance(data, lxml.objectify.ObjectifiedElement):
            self.xml = data
        else:
            raise TypeError("Unsupported data type:", type(data))
