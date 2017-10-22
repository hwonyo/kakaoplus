import json
import unittest
import mock

from kakao import kakao as KaKao
from kakao import payload as Payload
from kakao import template as Template

class KaKaoTest(unittest.TestCase):
    def setUp(self):
        self.agent = KaKao.KaKaoAgent()

    def test_handle_webhook(self):
        req = json.dumps({"user_key": "testID", "type": "text", "content": "test"})
        test_res = Payload.Payload(
            Template.Message('test')
        )

        counter = mock.MagicMock()

        @self.agent.callback
        def default_handler(req):
            self.assertTrue(req.recieved_text)
            self.assertFalse(req.recieved_photo)
            self.assertEqual(req.user_key, "testID")
            self.assertEqual(req.content, "test")
            counter()

            return test_res

        res = self.agent.handle_webhook(req)
        self.assertEquals(test_res.to_json(), res)
        self.assertEquals(1, counter.call_count)

        req2 = json.dumps({"user_key": "testID", "type": "text", "content": "hi my name is yo"})
        counter2 = mock.MagicMock()

        @self.agent.callback(['(hi).*'])
        def greeting_test(req):
            self.assertTrue(req.recieved_text)
            self.assertFalse(req.recieved_photo)
            self.assertEqual(req.user_key, "testID")
            self.assertEqual(req.content, 'hi my name is yo')
            counter2()
            return test_res

        res = self.agent.handle_webhook(req2)
        self.assertEquals(1, counter2.call_count)




