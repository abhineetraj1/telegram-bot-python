import requests
from time import sleep
set_token, line_cmd, response, chat_sec, history = [],[],[],[],[0]

#Creating Bot to set API keys , send and recieve message from group
class Bot:
	def set(api_key):
		try:
			#parameters = {"offset":chat_ID,"limit":"30"}
			req = requests.get("https://api.telegram.org/bot"+api_key+"/getUpdates")
			set_token.append(api_key)
			return "API is set"
		except:
			print("Enter correct api key")
	def sendMessage(text, chat_ID):
		idf = [(len(set_token) == 1), isinstance(text,str),isinstance(chat_ID,str)]
		if (False in idf):
			return "Error\nEnter the right format"
		else:
			parameters = {"chat_id":chat_ID,"text":text}
			req = requests.get("https://api.telegram.org/bot"+set_token[0]+"/sendMessage", params=parameters)
			return "Sent!"
	def getMessage(chat_ID):
		if (isinstance(chat_ID,str)):
			parameters = {"offset":chat_ID}
			a = requests.get("https://api.telegram.org/bot"+set_token[0]+"/getUpdates", data = parameters).json()
			return a["result"][len(a["result"])-1]["message"]["text"]
		else:
			return "Chat ID should be string"

#Creating class to steadily run bot in telegram group
class ServeBot:
	def command(chat_ID, res, text):
		if (False in [isinstance(chat_ID,str), isinstance(res, str), isinstance(text, str), ("/" in res)]):
			return "Error\nEnter correct parameters"
		else:
			chat_sec.append(chat_ID)
			line_cmd.append(res)
			response.append(text)
	def run():
		print("Bot is running!")
		while True:
			m=Bot.getMessage(chat_sec[0])
			if (m in line_cmd):
				if(history[len(history)-1] == m):
					sleep(1)
				else:
					history.append(m)
					Bot.sendMessage(response[line_cmd.index(m)], chat_sec[0])
					sleep(1)
			else:
				sleep(1)
