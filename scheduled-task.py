# must install modules from pip
# pip3 install pyautogui 
# pip3 install schedule
# and run this command too 
# sudo apt-get install python3-tk python3-dev

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