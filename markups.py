from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


# ! - Общие кнопки - ! #
# --- Выбор языка --- #
button_ru = InlineKeyboardButton("RU🇷🇺", callback_data = 'button_ru')
button_en = InlineKeyboardButton("EN🇬🇧", callback_data = 'button_en')
kb_lang = InlineKeyboardMarkup().add(button_ru, button_en)

# --- Кнопка меню --- #
button_menu_ru = InlineKeyboardButton("Меню🌍", callback_data = 'button_menu_ru')
button_menu_en = InlineKeyboardButton("Menu🌍", callback_data = 'button_menu_en')

# --- Кнопки инфы о пк --- #
button_pc_info_ru = InlineKeyboardButton("Информация о PC💻", callback_data = "button_pc_info_ru")
button_pc_info_en = InlineKeyboardButton("PC info💻", callback_data = "button_pc_info_en")


# ! - Русские кнопки - ! #
# --- Стартовая команда + меню --- #
button_help_ru = InlineKeyboardButton("Информация о боте📃", callback_data = 'button_help_ru')
kb_start_ru = InlineKeyboardMarkup().add(button_help_ru).add(button_menu_ru)

# --- Кнопка кто + меню --- #
button_who_ru = InlineKeyboardButton("Кто ты❓", callback_data = "button_who_ru")
kb_who_ru = InlineKeyboardMarkup().add(button_who_ru).add(button_menu_ru)

# --- Кнопка исходники + меню --- #
button_source_ru = InlineKeyboardButton("Исходники Бота📀", url = "https://github.com/sp11dh4ck/main_bot_alpha")
kb_source_ru = InlineKeyboardMarkup().add(button_source_ru).add(button_menu_ru)

# --- Главное меню --- #
button_shift_lang_ru = InlineKeyboardButton("Language change💾", callback_data = "button_shift_lang_ru")
kb_menu_ru = InlineKeyboardMarkup().add(button_pc_info_ru).add(button_shift_lang_ru)

# --- Меню инфы о пк + меню --- #
button_ip_addr_ru = InlineKeyboardButton("IP Адрес🌐", callback_data = 'button_ip_addr_ru')
button_pc_spec_ru = InlineKeyboardButton("Тех. Характеристики PC⚙️", callback_data = 'button_pc_spec_ru')
kb_menu_pc_ru = InlineKeyboardMarkup().add(button_ip_addr_ru, button_pc_spec_ru).add(button_menu_ru)


# ! - Английские кнопки - ! #
# --- Стартовая команда + меню --- #
button_help_en = InlineKeyboardButton("Bot Information📃", callback_data = 'button_help_en')
kb_start_en = InlineKeyboardMarkup().add(button_help_en).add(button_menu_en)

# --- Кнопка кто + меню --- #
button_who_en = InlineKeyboardButton("Who you are❓", callback_data = "button_who_en")
kb_who_en = InlineKeyboardMarkup().add(button_who_en).add(button_menu_en)

# --- Кнопка исходники + меню --- #
button_source_en = InlineKeyboardButton("Source Bot📀", url = "https://github.com/sp11dh4ck/main_bot_alpha")
kb_source_en = InlineKeyboardMarkup().add(button_source_en).add(button_menu_en)

# --- Главное меню --- #
button_shift_lang_en = InlineKeyboardButton("Изменить язык💾", callback_data = "button_shift_lang_en")
kb_menu_en = InlineKeyboardMarkup().add(button_pc_info_en).add(button_shift_lang_en)

# --- Меню инфы о пк + меню --- #
button_ip_addr_en = InlineKeyboardButton("IP Address🌐", callback_data = 'button_ip_addr_en')
button_pc_spec_en = InlineKeyboardButton("PC Specifications⚙️", callback_data = 'button_pc_spec_en')
kb_menu_pc_en = InlineKeyboardMarkup().add(button_ip_addr_en, button_pc_spec_en).add(button_menu_en)
# ------------- #