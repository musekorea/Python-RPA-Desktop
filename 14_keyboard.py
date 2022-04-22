import pyautogui
import pyperclip

memo = pyautogui.getWindowsWithTitle("제목 없음")[0]
memo.activate()

def 한글타이핑(text):
  pyperclip.copy(text)
  pyautogui.hotkey("ctrl","v") 

pyautogui.write("MOYA", interval=4)
한글타이핑("안녕하세요")
한글타이핑("재사용가능")


