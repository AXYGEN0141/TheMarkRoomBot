from aiogram import types
from loader import dp

from aiogram.dispatcher.filters import Command


@dp.message_handler(Command('info'))
async def bot_info(message: types.Message):
    text = ("Hello, mate!",
            "🎉🎉Welcome to <i>Kathrine Kollegiet's</i> personal bot!🎉🎉\n",
            "🇩🇰🇩🇰If you read this, hopefully right now you are in <b>Copenhagen</b> with which our team would like to congratulate you!🇩🇰🇩🇰\n",
            "This bot is designed specifically for KK's residents, just to make their life easier while their trip!\n",
            "Please type \"/help\" to see full list of commands 😉")
    await message.answer("\n".join(text))