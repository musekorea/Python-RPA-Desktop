import pyautogui

pixel = pyautogui.pixel(30,30)
test = pyautogui.pixelMatchesColor(30,30,(12,128,206))
print(test)