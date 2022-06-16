
import asyncio
import telegram 
from telegram.ext import Updater, CommandHandler, CallbackContext, \
    MessageHandler, Filters
from handler import get_pic

import os
PORT = int(os.environ.get('PORT', 5000))

def start(update: telegram.Update, context: CallbackContext) -> None:
    update.message.reply_text(text='Welcome to Mandybot!\nPlease insert an emotion and get back a nice pic of mandynator!')


def textHandler(update: telegram.Update, context: CallbackContext) -> None:
    user_message = str(update.message.text)
    photo = get_pic(user_message)
    update.message.reply_photo(photo=photo)

async def main():
    TOKEN = "YOUR BOT TOKEN"
            
    updater = Updater(TOKEN, use_context=True)
    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(MessageHandler(Filters.all & ~Filters.command, textHandler, run_async=True))
    updater.start_webhook(listen="0.0.0.0",
                            port=int(PORT),
                            url_path=TOKEN)
    updater.bot.setWebhook('https://frozen-thicket-23375.herokuapp.com/' + TOKEN)
    updater.idle()


if __name__ == '__main__':
    asyncio.run(main())