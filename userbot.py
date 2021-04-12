# In the current version only integer operations supported! 
from pyrogram import Client, filters
import re

app = Client("my_account")

@app.on_message(filters.me)
def echo(client, message):
	result = re.findall(r'\w+[+-/*]\w+', message.text)
	end_message = message.text
	for i in range(len(result)):
		splited = re.split(r'[+-/*]', result[i])
		if result[i].find('+') != -1:
			math_result = int(splited[0]) + int(splited[1])
			end_message = end_message.replace(result[i], str(math_result))
		if result[i].find('-') != -1:
			math_result = int(splited[0]) - int(splited[1])
			end_message = end_message.replace(result[i], str(math_result))
		if result[i].find('*') != -1:
			math_result = int(splited[0]) * int(splited[1])
			end_message = end_message.replace(result[i], str(math_result))
		if result[i].find('/') != -1:
			math_result = float(splited[0]) / float(splited[1])
			end_message = end_message.replace(result[i], "{:g}".format(math_result))
		print("Expression " + result[i] + " was changed to " + "{:g}".format(math_result))

	message.reply_text(end_message)
	message.delete()

app.run()