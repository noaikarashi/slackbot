import schedule
import time
 
def job():
  t = time.strptime(time.ctime())
  print(time.strftime("%Y/%m/%d %H:%M:%S", t))
 
#1/60分=1秒毎にjobを実行
schedule.every(1/60).minutes.do(job)
 
while True:
  schedule.run_pending()
  time.sleep(1)

#schedule.every(1).minutes.do(job) #分単位
#schedule.every().hour.do(job) #時間単位
#schedule.every().day.at("9:20").do(job) #時刻単位
#schedule.every().monday.do(job) #毎月曜日に
#schedule.every().wednesday.at("9:20").do(job) #水曜日の9:29に