from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
import texts

contact_support_kb = InlineKeyboardMarkup().add(InlineKeyboardButton(texts.support_btn, callback_data='support'))

back_kb = InlineKeyboardMarkup().add(InlineKeyboardButton(texts.back_btn, callback_data='back'))

cancel_kb = InlineKeyboardMarkup().add(InlineKeyboardButton(texts.cancel_btn, callback_data='cancel'))
