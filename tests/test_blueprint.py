import json
import unittest

from kakaoplus import kakaoplus as KaKao
from flask import Flask, Blueprint

class KaKaoTest(unittest.TestCase):
    def setUp(self):
        blueprint = Blueprint('blueprint_api', __name__, url_prefix="/test_prefix")
        self.agent = KaKao.KaKaoAgent(blueprint=blueprint)

        app = Flask(__name__)
        app.register_blueprint(blueprint)
        self.app = app

    def test_handle_keyboard(self):
        with self.app.test_client() as c:
            rv = c.get('/test_prefix/keyboard')
            self.assertEqual(
                json.loads(rv.get_data(as_text=True)),
                {
                    "type": "text"
                })

    def test_handle_message(self):
        req = {"user_key": "testID", "type": "text", "content": "test"}
        with self.app.test_client() as c:
            rv = c.post('/test_prefix/message', data=json.dumps(req),
                        content_type = 'application/json')
            self.assertEqual(rv.get_data(as_text=True), "ok")

    def test_second_blueprint(self):
        blueprint2 = Blueprint('blueprint_api2', __name__, url_prefix='/test_prefix_2')
        self.agent2 = KaKao.KaKaoAgent(blueprint=blueprint2)
        self.app.register_blueprint(blueprint2)

        # test blueprint2 keyboard handler
        with self.app.test_client() as c:
            rv = c.get('/test_prefix_2/keyboard')
            self.assertEqual(
                json.loads(rv.get_data(as_text=True)),
                {
                    "type": "text"
                })

        # test blueprint2 message handler
        req = {"user_key": "testID", "type": "text", "content": "test"}
        with self.app.test_client() as c:
            rv = c.post('/test_prefix_2/message', data=json.dumps(req),
                        content_type='application/json')
            self.assertEqual(rv.get_data(as_text=True), "ok")