import telebot

bot = telebot.TeleBot("5702823965:AAFgU4kOK16CBIpXfr-D4Kt8PMKvKlA1bzA")
@bot.message_handler(commands=["help","start"])


def send(message):
	bot.reply_to(message, "Hola")


bot.polling()