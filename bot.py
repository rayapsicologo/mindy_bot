from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext

# 🔹 Reemplaza con tu token
TOKEN = "8060435459:AAHzwRTRjf7PweJMlqBRAK_nqGSG1Em5NsA"

async def start(update: Update, context: CallbackContext):
    await update.message.reply_text("¡Hola! Soy Mindy, tu bot de salud mental. Usa /ayuda para ver las opciones.")

async def ayuda(update: Update, context: CallbackContext):
    mensaje = ("Opciones disponibles:\n"
               "/ansiedad - Información sobre ansiedad\n"
               "/estres - Consejos para el estrés\n"
               "/recursos - Enlaces y material de ayuda\n"
               "/contacto - Información de profesionales")
    await update.message.reply_text(mensaje)

def main():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("ayuda", ayuda))

    print("🤖 Bot en marcha... Presiona Ctrl+C para detenerlo.")
    app.run_polling()

if __name__ == '__main__':
    main()
