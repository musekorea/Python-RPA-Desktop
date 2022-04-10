import pyautogui

pyautogui.click(12,1425, duration=0.5) #윈도우 버튼 클릭
pyautogui.click(846, 1227, duration=0.5) #그림판 아이콘 클릭
pyautogui.click(424, 100, duration=0.5) #그림판 연필 선택
pyautogui.click(237, 469, duration=0.5) #그림판 캔버스 위에 마우스 위치 시킴 


pyautogui.mouseDown()
pyautogui.move(200,200, duration=3)
pyautogui.mouseUp()

pyautogui.sleep(2)
#pyautogui.rightClick(400,400)
pyautogui.middleClick(900,600)