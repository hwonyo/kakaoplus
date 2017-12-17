# kakaoplus
[![PyPI](https://img.shields.io/pypi/v/kakaoplus.svg?v=1&maxAge=3601)](https://pypi.python.org/pypi/kakaoplus)
[![Coverage Status](https://travis-ci.org/HwangWonYo/kakaoplus.svg?branch=master)](https://coveralls.io/github/wonyoHwang/kakaoplus?branch=master)
[![Coverage Status](https://coveralls.io/repos/github/HwangWonYo/kakaoplus/badge.svg?branch=doc)](https://coveralls.io/github/HwangWonYo/kakaoplus?branch=doc)
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
from kakao import Template, Payload

app = Flask(__name__)
KaKao = KaKaoAgent()


@app.route('/keyboard', methods=['GET'])
@KaKao.handle_keyboard
def keyboard_handler():

    return Template.Keyboard()


@app.route('/message', methods=['POST'])
def message_handler():
    res = KaKao.webhook_handler(request.get_data(as_text=True))

    return res


@KaKao.callback
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

