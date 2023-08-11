import os

from vkbottle.bot import Bot, Message
from dotenv import load_dotenv

load_dotenv()

bot = Bot(token=os.getenv("GROUP_TOKEN"))


@bot.on.message(text="Привет")
async def sey_hellow(message: Message):
    user = bot.api.users.get(message.from_id)
    await message.answer("Привет, {}".format(user[0].first_name))


bot.run_forever()
