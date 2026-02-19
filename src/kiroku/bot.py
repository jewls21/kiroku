from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters
 
TOKEN = '8267890580:AAE4EcVWBtwtolZk8gBBs_AsyIl0OL8WEeM'
 
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('¡Hola! Soy tu bot configurado con python-telegram-bot.')
 
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Envía /start para comenzar o /help para ayuda.')

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    text_received = ' '.join(context.args)
    if text_received:
        await update.message.reply_text(text_received)
    else:
        await update.message.reply_text('Por favor, envía algo después del comando /echo')
        
async def respuesta_general(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Me has enviado: ' + update.message.text)
 
if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
 
    app.add_handler(CommandHandler('start', start))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('echo', echo))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, respuesta_general))
 
    print('Bot iniciado...')
    app.run_polling()