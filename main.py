# ------------------------------------------------------------------- #
# Перед работой с ботом прочитайте файл REWADME в репозитории с ботом #
#             Там рассписанно какие файлы за что отвечают             #
# ------------------------------------------------------------------- #

# Импортируем библиотеки
import requests
import platform
import os
import logging

import markups as kb

from config import TOKEN
from messages import MESSAGES

from aiogram import Bot, types
from aiogram.utils.executor import start_webhook
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.middlewares.logging import LoggingMiddleware

# Определяем главные переменные для работы с ботом
bot = Bot(token = TOKEN)
dp = Dispatcher(bot, storage = MemoryStorage())
dp.middleware.setup(LoggingMiddleware())

HEROKU_APP_NAME = os.getenv("speedhackbot")
WEBHOOK_HOST = f'https://{HEROKU_APP_NAME}.herokuapp.com'
WEBHOOK_PATH = f'/webhook/{TOKEN}'
WEBHOOK_URL = f'{WEBHOOK_HOST}{WEBHOOK_PATH}'
WEBAPP_HOST = '0.0.0.0'
WEBAPP_PORT = os.getenv('PORT', default = 8000)

async def on_startup(dispatcher):
    await bot.set_webhook(WEBHOOK_URL, drop_pending_updates = True)

async def on_shutdown(dispatcher):
    await bot.delete_webhook()

# --- Call вызовы кнопок --- 
@dp.callback_query_handler(lambda call: call.data == 'button_help_in')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, MESSAGES['help'], reply_markup = kb.kb_who_in)

@dp.callback_query_handler(lambda call: call.data == 'button_commands_in')
async def process_callback_button2(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, MESSAGES['commands'], reply_markup = kb.kb_menu_commands_in)
@dp.callback_query_handler(lambda call: call.data == 'button_who_in')
async def process_callback_button3(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, MESSAGES['who'], reply_markup = kb.kb_source_in)

@dp.callback_query_handler(lambda call: call.data == 'button_menu_in')
async def process_callback_button4(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, MESSAGES['menu'], reply_markup = kb.kb_menu_in)

@dp.callback_query_handler(lambda call: call.data == 'button_ip_addr_in')
async def process_callback_button5(callback_query: types.CallbackQuery):
    response = requests.get("http://jsonip.com/").json()
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, "Ваш IP адресс: " f"{response['ip']}")

@dp.callback_query_handler(lambda call: call.data == 'button_pc_spec_in')
async def process_callback_button6(callback_query: types.CallbackQuery):
    banner = f"Название PC: {platform.node()}\nСистема: {platform.system()} {platform.release()}"
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, f"{banner}")
# -------------------------- #
#await bot.delete_message(message.from_user.id, message.message.message_id) - Удаление сообщения по кнопке
# Стартовая функция (команда = /start)
@dp.message_handler(commands = ["start"])
async def start_command(message: types.Message):
	await message.reply("Выберете действие:", reply_markup = kb.kb_start_in)

# Функция помощи (команда = /help)
@dp.message_handler(commands = ["help"])
async def help_command(message: types.Message):
    await message.answer(MESSAGES['help'])

# Функция с командами (команда = /commands)
@dp.message_handler(commands = ["commands"])
async def commands_command(message: types.Message):
    await message.answer(MESSAGES['commands'])

# Функция кто я (команда = who)
@dp.message_handler(commands = ["who"])
async def who_command(message: types.Message):
    await message.answer(MESSAGES['who'], reply_markup = kb.kb_source_in)

# Выдача ссылки на исходники бота (команда = /source_bot)
@dp.message_handler(commands = ["source_bot"])
async def who_command(message: types.Message):
    await message.reply("Исходники моего бота:\nhttps://github.com/sp11dh4ck/main_bot_alpha")

# Функция ip адресс (команда = ip)
@dp.message_handler(commands = ["ip"])
async def ip_addr(message: types.Message):
	response = requests.get("http://jsonip.com/").json()
	await message.answer("Ваш IP адресс: " f"{response['ip']}")

# Функция спецификация пк (команда = spec)
@dp.message_handler(commands = ["spec"])
async def spec(message: types.Message):
	banner = f"Название PC: {platform.node()}\nСистема: {platform.system()} {platform.release()}"
	await message.answer(f"{banner}")

# Функция с принятием кнопок или сообщений
@dp.message_handler()
async def text_user(message: types.Message):
	await message.reply("Я тебя не понимаю :(\n\nПопробуй написать команду /commands или /help")

"""
@bot.message_handler(commands = ["screen"])
def screen(message):
	filename = f"{time.time()}.jpg"
	pag.screenshot(filename)

	with open(filename, "rb") as image:
		bot.send_document(message.chat.id, image)
	os.remove(filename)
"""

if __name__ == '__main__':
    logging.basicConfig(level = logging.INFO)
    start_webhook(
        dispatcher = dp,
        webhook_path = WEBHOOK_PATH,
        skip_updates = True,
        on_startup = on_startup,
        on_shutdown = on_shutdown,
        host = WEBAPP_HOST,
        port = WEBAPP_PORT,
   )