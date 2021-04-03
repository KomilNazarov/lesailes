import telebot
from telebot.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, KeyboardButton, InlineKeyboardButton
from functions import *
import os
bot = telebot.TeleBot(os.environ.get("BOT_TOKEN"))

text_introduse_delivery = """
10:00 _ 22:00 - 1 km gacha bo`lgan buyurtmalar yetkazib berish narxi 5000 so`m\
10:00 _ 22:00 - 3 km gacha  9000 so`m, keyingi har 1 km uchun - 1000 so`m Toshkent shahari bo`ylab.
"""
a = ''

@bot.message_handler(commands=["start"])
def sart_message(message):
    text = "assalomu aleykum botga xush kelibsiz"
    bot.send_message(message.from_user.id, text, reply_markup=start_message_buttons())


@bot.message_handler(content_types="text")
def echo_message(message):
    if message.text == ORDER:
        text = "Buyurtmani olib keting yoki yetkazib berish ni bosing"
        bot.send_message(message.from_user.id, text, reply_markup=dostavka())

    if message.text == DOSTAVKA:
        text = "end yaqin shaxobsh"
        bot.send_message(message.from_user.id, text, reply_markup=sent_location())

    if message.text == OK:
        bot.send_message(message.from_user.id, text_introduse_delivery)
        text = "Nimadan boshlaymiz ?"
        bot.send_message(message.from_user.id, text, reply_markup=crete_menyu())


@bot.message_handler(content_types=['location'])
def geo(message):
    print(message)
    keyboard = ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    button_geo = KeyboardButton(text=LOCATION,
                                request_location=True)

    bot.send_message(message.from_user.id, text=text_introduse_delivery, reply_markup=sent_location())


bot.polling(none_stop=True)
