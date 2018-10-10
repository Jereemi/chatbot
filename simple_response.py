# -*- coding: utf-8 -*-
from chatterbot import ChatBot
import sys

# Uncomment the following lines to enable verbose logging
import logging
logging.basicConfig(level=logging.INFO)

# Create a new instance of a ChatBot
bot = ChatBot(
    "Terminal",
    storage_adapter="chatterbot.storage.SQLStorageAdapter",
    trainer='chatterbot.trainers.ListTrainer'
)

# Train the chat bot with a few responses
bot.train([
	'Hi',
	'Welcome, how may I help you?!!',
    'How can I help you?',
    'I want to create a chat bot',
    'Have you read the documentation?',
    'No, I have not',
    'This should help get you started: http://chatterbot.rtfd.org/en/latest/quickstart.html'
])

# The following loop will execute each time the user enters input
while True:
	
	message = raw_input('You--');
	if message.strip() != 'Bye':
		bot_input = bot.get_response(message)
		print ("ChatBot--",bot_input)
	
	if message.strip() == 'Bye':
		print ("ChatBot--Have a great day!!")
		break
