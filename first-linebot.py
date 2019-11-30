# coding: utf-8

from linebot import (
    LineBotApi
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)


def main(args):
    print(args)
    # account setting
    line_bot_api = LineBotApi(args['CHANNEL_ACCESS_TOKEN'])
    handler = WebhookHandler(args['CHANNEL_SECRET'])

    # make responce
    body = args["events"][0]
    try:
        line_bot_api.reply_message(
            body["replyToken"],
            TextSendMessage(text=body["message"]["text"])
        )
    except LineBotApiError as e:
        print(e)
        return {"status":400}

    return {"status":200}
