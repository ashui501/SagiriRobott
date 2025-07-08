import requests
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ParseMode, Update
from telegram.ext import CallbackContext

from SagiriRobot import BOT_NAME, BOT_USERNAME, dispatcher
from SagiriRobot.modules.disable import DisableAbleCommandHandler


def handwrite(update: Update, context: CallbackContext):
    message = update.effective_message
    if message.reply_to_message:
        text = message.reply_to_message.text
    else:
        text = update.effective_message.text.split(None, 1)[1]
    m = message.reply_text("Writing the text on notebook...")
    req = requests.get(f"https://apis.xditya.me/write?text={text}").url
    message.reply_photo(
        photo=req,
        caption=f"""
ꜱᴜᴄᴇꜱꜱꜰᴜʟʟʏ ᴡʀɪᴛᴇ ᴛʜᴇ ᴛᴇxᴛ🍂

✨ **ᴡʀɪᴛᴛᴇɴ ʙʏ :** [{BOT_NAME}](https://t.me/{BOT_USERNAME})
🥀 **ʀᴇqᴜᴇꜱᴛᴇᴇᴅ ʙʏ :** {update.effective_user.first_name}
""",
        parse_mode=ParseMode.MARKDOWN,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("• ᴛᴇʟᴇɢʀᴀᴩʜ •", url=req),
                ],
            ]
        ),
    )
    m.delete()


__help__ = """
 Writes the given text on white page with a pen 🖊

❍ /write <text> *:*Writes the given text.
"""

WRITE_HANDLER = DisableAbleCommandHandler("write", handwrite, run_async=True)
dispatcher.add_handler(WRITE_HANDLER)

__mod_name__ = "WʀɪᴛᴇTᴏᴏʟ"

__command_list__ = ["write"]
__handlers__ = [WRITE_HANDLER]
