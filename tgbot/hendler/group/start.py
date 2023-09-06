
from datetime import datetime
import json
import os
import logging

from aiogram import Bot
from aiogram.dispatcher.fsm.context import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.types import Message, CallbackQuery, InputMediaPhoto


from tgbot.hendler.group.users.router import user_router_g
from tgbot.filters.for_all.filters import AdminFilter 
#from tgbot.state.user.state import 
#from tgbot.keyboard.user.inline import 
from tgbot.config import Config

user_router_g.message.filter(AdminFilter())


@user_router_g.message(Command(commands=["start_a"]))
async def start( message: Message, state: FSMContext):
    
    
    
    await message.answer(f"Hallo admin {message.from_user.first_name} group!! ")

    
@user_router_g.message(Command(commands=["admins"]))
async def start( message: Message, state: FSMContext, config: Config):
    index=1
    for id in config.tg_bot.admin_ids:
        await message.answer(f"I have {index}. {id}!! ")
        index+=1

