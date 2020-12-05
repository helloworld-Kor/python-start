import telepot

tele_token = "1480467875:AAFQsa0P93WmXfQ1airEjmXcSexzmrZHc-E"


def handler(msg):
    content_type, chat_Type, chat_id, msg_date, msg_id = telepot.glance(
        msg, long=True)
    print(msg)

    if content_type == "text":
        bot.sendMessage(chat_id, "[반사] {}".format(msg["text"]))


bot = telepot.Bot(tele_token)
bot.message_loop(handler, run_forever=True)
