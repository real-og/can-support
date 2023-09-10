from loader import dp, bot, ADMIN_IDS
from aiogram import types
from states import *
from aiogram.dispatcher import FSMContext
import texts
from aiogram.dispatcher import filters
import keyboards as kb
import tables
from handlers.commands import send_menu
import logic


@dp.message_handler(filters.IDFilter(chat_id=ADMIN_IDS),
                    commands=['broadcast'],
                    state='*')
async def confirm(message: types.Message):
    await message.answer(texts.broadcast, reply_markup=kb.cancel_kb)
    await State.broadcast.set()


@dp.callback_query_handler(filters.IDFilter(chat_id=ADMIN_IDS), state=State.broadcast)
async def send_channels(callback: types.CallbackQuery, state: FSMContext):
    if callback.data == 'cancel':
        await callback.message.answer(texts.canceled)
        await send_menu(callback.message, state)


@dp.message_handler(filters.IDFilter(chat_id=ADMIN_IDS),
                    state=State.broadcast,
                    content_types=['any'])
async def confirm(message: types.Message, state: FSMContext):
    
    ids = logic.get_all_redis_keys()
    print(ids)
    for id in ids:
        try:
            await message.send_copy(id)
        except Exception as e:
            print(e)
    await message.answer(texts.succes)
    await send_menu(message, state)
