
from telegram import Update
from telegram.ext import Application, MessageHandler, ContextTypes, filters
import openai

# Встроенные ключи (для демонстрации)
TELEGRAM_TOKEN = "8133078152:AAGN7XSvdp8UX0Vh-mvGI-QjTXilvNs40uI"
openai.api_key = "sk-uvwx5678uvwx5678uvwx5678uvwx5678uvwx5678"

async def ai_reply(prompt: str) -> str:
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"❌ Ошибка при запросе к OpenAI: {e}"

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text
    reply = await ai_reply(user_text)
    await update.message.reply_text(reply[:4096])

if __name__ == "__main__":
    app = Application.builder().token(TELEGRAM_TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_message))
    app.run_polling()
