import os

from vkbottle import (Keyboard, KeyboardButtonColor,
                      Text, OpenLink,
                      EMPTY_KEYBOARD)
from vkbottle import API
from vkbottle.bot import Bot, Message
from dotenv import load_dotenv

load_dotenv()

api = API(token=os.getenv("GROUP_TOKEN"))
bot = Bot(api=api)


@bot.on.message(text="Привет")
async def sey_hellow(message: Message):
    user = bot.api.users.get(message.from_id)
    await message.answer("Привет, {}".format(user[0].first_name))


@bot.on.private_message(text="menu")
async def handler_menu(message: Message):
    keyboard = Keyboard(one_time=True)
    keyboard.add(Text("Диван двухместный"), color=KeyboardButtonColor.PRIMARY)
    keyboard.add(Text("Диван трехместный"), color=KeyboardButtonColor.PRIMARY)
    keyboard.add(Text("Диван угловой"), color=KeyboardButtonColor.PRIMARY)
    keyboard.row()
    keyboard.add(Text("Кресло"), color=KeyboardButtonColor.PRIMARY)
    keyboard.add(Text("Стул"), color=KeyboardButtonColor.PRIMARY)
    await message.answer("Клавиатура", keyboard=keyboard)

bot.run_forever()
