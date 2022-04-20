import pyautogui

test = pyautogui.getWindowsWithTitle("제목 없음 - Windows 메모장")[0]

if test.isActive == False:
  test.activate()

print(test)
pyautogui.sleep(2)

test.close()