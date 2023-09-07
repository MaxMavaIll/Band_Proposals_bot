from aiogram import Bot
from aiogram.dispatcher.fsm.context import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.types import Message, CallbackQuery, InputMediaPhoto
from WorkJson import WorkWithJson

import logging, toml
from logging.handlers import RotatingFileHandler
from tgbot.hendler.private.users.router import user_router
#from tgbot.state.user.state import 
#from tgbot.keyboard.user.inline import 

config_toml = toml.load("config.toml")

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
handler2 = RotatingFileHandler(f"logs/{__name__}.log", maxBytes=config_toml['logging']['max_log_size'] * 1024 * 1024, backupCount=config_toml['logging']['backup_count'])
formatter2 = logging.Formatter("%(name)s %(asctime)s %(levelname)s %(message)s")
handler2.setFormatter(formatter2)
log.addHandler(handler2)

json_work = WorkWithJson('user.json')

@user_router.message(Command(commands=["start"]))
async def start( message: Message, state: FSMContext):

    user_dict = json_work.get_json()

    
    if message.from_user.id not in user_dict['users']:
        log.info(f"New user: {message.from_user.id}")
        user_dict['users'].append(message.from_user.id)
        await message.answer(f"Hello, {message.from_user.first_name}! You will now receive voting proposals👌!!!!\n"
                             "If you want to stop tracking Proposals, run the following command /delete")
    
    else:
        await message.answer(f"Hello, {message.from_user.first_name}. You are already registered.\n"
                             "If you want to stop tracking Proposals, run the following command /delete")

    log.info(f"Tracking List Now: {user_dict['users']}")

    json_work.set_json(user_dict)


@user_router.message(Command(commands=["delete"]))
async def delete( message: Message, state: FSMContext):
    user_dict = json_work.get_json()
    
    if message.from_user.id in user_dict['users']:
        log.info(f"Delete user: {message.from_user.id}")
        user_dict['users'].remove(message.from_user.id)
        await message.answer(f"I deleted you. Now you will not receive proposals👌\n"
                             "If you want to start tracking Proposals, run the following command /start")
    else:
        await message.answer(f"You are not on the list\n"
                             "If you want to start tracking Proposals, run the following command /start")
    
    log.info(f"Tracking List Now: {user_dict['users']}")
    
    json_work.set_json(user_dict)