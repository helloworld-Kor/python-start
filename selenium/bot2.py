import time
import telepot
from telepot.loop import MessageLoop       # *1)
from telepot.namedtuple import InlineKeyboardMarkup, InlineKeyboardButton  # *2)


def on_chat_message(msg):  # *3)
    content_type, chat_type, chat_id = telepot.glance(msg)

    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='Press me', callback_data='press')],
        [InlineKeyboardButton(text='Press me', callback_data='press')],
    ])

    bot.sendMessage(chat_id, 'Use inline keyboard', reply_markup=keyboard)


def on_callback_query(msg):  # *4)
    query_id, from_id, query_data = telepot.glance(
        msg, flavor='callback_query')
    print('Callback Query:', query_id, from_id, query_data)

    bot.answerCallbackQuery(query_id, text='Got it')


TOKEN = "1480467875:AAFQsa0P93WmXfQ1airEjmXcSexzmrZHc-E"

bot = telepot.Bot(TOKEN)
MessageLoop(bot, {'chat': on_chat_message,
                  'callback_query': on_callback_query}).run_as_thread()  # *5)
print('Listening ...')

while 1:  # *6)
    time.sleep(10)
