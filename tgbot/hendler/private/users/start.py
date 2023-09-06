from aiogram import Bot
from aiogram.dispatcher.fsm.context import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.types import Message, CallbackQuery, InputMediaPhoto
from WorkJson import WorkWithJson

from tgbot.hendler.private.users.router import user_router
#from tgbot.state.user.state import 
#from tgbot.keyboard.user.inline import 


json_work = WorkWithJson('user.json')

@user_router.message(Command(commands=["start"]))
async def start( message: Message, state: FSMContext):
    user_dict = json_work.get_json()

    await message.answer(f"Hello, user {message.from_user.first_name}. You will now receive voting proposals.!! ")

    
    if message.from_user.id not in user_dict['users']:
        user_dict['users'].append(message.from_user.id)
    
    json_work.set_json(user_dict)


