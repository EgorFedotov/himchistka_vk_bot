from vkbottle import (Keyboard, KeyboardButtonColor,
                      Text, OpenLink,
                      EMPTY_KEYBOARD)
from vkbottle.bot import Message

from bot import bot


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