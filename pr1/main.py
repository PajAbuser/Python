import math
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
    else:
        return n * fact(n - 1)

def pseudoRandom(x, y):
    return x*math.sin(x  % fact(int(y * 2))) + y*math.cos(y  % fact(int(x * 2)))

def noise(x, y):
    return (math.sin(pseudoRandom(x, y) * 1000) + math.cos(pseudoRandom(x, y) * 1000))

def lerp(a, b, x):
    return a + x * (b - a)

def val_noise(x, y):
    n = 255
    n += 1
    x2 = round(n*x) % n
    y2 = round(n*y) % n
    return noise(x2, y2)
    

def func(x, y):
    x += 0
    y += 0
    val = noise(x, y)
    val = val_noise(x, y)
    return val, val, val


label = tk.Label()
img = tk.PhotoImage(data=pyshader(func, 256, 256)).zoom(3, 3)
label.pack()
label.config(image=img)
tk.mainloop()