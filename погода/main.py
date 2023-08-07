import telebot
import requests
from config import TOKEN, API
import json
bot = telebot.TeleBot(TOKEN)  # Token бота
Api_weather=API #Api погоды
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id,'Привет рад тебя видить ! Напиши имя города ')


@bot.message_handler(content_types=["text"])
def pogoda(message):
    gorod=message.text.strip().lower()
    
    p=requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={gorod}&appid={Api_weather}&&units=metric')
    j=json.loads(p.text)
    bot.reply_to(message,f"Сейчас погода{j['main']['temp']}")
bot.polling()