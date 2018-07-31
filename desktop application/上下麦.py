from pymouse import PyMouse
from pykeyboard import PyKeyboard
import time
#vlive sent message
m = PyMouse()
k = PyKeyboard()
for i in range(1,90000,1):
    m.click(826, 1011, 1)
    time.sleep(10)