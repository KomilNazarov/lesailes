import telebot
import os
from functions import *
from texts import *
from buttons_names import *

bot = telebot.TeleBot(os.environ.get("BOT_TOKEN"))


@bot.message_handler(commands=["start"])
def sart_message(message):

    bot.send_message(message.from_user.id, start_text, reply_markup=start_message_buttons())


@bot.message_handler(content_types="text")
def echo_message(message):
    if message.text == ORDER:
        bot.send_message(message.from_user.id, echo_order_text, reply_markup=dostavka())

    elif message.text == DOSTAVKA:
        bot.send_message(message.from_user.id, echo_dostavka_text, reply_markup=sent_location())

    elif message.text == OK:
        bot.send_message(message.from_user.id, text=None)
        text = "Nimadan boshlaymiz ?"
        bot.send_message(message.from_user.id, text, reply_markup=crete_menyu())
    elif message.text == INFO:
        bot.send_message(message.from_user.id, text_in_info, reply_markup=create_buttons_in_info())
    elif message.text == PUBLIC_OFFER:
        bot.send_message(message.from_user.id, text_in_publicoffer)


@bot.message_handler(content_types=['location'])
def geo(message):

    keyboard = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_geo = KeyboardButton(text=LOCATION,
                                request_location=True)

    bot.send_message(message.from_user.id, text=text_introduse_delivery, reply_markup=sent_location())


bot.polling(none_stop=True)
