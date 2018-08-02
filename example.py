#-*- coding:utf-8 -*-
from flask import Flask
from kakaoplus import KaKaoAgent

app = Flask(__name__)
KaKao = KaKaoAgent(app, '/')


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