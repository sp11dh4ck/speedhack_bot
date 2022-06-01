import markups1 as kb

from config import TOKEN, SP_ID
from messages import MESSAGES, MESSAGES_EN

from aiogram import Bot, types
from aiogram.utils import executor
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.middlewares.logging import LoggingMiddleware

# Определяем главные переменные для работы с ботом
bot = Bot(token = TOKEN)
dp = Dispatcher(bot, storage = MemoryStorage())
dp.middleware.setup(LoggingMiddleware())


@dp.callback_query_handler(lambda call: call.data == "button_lang_ru_in")
async def lang_ru(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, MESSAGES['help'])

@dp.callback_query_handler(lambda call: call.data == "button_lang_en_in")
async def lang_ru(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, MESSAGES_EN['help_en'])

@dp.message_handler(commands = ["start"])
async def start_command(message: types.Message):
    await message.answer("Выберете язык бота\n\nСhoose the language Bot", reply_markup = kb.kb_lang_in)

@dp.message_handler(commands = ["commands"])
async def commands_command(message: types.Message):
    await message.answer(MESSAGES['commands'])


if __name__ == '__main__':
	executor.start_polling(dp, skip_updates = True)