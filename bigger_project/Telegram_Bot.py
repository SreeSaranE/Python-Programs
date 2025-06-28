import json
from difflib import get_close_matches
from typing import Final
import credentials as credentials
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = credentials.TELEGRAM_API
BOT_USERNAME: Final[str] = credentials.TELEGRAM_USERNAME

with open('data.json', 'r') as file:
        knowledge = json.load(file)

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello there! Nice to meet you. Let\'s chat!!")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("If you are facing any problem, just notify me, I will try to rectify it...")

async def end_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Bye...Meet you later")

async def handle_response(text: str, update: Update, ):
    processed: str = text.lower()
    best_match: str | None = best_matches(processed, knowledge)

    if best_match is None:
        return "Bot: I don't understand"

    key = best_match.replace(" ", "_")  # Assuming keys use underscores
    answer = knowledge.get(key)

    return f"Bot: {answer}" if answer else "Bot: I don't understand"

def best_matches(user_questions: str, question) -> str | None:
    questions: list[str] = list(question.keys())
    matches: list = get_close_matches(user_questions, questions, n=1, cutoff=0.4)

    return matches[0] if matches else None
  
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text

    print(f"User ({update.message.chat.id}) in {message_type}: {text}")

    if message_type == 'group':
        if BOT_USERNAME in text:
            new_text: str = text.replace(BOT_USERNAME, '').strip()
            response: str = await handle_response(new_text, update)
            await update.message.reply_text(response)
    
    else:
        response: str = await handle_response(text=text, update=update)
        await update.message.reply_text(response)

    print('Bot:', response)

async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error: {context.error}')

def main():
    print("Starting the bot...")
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('end', end_command))

    app.add_handler(MessageHandler(filters.TEXT, handle_message))
    app.add_error_handler(error)

    print("Polling...")

    app.run_polling(poll_interval=1)

if __name__ == '__main__':
    main()
