import asyncio
from aiogram import Bot, Dispatcher, F # F - фильтр Для фильтров
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
import requests

from config import TOKEN, API_KEY, CITY


bot = Bot(token=TOKEN)
dp = Dispatcher()
api_adress = f'https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric'

@dp.message(Command('weather'))
async def weather(message: Message):
    weather_json = requests.get(api_adress).json() #Получаем данные о погоде в сыром виде
    weather_real = weather_json['weather'][0]['main'] #Получаем данные о погоде в реальном виде
    temp = weather_json['main']['temp'] #Получаем данные о температуре в реальном виде
    await message.answer(f'В городе {CITY} {weather_real}, температура {temp}') #Отправляем сообщение с данными погоды

@dp.message(Command('help'))
async def cmd_start(message: Message):
    await message.answer("""Тебе не пригодится... Ладно я тебе всё же помогу, но за это ты поможешь мне убить Сару Конер
                             /start - Начать диалог \n /help - Помощь, тебе уже ничто не поможет если забываешь команду которую только написал
                         """)

@dp.message(CommandStart)
async def start(message: Message):
    await message.answer('Привет кожаный, я Скайнет ☠☠☠')



async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())