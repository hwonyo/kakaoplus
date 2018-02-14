# kakaoplus
[![PyPI](https://img.shields.io/pypi/v/kakaoplus.svg?v=1&maxAge=3601)](https://pypi.python.org/pypi/kakaoplus)
[![Coverage Status](https://travis-ci.org/HwangWonYo/kakaoplus.svg?branch=master)](https://coveralls.io/github/wonyoHwang/kakaoplus?branch=master)
[![Coverage Status](https://coveralls.io/repos/github/HwangWonYo/kakaoplus/badge.svg?branch=master)](https://coveralls.io/github/HwangWonYo/kakaoplus?branch=master)
[![PyPI](https://img.shields.io/pypi/l/kakaoplus.svg?v=1&maxAge=2592000)](https://pypi.python.org/pypi/kakaoplus)

Python Handy Webhook Handler For Using KaKao Plus Friend Auto Reply

Inspired By : https://github.com/conbus/fbmq
# Install
```
pip install kakaoplus
```

# Handle webhook
Handle kakaotalk plus friend auto_reply

### Usage (with flask)
```python
from flask import Flask, request
from kakao import KaKaoAgent

app = Flask(__name__)
KaKao = KaKaoAgent()


@app.route('/keyboard', methods=['GET'])
def keyboard_handler():
    res = KaKao.handle_keyboard_webhook

    return res


@app.route('/message', methods=['POST'])
def message_handler():
    req = request.get_data(as_text=True)
    res = KaKao.handle_webhook(req)

    return res


@KaKao.handle_keyboard
def keyboard_handler(res):
    '''
    :param req: request from kakao
    :param res: response
    '''
    res.keyboard_buttons = [
        'button1',
        'button2',
        'button3'
    ]


@KaKao.callback
def handle_message(req, res):
    '''
    :param req: request from kakao
    :param res: response
    '''
    echo_message = req.content

    res.text = "Echo Message: " + echo_message


@KaKao.callback(['hello', 'hi'])
def greeting_callback(req, res):
    '''
    :param req: request from kakao
    :param res: response
    '''
    res.text = "Hello :)"
```

