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

        for command, method in commands.items():
            self.dispatcher.add_handler(CommandHandler(command, method))

        self.updater.start_polling()


def wiki(bot, update):
    query = ''.join(update.message.text.split()[1:])
    try:
        result = wikipedia.summary(query.strip()).split('\n')[0]
    except wikipedia.exceptions.PageError as e:
        result = e
    bot.send_message(chat_id=update.message.chat_id, text=result)


def veg(bot, update):
    query = ''.join(update.message.text.split()[1:])
    res = get_recipes(query)
    if not res:
        message = 'Not found :/'
    else:
        message = '\n'.join([re.sub('[{}]', '', str(i)) for i in res])
    bot.send_message(chat_id=update.message.chat_id, text=message)


if __name__ == '__main__':
    Botvinnik(commands={'wiki': wiki, 'veg': veg})
