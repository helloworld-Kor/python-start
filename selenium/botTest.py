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
# https://api.telegram.org/bot1480467875:AAFQsa0P93WmXfQ1airEjmXcSexzmrZHc-E/sendMessage?chat_id=1440556547%20&text=잘가냐?
updater = Updater(token=BOT_TOKEN, use_context=True)
dispatcher = updater.dispatcher


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
    print(query.message.chat_id)
    if '작업' in query.message.text:
        # print('작업@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
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
                    print(result)
                    context.bot.send_message(
                        chat_id=update.effective_chat.id, text='{}'.format(result))
            elif data == '2':
                crawl_zigbang(context)

    elif '직방' in query.message.text:
        result = upbit.zipbangFinal(const_zipbang, int(data))
        cnt = 0
        for i in result:
            cnt += 1
            context.bot.send_message(
                chat_id=update.effective_chat.id, text='{}. {}'.format(cnt, i))
    context.bot.send_message(
        chat_id=update.effective_chat.id, text='[{}] 작업을 완료하였습니다.'.format(
            data)
    )


def zigbang(update, context):
    task_buttons = []

    global const_zipbang
    const_zipbang = str(context.args[0])
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


def magnetSearch(update, context):
    magnetresult = upbit.magnetSearch(str(context.args[0]))
    context.bot.send_message(
        chat_id=update.effective_chat.id, text='{}'.format(magnetresult))
    context.bot.send_message(
        chat_id=update.effective_chat.id, text=' 작업을 완료하였습니다.')


def jungoSearch(update, context):
    jungoresult = upbit.junggo(str(context.args[0]))
    cnt = 0
    for i in jungoresult:
        cnt += 1
        context.bot.send_message(
            chat_id=update.effective_chat.id, text='{}. {}'.format(cnt, i))
    context.bot.send_message(
        chat_id=update.effective_chat.id, text=' 작업을 완료하였습니다.')


def crawl_zigbang(context):
    time.sleep(5)


task_buttons_handler = CommandHandler('tasks', cmd_task_buttons)
zigbang_handler = CommandHandler('zigbang', zigbang)
magnet_handler = CommandHandler('magnet', magnetSearch)
jungo_handler = CommandHandler('jungo', jungoSearch)
button_callback_handler = CallbackQueryHandler(cb_button)


dispatcher.add_handler(task_buttons_handler)
dispatcher.add_handler(button_callback_handler)
dispatcher.add_handler(zigbang_handler)
dispatcher.add_handler(magnet_handler)
dispatcher.add_handler(jungo_handler)


updater.start_polling()
updater.idle()
