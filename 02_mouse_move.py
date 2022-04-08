import pyautogui 

size = pyautogui.size()
size_width = size.width
size_height = size.height

print(size_width, size_height)


pyautogui.moveTo(100,100, duration=0.5)

pyautogui.move(100,100, duration=0.5)

pyautogui.move(100,100, duration=0.5)

position = pyautogui.position()
position_width = position.x
position_height = position.y
print(position_width, position_height)
print(position[0], position[1])
