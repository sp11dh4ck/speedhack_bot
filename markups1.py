from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


button_lang_ru_in = InlineKeyboardButton("RU", callback_data = "button_lang_ru_in")
button_lang_en_in = InlineKeyboardButton("EN", callback_data = "button_lang_en_in")

kb_lang_in = InlineKeyboardMarkup().add(button_lang_ru_in, button_lang_en_in)