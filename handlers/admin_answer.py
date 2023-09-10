from loader import dp, bot, ADMIN_IDS
from aiogram import types
from states import *
from aiogram.dispatcher import FSMContext
import texts
from aiogram.dispatcher import filters
import keyboards as kb


@dp.message_handler(filters.IsReplyFilter(types.Message()),
                    filters.IDFilter(chat_id=ADMIN_IDS),
                    state='*',
                    content_types=['any'])
async def confirm(message: types.Message):
    if message.reply_to_message.text:
        id_sender = message.reply_to_message.text.split(' ')[0]
    else:
        id_sender = message.reply_to_message.caption.split(' ')[0]
    try:
        await message.send_copy(id_sender)
    except Exception as e:
            print(e)
            await message.answer(texts.warn_id)
    await message.answer(texts.resent_to(id_sender))
        