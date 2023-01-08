import telebot
import key
from pyowm.owm import OWM
from pyowm.utils.config import get_default_config
from pyowm.commons.exceptions import NotFoundError

#язык
config_dict = get_default_config()
config_dict['language'] = 'ru'

#создание апи-ключа
owm = OWM('01b13d5b0bf7f7c01f3944bb415b4cb4', config_dict)
mgr = owm.weather_manager()

#создание бота
bot = telebot.TeleBot(key.TOKEN)

@bot.message_handler(commands=['start']) #команда старт и первое смс
def welcome(message):
    sti = open('hello.tgs', 'rb') #стикер
    qw = "Для получения информации о погоде, введите город: "
    bot.send_sticker(message.chat.id, sti)
    bot.send_message(message.chat.id, qw)

@bot.message_handler(content_types=['text']) #отправка смс с погодой
def send(message):
    try:
        observation = mgr.weather_at_place(message.text)  # исследование
    except NotFoundError: #обработка ошибки "неверный город"
        bot.send_message(message.chat.id, 'Неизвестный город.')
    else: #вывод если ошибок нет
        w = observation.weather  # статус погоды
        temp = w.temperature('celsius')["temp"]  # температура

        answer = 'В городе ' + message.text + ' сейчас ' + str(w.detailed_status) + "\n"
        answer += 'Температура: ' + str(temp) + "\n\n"
        if temp < 5:
            answer += 'Сейчас очень холодно, советуем одеться потеплее!' + "\n\n\n"
        elif temp < 17:
            answer += 'Сейчас прохладно, не советуем одеваться слишком легко.' + "\n\n\n"
        else:
            answer += 'Сейчас тепло, можно легко одеться!' + "\n\n\n"
        bot.send_message(message.chat.id, answer)

    finally: #постоянный вывод в конце смс
        qw = "Для получения информации о погоде, введите город: "
        bot.send_message(message.chat.id, qw)

#запуск бота
bot.polling(none_stop=True)