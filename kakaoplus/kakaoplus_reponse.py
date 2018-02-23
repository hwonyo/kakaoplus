from abc import *


class KakaoPlusResponseBase(metaclass=ABCMeta):
    @abstractmethod
    def to_dict(self):
        pass


class KakaoPlusResponse(KakaoPlusResponseBase):
    def __init__(self, message, keyboard):
        self.message = message
        self.keyboard = keyboard

    @property
    def message(self):
        return self.__message

    @message.setter
    def message(self, val):
        if isinstance(val, Message):
            self.__message = val

    @property
    def keyboard(self):
        return self.__keyboard

    @keyboard.setter
    def keyboard(self, val):
        if isinstance(val, Keyboard):
            self.__keyboard = val

    def to_dict(self):
        return {
            'message': self.message.to_dict(),
            'keyboard': self.keyboard.to_dict()
        }


class Message(KakaoPlusResponseBase):
    def __init__(self, text, photo=None, message_btn=None):
        self.text = text
        self.photo = photo
        self.message_btn = message_btn

    @property
    def photo(self):
        return self.__photo

    @photo.setter
    def photo(self, val):
        if isinstance(val, Photo) or val is None:
            self.__photo = val

    @property
    def message_btn(self):
        return self.__message_btn

    @message_btn.setter
    def message_btn(self, val):
        if isinstance(val, MessageButton) or val is None:
            self.__message_btn = val

    def to_dict(self):
        photo_dict = None
        if self.photo:
            photo_dict = self.photo.to_dict()

        message_btn_dict = None
        if self.message_btn:
            message_btn_dict = self.message_btn.to_dict()

        return {
            'text': self.text,
            'photo': photo_dict,
            'message_button': message_btn_dict
        }


class Photo(KakaoPlusResponseBase):
    def __init__(self, url, width=720, height=630):
        self.url = url
        self.width = width
        self.height = height

    def to_dict(self):
        return {
            'url': self.url,
            'width': self.width,
            'height': self.height
        }


class MessageButton(KakaoPlusResponseBase):
    def __init__(self, label, url):
        self.label = label
        self.url = url

    def to_dict(self):
        return {
            'label': self.label,
            'url': self.url
        }


class Keyboard(KakaoPlusResponseBase):
    def __init__(self, type='text', buttons=None):
        self.type = type
        self.buttons = buttons

    @property
    def buttons(self):
        return self.__buttons

    @buttons.setter
    def buttons(self, val):
        if isinstance(val, list) or val is None:
            self.__buttons = val

    def to_dict(self):
        return {
            'type': self.type,
            'buttons': self.buttons
        }
