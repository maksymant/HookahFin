

def start(update, context):
    update.message.reply_text("I'm a bot, please talk to me!")


def custom(update, context):
    update.message.reply_text("You just executed custom command")


def echo(update, context):
    # context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)
    update.message.reply_text(update.message.text)


def unknown(update, context):
    update.message.reply_text("Sorry, I didn't understand that command.")