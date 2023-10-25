from backend.services import text as ts
from bot.utils.base_keyboard_utils import get_base_keyboard, get_keyboard_button

__all__ = [
    "select_language",
]


async def select_language():
    keyboard = await get_base_keyboard(
        keyboard_options={
            "row_width": 1,
            "resize_keyboard": True
        },
        is_inline=False
    )
    for language in ts.get_all_languages():
        keyboard.add(
            await get_keyboard_button(
                button={"text": language.name,},
                is_inline=False
            )
        )
    return keyboard
