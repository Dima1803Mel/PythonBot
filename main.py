from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
import asyncio

token = "6687511439:AAFGUA5P6CCpDkkyH9-aHJpEBHgyWBMG40o"
bot = Bot(token=token)
dp = Dispatcher()

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Hello!!!")

async def main() -> None:
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
