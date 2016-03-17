from chatterbot import ChatBot
from flask import Flask
from flask import request
import subprocess

app = Flask(__name__)

# Create a new instance of a ChatBot
bot = ChatBot("Terminal",
    storage_adapter="chatterbot.adapters.storage.JsonDatabaseAdapter",
    logic_adapters=[
        "chatterbot.adapters.logic.EvaluateMathematically",
        "chatterbot.adapters.logic.ClosestMatchAdapter"
    ],
    io_adapters=[
        "chatterbot.adapters.io.TerminalAdapter"
    ],
    database="../database.db")

user_input = "Type something to begin..."

@app.route('/chatbot', methods=['POST'])
def getReply():
    try:
	chat_message = request.json['message']
        bot_input = bot.get_response(chat_message)
	return bot_input
    except (KeyboardInterrupt, EOFError, SystemExit):
      pass

if __name__=='__main__':
    app.debug = True
    app.run('0.0.0.0', 12000)
