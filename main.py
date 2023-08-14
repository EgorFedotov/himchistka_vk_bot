import os
from vkbottle.bot import Bot, Message
from vkbottle import (
        Keyboard,
        KeyboardButtonColor,
        Text,
        OpenLink,
        Location,
        template_gen,
        TemplateElement
    )
from dotenv import load_dotenv

load_dotenv()

bot = Bot(token=os.getenv("GROUP_TOKEN"))


@bot.on.private_message(text="test keyboard")
async def handler(message: Message):
    keyboard = Keyboard()
    keyboard.add(Text("Диван двух местный"), color=KeyboardButtonColor.PRIMARY)
    keyboard.add(Text("Диван трехместный"), color=KeyboardButtonColor.PRIMARY)
    keyboard.row()
    keyboard.add(Text("Угловой диван"), color=KeyboardButtonColor.PRIMARY)
    keyboard.add(Text("Кресло"), color=KeyboardButtonColor.PRIMARY)

    await message.answer("Keyboard", keyboard=keyboard)


@bot.on.private_message(text="test keyboard 2")
async def second_test_keyboard(message: Message):
    keyboard = (
            Keyboard(inline=True)
            .add(Text("Диван двух местный"), color=KeyboardButtonColor.PRIMARY)
            .add(Text("Диван трехместный"), color=KeyboardButtonColor.PRIMARY)
            .row()
            .add(Text("Угловой диван"), color=KeyboardButtonColor.PRIMARY)
            .add(Text("Кресло"), color=KeyboardButtonColor.PRIMARY)
        )

    await message.answer("Keyboard", keyboard=keyboard)


"""Keyboard payload"""


@bot.on.private_message(text="menu")
@bot.on.private_message(payload={"cmd": "menu"})
async def menu_handler(message: Message):
    keyboard = Keyboard(one_time=True).add(Text("Store", {"cmd": "store"}))
    await message.answer("MENU", keyboard=keyboard)


@bot.on.private_message(text="store")
@bot.on.private_message(payload={"cmd": "store"})
async def store_handler(message: Message):
    keyboard = Keyboard(one_time=True).add(Text("Back", {"cmd": "menu"}), color=KeyboardButtonColor.NEGATIVE)
    await message.answer("STORE", keyboard=keyboard)


"""Carousel"""


@bot.on.private_message(text="carousel")
async def carousel_handler(message: Message):
    keyboard = Keyboard().add(Text("Button"), color=KeyboardButtonColor.NEGATIVE)
    carousel = template_gen(
        TemplateElement(
            "Test title",
            "Description",
            "-203980592_457239029",
            keyboard.get_json()
        )
    )
    await message.answer("Carousel", template=carousel)


bot.run_forever()
