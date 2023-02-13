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

def fact(n):
    if n == 0:
        return 1
    return n * fact(n - 1)

def pseudoRandom(x, y):
    return math.sin(x * 618033988749895 % fact(int(y * 10))) + math.cos(y * 381966011250105 % fact(int(x * 10)))

def noise(x, y):
    return (math.sin(pseudoRandom(x, y) * 1000) + math.cos(pseudoRandom(x, y) * 1000))

def lerp(a, b, x):
    return a + x * (b - a)

def val_noise(x, y):
    d = 1/512
    return lerp(noise(x - d, y - d), noise(x + d, y + d), x+y)

def func(x, y):
    #val = noise(x, y)
    val = val_noise(x, y)
    return val, val, val



label = tk.Label()
img = tk.PhotoImage(data=pyshader(func, 256, 256)).zoom(2, 2)
label.pack()
label.config(image=img)
tk.mainloop()