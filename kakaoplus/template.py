from .base import Base

class Message(Base):
    def __init__(self, text=None, photo=None, message_button=None, **kwargs):
        super(Message, self).__init__(**kwargs)

        self.text = text
        self.photo = photo
        self.message_button = message_button


class Photo(Base):
    def __init__(self, url, width=640, height=480, **kwargs):
        super(Photo, self).__init__(**kwargs)

        self.url = url
        self.width = width
        self.height = height


class MessageButton(Base):
    def __init__(self, label, url, **kwargs):
        super(MessageButton, self).__init__(**kwargs)

        self.label = label
        self.url = url


class TextKeyboard(Base):
    def __init__(self, **kwargs):
        super(TextKeyboard, self).__init__(**kwargs)

        self.type = 'text'


class ButtonKeyboard(Base):
    def __init__(self, buttons, **kwargs):
        super(ButtonKeyboard, self).__init__(**kwargs)

        self.type = 'buttons'
        self.buttons = buttons
