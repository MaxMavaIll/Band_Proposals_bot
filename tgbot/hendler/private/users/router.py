from aiogram import Router
from tgbot.filters.for_all.filters import ChatTypeFilter

user_router = Router()
user_router.message.filter(
    ChatTypeFilter(chat_type='private')
)