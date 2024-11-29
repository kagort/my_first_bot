import logging
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
from telegram import Update

import settings

logging.basicConfig(filename='bot.log', level=logging.INFO)


async def greet_user(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Привет!')
    print('Вызван /start')
    print(update)

async def talk_to_me(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    print(text)
    await update.message.reply_text(text)

def main():

    mybot = ApplicationBuilder().token(settings.API_KEY).build()


    start_handler = CommandHandler('start', greet_user)
    mybot.add_handler(start_handler)

    message_handler = MessageHandler(filters.TEXT & ~filters.COMMAND, talk_to_me)
    mybot.add_handler(message_handler)

    logging.info('Бот в деле...')
    mybot.run_polling()

if __name__ == '__main__':
    main()
