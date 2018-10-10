from django.http import HttpResponse
import os
from os.path import join, dirname
from dotenv import load_dotenv
from linebot import LineBotApi, WebhookHandler

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

YOUR_CHANNEL_ACCESS_TOKEN= os.environ.get("YOUR_CHANNEL_ACCESS_TOKEN")
YOUR_CHANNEL_SECRET= os.environ.get("YOUR_CHANNEL_SECRET")

line_bot_api = LineBotApi(YOUR_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(YOUR_CHANNEL_SECRET)

def index(request):
    return HttpResponse("This is bot api.")

def callback(request):
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    handler.handle(body, signature)

    return 'OK'
