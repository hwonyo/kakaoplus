from . import utils
from .template import *

class Payload(object):
    def __init__(self, message=None, keyboard=None):
        if message is not None and not isinstance(message, Message):
            raise ValueError("message type must be template Message type")
        if keyboard is not None and not isinstance(keyboard, Keyboard):
            raise ValueError("keyboard type must be template Keyboard type")
        self.message = message
        if keyboard is not None:
            self.keyboard = keyboard

    def to_json(self):
        return utils.to_json(self)
