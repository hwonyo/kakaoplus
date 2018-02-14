#-*- coding:utf-8 -*-
from flask import Flask, request

from kakaoplus import KaKaoAgent


app = Flask(__name__)
KaKao = KaKaoAgent()

@app.route('/', methods=['GET','POST'])
def app_start():
    return "App launched Success"


@app.route('/keyboard', methods=['GET'])
def keyboard_handler():
    return KaKao.handle_keyboard_webhook()


@app.route('/message', methods=['POST'])
def message_handler():
    req = request.get_data(as_text=True)

    return KaKao.handle_webhook(req)

@KaKao.handle_keyboard
def handle_keywboard(res):
    res.text = True


@KaKao.handle_message
def handle_message(req, res):
    echo_message = req.content

    res.text = "Echo !!" + echo_message


@KaKao.handle_message(['hello', 'hi'])
def greeting_callback(req, res):
    res.text = 'hello my friend'


if __name__ == "__main__":
    app.run()