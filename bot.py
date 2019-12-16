import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import scraper as sc
import threading
import time
from datetime import datetime

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

logger = logging.getLogger(__name__)

data = [] #atttendance data

def timer():  #threading to keep the data updated every 90 seconds
    threading.Timer(90, timer).start()
    global data
    start = datetime.now()
    print("Fetching data")
    data = sc.fetch_data() 
    end = datetime.now()
    runtime  = end - start
    print("Data fetched")
    print("Runtime: " + str(runtime))

def start(update, context):
    update.message.reply_text("Kobe Bryant") #to test whether the bot is functioning

def fetch(update, context):
    for student in data:
        update.message.reply_text(student) #send out attendance data

def main():
    updater = Updater(token = '', use_context = True)
    timer()

    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CommandHandler('fetch', fetch))

    updater.start_polling()

    updater.idle()

if __name__ == '__main__':
    main()
    
