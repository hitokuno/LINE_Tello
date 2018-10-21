from django.http import HttpResponse
import os
from os.path import join, dirname
from dotenv import load_dotenv
from linebot import LineBotApi, WebhookHandler
import json
import requests
from django.shortcuts import render

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

YOUR_CHANNEL_ACCESS_TOKEN = os.environ.get("YOUR_CHANNEL_ACCESS_TOKEN")
YOUR_CHANNEL_SECRET = os.environ.get("YOUR_CHANNEL_SECRET")

line_bot_api = LineBotApi(YOUR_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(YOUR_CHANNEL_SECRET)

REPLY_ENDPOINT = 'https://api.line.me/v2/bot/message/reply'
HEADER = {
    "Content-Type": "application/json",
    "Authorization": "Bearer " + YOUR_CHANNEL_ACCESS_TOKEN
}

command = ""

def index(request):
    return HttpResponse("This is bot api.")

def line(request):
    return render(request, 'line.html', {})

def command(request):
    json_str = json.dumps(command, ensure_ascii=False, indent=2)
    response = HttpResponse(json_str, content_type='application/json; charset=UTF-8', status=None)
    return response

def clova(request):
    request_json = json.loads(request.body.decode('utf-8'))
    requestBody = request_json["request"]
    intent = requestBody["intent"]
    text = intent["name"]

    if text == '離陸':
        command = text
    elif text == '着陸':
        command = text
    elif text == 'フリップ':
        command = text
    else:
        text = "分かりません"
    ret = {"result": text}
    return ret


def callback(request):
    request_json = json.loads(request.body.decode('utf-8'))
    for e in request_json['events']:
        reply_token = e['replyToken']  # 返信先トークンの取得
        message_type = e['message']['type']   # typeの取得

        if message_type == 'text':
            text = e['message']['text']    # 受信メッセージの取得

    if text == '離陸':
        text
    elif text == '着陸':
        text
    elif text == 'フリップ':
        text
    else:
        text = "分かりません"

    payload = {
          "replyToken":reply_token,
          "messages":[
                {
                    "type":"text",
                    "text": text
                }
            ]
    }

    requests.post(REPLY_ENDPOINT, headers=HEADER, data=json.dumps(payload))
    return text
