import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import scraper as sc

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

logger = logging.getLogger(__name__)

def start(update, context):
    update.message.reply_text("Kobe Bryant")

def fetch(update, context):
    data = sc.fetch_data()
    for msg in data:
        update.message.reply_text(msg)

def main():
    updater = Updater(token = '***REMOVED***', use_context = True)

    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('fetch', fetch))

    updater.start_polling()

    updater.idle()

if __name__ == '__main__':
    main()
    
