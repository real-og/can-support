from loader import dp, ADMIN_IDS
from aiogram import types
from aiogram.dispatcher import FSMContext
import texts
import keyboards as kb
from states import State
from handlers.commands import send_menu
from logic import add_header_to_mes


@dp.callback_query_handler(state=State.menu)
async def send_channels(callback: types.CallbackQuery, state: FSMContext):
    if callback.data == 'support':
        await callback.message.answer(texts.ask_for_question, reply_markup=kb.back_kb)
        await State.entering_support_message.set()


@dp.callback_query_handler(state=State.entering_support_message)
async def send_channels(callback: types.CallbackQuery, state: FSMContext):
    if callback.data == 'back':
        await send_menu(callback.message, state)


@dp.message_handler(state=State.entering_support_message, content_types=['any'])
async def receive_check(message: types.Message, state: FSMContext):
    message_to_send = add_header_to_mes(message)
    for id in ADMIN_IDS:
        try:
            await message_to_send.send_copy(id)
        except Exception as e:
            print(e)
    await message.answer(texts.message_accepted)
    await send_menu(message, state)


    