from aiogram.utils.markdown import text

# ! - Русский язык - ! #
start_ru = text(
    "Приветствую!",
    "Это многофункциональный бот, который научит вас различным фишкам telegram.",
    "Для ознакомления с ботом вы можете написать /help_ru или сразу перейти в меню бота.",
    sep = "\n\n"
)

menu_ru = text(
    "Добро пожаловать в главное меню!\n",
    "Здесь вы можете выбрать, какие функции будет исполнять бот.",
    "Вся информация представлена на клавиатуре.",
    sep = "\n"
)

help_ru = text(
    "Этот бот создан в учебных целях :)",
    "Он поможет начинающим программистам узнать, как работают telegram боты.",
    "Для того, чтобы узнать функционал бота, введите /",
    "А если хочешь узнать больше о разработчике и о самом боте, то нажми кнопку ниже.",
    sep = "\n\n"
)

who_ru = text(
    "Меня зовут Захар, мне 16 лет и я Junior Python/C++ программист.\n",
    "В свободное время я люблю писать код, и это дело забавляет меня уже как год.\n",
    "Ну и как большинство программистов, я мечтаю стать классным хакером😎.\n",
    "Правда до этого мне ещё расти и расти :)",
    "А пока что, вы можете ввести команду /source_bot_ru\n",
    "Или нажать на кнопку ниже, чтобы ознакомиться с моим ботом поближе и с моим творчеством в целом👀",
    sep = "\n"
)

main_pc_ru = text(
    "Нажми на IP адрес🌐 или Тех. характеристики PC⚙️",
    "Также ты можешь вернуться в меню ;)",
    sep = "\n\n"
)


MESSAGES_RU = {
    'start_ru': start_ru,
    'menu_ru': menu_ru,
    'help_ru': help_ru,
    'who_ru': who_ru,
    'main_pc_ru': main_pc_ru
}

# ! - Английский язык - ! #
start_en = text(
    "Greetings!",
    "This is a multifunctional bot that will teach you various telegram tricks.",
    "To get acquainted with the bot, you can type /help_en or go directly to the bot menu.",
    sep = "\n\n"
)

menu_en = text(
    "Welcome to the main menu!\n",
    "Here you can choose which functions the bot will perform",
    "All information is presented on the keyboard",
    sep = "\n"
)

help_en = text(
    "This bot was created for educational purposes :)\n",
    "It will help novice programmers learn how telegram bots work.",
    "In order to find out the functionality of the bot, enter /",
    "And if you want to know more about the developer and about the bot itself, then click the button below.",
    sep = "\n"
)

who_en = text(
    "My name is Zakhar, I'm 16 and I'm Junior Python/C++ programmer.\n",
    "In my free time I like to write code, and it's been fun for me for about a year now.\n",
    "And like most programmers I dream to become a cool hacker😎.\n",
    "But I have to grow up to achieve it :)",
    "In the meantime, you can enter the command /source_bot_en\n",
    "Or click the button below to see my bot and my work in general👀",
    sep = "\n"
)

main_pc_en = text(
    "Click on the IP address🌐 or the PC Specifications⚙️",
    "You can also go back to the menu ;)",
    sep = "\n\n"
)


MESSAGES_EN = {
    'start_en': start_en,
    'menu_en': menu_en,
    'help_en': help_en,
    'who_en': who_en,
    'main_pc_en': main_pc_en
}