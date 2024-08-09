from aiogram import types, Bot, Dispatcher
from aiogram.types import Message
from single_bot.bot import Bot as ChatBot
import os
from single_bot.data_types import MessengerRequest, Metadata


### Работаю над: CMD, поддержка файлов в telegram
class BaseMessenger:
    def __init__(self, single_bot):
        self.single_bot = single_bot

    def run(self): ...


class TelegramBot:
    def __init__(self, bot: ChatBot, TELEGRAM_TOKEN: str):

        self.telegram_bot = Bot(TELEGRAM_TOKEN)
        self.chat_bot = bot
        self._create_dispatcher()

    async def run(self):

        import logging
        import sys

        logging.basicConfig(level=logging.INFO, stream=sys.stdout)
        await self.dp.start_polling(self.telegram_bot)

    def _create_buttons(self, buttons=None):
        kb = [[]]
        for button in buttons:
            kb[0].append(types.KeyboardButton(text=button))
        return kb

    def _create_dispatcher(self):

        self.dp = Dispatcher()

        @self.dp.message()
        async def message_handler(message: Message):
            async def send_message(text, reply_markup):
                if len(text) > 4095:
                    for x in range(0, len(text), 4095):
                        await message.answer(
                            text[x : x + 4095], reply_markup=reply_markup
                        )
                else:
                    await message.answer(text, reply_markup=reply_markup)

            request = {
                "metadata": {
                    "messenger_id": "telegram",
                    "messenger_user_id": str(message.from_user.id),
                    "messenger_chat_id": str(message.chat.id),
                    "authorized": True,
                    "reply_to_message_id": (
                        str(message.reply_to_message.message_id)
                        if message.reply_to_message
                        else None
                    ),
                },
                "message": {"text": message.text, "files": {}},
            }
            async for answer in self.chat_bot.get_answer(request):
                kb = [[]]
                text = await self._process_streaming(answer["text"])
                if text in ["", None]:
                    continue
                if "buttons" in answer.keys() and answer["buttons"]:
                    kb = self._create_buttons(answer["buttons"])
                    keyboard = types.ReplyKeyboardMarkup(
                        keyboard=kb, resize_keyboard=True
                    )
                    await send_message(text, keyboard)

                else:
                    await send_message(text, types.ReplyKeyboardRemove())

    async def _process_streaming(self, stream):
        answer = ""
        async for token in stream:
            answer += token
        return answer

    # @dp.message(F.contact)
    # async def contacts(message: Message):
    #     save_user_phone(message.from_user.id, message.contact.phone_number)
    #     await message.answer("Спасибо!")
    #     await message.answer(
    #         text="Добро пожаловать!\n\nТеперь бот в твоём распоряжении.\nЗадавай вопрос, связанный с ТК РФ:",
    #         reply_markup=types.ReplyKeyboardRemove(),
    #     )


class CmdBot:
    def __init__(self, bot: ChatBot):
        self.bot = bot

    async def run(self):

        while True:

            user_input = input("> ")
            metadata = Metadata(messenger_name="cmd", messenger_user_id=os.getlogin())
            request = MessengerRequest(metadata=metadata)
            request = {
                "metadata": {
                    "messenger_id": "cmd",
                    "messenger_user_id": os.getlogin(),
                    "messenger_chat_id": "0",
                    "authorized": True,
                    "reply_to_message_id": None,
                },
                "message": {"text": user_input, "files": {}},
            }

            async for message in self.bot.get_answer(request):
                async for token in message["text"]:
                    print(token, end="")
                print("\n", end="")
                buttons = message["buttons"]
            for button in buttons:
                print(f" - {button}")


# class VkBot:
#     def __init__(self, bot: ChatBot):
#         self.bot = bot

#     async def run(self):
