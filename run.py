import logging
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.types import ParseMode, ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils import executor

API_TOKEN = '7310816247:AAGdCAoCim82ca8AfLxhpbAgUA8Bb1k5cuc'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware())

# Define the keyboard buttons
button1 = KeyboardButton('Button 1')
button2 = KeyboardButton('Button 2')
keyboard_markup = ReplyKeyboardMarkup(resize_keyboard=True).add(button1).add(button2)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Welcome! This is the /start command. Use the buttons below to interact with the bot.", reply_markup=keyboard_markup)

@dp.message_handler(commands=['help'])
async def send_help(message: types.Message):
    help_text = (
        "This is the /help command. Here you can describe how to use your bot.\n"
        "You can add more detailed instructions or information as needed."
    )
    await message.reply(help_text)

@dp.message_handler(lambda message: message.text == "Button 1")
async def handle_button1(message: types.Message):
    await message.reply("You pressed Button 1!")

@dp.message_handler(lambda message: message.text == "Button 2")
async def handle_button2(message: types.Message):
    await message.reply("You pressed Button 2!")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
