from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton


# lvl 1
button_help_in = InlineKeyboardButton("Информация о боте📃", callback_data = 'button_help_in')
button_commands_in = InlineKeyboardButton("Команды бота💠", callback_data = 'button_commands_in')

kb_start_in = InlineKeyboardMarkup().add(button_help_in, button_commands_in)

# lvl 2
button_who_in = InlineKeyboardButton("Кто ты❓", callback_data = "button_who_in")

kb_who_in = InlineKeyboardMarkup().add(button_who_in)

# lvl 3
button_source_in = InlineKeyboardButton("Source Bot📀", url = "https://github.com/sp11dh4ck/main_bot_alpha")

kb_source_in = InlineKeyboardMarkup().add(button_source_in)
#kb_source_in.add(InlineKeyboardButton("Source Bot📀", url = "")) # = InlineKeyboardMarkup().add(button_source_in)