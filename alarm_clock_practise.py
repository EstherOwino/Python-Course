#Python Alarm Clock
import time
import datetime

target_time = datetime.datetime(2026, 7, 1, 13, 0,50)
ttf = target_time.strftime('%H:%M:%S')

current_time = datetime.datetime.now()
ctf = current_time.strftime('%H:%M:%S')

for x in range(0,20):
  current_time = datetime.datetime.now()
  ctf = current_time.strftime('%H:%M:%S')
  time.sleep(1)
  print(ctf)
  if ttf == ctf:
    print("Wake Up!")
    break