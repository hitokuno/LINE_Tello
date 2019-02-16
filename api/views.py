from django.http import HttpResponse
import os
from os.path import join, dirname
from dotenv import load_dotenv
from linebot import LineBotApi, WebhookHandler
import json
import requests
from django.shortcuts import render

load_dotenv()
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
    return HttpResponse("This is bot api." + str)

def line(request):
    return render(request, 'line.html', {})

def returnResult(command):
    ret = {
        "version": "1.0",
        "sessionAttributes": {},
        "response": {
            "outputSpeech": {
                "type": "SimpleSpeech",
                "values": {
                    "type": "PlainText",
                    "lang": "ja",
                    "value": command
                }
            },
            "card": {},
            "directives": [],
            "shouldEndSession": False
        }
    }
    return returnJson(json)

def returnJson(ret):
    response = HttpResponse(json.dumps(ret).encode("utf-8"), content_type='application/json; charset=UTF-8', status=None)
    return response

def status(request):
    global command
    local_command = '' + command
    command = ''
    return returnJson({ "status": local_command})

def clova(request):
    request_json = json.loads(request.body.decode('utf-8'))
    requestBody = request_json["request"]
    type = requestBody["type"]
    if type == 'LaunchRequest':
        return returnResult('準備が出来ました。')
    if type == 'SessionEndedRequest':
        return returnResult('終了します')
    intent = requestBody["intent"]
    text = intent["name"]
    global command
    command = text

    if text == 'TakeOff':
        returnText = '離陸します'
    elif text == 'Land':
        returnText = '着陸します'
    elif text == 'Flip':
        returnText = 'フリップします'
    else:
        command = "Unknown"
        returnText = "分かりません。"

    return returnResult(returnText)
