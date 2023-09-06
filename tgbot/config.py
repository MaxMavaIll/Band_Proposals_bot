
from dataclasses import dataclass
from typing import List
import toml

config_toml = toml.load("config.toml")

@dataclass
class Tg_bot:
    token: str
    admin_ids: List[int]

@dataclass
class Config:
    tg_bot: Tg_bot

def load_config(path: str = None):
    

    return Config(
        tg_bot=Tg_bot(
            token=config_toml["BOT_TOKEN"],
            admin_ids=config_toml["ADMINS"]
        )
    )