from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes, ConversationHandler

# Токен бота
TOKEN = "8434188817:AAHbq1d2H7kkKI2FsOQXbRY7dGXRKUA1ua4"

AGE, HEIGHT, WEIGHT, GENDER, ACTIVITY = range(5)

user_data = {}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Давай рассчитаем твою дневную норму калорий. Введи свой возраст:")
    return AGE

async def get_age(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_data["age"] = int(update.message.text)
    await update.message.reply_text("Теперь введи свой рост (в см):")
    return HEIGHT

async def get_height(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_data["height"] = int(update.message.text)
    await update.message.reply_text("Теперь введи свой вес (в кг):")
    return WEIGHT

async def get_weight(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_data["weight"] = int(update.message.text)
    keyboard = [["Мужской", "Женский"]]
    await update.message.reply_text("Выбери пол:", reply_markup=ReplyKeyboardMarkup(keyboard, one_time_keyboard=True))
    return GENDER

async def get_gender(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_data["gender"] = update.message.text.lower()
    keyboard = [["1.2", "1.375", "1.55", "1.725", "1.9"]]
    await update.message.reply_text(
        "Выбери уровень активности:\n"
        "1.2 – минимальная\n"
        "1.375 – лёгкие тренировки\n"
        "1.55 – 3-5 раз/нед\n"
        "1.725 – интенсивные\n"
        "1.9 – очень высокая",
        reply_markup=ReplyKeyboardMarkup(keyboard, one_time_keyboard=True))
    return ACTIVITY

async def get_activity(update: Update, context: ContextTypes.DEFAULT_TYPE):
    activity = float(update.message.text)
    age, height, weight, gender = user_data["age"], user_data["height"], user_data["weight"], user_data["gender"]

    if gender.startswith("м"):  # мужчина
        bmr = 10*weight + 6.25*height - 5*age + 5
    else:  # женщина
        bmr = 10*weight + 6.25*height - 5*age - 161

    tdee = bmr * activity

    await update.message.reply_text(
        f"✅ Твоя норма калорий: {tdee:.0f} ккал/день\n\n"
        f"Для похудения: {tdee - 500:.0f} ккал/день\n"
        f"Для набора массы: {tdee + 300:.0f} ккал/день"
    )
    return ConversationHandler.END

def main():
    app = Application.builder().token(TOKEN).build()

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={
            AGE: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_age)],
            HEIGHT: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_height)],
            WEIGHT: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_weight)],
            GENDER: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_gender)],
            ACTIVITY: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_activity)],
        },
        fallbacks=[]
    )

    app.add_handler(conv_handler)
    print("Бот запущен...")
    app.run_polling()

if __name__ == "__main__":

    main()
