import pyautogui

size = pyautogui.size()
size_width = size.width
size_height = size.height

print(size_width, size_height)
print(size[0], size[1])