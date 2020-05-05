import telebot
import requests
import randdom
from telebot import types
import random
import os
import subprocess

from bs4 import BeautifulSoup as BS
from bs4 import BeautifulSoup

bot = telebot.TeleBot('1169789938:AAEhYYHENsallSaGJzGsF5Vb_Z2R7SvSqv')


	


@bot.message_handler(commands=['start'])
def welcome(message):
		markup = types.ReplyKeyboardMarkup(resize_keyboard=False)
		item1 = types.KeyboardButton('🎲Рандомная фотография')
		markup.add(item1)
		gg = gg = 'Привет, <b>' + message.from_user.first_name.title() + '</b>!\nЯ очереднярский бот в таком прекрасном мире как Telegram, но я смогу тебя удивить\n\nПроверим?)😃\n\nСоздатель - Якублевич Ренат\nGithub - https://github.com/RenatYakublevich'.format(message.from_user, bot.get_me()) 
		bot.send_message(message.chat.id, gg ,parse_mode='html',reply_markup=markup)

@bot.message_handler(content_types=['text'])
def random_pic(message):
	if message.chat.type == 'private':
		if message.text == '🎲Рандомная фотография':
			randdom.main(1,'images')
			gg = randdom.main(1,'images')
			gg.replace('http://i.imgur.com/','')
			bot.send_photo(message.chat.id,gg,'Вот ваша картинка☝️')


bot.polling(none_stop=True)
