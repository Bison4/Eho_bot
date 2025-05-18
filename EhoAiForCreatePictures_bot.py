import telebot,keybords
import fsm
TOKEN = '7931226849:AAEyPiV7BdqT6iiwBb7AjQbkcIp9FuHYJis'
stater = fsm.FMS()
bot = telebot.TeleBot(TOKEN)
def main_menu(message):
        if message.text =="Генерация изображения 🌅":
            stater.set_state(message.chat.id, fsm.IMAGE_STATE)
            bot.send_message(message.chat.id,text='Напиши что хочешь сгенерировать😍',reply_markup=keybords.keybord_back)
        elif  message.text =="Генерация текста💬":
            stater.set_state(message.chat.id, fsm.TEXT_STATE)
            bot.send_message(message.chat.id,text='Напиши что нужно написать ✍',reply_markup=keybords.keybord_back)
        elif  message.text =="/start":
            bot.send_message(message.chat.id,text='выбирай 🫣',reply_markup=keybords.keybord_2)
        else :
            bot.send_message(message.chat.id,text='Я тебя не понял😘',reply_markup=keybords.keybord_2)
def image_menu(message):
        if message.text == "Назад↩":
            back_main_menu(message)
        else:
            bot.send_message(message.chat.id,text='Окак , делаю ...🛠')            
def text_menu(message):
        if message.text == "Назад↩":
            back_main_menu(message)
        else:
            bot.send_message(message.chat.id,text='Окак , делаю ...🛠')            
def back_main_menu(message):
    stater.set_state(message.chat.id, fsm.DEFAULT_STATE)
    bot.send_message(message.chat.id,text='Главное меню🤯',reply_markup=keybords.keybord_2)
@bot.message_handler(func = lambda message:True)
def ehno_call(message):
    status = stater.get_state(message.chat.id)
    if status == fsm.DEFAULT_STATE:
        main_menu(message)
    elif status == fsm.IMAGE_STATE:
        image_menu(message)
    elif status == fsm.TEXT_STATE:
        text_menu(message)
    else:
        back_main_menu(message)



            





bot.polling()