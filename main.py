import os
from flask import Flask
from flask import request
from flask import Response
from dotenv import load_dotenv

from sendChat import telSendMessage
from retriveData import getChatDetails
from teleConnector import connectbot

load_dotenv()
TOKEN = os.getenv('API_KEY')
app = Flask(__name__)
# connection_string = connectbot(TOKEN)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        msg = request.get_json()
       
        chat_id,txt = getChatDetails(msg)
        if txt == "/hi":
            telSendMessage(chat_id,"Hello!!", TOKEN)
        else:
            telSendMessage(chat_id,'from webhook',TOKEN)
       
        return Response('ok', status=200)
    else:
        return "<h1>Welcome!</h1>"

if __name__ == '__main__':
    context = ('certificate.crt', 'private.key')#certificate and key files

    # app.run(host='0.0.0.0', port=443, debug=True,ssl_context=context)
    app.run(debug=True, port=5002)
    # connection_string = connectbot(TOKEN)