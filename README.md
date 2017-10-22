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

