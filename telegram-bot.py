from twx.botapi import TelegramBot
from random import randint
import re, setup_photos

token = str((open("token.txt", "r")).read()) # get API token

bot = TelegramBot(token) # create bot with the given authorization token
bot.update_bot_info().wait() # setup bot

photos = setup_photos.setup() # defined in setup_photos module

def send_input_location(message) :
	_, longitude, latitude = cur_message.text.split() # unpack array into variables for sending
	bot.send_location(cur_message.chat, float(latitude), float(longitude))
	print "Location sent"

def send_help_text(message) :
	bot.send_message(message.chat, "This is a basic telegram bot. This bot will send a photo if \"dank\" is in the message")
	print "Help message sent"

def send_about_text(message) :
	bot.send_message(message.chat, "This bot is written in Python using a wrapper for the Telegram API written by datamachine")
	print "About message sent"

def send_author_info(message) :
	bot.send_message(message.chat, "Created by: GMCtree")
	print "Author info sent"

def send_meme(message) :
	bot.send_photo(message.chat, photos[randint(0, (len(photos) - 1))])
	print "Photo sent"

def command_response(message) : # respond to commands typed by the user
	commands = {"/help" : send_help_text,
				"/about" : send_about_text,
				"/author" : send_author_info }

	if message.text in commands :
		commands[message.text](message)
	else :
		bot.send_message(message.chat, "That is not a command that this bot knows")

print "Bot running..."
updates = bot.get_updates(1, None, None).wait() # get first update

if len(updates) == 0 :
	print "There must be at least 1 message in the current chat"
elif len(updates) == 1 : # account for bot's first update
	current = updates[0]
else :
	current = updates[-1]

dank_pattern = re.compile('(\w\sdank\s\w)|(dank\s\w)|(\w\sdank)|(Dank)')
command_pattern = re.compile('/\w')
location_pattern = re.compile('(location -?\d\d -?\d\d)')

try :
	while True : # use long polling
		prev = current.update_id
		updates = bot.get_updates(1, None, None).wait() # get next update
		current = updates[-1]
		if prev == current.update_id : # avoid redundant checks of the update by checking previous and current update_id
			continue

		cur_message = current.message # hold current Message object

		if dank_pattern.search(cur_message.text) : # check message for keywords and send photo
			send_meme(cur_message)

		if command_pattern.match(cur_message.text) : # check message for commands
			command_response(cur_message)

		if location_pattern.match(cur_message.text) :
			send_input_location(cur_message);

except KeyboardInterrupt :
	print "\nExiting..."

