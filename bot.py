import asyncio
import logging
import os
from time import sleep

from aiogram import Bot, Dispatcher, F, types
from aiogram.filters.command import Command
import emoji
from dotenv import load_dotenv

from constants import PAUSE_DURATION_SECONDS_BOT
from utils import get_copout


load_dotenv()

bot = Bot(token=os.getenv('API_TOKEN'))
dp = Dispatcher()


@dp.message(Command('start'))
async def command_start(message: types.Message):

    kb = [[types.KeyboardButton(text='Сгенерировать отмазку')],]

    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder='Сгенерировать отмазку'
    )

    await message.answer(
        'Профакапил? Сорвал сроки? Не знаешь что сказать боссу?\n'
        'Помогу тебе получить отмазку',
        reply_markup=keyboard
    )


@dp.message(F.text.lower() =='сгенерировать отмазку')
async def send_copout(message: types.Message):
    await message.answer('Генерируем отмазку...\n')
    sleep(PAUSE_DURATION_SECONDS_BOT)

    await message.answer(
        'Сверяемся с лунным календарем и положением планет\n'
        f'  {emoji.emojize(":crystal_ball:")} '
        f'  {emoji.emojize(":crystal_ball:")} '
        f'  {emoji.emojize(":crystal_ball:")} '
    )
    sleep(PAUSE_DURATION_SECONDS_BOT)
    await message.answer(
        'Подожди немного прооисходит магия\n'
        f'  {emoji.emojize(":magic_wand:")} '
        f'  {emoji.emojize(":magic_wand:")} '
        f'  {emoji.emojize(":magic_wand:")} '
    )
    copout = get_copout()
    await message.answer(
        f'Готово!\n {emoji.emojize(":grinning_face_with_sweat:")}'
    )
    await message.answer(copout)


async def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - [%(levelname)s] - %(name)s - "
               "(%(filename)s).%(funcName)s(%(lineno)d) - %(message)s"
    )

    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
