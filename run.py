import asyncio
import logging
import aiogram
from aiogram import Bot, Dispatcher, F, types
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, KeyboardButton, ReplyKeyboardRemove, InlineKeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder
from config import Token
from random import randint

bot=Bot(token=Token)
dp=Dispatcher()

@dp.message(CommandStart())
async def cmd_start(message: Message):
   await message.answer(f'Привет {message.chat.first_name}')

@dp.message(Command('info'))
async def cmd_info(message):
   await message.answer(f'{message}')

@dp.message(Command('key'))
async def cmd_key(message: Message):
   R_builder = ReplyKeyboardBuilder()
   R_builder.row(
      KeyboardButton(text="1"),
      KeyboardButton(text="stop") 
    )
   R_builder.row(
        KeyboardButton(text="Запросить геолокацию", request_location=True),
        KeyboardButton(text="Запросить контакт", request_contact=True)
    )
   await message.answer('описание',
                        reply_markup=R_builder.as_markup(resize_keyboard=True, input_field_placeholder="Выбирай"))

@dp.message(F.text.lower() =='stop')
async def cmd_stop(message: Message):
   await message.answer(f'Пока', reply_markup=ReplyKeyboardRemove())


@dp.message(Command("random"))
async def cmd_random(message: Message):
    builder = InlineKeyboardBuilder()
    builder.add(InlineKeyboardButton(
        text="Нажми меня",
        callback_data="random_value")
    )
    await message.answer(
        "Нажмите на кнопку, чтобы бот отправил число от 1 до 10",
        reply_markup=builder.as_markup()
    )
@dp.callback_query(F.data == "random_value")
async def send_random_value(callback: types.CallbackQuery):
    await callback.message.answer(str(randint(1, 10)))
    
async def main():
   await dp.start_polling(bot)

if __name__ == '__main__':
   logging.basicConfig(level=logging.INFO)
   try:
      asyncio.run(main())
   except KeyboardInterrupt:
      print('Exit')
     
     