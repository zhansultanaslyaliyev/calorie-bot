# calorie-bot
Simple Telegram bot that calculates daily calorie needs based on user input (age, height, weight, gender, activity level).

# Telegram Calorie Bot 🥗

A simple Telegram bot built with Python (aiogram v3) that calculates daily calorie needs using the Mifflin-St Jeor formula.  
The bot asks for age, height, weight, gender, and activity level, then provides the daily calorie intake to maintain weight.

## 🚀 Features
- Collects user data: age, height, weight, gender, activity level
- Calculates daily calorie needs (BMR × activity factor)
- Uses FSM (Finite State Machine) in aiogram v3
- Easy to extend: add macros (protein, fats, carbs), nutrition tips, user history, etc.

## 📸 Example Usage
1. Start the bot with `/start`
2. Answer the bot’s questions (age, height, weight, gender, activity level)
3. Receive your daily calorie recommendation ✅

Example output:
✅ Твоя норма калорий: 2154 ккал/день

Для похудения: 1654 ккал/день
Для набора массы: 2454 ккал/день
