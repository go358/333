from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def back_button():
    return InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='⬅️ Назад', callback_data='back')]])
