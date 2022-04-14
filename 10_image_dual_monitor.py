from PIL import ImageGrab
from functools import partial
import pyautogui

ImageGrab.grab = partial(ImageGrab.grab, all_screens=True)

boxes=pyautogui.locateAllOnScreen("./checkbox.png")

for box in boxes:
  pyautogui.click(box, duration=1)

