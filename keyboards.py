from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


#Создаем стартвою клавиатуру
def start_kb():
    inline_kb_list = [
        [InlineKeyboardButton(text="Кнопка 1", callback_data='but_1')],
        [InlineKeyboardButton(text="Кнопка 2", callback_data='but_2')],
        [InlineKeyboardButton(text="Кнопка 3", callback_data='but_3')],
        [InlineKeyboardButton(text="Кнопка 4", callback_data='but_4')]
    ]
    return InlineKeyboardMarkup(inline_keyboard=inline_kb_list)

#Создаем клавиатуру с сылкой для первого задания
def url_kb():
    inline_kb_list = [
        [InlineKeyboardButton(text="Ленина-1",
                              url='https://yandex.ru/maps/10716/balashiha/house/prospekt_lenina_1'
                                  '/Z04YfwVoSEcOQFtvfXt4eX9nZw==/?ll=37.928129%2C55.798344&z=16.27'
                              )],
        [InlineKeyboardButton(text="Назад", callback_data="back")],
    ]

    return InlineKeyboardMarkup(inline_keyboard=inline_kb_list)

#Создаем клавитауру с кнопкой назад
def back_kb():
    inline_kb_list = [
        [InlineKeyboardButton(text="Назад", callback_data="back")],
    ]
    return InlineKeyboardMarkup(inline_keyboard=inline_kb_list)
