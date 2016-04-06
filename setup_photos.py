from twx.botapi import InputFile, InputFileInfo
import os

path = 'photos/'
photos = []

def setup() :
	for filename in os.listdir(path) :
		file = open(path + filename, 'rb') # open the image file
		file_info = InputFileInfo(path + filename, file, 'image/png') # instantiate needed file info for Telegram
		photo = InputFile('photo', file_info) # instantiate photo in Telegram's InputFile format
		photos.append(photo)

	return photos
