#coding=utf-8
from pymouse import PyMouse
import time
import random
#whiteboard drawing
m = PyMouse()
for i in range(1,500,1):
    x = random.randint(365, 1191)
    y = random.randint(182, 755)
    m.drag(x,y)
    time.sleep(random.randint(0,1))
