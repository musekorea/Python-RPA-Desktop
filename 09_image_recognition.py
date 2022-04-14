import pyautogui

pyautogui.sleep(2)
boxes = pyautogui.locateAllOnScreen("./checkbox.png")
print(boxes)
for box in boxes:
  pyautogui.click(box, duration=0.5)