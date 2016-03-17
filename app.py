from chatterbot import ChatBot
from flask import Flask
from flask import request
import subprocess

app = Flask(__name__)
list_of_database = ['example']

# Check for duplication
def checkDatabase(database_example):
    global list_of_database
    if database_example in list_of_database[-1]:
	return False
    else:
        list_of_database.append(database_example)
	return True

# Create a new instance of a ChatBot
def createDB(database_example):
    database_directory = "%s.db" % database_example
    createDB.bot = ChatBot("Terminal",
        storage_adapter="chatterbot.adapters.storage.JsonDatabaseAdapter",
        logic_adapters=[
            "chatterbot.adapters.logic.EvaluateMathematically",
            "chatterbot.adapters.logic.ClosestMatchAdapter"
        ],
        io_adapters=[
            "chatterbot.adapters.io.TerminalAdapter"
        ],
        database=database_directory)

@app.route('/chatbot/<database_name>', methods=['POST'])
def getReply(database_name):
    try:
	if checkDatabase(database_name):
            print database_name
	    createDB(database_name)
        else:
            print "Accessing existing database..."
        chat_message = request.json['message']
        bot_input = createDB.bot.get_response(chat_message)
        return bot_input
    except (KeyboardInterrupt, EOFError, SystemExit):
      pass

if __name__=='__main__':
    app.debug = True
    app.run('0.0.0.0', 12000)
