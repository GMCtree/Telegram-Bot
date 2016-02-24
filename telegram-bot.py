from twx.botapi import TelegramBot, InputFile, InputFileInfo

bot = TelegramBot('165023625:AAGcL7UPoQQsuYU1wBdt9oF5TCMTnZ6YaQo') # create bot with the given authorization token
bot.update_bot_info().wait() # setup bot

file = open('Pepe_rare.png', 'rb') # open the image file
file_info = InputFileInfo('Pepe_rare.png', file, 'image/png') # instantiate needed file info for Telegram
photo = InputFile('photo', file_info) # instantiate photo in Telegram's InputFile format

updates = bot.get_updates(1, None, None).wait() # get first update
if len(updates) == 1 : # account for bot's first update
	current = updates[0]
else :
	current = updates[len(updates) - 1]

while True :
	prev = current.update_id
	updates = bot.get_updates(1, None, None).wait() # get next update
	current = updates[len(updates) - 1]
	if prev == current.update_id : # avoid redundant checks of the update
		continue
	cur_message = current.message # hold current Message object
	if current.message.text == "Dank" :
		bot.send_photo(cur_message.chat, photo)
		

