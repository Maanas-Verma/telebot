import os
import requests

def connectbot(token):
    # for mac 
    ipaddr_string = os.popen('ipconfig getifaddr en0').read()
    ipaddr = ipaddr_string[:-1]
    url = 'https://api.telegram.org/bot'
    url = url + token
    url = url + '/setWebhook?url='
    url = url + ipaddr
    print('                    ',url)
    r = requests.get(url)
    print('\n',r.content)
    return r