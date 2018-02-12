from telegram.ext import Updater, CommandHandler
from vegan import get_recipes
import logging
import re
import os
import wikipedia


class Botvinnik:
    def __init__(self, commands={}, token=os.environ['TELEGRAM']):
        self.__token = token
        self.updater = Updater(token=self.__token)
        self.dispatcher = self.updater.dispatcher
        self.commands = commands
        logging.basicConfig(format='''%(asctime)s - %(name)s
                                    - %(levelname)s - %(message)s''',
                            level=logging.INFO)
        self.logger = logging.getLogger(__name__)

        for m in methods:
            self.dispatcher.add_handler(CommandHandler(m.__name__, m))

        self.updater.start_polling()
        self.updater.idle()


def start(bot, update):
    '/start -- I introduce myself'
    message = "Hello, my name is Botvinnik, like the fammous Grand Master."
    update.message.reply_text(message)


def wiki(bot, update):
    '/wiki query_string -- returns wiki summary'
    query = ''.join(update.message.text.split()[1:])
    try:
        message = wikipedia.summary(query.strip()).split('\n')[0]
    except wikipedia.exceptions.PageError as e:
        message = e
        update.message.reply_text(message)


def veg(bot, update):
    '/veg query_string -- returns top for recipes from tudoreceitas.com'
    query = ''.join(update.message.text.split()[1:])
    res = get_recipes(query)
    if not res:
        messages = ['Not found :/']
    else:
        messages = [re.sub('[{}]', '\n', str(i)) for i in res[:4]]
    [update.message.reply_text(message) for message in messages]


def help(bot, update):
    '/help -- prints all avaiable commands and respective docs'
    message = '\n'.join([i.__doc__ for i in methods])
    update.message.reply_text(message)


methods = [start, wiki, veg, help]

if __name__ == '__main__':
    Botvinnik(commands=methods)
