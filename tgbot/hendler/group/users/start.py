from aiogram import Bot
from aiogram.dispatcher.fsm.context import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.types import Message, CallbackQuery, InputMediaPhoto


from tgbot.hendler.group.users.router import user_router_g
#from tgbot.state.user.state import 
#from tgbot.keyboard.user.inline import 




@user_router_g.message(Command(commands=["start"]))
async def start( message: Message, state: FSMContext):
    
    
    
    await message.answer(f"Hallo {message.from_user.first_name} in group!! ")

    


