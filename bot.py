import asyncio
import logging
# from distutils.command.config import config
from datetime import datetime

from aiogram import Bot, Dispatcher, types
from tgbot.hendler.private.users.router import user_router
from tgbot.hendler.group.users.router import user_router_g
from tgbot.config import load_config
from Scheduler.base import setup_scheduler
from Proposer.proposal import Proposer
from apscheduler.triggers.interval import IntervalTrigger

import toml

logger = logging.getLogger(__name__)

config_toml = toml.load("config.toml")


async def main():
    logging.basicConfig(
        level=logging.INFO,
        format=u'%(filename)s:%(lineno)d #%(levelname)-8s [%(asctime)s] - %(name)s - %(message)s',
    )
    logger.info("Starting bot")

    config = load_config(".env")
    bot = Bot(token=config.tg_bot.token, parse_mode="HTML")
    dp = Dispatcher()
    scheduler = setup_scheduler(bot, config)
    dp['scheduler'] = scheduler
    dp['config'] = config
    
    for router in [
        user_router
    ]:
        dp.include_router(router)
    
    scheduler.add_job(
                    Proposer,
                    IntervalTrigger(minutes=config_toml['proposal']['time_sleep']),
                    next_run_time=datetime.now(),
                    replace_existing=True
                )
    scheduler.start()
    
    await dp.start_polling(bot)




if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.error('I was stopped')
