from aiogram import Dispatcher
from aiogram.dispatcher import filters

from bot.filters.not_registered import NotRegistered
from bot.states.Language import LanguageState
# from bot.data import text_data as td
# from bot.data import callback_data as cd
from . import commands

def setup(dp: Dispatcher):
    dp.register_message_handler(
        commands.new_user,
        filters.CommandStart(),
        NotRegistered(),
        state="*",
    )
    dp.register_message_handler(
        commands.old_user,
        filters.CommandStart(),
        state="*",
    )
    dp.register_message_handler(
        commands.select_language,
        filters.Command("language"),
        state="*",
    )
    dp.register_message_handler(
        commands.set_language,
        state=LanguageState.SELECTING,
    )
    # dp.register_callback_query_handler(commands.start_call, filters.Text(cd.BACK), state="*")
    # dp.register_message_handler(commands.start_command, filters.CommandStart(), state="*")
    # dp.register_message_handler(select_activity.selector, filters.Text(td.ACTIVITY), state="*")
    # #dp.register_message_handler(select_activity.selector, filters.Text(td.SPORT), state="*")
    # dp.register_message_handler(select_activity.selector, filters.Text(td.ACT_PROGRAMM), state="*")
    # win_merch.setup(dp=dp)
    # # feduk.setup(dp=dp)
    # # family_run.setup(dp=dp)
    # # solo_run.setup(dp=dp)
    # # streetball.setup(dp=dp)