import requests

def telSendMessage(chat_id, text, token):
    url = f'https://api.telegram.org/bot{token}/sendMessage'
    payload = {
                'chat_id': chat_id,
                'text': text,
                'parse_mode': 'Markdown',
                'disable_web_page_preview': True
                }
   
    r = requests.post(url,json=payload)
    return r