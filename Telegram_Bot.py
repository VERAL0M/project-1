import sqlite3
import telebot
from telebot import types
from datetime import date
import os

save_path = None
current_date = None

bot = telebot.TeleBot('6627094084:AAGp0P2xi9K_rRxfvh4qfxLuPTL23BZtpL8')

@bot.message_handler(commands=['start'])
def main(message):

    """Создание базы данных"""
    conn = sqlite3.connect('C:\\Users\\mvs05\\data_gp.db')
    cur = conn.cursor()

    cur.execute('CREATE TABLE IF NOT EXISTS photos (id int  PRIMARY KEY, photo BLOB)')
    # cur.execute('CREATE TABLE IF NOT EXISTS photos (photo BLOB)')
    conn.commit()
    cur.close()
    conn.close()

    bot.send_message(message.chat.id, 'Работа началась. Загрузите изображение')

# @bot.message_handler(content_types=['text'])
# def func(message):
    # if message.text =='Загрузить изображение расписания(с 5А по 6В)':
@bot.message_handler(content_types=['photo'])
def get_photo(message):

    """Загрузка изображения"""
    conn = sqlite3.connect('C:\\Users\\mvs05\\data_gp.db')
    cur = conn.cursor()

    file_id = message.photo[-1].file_id
    file_info = bot.get_file(file_id)
    file_name = file_info.file_path.split('/')[-1]
    unique_name = f"{file_id}_{file_name}"
    
    # Загрузка и сохранение картинки
    
    file = bot.download_file(file_info.file_path)
    with open(unique_name , 'wb') as new_file:
        new_file.write(file)
        

    with open(unique_name, 'rb') as photo:
        h= photo.read()
    cur.execute('DELETE FROM photos')
    cur.execute('INSERT INTO photos(photo) VALUES(?)', [h])


    os.remove(f'{unique_name}')
 

            
    conn.commit()
    cur.close()
    conn.close()

    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('Изменить фото' , callback_data='change_photo')

    markup.row(btn1)

    bot.reply_to(message, 'Изображение загружено на сервер ', reply_markup = markup )
 

@bot.callback_query_handler(func=lambda callback:True)
def delete_photo(callback):
    if callback.data == 'change_photo':
        bot.delete_message(callback.message.chat.id, callback.message.message_id -1)
        bot.send_message(callback.message.chat.id, 'Фото удалено')


bot.polling(none_stop=True)

