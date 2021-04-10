from pyrogram import Client, filters

app = Client("my_account")

@app.on_message()
def echo(client, message):
	splited = message.text.split()
	if(splited[0] == "+"):
		message.reply_text(float(splited[1]) + float(splited[2]))
		message.delete()
	if(splited[0] == "-"):
		message.reply_text(float(splited[1]) - float(splited[2]))
		message.delete()
	if(splited[0] == "*"):
		message.reply_text(float(splited[1]) * float(splited[2]))
		message.delete()
	if(splited[0] == "/"):
		message.reply_text(float(splited[1]) / float(splited[2]))
		message.delete()

app.run()