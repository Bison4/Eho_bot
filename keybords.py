import telebot

button_pictures = telebot.types.KeyboardButton(text= 'Генерация изображения 🌅')
button_text = telebot.types.KeyboardButton(text= 'Генерация текста💬')
button_back = telebot.types.KeyboardButton(text= 'Назад↩')


keybord_2 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
keybord_back = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
keybord_2.add(button_pictures,button_text)
keybord_back.add(button_back)
