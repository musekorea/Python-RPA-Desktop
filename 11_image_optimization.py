from PIL import ImageGrab
from functools import partial
import pyautogui

ImageGrab.grab = partial(ImageGrab.grab, all_screens=True)

boxes=pyautogui.locateOnScreen("./daum.png",confidence=0.7 )
print(boxes)

