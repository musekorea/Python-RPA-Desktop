import pyautogui
import time
import sys
 
timeout = 10        #대기할 시간 
start_time = time.time() #시작시간

image = pyautogui.locateOnScreen("file.png")
if image:
  print("바로실행")
  pyautogui.click(image)
  sys.exit()

while image==None:
  image = pyautogui.locateOnScreen("file.png")
  current_time = time.time()
  if current_time-start_time>10:
    print("시간초과")
    sys.exit()

pyautogui.click(image)
