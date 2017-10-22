# FBMQ (Facebook Messenger Platform Python Library)
[![PyPI](https://img.shields.io/pypi/v/kakaoplus.svg?v=1&maxAge=3601)](https://pypi.python.org/pypi/kakaoplus)
[![Build Status](https://travis-ci.org/wonyoHwang/kakaoplus.svg?branch=master&v=1)](https://travis-ci.org/wonyoHwang/kakaoplus)
[![Coverage Status](https://travis-ci.org/HwangWonYo/kakaoplus.svg?branch=master)](https://coveralls.io/github/wonyoHwang/kakaoplus?branch=master)
[![PyPI](https://img.shields.io/pypi/l/kakaoplus.svg?v=1&maxAge=2592000)](https://pypi.python.org/pypi/kakaoplus)

Python Handy Webhook Handler For Using KaKao Plus Friend Auto Reply

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
    payload = KaKao.Payload(
        Template.Message("User has just entered."),
        Template.Keyboard()
    )
    res = payload.to_json()

    return res


@app.route('/message', methods=['POST'])
def message_handler():
    res = KaKao.webhook_handler(request.get_data(as_text=True))

    return res


@KaKao.default_callback
def handle_message(req):
    '''
    :param req: kakao.Req
    :return: Template.Payload
    '''
    echo_message = req.content
    res = KaKao.Payload(
        Template.Message(echo_message)
    )

    return res


@KaKao.callback(['hello', 'hi'])
def greeting_callback(req):
    '''
    :param req: kakao.Req
    :return: Template.Payload
    '''
    res = KaKao.Payload(
        Template.Message('Hello friend')
    )

    return res
```

