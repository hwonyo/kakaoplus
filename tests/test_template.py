import json
import unittest
from kakaoplus import template as Template
from kakaoplus import utils

class TemplateTest(unittest.TestCase):
    def test_photo(self):
        photo = Template.Photo('http://test.jpg')
        target = {'url': 'http://test.jpg',
                  'width': 640, 'height': 480}
        self.assertEqual(json.dumps(target, sort_keys=True), utils.to_json(photo))

    def test_message_button(self):
        message_button = Template.MessageButton('LINK', 'http://test.com')
        target = {'label': 'LINK', 'url': 'http://test.com'}
        self.assertEqual(json.dumps(target, sort_keys=True), utils.to_json(message_button))

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
        self.assertEqual(json.dumps(target, sort_keys=True), utils.to_json(message))

        with self.assertRaises(ValueError):
            Template.Message()

        with self.assertRaises(ValueError):
            Template.Message(photo='hi')

        with self.assertRaises(ValueError):
            Template.Message(message_button='check')

        with self.assertRaises(ValueError):
            Template.Message(text=1)

    def test_keyboard(self):
        keyboard = Template.Keyboard()
        self.assertEqual('{"type": "text"}', utils.to_json(keyboard))

        keyboard = Template.Keyboard(['1', '2', '3'], 'buttons')
        target = {'type': 'buttons',
                  'buttons': ['1', '2', '3']}
        self.assertEqual(json.dumps(target, sort_keys=True), utils.to_json(keyboard))

        with self.assertRaises(ValueError):
            Template.Keyboard(type='Text')

        with self.assertRaises(ValueError):
            Template.Keyboard(type='buttons', buttons='check')