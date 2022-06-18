



import telebot
from telebot import types
from decouple import config

def tg_bot():
    prod = Product.objects.all()
    bot = telebot.TeleBot(config("TOKEN"))

    @bot.message_handler(commands=["start"])

    def start(message):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("👋 Поздороваться")
        btn2 = types.KeyboardButton("🍔 Продукты")
        markup.add(btn1, btn2)
        bot.send_message(message.chat.id, text="Привет, {0.first_name}! Я тестовый бот для твоего магазина".format(message.from_user), reply_markup=markup)

    @bot.message_handler(content_types=['text'])
    def func(message):
        if(message.text == "👋 Поздороваться"):
            bot.send_message(message.chat.id, text="Привеет.. Спасибо что следишь за нами!)")
        elif(message.text == "🍔 Продукты"):
            bot.send_message(message.chat.id, text=prod)


    bot.polling(none_stop=True)


