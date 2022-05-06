# must install module from pip
# pip3 install pyautogui

import schedule
import time
from pyautogui import press

def job(t):
    # print "I'm working...", t
    press('tab')
    press('enter')
    return

schedule.every().day.at("08:00").do(job,'It is time!')
schedule.every().day.at("12:00").do(job,'It is time!')
schedule.every().day.at("17:00").do(job,'It is time!')
schedule.every().day.at("23:55").do(job,'It is time!')

while True:
    schedule.run_pending()
    time.sleep(60) # wait one minute