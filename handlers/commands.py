from loader import dp
from aiogram import types
from aiogram.dispatcher import FSMContext
import texts
import keyboards as kb
from states import State

@dp.message_handler(commands=['start'], state="*")
async def send_menu(message: types.Message, state: FSMContext):
    await message.answer(f'{message.from_user.language_code} - {texts.your_lang}')
    await message.answer(texts.greeting, reply_markup=kb.contact_support_kb)
    await State.menu.set()