import math
import random
import tkinter as tk


def pyshader(func, w, h):
    scr = bytearray((0, 0, 0) * w * h)
    for y in range(h):
        for x in range(w):
            p = (w * y + x) * 3
            scr[p:p + 3] = [max(min(int(c * 255), 255), 0)
                            for c in func(x / w, y / h)]
    return bytes('P6\n%d %d\n255\n' % (w, h), 'ascii') + scr

def func(x, y):
    r1 = 80/255
    r2 = 20/255
    circ1 = (x - 0.48)**2 + (y - 0.48)**2
    circ2 = (x - 0.52)**2 + (y - 0.52)**2
    return 1-(circ2)/(r1**2), 1-(circ1)/(r1**2), 0


label = tk.Label()
img = tk.PhotoImage(data=pyshader(func, 256, 256)).zoom(3, 3)
label.pack()
label.config(image=img)
tk.mainloop()