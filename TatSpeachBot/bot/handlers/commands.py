from aiogram import types
from aiogram.dispatcher import FSMContext

from bot.utils.text import get_text
from bot.data import text_data as td
from backend.services import text as ts
from backend.services import telegram_user as tus
from bot.keyboards import reply as rk


async def new_user(message: types.Message, state: FSMContext):
    telegram_id = message.chat.id
    full_name = message.from_user.full_name
    default_language = ts.get_default_language()
    await message.reply(
        text=get_text(key=td.HELLO_MES, lang=default_language)
    )
    await message.reply(
        text=get_text(key=td.SET_LANGUAGE, lang=default_language),
        reply_markup=await rk.select_language()
    )
    tus.create_user(telegram_id=telegram_id, full_name=full_name)
    
    

async def old_user(message: types.Message, state: FSMContext):
    await main_menu(message=message, state=state)

async def main_menu(message: types.Message, state: FSMContext):
    pass

