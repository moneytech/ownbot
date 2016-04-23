#!/usr/bin/python
# -*- coding: utf-8 -*-
"""Provides a simple private telegram bot example.

    Provides an example telegram-bot using the
    authentication decorators from private-telegram-bot.
"""

from telegram.ext import Updater, CommandHandler

from ownbot.auth import requires_usergroup, assign_first_to

TOKEN = open("token.txt").read().strip()


# The first client who sends the '/start' command will be added
# to the admin group.
@assign_first_to("admin")
# If a user wants to execute the '/start' command he has to be
# a member of the 'user' group. Otherwise the decorator will not
# execute the handler function.
@requires_usergroup("user")
def start_handler(bot, update):
    """Handles the command '/start'.

        Sends a Hello World message to the client.
    """
    bot.sendMessage(chat_id=update.message.chat_id, text="Hello World")


def main():
    """
        Simple private telegram bot example.
    """
    import logging
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )

    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher
    dispatcher.addHandler(CommandHandler("start", start_handler))

    updater.start_polling()

if __name__ == "__main__":
    main()
