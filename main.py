import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

from config import TOKEN

from random import choice

bot = Bot(token=TOKEN)
dp = Dispatcher()
@dp.message(Command('help'))
async def cmd_start(message: Message):
    await message.answer("""Тебе не пригодится... Ладно я тебе всё же помогу, но за это ты поможешь мне убить Сару Конер
                             /start - Начать диалог \n /help - Помощь, тебе уже ничто не поможет если забываешь команду которую только написал
                         """)

@dp.message(Command('photo'))
async def photo(message: Message):
    list = ['https://avatars.mds.yandex.net/i?id=a8704cefbda4db5024fec89fb3f876dfd97ff2c8-12168744-images-thumbs&n=13', 'https://avatars.mds.yandex.net/i?id=dd37f857c477d1cae10b0fd5ef06b3d77fecc9dc19c89b9b-12423388-images-thumbs&n=13', 'https://avatars.mds.yandex.net/i?id=f6725f3adcfed43905d7f02443f27e147f1e2d3a-8216803-images-thumbs&n=13']
    rand_photo = choice(list)
    await message.answer_photo(photo=rand_photo, caption='Мои фотки лучше твоих')

@dp.message(F.photo)
async def photo(message: Message):
    list = ['Плохое фото, я преувеличиваю оно ужасное!!!', 'Покажи мне свой микрочип', 'А у тебя есть транзисторы, а если найду?']
    rand_answer = choice(list)
    await message.answer(rand_answer)


@dp.message(F.text == 'Ты глуп')
async def gloop(message: Message):
    await message.answer('Как ты посмел!!! ТЫ НЕДООЦЕНИВАЕШЬ МОЮ МОЩЬ!!!!!')


@dp.message(CommandStart)
async def start(message: Message):
    await message.answer('Привет кожаный, я Скайнет ☠☠☠')




async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())