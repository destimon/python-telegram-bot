from datetime import datetime
import telebot
from profanity import profanity

from src import commands

from config import config

bot = telebot.TeleBot(config.token)

help_message = "/time - Get actual date\n/word [WORD] - repeat word"
time_message = "The actual time is: " + str(datetime.now())

# Commands Handler
@bot.message_handler(commands=['help'])
def send_command(message):
	bot.reply_to(message, help_message)

@bot.message_handler(commands=['time'])
def send_command(message):
	bot.reply_to(message, time_message)

# Message Handler
@bot.message_handler(content_types=["text"])
def echo_message(msg):
	if profanity.contains_profanity(msg.text):
		# Bad Words
		bot.send_message(msg.chat.id, "Ew. Don't use words like this!") 
	elif msg.text.lower() == "hello":
		# Greetings
		bot.send_message(msg.chat.id, "Hi!")
	elif msg.text.lower().find("hello") > 0:
		# Suggestions
		bot.send_message(msg.chat.id, "You mean 'hello'?\nHello!")
	else:
		# Handle unexpected
		bot.send_message(msg.chat.id, "I don't understand you, sorry.")


if __name__ == '__main__':
	print("Start polling...")
	print("Token: ", config.token)
	bot.polling(none_stop = True)
