from config import config
import telebot

bot = telebot.TeleBot(config.token)

@bot.message_handler(content_types=["text"])
def echo_message(msg):
	if msg.text == "Hello":
		bot.send_message(msg.chat.id, "Hi!")
	else:
		bot.send_message(msg.chat.id, "I don't understand you, sorry.")

if __name__ == '__main__':
	print("Start polling...")
	print("Token: ", config.token)
	bot.polling(none_stop = True)
