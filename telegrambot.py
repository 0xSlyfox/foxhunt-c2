#!/bin/python3

import telebot

class TelegramBot:
	def __init__(self, apiToken):
		self.bot = telebot.Telebot(apiToken)
		
	@bot.message_handler(commands=['start'])
	def startMessage(self, message):
		self.bot.reply_to(message)
		
	def sendMessage(self, chatID, message):
		self.bot.sendMessage(chatID, message)
		

