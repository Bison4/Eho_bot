import telebot,keybords
import fsm
import ai
import loguru
import yaml
import sys

# https://api.telegram.org/bot7931226849:AAEyPiV7BdqT6iiwBb7AjQbkcIp9FuHYJis/deleteWebhook
logger = loguru.logger

try:
     with open("./config_2.yaml","r") as file:
        cfg = yaml.safe_load(file)
        logger.info('Успешно загружен конфиг')
except Exception as e:
     logger.warning('Error config ({})',str(e))
     input()
     sys.exit(1)
TOKEN = cfg['telegram_token']
stater = fsm.FMS()
ai_servise = ai.AI(cfg)


bot = telebot.TeleBot(TOKEN,threaded=False)
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
            try:
                msg = bot.send_message(message.chat.id,text='Окак , делаю ...🛠')      
                image_url = ai_servise.generate_image(message.text)
                bot.delete_message(chat_id=message.chat.id,message_id=msg.id)
                bot.send_photo(chat_id=message.chat.id,caption="Держи фото🦾",photo=image_url)
            except Exception as e:
                bot.send_message(message.chat.id,text=f'Окак ,EEErOo0r({str(e)})')      
def text_menu(message):
        if message.text == "Назад↩":
            ai_servise.clear_dialog(message.chat.id)
            back_main_menu(message)
        else:
            msg = bot.send_message(message.chat.id,text='Окак , делаю ...🛠')   
            txt = ai_servise.genrate_text(message.text,message.chat.id)     
            msg = bot.edit_message_text(text = txt,chat_id= message.chat.id,message_id=msg.id)    
def back_main_menu(message):
    stater.set_state(message.chat.id, fsm.DEFAULT_STATE)
    bot.send_message(message.chat.id,text='Главное меню🤯',reply_markup=keybords.keybord_2)
@bot.message_handler(func = lambda message:True)
def ehno_call(message):
    status = stater.get_state(message.chat.id)
    logger.info(
         "пользователь[{}:{}]отправил сообщение '{}' в состоянии{}",
         message.chat.id,
         message.from_user.first_name,
         message.text,
         status
    )

    if status == fsm.DEFAULT_STATE:
        main_menu(message)
    elif status == fsm.IMAGE_STATE:
        image_menu(message)
    elif status == fsm.TEXT_STATE:
        text_menu(message)
    else:
        back_main_menu(message)



            





bot.polling()