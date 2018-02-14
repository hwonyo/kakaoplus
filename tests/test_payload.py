import unittest

from kakaoplus import payload as Payload

class PayloadTest(unittest.TestCase):
    def test_payload(self):
        p = Payload.Payload()
        p.text = 'hi'
        p.photo = {
            'url': 'https://photo.src',
            'width': 640,
            'height': 480
        }
        p.message_button = {
            'label': 'test',
            'url': 'test.url'
        }
        target = {
            'message': {
                'text': 'hi',
                'photo': {
                    'url': 'https://photo.src',
                    'width': 640,
                    'height': 480
                },
                'message_button': {
                    'label': 'test',
                    'url': 'test.url'
                }
            },
            'keyboard': {'type': 'text'}}
        self.assertEqual(target, p)

        p = Payload.Payload()
        p.text = 'hi'
        p.keyboard_buttons = ['1', '2', '3']
        target = {'message': {'text': 'hi'},
                  'keyboard': {'type': 'buttons', 'buttons': ['1', '2', '3']}}
        self.assertEqual(target, p)

    def test_keyboard_payload(self):
        kp = Payload.KeyboardPayload()
        self.assertEqual(
            kp,
            {
                'type': 'text'
            }
        )

        kp.keyboard_buttons = ['test1', 'test2']
        self.assertEqual(
            kp,
            {
                'buttons': [
                    'test1',
                    'test2'
                ],
                'type': 'buttons'
            }
        )