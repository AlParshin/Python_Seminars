from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


async def log(update: Update, context: ContextTypes):
    file = open('db.txt', 'a')
    file.write(
        f'{update.effective_user.first_name},{update.effective_user.id}, {update.message.text}\n')
    file.close()
