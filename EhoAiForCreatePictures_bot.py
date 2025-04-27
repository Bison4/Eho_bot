import telebot
TOKEN = '7931226849:AAHRaUKMoSaD2YjwovnvBlqVZP0tcgCuCRc'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(func = lambda message:True)
def ehno_call(message):
    bot.send_message(message.chat.id,message.text)


bot.polling()