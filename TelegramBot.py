from telegram.ext.updater import Updater  # type: ignore
from telegram.update import Update  # type: ignore
from telegram.ext.callbackcontext import CallbackContext  # type: ignore
from telegram.ext.commandhandler import CommandHandler  # type: ignore
from telegram.ext.messagehandler import MessageHandler  # type: ignore
from telegram.ext.filters import Filters # type: ignore

updater = Updater("your_own_API_Token got from BotFather",
                  use_context=True)


def start(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Enter the text you want to show to the user whenever they start the bot")
    
def help(update: Update, context: CallbackContext):
    update.message.reply_text("Your Message")
    
def gmail_url(update: Update, context: CallbackContext):
    update.message.reply_text("gmail link here")


def youtube_url(update: Update, context: CallbackContext):
    update.message.reply_text("youtube link")


def linkedIn_url(update: Update, context: CallbackContext):
    update.message.reply_text("Your linkedin profile url")


def geeks_url(update: Update, context: CallbackContext):
    update.message.reply_text("GeeksforGeeks url here")


def unknown_text(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Sorry I can't recognize you , you said '%s'" % update.message.text)


def unknown(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Sorry '%s' is not a valid command" % update.message.text)

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('youtube', youtube_url))
updater.dispatcher.add_handler(CommandHandler('help', help))
updater.dispatcher.add_handler(CommandHandler('linkedin', linkedIn_url))
updater.dispatcher.add_handler(CommandHandler('gmail', gmail_url))
updater.dispatcher.add_handler(CommandHandler('geeks', geeks_url))
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown))
updater.dispatcher.add_handler(MessageHandler(
    # Filters out unknown commands
    Filters.command, unknown))

# Filters out unknown messages.
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown_text))

updater.start_polling()