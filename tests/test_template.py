import json
import unittest
from kakaoplus import template as Template
from kakaoplus import utils

class TemplateTest(unittest.TestCase):
    def test_photo(self):
        photo = Template.Photo('http://test.jpg')
        target = {'url': 'http://test.jpg',
                  'width': 640, 'height': 480}
        self.assertEqual(target, photo)

    def test_message_button(self):
        message_button = Template.MessageButton('LINK', 'http://test.com')
        target = {'label': 'LINK', 'url': 'http://test.com'}
        self.assertEqual(target, message_button)

    def test_message(self):
        message = Template.Message(
            'hi',
            Template.Photo('http://test.jpg'),
            Template.MessageButton('LINK', 'http://test.com'),
        )
        target = {
            'text': 'hi',
            'photo': {'url': 'http://test.jpg', 'width': 640, 'height': 480},
            'message_button': {'label': 'LINK', 'url': 'http://test.com'}
        }
        self.assertEqual(target, message)

    def test_keyboard(self):
        keyboard = Template.TextKeyboard()
        self.assertEqual('{"type": "text"}', utils.to_json(keyboard))

        keyboard = Template.ButtonKeyboard(['1', '2', '3'])
        target = {'type': 'buttons',
                  'buttons': ['1', '2', '3']}
        self.assertEqual(target, keyboard)