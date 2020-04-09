# coding: utf-8

import json
from linebot import (
    WebhookHandler, LineBotApi
)
from linebot.exceptions import (
    InvalidSignatureError,
    LineBotApiError
)
from linebot.models import (
    TextSendMessage,
    MessageEvent,
    TextMessage,
)


def main(args):
    print(args)
    # account setting
    line_bot_api = LineBotApi(args['CHANNEL_ACCESS_TOKEN'])
    handler = WebhookHandler(args["CHANNEL_SECRET"])
    signature = args["__ow_headers"]["x-line-signature"]
    @handler.add(MessageEvent, message=TextMessage)
    def handle_message(event):
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=event.message.text))

    # make responce
    body = args["events"][0]
    try:
        if body["source"]["userId"] == "Udeadbeefdeadbeefdeadbeefdeadbeef":
            return {"status": 200}
        else:
            body = json.dumps(args)
            handler.handle(body, signature)
    except LineBotApiError as e:
        print("Got exception from LINE Messaging API: %s\n" % e.message)
        for m in e.error.details:
            print("  %s: %s" % (m.property, m.message))
        return {"status": 403}
    except InvalidSignatureError:
        return {"status": 403}

    return {"status": 200}
