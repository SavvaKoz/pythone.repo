# Imort library
from main import dp, bot
from aiogram import types
from aiogram.types import Message

# Send message to admin
async def send_to_admin(dp):
        await bot.send_message(chat_id=477072646, text="Bot start")

# Start bot using func
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
        text = 'Bot moi'
        await message.answer(text=text)
