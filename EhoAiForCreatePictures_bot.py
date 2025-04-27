import telebot,keybords
TOKEN = '7931226849:AAHRaUKMoSaD2YjwovnvBlqVZP0tcgCuCRc'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(func = lambda message:True)
def ehno_call(message):
    msg_text = message.text
    if msg_text =="Удприть ребенка негра🥰" or msg_text =="Ударить негра😂":
        bot.send_message(message.chat.id,text='1',reply_markup=keybords.keybord_back)
    elif msg_text =="Назад":
        bot.send_message(message.chat.id,text='1',reply_markup=keybords.keybord_start)
    else :
        bot.send_message(message.chat.id,text='1',reply_markup=keybords.keybord_2)



bot.polling()