from pymouse import PyMouse
from pykeyboard import PyKeyboard
import time
#vlive sent message
m = PyMouse()
k = PyKeyboard()
for i in range(1,1000,1):
    m.click(1650, 1006, 1)
    context=str(i)
    k.type_string(context)
    m.click(1887, 1009, 1)
    time.sleep(1)