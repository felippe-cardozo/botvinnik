from functools import wraps


def bot_command(func):
    @wraps(func)
    def wrapper(bot, update):
        messages = func(update.message.text)
        for message in messages:
            update.message.reply_text(message)
    return wrapper
