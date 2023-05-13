import requests
import datetime
from pprint import pprint
from config import token


# Функция получения погоды
def get_weather(city, token):
    icon_code = {
        'Clear': 'Ясно \U00002600',
        'Clouds': 'Облачно \U00002601',
        'Rain': 'Дождь \U00002614',
        'Drizzle': 'Дождь \U00002614',
        'Thunderstorm': 'Гроза \U000026A1',
        'Snow': 'Снег \U0001F328',
        'Mist': 'Туман \U0001F32B'

    }
    try:
        req = requests.get(
            f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={token}&units=metric&lang=ru')
        data = req.json()
        # pprint(data)

        city = data['name']
        temp_now = data['main']['temp']
        weather_icon = data['weather'][0]['main']
        # Условие для отображения иконки по погоде
        if weather_icon in icon_code:
            wi = icon_code[weather_icon]
        else:
            wi = 'Блин, чет хз, а может в окно глянешь?'
        pressure = data['main']['pressure']
        humidity = data['main']['humidity']
        wind = data['wind']['speed']
        sunrise = datetime.datetime.fromtimestamp(data['sys']['sunrise'])
        sunset = datetime.datetime.fromtimestamp(data['sys']['sunset'])

        print(f"***{datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}***\n"
              f'Погода в городе: {city}\n'
              f'Температура: {temp_now}°С {wi}\n'
              f'Давление: {pressure} мм.рт.ст.\n'
              f'Влажность: {humidity}%\n'
              f'Ветер: {wind}м/с\n'
              f'Рассвет: {sunrise}\n'
              f'Закат: {sunset}\n'
              f'Хорошего дня!')
    except Exception as ex:
        print(ex)
        print('Название города указано не верно!')


def main():
    city = input('Введите город: ')
    get_weather(city, token)


if __name__ == '__main__':
    main()
