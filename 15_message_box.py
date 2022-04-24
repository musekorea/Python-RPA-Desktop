import pyautogui

x = pyautogui.password(text="비밀번호를 입력해주세요", title="비밀번호", default="", mask="*")
print(x)