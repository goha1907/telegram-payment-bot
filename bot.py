import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Настройка логирования
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

# Функция для обработки команды /start
def start(update, context):
    update.message.reply_text('Привет! Я бот для обработки платежей. Выберите валюту: RUB, USDT или ARS.')

def main():
    # Здесь будет ваш токен, который вы получите от BotFather
    TOKEN = 'YOUR_BOT_TOKEN'
    
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    # Обработчики команд
    dp.add_handler(CommandHandler("start", start))

    # Запуск бота
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()