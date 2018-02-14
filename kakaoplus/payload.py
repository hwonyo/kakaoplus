from .base import Base

class Payload(Base):
    def __init__(self, **kwargs):
        super(Payload, self).__init__(**kwargs)

        self.message = dict()
        self.keyboard = {'type': 'text'}

    @property
    def text(self):
        return getattr(self.message, 'text', None)

    @text.setter
    def text(self, text):
        self.message['text'] = text

    @property
    def photo(self):
        return getattr(self.message, 'photo', None)

    @photo.setter
    def photo(self, value):
        self.message['photo'] = value

    @property
    def message_button(self):
        return getattr(self.message, 'message_button', None)

    @message_button.setter
    def message_button(self, value):
        self.message['message_button'] = value

    @property
    def keyboard_buttons(self):
        return getattr(self.keyboard, 'buttons', None)

    @keyboard_buttons.setter
    def keyboard_buttons(self, value):
        self.keyboard = {
            'type': 'buttons',
            'buttons': value
        }

class KeyboardPayload(Base):
    def __init__(self, **kwargs):
        super(KeyboardPayload, self).__init__(**kwargs)

        self.type = 'text'

    @property
    def keyboard_buttons(self):
        return getattr(self, 'keyboard', None)

    @keyboard_buttons.setter
    def keyboard_buttons(self, value):
        self.type = 'buttons'
        self.buttons = value