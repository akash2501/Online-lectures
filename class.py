import schedule
import os
import time
from datetime import datetime
def job():
    os.system("python C:\\Users\\Akash\\Desktop\\class\\sd.py")
schedule.every().day.at("9:00:00").do(job)
schedule.every().day.at("10:00:00").do(job)
schedule.every().day.at("11:00:00").do(job)
schedule.every().day.at("12:00:00").do(job)
schedule.every().day.at("13:00:00").do(job)
schedule.every().day.at("14:00:00").do(job)
schedule.every().day.at("15:00:00").do(job)
schedule.every().day.at("16:00:00").do(job)
schedule.every().day.at("17:00:00").do(job)
while True:
    schedule.run_pending()
    time.sleep(1)