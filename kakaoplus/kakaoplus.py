import sys
import json
import re

from .payload import Payload
from .template import *
from .utils import to_json

class Req(object):
    def __init__(self, data=None):
        if data is None:
            data = {}

        self.data = data

    @property
    def user_key(self):
        return self.data.get('user_key')

    @property
    def message_type(self):
        return self.data.get('type')

    @property
    def content(self):
        if sys.version_info >= (3, 0):
            content = self.data.get('content')
        else:
            content = self.data.get('content')
            if isinstance(content, unicode):
                content = content.encode('utf-8')

        return content

    @property
    def recieved_photo(self):
        return self.message_type == 'photo'

    @property
    def recieved_text(self):
        return self.message_type == 'text'


class KaKaoAgent(object):
    _button_callbacks = {}
    _button_callbacks_key_regex = {}
    _photo_handler = None
    _default_callback = None

    def handle_webhook(self, request):
        data = json.loads(request)
        req = Req(data)

        if req.recieved_photo:
            matched_callback = self._photo_handler
        elif req.recieved_text:
            matched_callback = self.get_content_callback(req)
        else:
            raise TypeError('Unknown type %s'%req.message_type)

        if matched_callback is not None:
            res = matched_callback(req)
        else:
            print("There is no matching handler")
            return "ok"

        if not isinstance(res, Payload):
            raise ValueError('Return type must be Payload')

        return res.to_json()

    '''
    decorators
    '''
    def photo_handler(self, func):
        self._photo_handler = func

    '''
    setting regular expressions
    '''

    def callback(self, payloads=None):
        if hasattr(payloads, '__call__'):
            self._default_callback = payloads
            return
        def wrapper(func):
            for payload in payloads:
                self._button_callbacks[payload] = func

            return func

        return wrapper

    def get_content_callback(self, req):
        callback = None
        for key in self._button_callbacks.keys():
            if key not in self._button_callbacks_key_regex:
                self._button_callbacks_key_regex[key] = re.compile(key + '$')
        for key in self._button_callbacks.keys():
            if self._button_callbacks_key_regex[key].match(req.content):
                callback = self._button_callbacks[key]
                print("matched callback handler %s"%key)
                break
        if callback is None:
            print("default callback handler")
            callback = self._default_callback

        return callback

    def handle_keyboard(self, func):
        def wrapper(*args, **kwargs):
            res = func(*args, **kwargs)
            return to_json(res)

        return wrapper