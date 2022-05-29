import requests

from messages import MESSAGES

from aiogram import Bot, types
from aiogram.utils import executor
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


bot = Bot(token = "My:TOKEN")
dp = Dispatcher(bot, storage = MemoryStorage())
dp.middleware.setup(LoggingMiddleware())

button_ip_addr_in = InlineKeyboardButton("Ip Address🌐", callback_data = 'button_ip_addr_in')
kb_menu_in = InlineKeyboardMarkup().add(button_ip_addr_in)


@dp.callback_query_handler(lambda call: call.data == 'button_ip_addr_in')
async def process_callback_button5(callback_query: types.CallbackQuery, message: types.Message):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, f"Ваш IP: {ip_addr(message)}")

@dp.message_handler(commands = ["start"])
async def start_command(message: types.Message):
	await message.reply("Выберете действие:", reply_markup = kb.kb_start_in)

@dp.message_handler(commands = ["ip"])
async def ip_addr(message: types.Message):
	response = requests.get("http://jsonip.com/").json()
	await message.answer("Ваш IP адресс: " f"{response['ip']}")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates = True)