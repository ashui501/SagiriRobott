import requests
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ParseMode, Update
from telegram.ext import CallbackContext, CommandHandler

from SagiriRobot import TOKEN, dispatcher

url = "https://google-reverse-image-api.vercel.app/reverse"


def reverse(update: Update, context: CallbackContext):
    if not update.effective_message.reply_to_message:
        update.effective_message.reply_text("ʀᴇᴘʟʏ ᴛᴏ ᴀ ᴘʜᴏᴛᴏ ʙᴜᴅᴅʏ.")

    elif not update.effective_message.reply_to_message.photo:
        update.effective_message.reply_text("ʀᴇᴘʟʏ ᴛᴏ ᴀɴ ɪᴍᴀɢᴇ ʙᴜᴅᴅʏ.")

    elif update.effective_message.reply_to_message.photo:
        msg = update.effective_message.reply_text("➙ 𝙾ɴɪᴄʜᴀɴ ɪ'ᴍ sᴇᴀʀᴄʜɪɴɢ ʏᴏᴜʀ ǫᴜᴇʀʏ...")

        photo_id = update.effective_message.reply_to_message.photo[-1].file_id
        get_path = requests.post(
            f"https://api.telegram.org/bot{TOKEN}/getFile?file_id={photo_id}"
        ).json()
        file_path = get_path["result"]["file_path"]
        data = {
            "imageUrl": f"https://images.google.com/searchbyimage?safe=off&sbisrc=tg&image_url=https://api.telegram.org/file/bot{TOKEN}/{file_path}"
        }

        response = requests.post(url, json=data)
        result = response.json()
        if response.ok:
            msg.edit_text(
                f"[{result['data']['resultText']}]({result['data']['similarUrl']})",
                parse_mode=ParseMode.MARKDOWN,
                reply_markup=InlineKeyboardMarkup(
                    [[InlineKeyboardButton("𝚈ᴀᴍᴀᴅᴀ 𝚂ᴀɢɪʀɪ", url="https://t.me/yamada_sagirix")]]
                ),
            )
        else:
            update.effective_message.reply_text("Some exception occured")

reverse_cmd = CommandHandler(
    ["grs", "reverse", "pp", "p", "P"], reverse, run_async=True
)
dispatcher.add_handler(reverse_cmd)

__mod_name__ = "Rᴇᴠᴇʀsᴇ"
__help__ = """
~ /reverse |pp |grs |p : Does a reverse image search of the media which it was replied to.
"""
