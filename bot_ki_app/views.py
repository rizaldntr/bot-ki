from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt

from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

import json
import os

# line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)
line_bot_api = LineBotApi(os.environ.get('LINE_CHANNEL_ACCESS_TOKEN', "NULL"))
# parser = WebhookParser(settings.LINE_CHANNEL_SECRET)
parser = WebhookParser(os.environ.get('LINE_CHANNEL_SECRET', "NULL"))

@csrf_exempt
def callback(request):
    if request.method == 'POST':
        signature = request.META['HTTP_X_LINE_SIGNATURE']
        body = request.body.decode('utf-8')

        try:
            events = parser.parse(body, signature)
        except InvalidSignatureError:
            return HttpResponseForbidden()
        except LineBotApiError:
            return HttpResponseBadRequest()

        for event in events:
            print (event)

        return HttpResponse()
    else:
        return HttpResponseBadRequest()