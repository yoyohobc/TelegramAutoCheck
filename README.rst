Telegram自動打卡上下班
========
介紹
-------------
可用自己的帳號在設定好的時間自動發訊息，以達到自動打卡上下班

發訊息的部分利用 Telethon 套件操作 Telegram的API 來完成

設定時間部分則使用APScheduler定時任務框架來完成

Telethon : https://github.com/LonamiWebs/Telethon

APScheduler : https://github.com/agronholm/apscheduler


安裝
----------
pip install telethon

pip install apscheduler

使用方式
-----------------
修改parameters.py

app_id & api_hash 需至 https://my.telegram.org 用自己帳號申請,並開啟API Development Tools

chat_name改成自己想發送的群組/用戶名稱

chat_id 則在改完chat_name後執行checkChatId.py就可獲得

第一次執行checkChatId.py時會需要輸入自己的手機號碼(含+之國際號)

上下班時間和資訊可參考下面check開頭的變數，依個人需求填寫

checkWeek部分可設定星期幾觸發'mon-fri'為周一至周五

修改完後執行telegramAutoCheck.py就會開始運作

執行期間會產生CSV檔紀錄打卡的訊息和時間

.. code-block:: python

    import csv,asyncio
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
