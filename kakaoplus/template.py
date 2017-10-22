class Photo(object):
    def __init__(self, url, width=640, height=480):
        self.url = url
        self.width = width
        self.height = height


class MessageButton(object):
    def __init__(self, label, url):
        self.label = label
        self.url = url


class Message(object):
    def __init__(self, text=None, photo=None, message_button=None):
        if text is None and photo is None and message_button is None:
            raise ValueError('At least one params is required')
        if not isinstance(text, str) and text is not None:
            raise ValueError('text type must be str')
        if not isinstance(message_button, MessageButton) and message_button is not None:
            raise ValueError('message_button must be template MessageButton type')
        if not isinstance(photo, Photo) and photo is not None:
            raise ValueError('photo must be template Photo type')
        self.text = text
        self.message_button = message_button
        self.photo = photo


class Keyboard(object):
    def __init__(self, buttons=None, type='text'):
        if type != 'text' and type != 'buttons':
            raise ValueError('Keyboard type must be buttons or text')
        if type == 'buttons':
            if not isinstance(buttons, list):
                raise ValueError('Buttons must be list include more than one element')
            self.buttons = buttons
        self.type = type
