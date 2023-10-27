

from bot.utils.text import get_text
from bot.utils.base_keyboard_utils import get_base_keyboard, get_inline_button
from backend.services import telegram_user as tus
from bot.data import text_data as td


__all__ = [
    "select_action",
    "back_to_mm"
]

async def select_action(telegram_id):
    keyboard = await get_base_keyboard(
        keyboard_options={
            "row_width": 1,
        },
    )
    user = tus.get_profile_by_telegram_id(telegram_id=telegram_id)
    txt = [td.SEND_TAT_VOICE,td.SEND_RU_VOICE,td.SEND_TAT_TEXT,td.SEND_RU_TEXT]
    for text in txt:
        keyboard.add(
            await get_inline_button(
                text=get_text(key=text, lang=user.selected_language), 
                cd="splitter|"+text
            )
        )
    return keyboard

async def back_to_mm(telegram_id):
    keyboard = await get_base_keyboard(
        keyboard_options={
            "row_width": 1,
        },
    )
    user = tus.get_profile_by_telegram_id(telegram_id=telegram_id)
    keyboard.add(
        await get_inline_button(
            text=get_text(key=td.BACK, lang=user.selected_language),
            cd=td.BACK
        )
    )
    return keyboard