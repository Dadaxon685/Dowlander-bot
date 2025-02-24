import logging
import os
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.filters import CommandStart
from aiogram.types import FSInputFile
import yt_dlp
import asyncio
logging.basicConfig(level=logging.INFO)

token = "7548128169:AAHkI255NhOskgx1uQ6bpzyN7DCMooAUVvE"  # Bu yerga bot tokeningizni kiriting

bot = Bot(token=token)
dp = Dispatcher()


@dp.message(CommandStart())
async def StartBot(message: Message):
    await message.answer("Assalomu alaykum! Video yuklash uchun menga YouTube havolasini yuboring 🎥")


@dp.message(F.text)
async def yuklab_ber(message: Message):
    link = message.text.strip()
    
    # Yangi nom berish
    video_name = "downloaded_video.mp4"
    video_options = {
        "format": "best",
        "outtmpl": video_name
    }
    
    try:
        await message.answer("⏳ Videoni yuklab olish jarayoni boshlandi...")
        
        # YouTube'dan video yuklash
        with yt_dlp.YoutubeDL(video_options) as downloader:
            downloader.download([link])
        
        # Faylni Telegramga yuborish
        video = FSInputFile(video_name)
        await message.answer_video(video=video, caption="🎬 Siz so‘ragan video tayyor!")

    except Exception as e:
        await message.answer(f"❌ Xatolik yuz berdi: {str(e)}")
    
    finally:
        # Faylni o‘chirish
        if os.path.exists(video_name):
            os.remove(video_name)


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
