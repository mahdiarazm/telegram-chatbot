import logging
import g4f  # اتصال به gpt4free
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext

# توکن ربات تلگرام (از BotFather بگیر)
TELEGRAM_BOT_TOKEN = "8369848551:AAGi3_stV3DDergQy2mIYz59qvCiRHZzBgw"

# تنظیمات لاگ‌گیری
logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)

# ارسال پیام به ChatGPT و دریافت پاسخ
async def chat_with_gpt(prompt):
    try:
        response = g4f.ChatCompletion.create(
            model="gpt-4",  # می‌تونی "gpt-3.5-turbo" هم بذاری
            messages=[{"role": "user", "content": prompt}]
        )
        return response
    except Exception as e:
        return f"❌ خطا: {e}"

# پردازش پیام‌های کاربران و ارسال پاسخ
async def handle_message(update: Update, context: CallbackContext):
    user_text = update.message.text
    chat_response = await chat_with_gpt(user_text)
    await update.message.reply_text(chat_response)

# شروع ربات
async def start(update: Update, context: CallbackContext):
    await update.message.reply_text("سلام! من یک ربات هوش مصنوعی هستم 🤖 هر سوالی داری ازم بپرس.")

# راه‌اندازی و اجرای ربات
def main():
    app = Application.builder().token(TELEGRAM_BOT_TOKEN).build()

    # فرمان‌ها
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("✅ ربات در حال اجرا است...")
    app.run_polling()

# اجرای برنامه
if __name__ == "__main__":
    main()
