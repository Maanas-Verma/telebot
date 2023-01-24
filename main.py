import os
from flask import Flask
from flask import request
from flask import Response
from dotenv import load_dotenv

from sendChat import telSendMessage
from retriveData import getChatDetails
from teleConnector import connectbot
from db_manager.pandas_read import get_validated_tokens
from replies.bydate import get_todays_tokens, get_tomorrows_tokens, get_later_tokens, get_3days_tokens
from replies.addtax import add_tax
from replies.bytype import get_tokens_by_category

load_dotenv()
TOKEN = os.getenv('API_KEY')
app = Flask(__name__)
# connection_string = connectbot(TOKEN)


greedings = """Hello!!, 
I am a bot, I can help you to get the latest information about the Pinksale Launchpad.
You can use the following commands to get the information:

1. /hi - to get the greetings
2. /info - to get the latest information about the Pinksale Launchpad
3. /help - to get the list of commands
"""

info = """Pinksale Launchpad is a platform for launching new projects.
The platform is based on the Binance Smart Chain and is designed to provide a safe and secure environment for launching new projects.
"""
help = """You can use the following commands to get the information:
1. /sofu - to get tokens with SOFU
2. /doxx - to get tokens with DOXX
3. /kyc - to get tokens with KYC
4. /audit - to get tokens with Audit
5. /today - to get tokens launching today
6. /tomorrow - to get tokens launching tomorrow
7. /later - to get tokens launching later
8. /3days - to get tokens launching in 3 days
"""

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        msg = request.get_json()
       
        chat_id,txt = getChatDetails(msg)
        if txt == "/hi":
            telSendMessage(chat_id, greedings, TOKEN)
        elif txt == "/info":
            telSendMessage(chat_id, info, TOKEN)
        elif txt == "/help":
            telSendMessage(chat_id, help, TOKEN)
        elif txt == "/sofu":
            sofu = get_tokens_by_category('Safu')
            telSendMessage(chat_id, sofu, TOKEN)
        elif txt == "/doxx":
            sofu = get_tokens_by_category('Doxx')
            telSendMessage(chat_id, sofu, TOKEN)
        elif txt == "/kyc":
            sofu = get_tokens_by_category('KYC')
            telSendMessage(chat_id, sofu, TOKEN)
        elif txt == "/audit":
            sofu = get_tokens_by_category('Audit')
            telSendMessage(chat_id, sofu, TOKEN)
        elif txt == "/today":
            today = get_todays_tokens(5)
            telSendMessage(chat_id, today, TOKEN)
        elif txt == "/tomorrow":
            tomorrow = get_tomorrows_tokens(5)
            telSendMessage(chat_id, tomorrow, TOKEN)
        elif txt == "/later":
            later = get_later_tokens()
            telSendMessage(chat_id, later, TOKEN)
        elif txt == "/3days":
            three_days = get_3days_tokens()
            telSendMessage(chat_id, three_days, TOKEN)
        elif txt.split(' ')[0] == "/addtax":
            add_txt_status = add_tax(txt)
            telSendMessage(chat_id, add_txt_status, TOKEN)
        else:
            telSendMessage(chat_id,'type /hi',TOKEN)
       
        return Response('ok', status=200)
    else:
        return "<h1>Welcome!</h1>"

if __name__ == '__main__':
    # creating a thread for running file scrape.py
    from scrape import ScrapeThread
    ScrapeThread().start()



    # context = ('certificate.crt', 'private.key')#certificate and key files

    # app.run(host='0.0.0.0', port=443, debug=True,ssl_context=context)
    from waitress import serve
    serve(app, host="0.0.0.0", port=5002)
    # app.run(debug=True, port=5002)
    # connection_string = connectbot(TOKEN)