import pyautogui
import time
import sys

timeout = 10

def find_target(img):
  start_time = time.time()
  target = None
  while target==None:
    target = pyautogui.locateOnScreen(img)
    current_time = time.time()
    if current_time-start_time>timeout:
      break
  return target

def click_target(img):
  target = find_target(img)
  if target==None:
     print(f"[{img}] Not Found, Time out error occured")
     sys.exit()
  else:
    print(target)
    pyautogui.click(target)

click_target("file.png")