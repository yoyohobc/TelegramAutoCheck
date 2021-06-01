from parameters import *

client = TelegramClient('session_name', api_id, api_hash)
client.start()
#印出發送端帳號資料
clientInfo = client.get_me().__dict__
for key, value in clientInfo.items():
    if(key == 'first_name' or key == 'last_name' or key == 'phone'):
        print(key, ':', value)
#印出接收端群組、帳號資料
print("chat_name :", chat_name)
print("chat_id :", chat_id)

#實例化一個調度器 
scheduler = AsyncIOScheduler()
scheduler.add_job(checkIn, 'cron', minute=checkInTime[3:5],hour=checkInTime[:2],day_of_week=checkWeek) 
scheduler.add_job(checkOut, 'cron', minute=checkOutTime[3:5],hour=checkOutTime[:2],day_of_week=checkWeek) 
#開始運行調度器 
scheduler.start()
asyncio.get_event_loop().run_forever()
    

