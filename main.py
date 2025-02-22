import logging
import os
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.filters import CommandStart
from aiogram.types import FSInputFile
import yt_dlp
import asyncio
logging.basicConfig(level=logging.INFO)

token = "7584542296:AAG52pR5J2tA9FlR4l4Jbf2QdxvnuteHqj4"  # Bu yerga bot tokeningizni kiriting

bot = Bot(token=token)
dp = Dispatcher()


@dp.message(CommandStart())
async def StartBot(message: Message):
    await message.answer("Assalomu alaykum, botdan foydalanishingiz mumkin")


@dp.message(F.text)
async def YuklaBot(message: Message):
    link = message.text
    videos = {"format": "mp4", "outtmpl": "video.%(ext)s"}

    with yt_dlp.YoutubeDL(videos) as dow:
        dow.download([link])

    video = FSInputFile("video.mp4")
    await message.answer_video(video=video, caption="Siz so‘ragan video")

    os.remove("video.mp4")


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
