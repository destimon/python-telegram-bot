import telebot
from profanity import profanity
from config import config
bot = telebot.TeleBot(config.token)

@bot.message_handler(content_types=["text"])
def echo_message(msg):
	if profanity.contains_profanity(msg.text):
		bot.send_message(msg.chat.id, "Ew. Don't use words like this!") 
	elif msg.text.lower() == "hello":
		bot.send_message(msg.chat.id, "Hi!")
	elif msg.text.lower().find("hello") > 0:
		bot.send_message(msg.chat.id, "You mean 'hello'?\nHello!")
	else:
		bot.send_message(msg.chat.id, "I don't understand you, sorry.")

if __name__ == '__main__':
	print("Start polling...")
	print("Token: ", config.token)
	bot.polling(none_stop = True)
