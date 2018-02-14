import json

from .utils import to_json


class Base(object):
    """Base class of model.
    Suitable for JSON base data.
    """

    def __init__(self, **kwargs):
        pass

    def __str__(self):
        return json.dumps(self.__dict__)

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        if isinstance(other, dict):
            return other == self.__dict__
        elif isinstance(other, Base):
            return self.__dict__ == other.__dict__
        return other == str(self)

    def __ne__(self, other):
        return not self.__eq__(other)

    def to_json(self):
        return to_json(self)