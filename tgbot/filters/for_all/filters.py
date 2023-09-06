from typing import Union

from aiogram.dispatcher.filters import BaseFilter
from aiogram.types import Message

from tgbot.config import Config
from tgbot.config import load_config

class ChatTypeFilter(BaseFilter):  # [1]
    chat_type: Union[str, list]    # [2]

    async def __call__(self, message: Message) -> bool:  # [3]
        if isinstance(self.chat_type, str):
            return message.chat.type == self.chat_type
        else:
            return message.chat.type in self.chat_type


class AdminFilter(BaseFilter):
    is_admin: bool = True

    async def __call__(self, obj: Message,config: Config) -> bool:
        # admin_ids = load_config()
        return (obj.from_user.id in config.tg_bot.admin_ids) == self.is_admin