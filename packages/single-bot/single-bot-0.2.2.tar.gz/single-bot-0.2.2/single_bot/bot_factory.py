from single_bot.messengers import TelegramBot, CmdBot
from single_bot.user_id_storage import UserIdStorage
from single_bot.user_state_storage import UserStateStorage
from single_bot.bot import Bot
from typing import Literal
import shutil
import os


class BotFactory:
    # Responsible for creating and starting messengers
    def __init__(self, first_node, data_path: str = "data/"):
        self.data_path = data_path
        self.first_node = first_node
        

    async def start(
        self, platform: Literal["telegram", "cmd"], token: str | None = None
    ):
        self.bot = Bot(
            UserIdStorage(data_path=self.data_path),
            UserStateStorage(data_path=self.data_path),
            first_node=self.first_node,
        )
        if platform == "telegram":
            if token is None:
                messenger = TelegramBot(self.bot)
            else:
                messenger = TelegramBot(self.bot, token)
            await messenger.run()
        if platform == "cmd":
            messenger = CmdBot(self.bot)
            await messenger.run()

    def remove_data():
        if os.path.exists(self.data_path[:-1]):
            shutil.rmtree(self.data_path[:-1])