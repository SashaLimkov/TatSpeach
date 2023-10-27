import os
from aiogram import types
from aiogram.dispatcher import FSMContext
from TatSpeachBot.settings import BASE_DIR
from bot.config.loader import bot
from bot.utils import message_worker as mw
from bot.data import text_data as td
from bot.states.MainMenu import MainMenuState
from bot.keyboards import inline as ik
from bot.utils.text import get_text
from backend.services import telegram_user as tus
from bot.handlers.commands import main_menu

__all__=[
    "splitter",
    "tat_aud_to_txt"
]


async def splitter(call:types.CallbackQuery, state:FSMContext):
    telegram_id = call.message.chat.id
    user = tus.get_profile_by_telegram_id(telegram_id=telegram_id)
    cd = call.data.split("|")[1]
    if cd == td.SEND_TAT_VOICE:
        await MainMenuState.TAT_VOICE.set()
        text = get_text(key=td.SEND_TAT_VOICE, lang=user.selected_language)
    elif cd == td.SEND_RU_VOICE:
        text = get_text(key=td.SEND_RU_VOICE, lang=user.selected_language)
    elif cd == td.SEND_TAT_TEXT:
        text = get_text(key=td.SEND_TAT_TEXT, lang=user.selected_language)
    else:
        text = get_text(key=td.SEND_RU_TEXT, lang=user.selected_language)
    await mw.dry_message_editor(
        text=text,
        keyboard=await ik.back_to_mm(telegram_id=telegram_id),
        state=state,
        message=call.message
    )
async def tat_aud_to_txt(message: types.message, state: FSMContext):
    telegram_id = message.chat.id
    file_id = message.voice.file_id
    file = await bot.get_file(file_id)
    file_path = file.file_path
    file_name = f"{telegram_id} {file_id}.mp3"
    downloaded_file = await bot.download_file(file_path, os.path.join(BASE_DIR,"voice","tat",file_name))
    print(downloaded_file)
    await mw.try_send_voice(
        user_id=telegram_id,
        text="asd",
        voice=file_id,
        keyboard=None,
        state=state
    )
    await main_menu(message=message, state=state, back=True)
