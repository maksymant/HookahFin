from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

from settings import API_TOKEN, CONNECTION_ID
from handlers import start, echo, unknown, custom
from pymongo import MongoClient


def main():
    updater = Updater(token=API_TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    # cluster = MongoClient(CONNECTION_ID)
    # db = cluster['Sommelier']
    # collection = db['Users']

    dispatcher.add_handler(CommandHandler('custom', custom))
    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(MessageHandler(Filters.text & (~Filters.command), echo))
    dispatcher.add_handler(MessageHandler(Filters.command, unknown))

    updater.start_polling(clean=True)
    updater.idle()


if __name__ == '__main__':
    main()
