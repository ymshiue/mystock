﻿#載入LineBot所需要的套件
from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

app = Flask(__name__)

# 必須放上自己的Channel Access Token
line_bot_api = LineBotApi('Gy2gf86vniuzvdqPbMyi5KDKtc3flCXVatA1REp7eGScL9bms6FIHgo3CRxahlNdlMVSWkh/KOZ+Ip3e3lHO0hAyrNdlpKRJa5xLi/0t+6ighTrvLq5Us7ge6YJvMXu8rLMOZ17TmzssdFjaUlsYWwdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('005ddfb1334f26b1278fa2cf6dda3516')

line_bot_api.push_message('Uc0528640671f920eb271d4e3b3b9d7c5', TextSendMessage(text='你可以開始了'))

# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

#訊息傳遞區塊
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    message = TextSendMessage(text=event.message.text)
    line_bot_api.reply_message(event.reply_token,message)

#主程式
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
