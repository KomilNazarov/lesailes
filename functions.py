from telebot.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, KeyboardButton, InlineKeyboardButton
from buttons_names import *


def start_message_buttons():
    reply_markup = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=True)
    reply_markup.row(KeyboardButton(ORDER))
    reply_markup.add(*[KeyboardButton(text=text) for text in START_BUTTONS])
    reply_markup.row(SETTING)
    return reply_markup


def dostavka():
    reply_markup = ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    reply_markup.add(KeyboardButton(text=DOSTAVKA, request_location=True))
    reply_markup.add(KeyboardButton(text=TAKE_AWAY))
    reply_markup.row(BACK)
    return reply_markup


def sent_location():
    loc_markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    sent_geo = KeyboardButton(LOCATION, request_location=True)
    loc_markup.row(sent_geo)
    loc_markup.add(*[OK, BACK])
    return loc_markup


def crete_menyu():
    menyu_markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    menyu_markup.add(*[KeyboardButton(text=text) for text in menyu])
    return menyu_markup


def create_buttons_in_info():
    info_markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    info_markup.add(*[BRANCHES, PUBLIC_OFFER, BACK])
    return info_markup


def create_buttons_in_branches():
    branches_markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    branches_markup.add(*[KeyboardButton(text) for text in branches_button])
    branches_markup.row(BACK)
