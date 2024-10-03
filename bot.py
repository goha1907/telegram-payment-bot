import os
import logging
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Загрузка переменных окружения из файла .env
load_dotenv()

# Настройка логирования
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Получение токена из переменной окружения
BOT_TOKEN = os.getenv('BOT_TOKEN')

# Функция для обработки команды /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Привет! Я бот для обработки платежей. Выберите валюту: RUB, USDT или ARS.')

def main():
    # Проверка наличия токена
    if not BOT_TOKEN:
        logger.error("BOT_TOKEN не найден. Убедитесь, что он установлен в файле .env")
        return

    # Создание и настройка приложения
    application = ApplicationBuilder().token(BOT_TOKEN).build()

    # Обработчики команд
    application.add_handler(CommandHandler("start", start))

    # Запуск бота
    application.run_polling()

if __name__ == '__main__':
    main()