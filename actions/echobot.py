# coding: utf-8
from linebot import (
    LineBotApi
)
from linebot.exceptions import (
    InvalidSignatureError,
    LineBotApiError
)
from linebot.models import (
    TextSendMessage,
)


def main(args):
    print(args)
    # account setting
    line_bot_api = LineBotApi(args['CHANNEL_ACCESS_TOKEN'])

    # make responce
    body = args["events"][0]
    try:
        if body["source"]["userId"] == "Udeadbeefdeadbeefdeadbeefdeadbeef":
            return {"status": 200}
        else:
            line_bot_api.reply_message(
                body["replyToken"],
                TextSendMessage(text=body["message"]["text"]))
    except LineBotApiError as e:
        print("Got exception from LINE Messaging API: %s\n" % e.message)
        for m in e.error.details:
            print("  %s: %s" % (m.property, m.message))
        return {"status": 403}
    except InvalidSignatureError:
        return {"status": 403}

    return {"status": 200}
