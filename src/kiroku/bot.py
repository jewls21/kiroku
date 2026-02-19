from telegram.ext import ApplicationBuilder, MessageHandler, filters
import os

INCOMING_FOLDER = "incoming"

async def save_photo(update, context):
    if update.message.photo:
        file_id = update.message.photo[-1].file_id
        file = await context.bot.get_file(file_id)
        os.makedirs(INCOMING_FOLDER, exist_ok=True)
        file_path = f"{INCOMING_FOLDER}/{file_id}.jpg"
        await file.download_to_drive(file_path)
        print(f"Foto guardada: {file_path}")

app = ApplicationBuilder().token("T8267890580:AAE4EcVWBtwtolZk8gBBs_AsyIl0OL8WEeM").build()
app.add_handler(MessageHandler(filters.PHOTO, save_photo))

app.run_polling()
