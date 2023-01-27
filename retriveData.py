def getChatDetails(message):
    print("message-->",message)
    if('message' in message):
        # print('message is there', message['message'])
        chat_id = message['message']['chat']['id']
        # recive messages
        if('text' in message['message']):
            # print('message text is there', message['message']['text'])
            txt = message['message']['text']
            print("chat_id-->", chat_id)
            print("txt-->", txt)
            return chat_id,txt, 'message'
        else:
            # print('message text is not there')
            return chat_id, 'left', 'left'
    else:
        # some one is removed
        chat_id = message['my_chat_member']['chat']['id']
        group_name = message['my_chat_member']['chat']['title']
        print("chat_id-->", chat_id)
        return chat_id, group_name, 'bot_removed'