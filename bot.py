from telebot import TeleBot
import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton, Message, InputFile
import info
TOKEN = "6754967146:AAF7xmgkMjbgJv0vYPoIVW4OVrkv11Yhvps"
bot = telebot.TeleBot(TOKEN)

content = {
    'start': {
        'text': 'Привет, это бот с расписанием. В этом боте есть только глобальное расписание на 3-ю четверть. Из какого ты класса?',
        'buttons': ["5-й", "6-й", "7-й", "8-й", "9-й", "8-й б"],
        'loose': False,
        'img': ''
    },
    '8-й': {
        'text': 'На какой день тебе нужно расписание?',
        'buttons': ['Понедельник(8)', 'Вторник(8)', "Среда(8)", "Четверг(8)", "Пятница(8)"],
        'loose': False,
        'img': ''
    },
    'Понедельник(8)': {
        'text': """1. РОВ
2. Рус. яз.
3. История
4. География
5. Алгебра
6. Физика
 7. Ин. яз.
8. ОПД""",
        'buttons': [],
        'loose': False,
        'img': ''
    },
    'Вторник(8)': {
        'text': """1. -
2. Геометрия
3. Информатика
4. Ин.яз.
5. Физ-ра
6. Литература
7. Биология'
8. Химия""",
        'buttons': [],
        'loose': False,
        'img': ''
    },
    'Среда(8)': {
        'text': """1. Алгебра
2. Вероятность и Статистика
3. История
4. Технология
5. География
6. Физ-ра
7. Музыка
8. ЛАФ""",
        'buttons': [],
        'loose': True,
        'img': ''
    },
    'Четверг(8)': {
        'text': """1. -
2. -
3. -
4. РМГ
5. Рус. яз.
6. Литература
7. Геометрия
8. Физика
9. Химия
10. Биология""",
        'buttons': [],
        'loose': False,
        'img': ''
    },
    'Пятница(8)': {
        'text': """1. -
2. Рус. яз.
3. Общество
4. Алгебра
5. ОБЖ
6. Ин. яз.""",
        'buttons': [],
        'loose': False,
        'img': ""
    },
    '7-й': {
        'text': 'На какой день тебе нужно расписание?',
        'buttons': ['Понедельник(7)', 'Вторник(7)', "Среда(7)", "Четверг(7)", "Пятница(7)"],
        'loose': False,
        'img': ''
    },
    'Понедельник(7)': {
        'text': """1. РОВ
2. География
3. Ин. яз. 
4. Математика
5. История
6. Рус. яз.
7. Биология""",
        'buttons': [],
        'loose': False,
        'img': ''
    },
    'Вторник(7)': {
        'text': """1. Музыка
2. Общество
3. Рус.яз
4. ИЗО
5. Математика
6. Информатика
7. Ин. яз. Ф""",
        'buttons': [],
        'loose': False,
        'img': ''
    },
    'Среда(7)': {
        'text': """1. Физ-ра
2. География
3. Рус. яз.
4. Литература
5. Математика
6. Физика
7. Биология""",
        'buttons': [],
        'loose': True,
        'img': ''
    },
    'Четверг(7)': {
        'text': """1. ВН РМГ
2. Математика
3. Математика
4. История
5. Ин. яз.
6. Технология
7. Технология""",
        'buttons': [],
        'loose': False,
        'img': ''
    },
    'Пятница(7)': {
        'text': """1. Рус. яз.
2. Ин. яз.
3. Математика
4. Физ-ра
5. Физика
6. Литература
7. ОПД""",
        'buttons': [],
        'loose': False,
        'img': ""
    },
    '9-й': {
        'text': 'На какой день тебе нужно расписание?',
        'buttons': ['Понедельник(9)', 'Вторник(9)', "Среда(9)", "Четверг(9)", "Пятница(9)"],
        'loose': False,
        'img': ''
    },
    'Понедельник(9)': {
        'text': """1. РОВ
2. История
3. География 
4. Ин. яз.
5. Рус. яз. 
6. Технология
7. Математика
8. Физика""",
        'buttons': [],
        'loose': False,
        'img': ''
    },
    'Вторник(9)': {
        'text': """1. -
2. -
3. -
4. Рус. яз.
5. Литература
6. Физ-ра
7. Математика
8. Физика
9. Биология
10. Химия""",
        'buttons': [],
        'loose': False,
        'img': ''
    },
    'Среда(9)': {
        'text': """1. -
2. Ин. яз.
3. Физ-ра
4. География
5. Рус. яз.
6. Литература
7. Математика
8. Информатика""",
        'buttons': [],
        'loose': True,
        'img': ''
    },
    'Четверг(9)': {
        'text': """1. -
2. История
3. Ин. яз.
4. РМГ
5. Математика
6. Математика
7. Химия
8. Биология""",
        'buttons': [],
        'loose': False,
        'img': ''
    },
    'Пятница(9)': {
        'text': """1. -
2. Общество
3. ОБЖ
4. История
5. Литература
6. Математика
7. Физика
8. ВН ФГ""",
        'buttons': [],
        'loose': False,
        'img': ""
    },
'6-й': {
        'text': 'На какой день тебе нужно расписание?',
        'buttons': ['Понедельник(6)', 'Вторник(6)', "Среда(6)", "Четверг(6)", "Пятница(6)"],
        'loose': False,
        'img': ''
    },
    'Понедельник(6)': {
        'text': """1. РОВ
2. Литература
3. Математика
4. Рус. яз.
5. Биология
6. Музыка""",
        'buttons': [],
        'loose': False,
        'img': ''
    },
    'Вторник(6)': {
        'text': """1. Рус. яз.
2. Ин. яз.
3. История
4. Математика
5. ОДНКНР
6. Литература
7. Физ-ра""",
        'buttons': [],
        'loose': False,
        'img': ''
    },
    'Среда(6)': {
        'text': """1. География
2. Рус. яз.
3. Математика
4. Ин. яз.
5. Технология
6. Технология
7. ГТО""",
        'buttons': [],
        'loose': True,
        'img': ''
    },
    'Четверг(6)': {
        'text': """1. РМГ
2. Рус. яз.
3. Рус. яз.
4. Математика
5. История
6. ИЗО""",
        'buttons': [],
        'loose': False,
        'img': ''
    },
    'Пятница(6)': {
        'text': """1. Общество
2. Математика
3. Ин. яз.
4. Рус. яз.
5. Литература
6. Физ-ра
7. Факультатив""",
        'buttons': [],
        'loose': False,
        'img': ""
    },
}

def knopki(buttons):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    for ell in buttons:
        keyboard.add(KeyboardButton(ell))

    return keyboard

@bot.message_handler(commands=['start'])
def handler_start(message: Message):
    user_id = message.from_user.id
    data_location = content['start']
    keyword_now = knopki(data_location['buttons'])
    if data_location['img'] != '':
        img = open(data_location['img'], 'rb')
        bot.send_photo(chat_id=user_id, photo=img)
    bot.send_message(chat_id=user_id, text=data_location['text'], reply_markup=keyword_now)

@bot.message_handler(content_types=['text'])
def handler_text(message: Message):
    user_id = message.from_user.id
    if message.text in content:
        buttons = content[message.text]['buttons']
        if buttons:
            keyboard = knopki(buttons)
            bot.send_message(chat_id=user_id, text=content[message.text]['text'], reply_markup=keyboard)
        else:
            bot.send_message(chat_id=user_id, text=content[message.text]['text'])

bot.polling()
