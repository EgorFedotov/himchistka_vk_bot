import os
import asyncio

from vkbottle import API
from dotenv import load_dotenv

load_dotenv()


async def main():
    api = API(token=os.getenv("GROUP_TOKEN"))
    await api.wall.post(message="Здравствуйте!")