from aiogram import Router
from tgbot.filters.for_all.filters import ChatTypeFilter

user_router_g = Router()
user_router_g.message.filter(
    ChatTypeFilter(chat_type=["group", "supergroup"]))