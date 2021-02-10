import time
from translation import Translation
from pyrogram import Client, filters as Filters

# ********************************************** STARTING MESSAGE *****************************************************#
@Client.on_message(Filters.private & Filters.command(["start"]))
async def start(bot, update):
    await bot.delete_messages(chat_id=update.chat.id, message_ids=update.message_id)
    await bot.send_message(chat_id=update.chat.id, text=Translation.START_MSG.format(update.from_user.first_name))


# ********************************************** HELP MESSAGE *********************************************************#
@Client.on_message(Filters.private & Filters.command(["help"]))
async def help_me(bot, update):
    await bot.delete_messages(chat_id=update.chat.id, message_ids=update.message_id)
    await bot.delete_messages(chat_id=update.chat.id, message_ids=update.message_id)
    a = await bot.send_message(chat_id=update.chat.id, text=Translation.HELP, disable_web_page_preview=True)
    time.sleep(60)
    await a.delete()