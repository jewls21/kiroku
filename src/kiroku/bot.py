from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters
import os

INCOMING_FOLDER = 'incoming'

TOKEN = '8267890580:AAE4EcVWBtwtolZk8gBBs_AsyIl0OL8WEeM'
 
   
async def save_photo(update, context):
    if update.message.photo:
        file_id = update.message.photo[-1].file_id
        file = await context.bot.get_file(file_id)
        os.makedirs(INCOMING_FOLDER, exist_ok=True)
        file_path = f"{INCOMING_FOLDER}/{file_id}.jpg"
        await file.download_to_drive(file_path)
        print(f"Foto guardada: {file_path}")

 
if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
 
    app.add_handler(MessageHandler(filters.PHOTO, save_photo))

 
    print('Bot iniciado...')
    app.run_polling()