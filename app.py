from chatterbot import ChatBot
from flask import Flask
from flask import request
import subprocess

app = Flask(__name__)

@app.route('/chatbot/<database_name>', methods=['POST'])
def getReply(database_name):
    try:
    	# Create a new instance of a ChatBot
    	database_directory = "%s.db" % database_name
	bot = ChatBot("Terminal",
    	    storage_adapter="chatterbot.adapters.storage.JsonDatabaseAdapter",
    	    logic_adapters=[
        	"chatterbot.adapters.logic.EvaluateMathematically",
        	"chatterbot.adapters.logic.ClosestMatchAdapter"
    	    ],
    	    io_adapters=[
        	"chatterbot.adapters.io.TerminalAdapter"
    	    ],
    	    database=database_directory)

	user_input = "Type something to begin..."
	chat_message = request.json['message']
        bot_input = bot.get_response(chat_message)
	return bot_input
    except (KeyboardInterrupt, EOFError, SystemExit):
      pass

if __name__=='__main__':
    app.debug = True
    app.run('0.0.0.0', 8080)
