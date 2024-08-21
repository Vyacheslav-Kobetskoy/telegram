import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from config import Token

bot=Bot(token=Token)
dp=Dispatcher()

@dp.message(CommandStart())
async def cmd_start(message: Message):
   await message.answer('Привет')

async def main():
   await dp.start_polling(bot)
   print('Sart')
   

if __name__ == '__main__':
   logging.basicConfig(level=logging.INFO)
   try:
      asyncio.run(main())
   except KeyboardInterrupt:
      print('Exit')
     
     