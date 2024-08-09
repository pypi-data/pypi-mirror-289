from single_bot.messengers import TelegramBot, CmdBot
from single_bot.user_id_storage import UserIdStorage
from single_bot.user_state_storage import UserStateStorage
from single_bot.bot import Bot
from typing import Literal
import shutil
import os


class BotFactory:
    # Responsible for creating and starting messengers
    def __init__(self, first_node, data_path: str = "data/", remove_data: bool = False):
        if remove_data:
            if os.path.exists(data_path[:-1]):
                shutil.rmtree(data_path[:-1])
        self.bot = Bot(
            UserIdStorage(data_path=data_path),
            UserStateStorage(data_path=data_path),
            first_node=first_node,
        )

    async def start(
        self, platform: Literal["telegram", "cmd"], token: str | None = None
    ):
        if platform == "telegram":
            if token is None:
                messenger = TelegramBot(self.bot)
            else:
                messenger = TelegramBot(self.bot, token)
            await messenger.run()
        if platform == "cmd":
            messenger = CmdBot(self.bot)
            await messenger.run()
