from pyowm.owm import OWM
from pyowm.utils.config import get_default_config

#язык
config_dict = get_default_config()
config_dict['language'] = 'ru'

#создание апи-ключа
owm = OWM('01b13d5b0bf7f7c01f3944bb415b4cb4', config_dict)
mgr = owm.weather_manager()

place = input("Введите город: ") #место исследования

observation = mgr.weather_at_place(place) #исследование

w = observation.weather #статус погоды
temp = w.temperature('celsius')["temp"] #температура

#вывод
print('В городе ' + place + ' сейчас ' + w.detailed_status)
print('Температура: ', temp)
if temp < 5:
    print('Сейчас очень холодно, советуем одеться потеплее!')
elif temp < 17:
    print('Сейчас прохладно, не советуем одеваться слишком легко.')
else:
    print('Сейчас тепло, можно легко одеться!')