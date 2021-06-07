import csv,asyncio,random,time
from os import path
from telethon import TelegramClient, sync
from datetime import datetime
from apscheduler.schedulers.asyncio import AsyncIOScheduler

#接收端資料
chat_name = '群組1'
chat_id = -66666666
#上下班時間
checkInTime = '08:40'
checkOutTime = '18:01'
#上下班傳的訊息
checkInText = '上班打卡'
checkOutText = '下班打卡'
#設定星期範圍
checkWeek = 'mon-fri'
#發送端APP設定
api_id = 123456
api_hash = '0123456789abcdef0123456789abcdef'

#隨機暫停0-X分鐘
def randomMinutes(maxMins):
    mins = random.randit(0,maxMins)
    secs = mins*60
    time.sleep(secs)

#寫入csv
def writeCsv(checkText, clientInfo):
    csvName = str(clientInfo.get('first_name')) + '_' + str(clientInfo.get('last_name')) + '.csv'
    if(path.isfile(csvName)):
        #讀取CSV
        with open(csvName, newline='',encoding="utf-8") as csvfile:
            #讀取CSV內容並存入writed_csv
            rows = csv.reader(csvfile)
            writed_csv = list(rows)
        #寫入
        with open(csvName, 'w', newline='',encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile)
            #寫入打卡訊息
            writed_csv.append([checkText, datetime.now().ctime(), chat_name])
            # 寫入CSV
            writer.writerows(writed_csv)
    else:
        #寫入
        with open(csvName, 'w', newline='',encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile)
            # 寫入第一列的欄位名稱
            writer.writerow(['打卡訊息','打卡時間','群組/用戶名稱'])
            # 寫入打卡訊息
            writer.writerow([checkText, datetime.now().ctime(), chat_name])