from telethon import TelegramClient
from parameters import api_id, api_hash, chat_name

client = TelegramClient('session_name', api_id, api_hash)
client.start()

chat_id = None
for dialog in client.iter_dialogs():
    if dialog.name == chat_name:
        chat_id = dialog.id
        break
if(chat_id != None):
    print("chat_name :", chat_name)
    print("chat_id :", chat_id)
else:
    print("找不到chat_id")

    

