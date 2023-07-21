

import logging

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '6153682995:AAGoKbZKFdDvJwl-JS6R_VzRsGEt3eC_8is'

logging.basicConfig(level=logging.INFO)


bot = Bot(token=API_TOKEN, parse_mode='html')
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', ])
async def send_welcome(message: types.Message): 
    image = types.InputFile("image.png")
    await message.answer_photo(photo=image)

@dp.message_handler(commands = ['photo'])
async def send_photo_handler(message : types.Message):
    image = types.InputFile("photo.jpg")
    await message.answer_photo(photo=image)


    print (message.from_user.id)
    print (message.from_user.first_name)
    print (message.from_user.last_name)
    print (message.from_user.username)

    await message.reply("Salom")




@dp.message_handler(commands=['text'])
async def start(message: types.Message):
    await message.answer("<b>happy</b>")
    await message.answer("<i>birthday</i>")
    await message.answer("<u>to</u>")
    await message.answer("<s>you</s>")
    await message.answer("<tg-spoiler>Sogdiana</tg-spoiler>")
    await message.answer("<a href='t.me/gutsy_di'>gutsy_di</a>")
    await message.answer("<code>kahoot</code>")
    await message.answer("<pre>kahoot</pre>")

    





@dp.message_handler(commands=['audio'])
async def send_audio_handler(message: types.Message):
    audio = types.InputFile("vaudio.mp3")
    await message.answer_audio(audio = audio)

@dp.message_handler(commands=['voice'])
async def send_voice_handler(message: types.Message):
    voice = types.InputFile("voice.ogg")
    await message.answer_voice(voice = voice)

@dp.message_handler(commands=['animation'])
async def send_animation_handler(message: types.Message):
    animation = types.InputFile("animation.gif.mp4")
    await message.answer_animation(animation = animation)

@dp.message_handler(commands=['sticker'])
async def send_sticker_handler(message: types.Message):
    sticker = types.InputFile("sticker.webp")
    await message.answer_sticker(sticker = sticker)
    




if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)