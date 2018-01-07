import json
import logging
import sys

LOGGER = logging.getLogger('kakaoplus')

PY3 = sys.version_info[0] == 3

def to_json(obj):
    return json.dumps(obj, default=lambda o: o.__dict__, sort_keys=True)


def _byteify(input):
    """
    for python2 encoding utf-8 error
    encode UTF-8

    Args:
        - input: unicode string

    Return: utf-8 encoded byte
    """
    if isinstance(input, dict):
        return {_byteify(key): _byteify(value)
                for key, value in input.items()}
    elif isinstance(input, list):
        return [_byteify(element) for element in input]
    elif isinstance(input, unicode):
        return input.encode('utf-8')
    else:
        return input