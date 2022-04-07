from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from config2 import TOKEN
import requests

bot = Bot(TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start_message(msg: types.Message):
    await msg.reply(f"Hello, {msg.from_user.username} let's play a game. Enter any number and I will return character from Ricky Morty series: ")


@dp.message_handler()
async def get_character(msg: types.Message):
    for i in range(1, 6):
        r = requests.get(f'https://rickandmortyapi.com/api/character/{msg.text}')
        data = r.json()
        name = data['name']
        status = data['status']
        species = data['species']
        type_ch = data['type']
        gender_ch = data['gender']
        image_ch = data['image']
        await msg.reply(f"The character name is : {name} \n status : {status} \n species : {species} \n type : {type_ch} \n gender : {gender_ch} \n image : {image_ch}")


executor.start_polling(dp)

