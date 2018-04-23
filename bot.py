import config
import telebot

bot = telebot.TeleBot(config.token)

@bot.message_handler(content_types=["text"])
def echo_message(msg):
	bot.send_message(msg.chat.id, msg.text)

if __name__ == '__main__':
	print("Start polling...")
	print("Token: ", config.token)
	bot.polling(none_stop = True)
