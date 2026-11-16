import asyncio, os
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart
from aiogram.types import (WebAppInfo, InlineKeyboardMarkup, InlineKeyboardButton,
                           MenuButtonWebApp)

TOKEN = os.environ["BOT_TOKEN"]            # токен от @BotFather
WEBAPP_URL = os.environ["WEBAPP_URL"]      # https-адрес, где лежит webapp/index.html

bot = Bot(TOKEN)
dp = Dispatcher()

@dp.message(CommandStart())
async def start(m):
    kb = InlineKeyboardMarkup(inline_keyboard=[[
        InlineKeyboardButton(text="🎧 Открыть плеер", web_app=WebAppInfo(url=WEBAPP_URL))]])
    await m.answer("Музыка без рекламы. Жми кнопку 👇", reply_markup=kb)

async def main():
    # кнопка-меню рядом с полем ввода
    await bot.set_chat_menu_button(menu_button=MenuButtonWebApp(
        text="Плеер", web_app=WebAppInfo(url=WEBAPP_URL)))
    await dp.start_polling(bot)

asyncio.run(main())
