# buttons_bot.py
import requests
import time
from telegram import ChatAction
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, Filters
from telegram.ext import CommandHandler, MessageHandler, CallbackQueryHandler
import botTestModule
import upbit
from emoji import emojize
import pprint
import json
BOT_TOKEN = '1480467875:AAFQsa0P93WmXfQ1airEjmXcSexzmrZHc-E'

updater = Updater(token=BOT_TOKEN, use_context=True)
dispatcher = updater.dispatcher


# def handler(bot, update):
#     text = update.message.text
#     chat_id = update.message.chat_id

#     if '모해' in text:
#         bot.send_message(chat_id=chat_id, text='오빠 생각 ㅎㅎ')
#     elif '아잉' in text:
#         bot.send_message(chat_id=chat_id, text=emojize(
#             '아잉:heart_eyes:', use_aliases=True))
#     elif '몇시에' in text:
#         bot.send_message(chat_id=chat_id, text='7시에 보자')
#     elif '사진' in text:
#         bot.send_photo(chat_id=chat_id, photo=open('img/mj.jpg', 'rb'))
#     else:
#         bot.send_message(chat_id=chat_id, text='몰라')


def cmd_task_buttons(update, context):
    task_buttons = [[
        InlineKeyboardButton('1.네이버 뉴스', callback_data=1), InlineKeyboardButton(
            '2.직방 매물', callback_data=2)
    ], [
        InlineKeyboardButton('3.취소', callback_data=3)
    ]]

    reply_markup = InlineKeyboardMarkup(task_buttons)

    context.bot.send_message(
        chat_id=update.message.chat_id, text='작업', reply_markup=reply_markup
    )


def cb_button(update, context):
    query = update.callback_query
    data = query.data
    # print("@@@@@@@@@@@@@"*5)
    # json.dumps(book)

    if '작업' in query.message.text:
        print('작업@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
        context.bot.send_chat_action(
            chat_id=update.effective_user.id, action=ChatAction.TYPING
        )

        if data == '3':
            context.bot.edit_message_text(
                text='작업이 취소되었습니다.', chat_id=query.message.chat_id, message_id=query.message.message_id
            )
        else:
            context.bot.edit_message_text(
                text='[{}] 작업이 진행중입니다.'.format(data), chat_id=query.message.chat_id, message_id=query.message.message_id
            )

            if data == '1':
                # results = []
                results = upbit.upbit()
                for result in results:
                    # print(result)
                    context.bot.send_message(
                        chat_id=update.effective_chat.id, text='{}'.format(result))
            elif data == '2':
                crawl_zigbang(context)

            context.bot.send_message(
                chat_id=update.effective_chat.id, text='[{}] 작업을 완료하였습니다.'.format(
                    data)
            )
    elif '직방' in query.message.text:
        print('직방@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
        print(data)


def zigbang(update, context):
    task_buttons = []
    zigbangresult = upbit.zipbang(str(context.args[0]))
    for i in range(len(zigbangresult)):
        line = []
        for j in range(1):
            line.append(InlineKeyboardButton(
                '{}'.format(zigbangresult[i]), callback_data="{}".format(i+1)))
        task_buttons.append(line)

    reply_markup = InlineKeyboardMarkup(task_buttons)

    context.bot.send_message(
        chat_id=update.message.chat_id, text='직방', reply_markup=reply_markup)
    # context.bot.send_message(chat_id=update.effective_chat.id,
    #                          text='[{}] 작업을 완료하였습니다.'.format())


def crawl_navernews():
    time.sleep(5)
    print('네이버에서 뉴스를 수집했다.')


def crawl_zigbang(context):
    time.sleep(5)
    print(context)


# echo_handler = MessageHandler(Filters.text, handler)
task_buttons_handler = CommandHandler('tasks', cmd_task_buttons)
zigbang_handler = CommandHandler('zigbang', zigbang)
button_callback_handler = CallbackQueryHandler(cb_button)
# zipbang_callback_handler = CallbackQueryHandler(zipbang)

dispatcher.add_handler(task_buttons_handler)
dispatcher.add_handler(button_callback_handler)
dispatcher.add_handler(zigbang_handler)
# dispatcher.add_handler(zipbang_callback_handler)
# dispatcher.add_handler(echo_handler)


updater.start_polling()
updater.idle()
