from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


# start command
button_help_in = InlineKeyboardButton("Информация о боте📃", callback_data = 'button_help_in')
button_commands_in = InlineKeyboardButton("Команды бота💠", callback_data = 'button_commands_in')
button_menu_in = InlineKeyboardButton("Меню🌍", callback_data = 'button_menu_in')

kb_start_in = InlineKeyboardMarkup().add(button_help_in, button_commands_in).add(button_menu_in)

# who command
button_who_in = InlineKeyboardButton("Кто ты❓", callback_data = "button_who_in")

kb_who_in = InlineKeyboardMarkup().add(button_who_in).add(button_menu_in)

# source command
button_source_in = InlineKeyboardButton("Исходники Бота📀", url = "https://github.com/sp11dh4ck/main_bot_alpha")

kb_source_in = InlineKeyboardMarkup().add(button_source_in).add(button_menu_in)

# menu command
button_ip_addr_in = InlineKeyboardButton("IP адрес🌐", callback_data = 'button_ip_addr_in')
button_pc_spec_in = InlineKeyboardButton("Тех. характеристики PC💻", callback_data = 'button_pc_spec_in')

kb_menu_in = InlineKeyboardMarkup().add(button_ip_addr_in, button_pc_spec_in).add(button_commands_in)

kb_menu_commands_in = InlineKeyboardMarkup().add(button_menu_in)