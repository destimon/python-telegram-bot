from config import config
import telebot

bot = telebot.TeleBot(config.token)

@bot.message_handler(content_types=["text"])
def echo_message(msg):
	if msg.text.lower() == "hello":
		bot.send_message(msg.chat.id, "Hi!")
	elif msg.text.lower().find("hello") > 0:
		bot.send_message(msg.chat.id, "You mean 'hello'?\nHello!")
		
	else:
		bot.send_message(msg.chat.id, "I don't understand you, sorry.")

if __name__ == '__main__':
	print("Start polling...")
	print("Token: ", config.token)
	bot.polling(none_stop = True)
