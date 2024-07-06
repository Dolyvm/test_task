import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from config import token
from handlers import start_router, button_router, payment_router, text_router

#Включаем логирование для удобства
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

bot = Bot(token=token)
dp = Dispatcher(storage=MemoryStorage())

#Запускаем бота
async def main():
    dp.include_router(start_router)
    dp.include_router(button_router)
    dp.include_router(payment_router)
    dp.include_router(text_router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
