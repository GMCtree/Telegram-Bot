# gets the needed API files and adds them to the PYTHONPATH
import sys
sys.path.append("/usr/local/lib/python2.7/dist-packages/telebot")

# import files from the newly added path
import telebot

# this bot's API token
API_TOKEN = '165023625:AAGcL7UPoQQsuYU1wBdt9oF5TCMTnZ6YaQo'

bot = telebot.TeleBot(API_TOKEN)

# Handle '/start' and '/help'
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Hello, I am a bot that provides the dankest of memes");

# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: "dank")
def echo_message(message):
    bot.reply_to(message, message.text)

bot.polling()