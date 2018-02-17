import json
import re

from .payload import Payload, KeyboardPayload
from .utils import PY3, _byteify, LOGGER

class Req(object):
    def __init__(self, data):
        if not PY3:
            self.data  = json.loads(data, object_hook=_byteify)
        else:
            self.data  = json.loads(data)

    @property
    def user_key(self):
        return self.data.get('user_key')

    @property
    def message_type(self):
        return self.data.get('type')

    @property
    def content(self):
        return self.data.get('content')

    @property
    def recieved_photo(self):
        return self.message_type == 'photo'

    @property
    def recieved_text(self):
        return self.message_type == 'text'


class KaKaoAgent(object):
    _keyboard_callback = None
    _message_callbacks = {}
    _message_callbacks_key_regex = {}
    _photo_handler = None
    _default_callback = None

    def handle_webhook(self, request):
        req = Req(request)
        res = Payload()

        if req.recieved_photo:
            matched_callback = self._photo_handler
        elif req.recieved_text:
            matched_callback = self.get_message_callback(req)
        else:
            LOGGER.warn('Unknown type %s' % req.message_type)
            return "ok"

        if matched_callback is not None:
            matched_callback(req, res)
        else:
            LOGGER.info("There is no matching handler")
            return "ok"

        if not res.message:
            LOGGER.info('Message Required at least one element')
            return "ok"

        return res.to_json()

    def handle_keyboard_webhook(self):
        res = KeyboardPayload()

        if self._keyboard_callback:
            self._keyboard_callback(res)

        return res.to_json()

    '''
    decorators
    '''
    def handle_photo(self, func):
        self._photo_handler = func

    def handle_keyboard(self, func):
        self._keyboard_callback = func

    '''
    setting regular expressions
    '''
    def handle_message(self, payloads=None):
        if callable(payloads):
            self._default_callback = payloads
            return
        def wrapper(func):
            for payload in payloads:
                self._message_callbacks[payload] = func
                self._message_callbacks_key_regex[payload] = re.compile(payload + '$')
            return func

        return wrapper

    def get_message_callback(self, req):
        callback = None

        for key in self._message_callbacks.keys():
            if self._message_callbacks_key_regex[key].match(req.content):
                callback = self._message_callbacks[key]
                LOGGER.info("matched message handler %s" % key)
                break
        if callback is None:
            LOGGER.info("default message handler")
            callback = self._default_callback

        return callback