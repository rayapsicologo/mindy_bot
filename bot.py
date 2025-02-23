import os
import asyncio
import nest_asyncio
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext

# Aplicar patch para evitar errores de event loop en Replit
nest_asyncio.apply()

# Cargar variables de entorno desde .env
load_dotenv()
TOKEN = os.getenv("TOKEN")

async def start(update: Update, context: CallbackContext):
    await update.message.reply_text("¡Hola! Soy Mindy, tu bot de salud mental. Usa /ayuda para ver las opciones.")

async def ayuda(update: Update, context: CallbackContext):
    mensaje = ("Opciones disponibles:\n"
               "/ansiedad - Información sobre ansiedad\n"
               "/estres - Consejos para el estrés\n"
               "/recursos - Enlaces y material de ayuda\n"
               "/contacto - Información de profesionales")
    await update.message.reply_text(mensaje)

async def main():
    if not TOKEN:
        print("⚠️ ERROR: No se encontró el TOKEN en el archivo .env")
        return

    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("ayuda", ayuda))

    print("🤖 Bot en marcha... Presiona Ctrl+C para detenerlo.")
    await app.run_polling()

# ✅ Manejo correcto del loop en Replit
if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    if loop.is_running():
        print("⚠️ El loop de eventos ya está en ejecución, usando create_task()")
        loop.create_task(main())  # Ejecuta el bot sin cerrar el loop
    else:
        print("✅ Ejecutando asy
