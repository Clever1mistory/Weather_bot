import requests
import datetime
from config import tg_bot_token, token
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

# Создаем объект бота и передаем в него токен
bot = Bot(token=tg_bot_token)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start_c(message: types.Message):
    await message.reply('Привет! Напиши название города и получишь информацию о погоде')


@dp.message_handler()
async def get_weather(message: types.Message):
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
            f'https://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={token}&units=metric&lang=ru')
        data = req.json()

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

        await message.reply(f"Сегодня {datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}\n"
                            f'Погода в городе: {city}\n'
                            f'Температура: {temp_now}°С {wi}\n'
                            f'Давление: {pressure} мм.рт.ст.\n'
                            f'Влажность: {humidity}%\n'
                            f'Ветер: {wind}м/с\n'
                            f'Рассвет: {sunrise}\n'
                            f'Закат: {sunset}\n'
                            f'Хорошего дня!')

    except:
        await message.reply('\U00002620 Название города указано не верно! \U00002620')


if __name__ == '__main__':
    executor.start_polling(dp)
