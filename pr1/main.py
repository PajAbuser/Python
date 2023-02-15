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

def pseudoRandom(x, y):
    return x*math.sin(( y * 255)) + y*math.cos((x * 255) )

def noise(x, y):
    return (math.sin(pseudoRandom(x, y) * 1000) + math.cos(pseudoRandom(y, x) * 1000))

def lerp(a, b, x):
    return a + x * (b - a)

def val_noise(x, y):
    n = 800
    #n = 127*(x+y) + 1
    x2  = ( ( (n*x) + 1 ) / ( round(n*x) + 1) ) % n
    y2  = ( ( (n*y) + 1 ) / ( round(n*y) + 1) ) % n
    x22 = ( ( (n*x) + 2 ) / ( round(n*x) + 2) ) % n
    y22 = ( ( (n*y) + 2 ) / ( round(n*y) + 2) ) % n
    return noise(x2,y2)*(x2+y2) + (1 - noise(x22,y22)*(x22+y22))
    

def func(x, y):
    x += 0
    y += 0
    #val = noise(x, y)
    val = val_noise(x, y)
    return val, val, val


label = tk.Label()
img = tk.PhotoImage(data=pyshader(func, 256, 256)).zoom(3, 3)
label.pack()
label.config(image=img)
tk.mainloop()