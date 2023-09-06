from typing import Union

from aiogram.dispatcher.filters import BaseFilter
from aiogram.types import Message

"""
Example

class ChatTypeFilter(BaseFilter):  # [1]
    chat_type: Union[str, list]    # [2]

    async def __call__(self, message: Message) -> bool:  # [3]
        if isinstance(self.chat_type, str):
            return message.chat.type == self.chat_type
        else:
            return message.chat.type in self.chat_type

"""