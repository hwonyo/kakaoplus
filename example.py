#-*- coding:utf-8 -*-
from flask import Flask, request

from kakaoplus import KaKaoAgent
from kakaoplus import Template
from kakaoplus import Payload

app = Flask(__name__)
KaKao = KaKaoAgent()

@app.route('/', methods=['GET','POST'])
def app_start():
    return "App launched Success"


@app.route('/keyboard', methods=['GET'])
@KaKao.handle_keyboard
def keyboard_handler():

    return Template.Keyboard()


@app.route('/message', methods=['POST'])
def message_handler():
    res = KaKao.handle_webhook(request.get_data(as_text=True))

    return res


@KaKao.callback
def handle_message(req):
    '''
    :param req: kakao.Req
    :return: Template.Payload
    '''
    echo_message = req.content
    res = Payload(
        Template.Message(echo_message)
    )

    return res


@KaKao.callback(['hello', 'hi'])
def greeting_callback(req):
    '''
    :param req: KaKao.Req
    :return: Template.Payload
    '''
    res = Payload(
        Template.Message('Hello friend')
    )

    return res


if __name__ == "__main__":
    app.run()