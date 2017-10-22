import json
import unittest

from kakao import payload as Payload
from kakao import template as Template

class PayloadTest(unittest.TestCase):
    def test_payload(self):
        message = Template.Message('hi')
        p = Payload.Payload(message)
        target = {'message': {'text': 'hi', 'message_button': None, 'photo': None}}
        self.assertEqual(json.dumps(target, sort_keys=True), p.to_json())

        keyboard = Template.Keyboard('buttons', ['1', '2', '3'])
        p = Payload.Payload(message, keyboard=keyboard)
        target = {'message': {'text': 'hi', 'message_button': None, 'photo': None},
                  'keyboard': {'type': 'buttons', 'buttons': ['1', '2', '3']}}
        self.assertEqual(json.dumps(target, sort_keys=True), p.to_json())

        with self.assertRaises(ValueError):
            Payload.Payload("hi")

        with self.assertRaises(ValueError):
            Payload.Payload(Template.Message('hi'), [1, 2, 3])