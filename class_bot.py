from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor # is required for running the bot
from config2 import open_weather_api, TOKEN
import datetime
import requests # is required for sending request
# python3 -m venv name of the virtual space
# source name of the virtual space/bin/activate.fish or ../name of the virtual space/bin/activate.fish
# pip install -- upgrade pip
# pip install -U aiogram
# pip install requests
bot = Bot(TOKEN)
dp = Dispatcher(bot)

# function has three types of arguments: compulsory, default, random
# @dp is required for extending functions of the main function dp without re-writing
@dp.message_handler(commands=['start'])  # commands for processing command start
async def start_message(msg: types.Message): # async for  working asynchronize
    await msg.reply(f'Hello, {msg.from_user.username} enter your city ')


@dp.message_handler()
async def get_weather(msg: types.Message):
    try:
        r = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={msg.text}&appid={open_weather_api}&units=metric')
        data = r.json()
        city = data['name']
        weather_description = data['weather'][0]['description']
        temp = data['main']['temp']
        sunset = datetime.datetime.fromtimestamp(data['sys']['sunset'])
        sunrise = datetime.datetime.fromtimestamp(data['sys']['sunrise'])
        wind = data['wind']['speed']
        humidity = data['main']['humidity']
        await msg.reply(f'Your city is : {city} \n the weather is : {weather_description} \n temperature is : {temp} degrees per Celsium \n sunset due at : {sunset} \n sunrise due at: {sunrise} \n speed of wind is : {wind} km/h \n level of humidity is: {humidity}%')
    except:
        await msg.reply('Maybe name of the city is incorrect')


executor.start_polling(dp)


