# ------------------------------------------------------------------- #
# Перед работой с ботом прочитайте файл REWADME в репозитории с ботом #
#             Там рассписанно какие файлы за что отвечают             #
# ------------------------------------------------------------------- #

# Импортируем библиотеки
import requests
import platform
import os

import markups as kb

from config import TOKEN, SP_ID
from messages import MESSAGES_EN, MESSAGES_RU

from aiogram import Bot, types
from aiogram.utils import executor
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.middlewares.logging import LoggingMiddleware

# Определяем главные переменные для работы с ботом
bot = Bot(token = TOKEN)
dp = Dispatcher(bot, storage = MemoryStorage())
dp.middleware.setup(LoggingMiddleware())


# ? ----- Блок с русским ботом ----- ? #
# !- Ip -! #
response = requests.get("http://jsonip.com/").json()

# !- Specification -! #
banner_ru = f"Название PC: {platform.node()}\nСистема: {platform.system()} {platform.release()}"
# * ------------------------------------------------------------------- * #

# ! - Call вызовы РУССКИХ кнопок - ! #
@dp.callback_query_handler(lambda call: call.data == "button_ru")
async def button_ru(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, MESSAGES_RU['start_ru'], reply_markup = kb.kb_start_ru)

@dp.callback_query_handler(lambda call: call.data == 'button_help_ru')
async def button_help_ru(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, MESSAGES_RU['help_ru'], reply_markup = kb.kb_who_ru)

@dp.callback_query_handler(lambda call: call.data == 'button_who_ru')
async def button_who_ru(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, MESSAGES_RU['who_ru'], reply_markup = kb.kb_source_ru)

@dp.callback_query_handler(lambda call: call.data == 'button_menu_ru')
async def button_menu_ru(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, MESSAGES_RU['menu_ru'], reply_markup = kb.kb_menu_ru)

@dp.callback_query_handler(lambda call: call.data == 'button_pc_info_ru')
async def button_pc_info_ru(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, MESSAGES_RU['main_pc_ru'], reply_markup = kb.kb_menu_pc_ru)

@dp.callback_query_handler(lambda call: call.data == 'button_ip_addr_ru')
async def button_ip_addr_ru(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, "Ваш IP адрес: " f"{response['ip']}")

@dp.callback_query_handler(lambda call: call.data == 'button_pc_spec_ru')
async def button_pc_spec_ru(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, f"{banner_ru}")

@dp.callback_query_handler(lambda call: call.data == 'button_shift_lang_ru')
async def button_shift_lang_ru(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, MESSAGES_EN['menu_en'], reply_markup = kb.kb_menu_en)
    await bot.delete_message(callback_query.from_user.id, callback_query.message.message_id)
# * ------------------------------------------------------------------- * #

# ! - Блок функций - ! #
@dp.message_handler(commands = ["start"])
async def start_command(message: types.Message):
	await message.answer("Выбери язык\n\nChoose language", reply_markup = kb.kb_lang)

# Функция помощи (команда = /help)
@dp.message_handler(commands = ["help_ru"])
async def help_command(message: types.Message):
    await message.answer(MESSAGES_RU['help_ru'], reply_markup = kb.kb_who_ru)

# Функция кто я (команда = who)
@dp.message_handler(commands = ["who_ru"])
async def who_command(message: types.Message):
    await message.answer(MESSAGES_RU['who_ru'], reply_markup = kb.kb_source_ru)

# Выдача ссылки на исходники бота (команда = /source_bot)
@dp.message_handler(commands = ["source_bot_ru"])
async def source_command(message: types.Message):
    await message.reply("Исходники моего бота:\nhttps://github.com/sp11dh4ck/main_bot_alpha")

# Запуск меню бота (команда = menu)
@dp.message_handler(commands = ["menu_ru"])
async def menu_command(message: types.Message):
    await message.answer(MESSAGES_RU['menu_ru'], reply_markup = kb.kb_menu_ru)

# Функция отключения пк (только для создателя)
@dp.message_handler(commands = ["off_pc"])
async def pc_off_command(message: types.Message):
    if message.from_user.id == SP_ID:
        os.system("shutdown -s -t 0")
    else:
        await message.reply("У вас нет прав на выполнение данной команды!\n"
        "Лучше введите /commands и узнайте, какие команды вы можете использовать ;)\n\n"
        "You do not have the rights to execute this command!\n"
        "Better type / and see what commands you can use ;)")

# Функция с принятием сообщений
@dp.message_handler()
async def text_user(message: types.Message):
	await message.reply("Я тебя не понимаю :(\n"
    "Попробуй написать /commands или /help\n\n"
    "I don't understand you :(\n"
    "Try writing /commands or /help")
# * ------------------------------------------------------------------- * #


# ? ----- Блок с английским ботом ----- ? #
# !- Specification -! #
banner_en = f"Name PC: {platform.node()}\nSystem: {platform.system()} {platform.release()}"
# * ------------------------------------------------------------------- * #

# ! - Call вызовы АНГЛИЙСКИХ кнопок - ! #
@dp.callback_query_handler(lambda call: call.data == "button_en")
async def button_en(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, MESSAGES_EN['start_en'], reply_markup = kb.kb_start_en)

@dp.callback_query_handler(lambda call: call.data == 'button_help_en')
async def button_help_ru(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, MESSAGES_EN['help_en'], reply_markup = kb.kb_who_en)

@dp.callback_query_handler(lambda call: call.data == 'button_who_en')
async def button_who_ru(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, MESSAGES_EN['who_en'], reply_markup = kb.kb_source_en)

@dp.callback_query_handler(lambda call: call.data == 'button_menu_en')
async def button_menu_ru(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, MESSAGES_EN['menu_en'], reply_markup = kb.kb_menu_en)

@dp.callback_query_handler(lambda call: call.data == 'button_pc_info_en')
async def button_pc_info_ru(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, MESSAGES_EN['main_pc_en'], reply_markup = kb.kb_menu_pc_en)

@dp.callback_query_handler(lambda call: call.data == 'button_ip_addr_en')
async def button_ip_addr_ru(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, "Your IP address: " f"{response['ip']}")

@dp.callback_query_handler(lambda call: call.data == 'button_pc_spec_en')
async def button_pc_spec_ru(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, f"{banner_en}")

@dp.callback_query_handler(lambda call: call.data == 'button_shift_lang_en')
async def button_shift_lang_ru(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, MESSAGES_RU['menu_ru'], reply_markup = kb.kb_menu_ru)
    await bot.delete_message(callback_query.from_user.id, callback_query.message.message_id)
# * ------------------------------------------------------------------- * #

# Функция помощи (команда = /help)
@dp.message_handler(commands = ["help_en"])
async def help_command(message: types.Message):
    await message.answer(MESSAGES_RU['help_en'], reply_markup = kb.kb_who_en)

# Функция кто я (команда = who)
@dp.message_handler(commands = ["who_en"])
async def who_command(message: types.Message):
    await message.answer(MESSAGES_RU['who'], reply_markup = kb.kb_source_en)

# Выдача ссылки на исходники бота (команда = /source_bot)
@dp.message_handler(commands = ["source_bot_en"])
async def source_command(message: types.Message):
    await message.reply("Исходники моего бота:\nhttps://github.com/sp11dh4ck/main_bot_alpha")

# Запуск меню бота (команда = menu)
@dp.message_handler(commands = ["menu_en"])
async def menu_command(message: types.Message):
    await message.answer(MESSAGES_RU['menu_en'], reply_markup = kb.kb_menu_en)
# * ------------------------------------------------------------------- * #


if __name__ == '__main__':
	executor.start_polling(dp, skip_updates = True)