from typing import Final
import udemy.Bug.credentials as credentials
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# These are hidden due t confidential reasons... 
TOKEN = credentials.TELEGRAM_API
BOT_USERNAME: Final[str] = credentials.TELEGRAM_USERNAME

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello there! Nice to meet you. Let\'s chat!!")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("If you are facing any problem, just notify me, I will try to rectify it...")

async def end_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Bye...Meet you later")

async def handle_response(text: str, update: Update):
    processed: str = text.lower()

    if 'hello' in processed:
        await update.message.reply_text("Hello there! Nice to meet you. Let\'s chat!!")
    
    if 'name' in processed:
        return 'I am AlienX'
    
    if 'bye' in processed:
        return 'meet you later'
    
    return 'Can\'t under stand'

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text

    print(f"User ({update.message.chat.id}) in {message_type}: {text}")

    if message_type == 'group':
        if BOT_USERNAME in text:
            new_text: str = text.replace(BOT_USERNAME, '').strip()
            response: str = handle_response(new_text)
        else:
            return
    
    else:
        response: str = handle_response(text=text)

    print('Bot:', response)

async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error: {context.error}')

def main():
    print("Starting the bot...")
    app = Application.builder().token(token=TOKEN).build()

    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('end', end_command))

    app.add_handler(MessageHandler(filters.TEXT, handle_message))
    app.add_error_handler(error)

    print("Polling...")

    app.run_polling(poll_interval=5)

if __name__ == '__main__':
    main()
