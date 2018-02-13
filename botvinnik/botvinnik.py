from telegram.ext import Updater, CommandHandler
from .vegan import get_recipes
from .bot_decorators import bot_command
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
        self.dispatcher.add_handler(CommandHandler('help', _help))

        self.updater.start_polling()
        self.updater.idle()


@bot_command
def start(message):
    '/start -- I introduce myself'
    return ["Hello, my name is Botvinnik, like the fammous Grand Master."]


def wiki(message):
    '/wiki query_string -- returns wiki summary'
    query = ''.join(message.split()[1:])
    try:
        message = wikipedia.summary(query.strip()).split('\n')[0]
    except wikipedia.exceptions.PageError as e:
        message = str(e)
    return [message]


def veg(message):
    '/veg query_string -- returns top four recipes from tudoreceitas.com'
    query = ''.join(message.split()[1:])
    res = get_recipes(query)
    if not res:
        messages = ['Not found :/']
    else:
        messages = [re.sub('[{}]', '', str(i)) for i in res[:4]]
    return messages


def _help(message):
    '/help -- prints all avaiable commands and respective docs'
    message = [i.__doc__ for i in methods]
    message.append(_help.__doc__)
    return ['\n'.join(message)]


methods = [start, wiki, veg]

if __name__ == '__main__':
    Botvinnik(commands=methods)
