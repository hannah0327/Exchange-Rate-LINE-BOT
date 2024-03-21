import os, sys

from flask import Flask, request, abort, jsonify
import requests


from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

# get channel_secret and channel_access_token from your environment variable
channel_secret = ('0c70ae301b094d074c7ba9b484546115')
channel_access_token =('pvDCBNx02xb2Zz9mwSQwK6tdxAhOPFvSR08H7L5DwQ3BxLwnHcOpmmmj0f9HJqASR+FbRwjJkdXzLzMnxxNK/mPU3ZHViSv4CN++oq6zo8MyfShAbSloRzVyOwieXClzwmb55Tw/wEmt6Q+sL2X1rwdB04t89/1O/w1cDnyilFU=')


line_bot_api = LineBotApi(channel_access_token)
handler = WebhookHandler(channel_secret)


@app.route('/callback', methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info('Request body: ' + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print('Invalid signature. Please check your channel access token/channel secret.')
        abort(400)

    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    input_text = event.message.text

    resp = requests.get('https://tw.rter.info/capi.php')
    currency_data = resp.json()
    
    if input_text == '@查詢匯率':
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=f'請輸入查詢代號@1:USDTWD @2:USDEUR @3:USDJPY @4:TWDUSD @5:TWDEUR @6:TWDJPY'))

    if input_text == '@1':
        usd_to_twd = currency_data['USDTWD']['Exrate']
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=f'美元 USD 對台幣 TWD：1:{usd_to_twd}'))

    if input_text == '@2':
        usd_to_twd = currency_data['USDEUR']['Exrate']
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=f'美元 USD 對歐元 EUR：1:{usd_to_twd}'))
        
    if input_text == '@3':
        usd_to_twd = currency_data['USDJPY']['Exrate']
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=f'美元 USD 對日幣 JPY：1:{usd_to_twd}'))
        
    if input_text == '@4':
        usd_to_twd = 1/currency_data['USDTWD']['Exrate']
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=f'台幣 TWD 對美元 USD：1:{usd_to_twd}'))
        
    if input_text == '@5':
        usd_to_twd = currency_data['USDEUR']['Exrate']/currency_data['USDTWD']['Exrate']
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=f'台幣 TWD 對歐元 EUR：1:{usd_to_twd}'))
        
    if input_text == '@6':
        usd_to_twd = currency_data['USDJPY']['Exrate']/currency_data['USDTWD']['Exrate']
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=f'台幣 TWD 對日幣 JPY：1:{usd_to_twd}'))

if __name__ == '__main__':
    app.run()
