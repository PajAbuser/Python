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
    return abs( (math.sin(pseudoRandom(x, y) * 1000) + math.cos(pseudoRandom(y, x) * 1000) ) ) % 1

def lerp(a, b, x):
    return a + x * (b - a)

def QFunc(t):
    return t**3 * (t * (t * 6 - 15) + 10) 

def val_noise(x, y):
    n = 10

    x2 = n*lerp(0, 1, x) 
    y2 = n*lerp(0, 1, y) 
    x3 = round(x2) # n(x) 
    y3 = round(y2) # n(y)
    xn = ( x3 ) / n # xn(x) - [0,1], 1/n
    yn = ( y3 ) / n # yn(x) - [0,1], 1/n

    dist1 = ( ( (      (x - xn)  ** 2 ) + (      (y - yn)  ** 2 ) ) ** (1/2) )
    dist2 = ( ( ( (1 - (x - xn)) ** 2 ) + (      (y - yn)  ** 2 ) ) ** (1/2) )
    dist3 = ( ( (      (x - xn)  ** 2 ) + ( (1 - (y - yn)) ** 2 ) ) ** (1/2) )
    dist4 = ( ( ( (1 - (x - xn)) ** 2 ) + ( (1 - (y - yn)) ** 2 ) ) ** (1/2) )

    # print(noise(xn, yn)             * dist1 +
    #     noise(xn, yn + 1/n)       * dist3 +
    #     noise(xn + 1/n, yn + 1/n) * dist4 +
    #     noise(xn + 1/n, yn)       * dist2 )
    return (
        noise(xn, yn)             * lerp(0, 1, QFunc(dist1) ) +
        noise(xn, yn + 1/n)       * lerp(0, 1, QFunc(dist3) ) +
        noise(xn + 1/n, yn + 1/n) * lerp(0, 1, QFunc(dist4) ) +
        noise(xn + 1/n, yn)       * lerp(0, 1, QFunc(dist2) ) 
    )

    # return ((x - xn) + (y - yn))*n
    # return 0.5 + (
    #     (noise(xn + 1/n, yn) - noise(xn, yn)) * ( (     abs(x - xn) ) / n ) + 
    #     (noise(xn, yn + 1/n) - noise(xn, yn)) * ( (     abs(y - yn) ) / n ) + 
    #     (noise(xn - 1/n, yn) - noise(xn, yn)) * ( ( 1 - abs(x - xn) ) / n ) + 
    #     (noise(xn, yn - 1/n) - noise(xn, yn)) * ( ( 1 - abs(y - yn) ) / n )
    #     ) / 4
    #return noise(xn, yn) * (( ((x) - (xn))*n ) + ( ((y) - (yn))*n ))


    #n = 127*(x+y) + 1
    # x2  = ( ( (n*x) + 1 ) / ( round(n*x) + 1) )
    # y2  = ( ( (n*y) + 1 ) / ( round(n*y) + 1) )
    # return noise(x2,y2) + (x/x2)*(noise(x2 + 1/n, y2) - noise(x2,y2)) + (y/y2)*(noise(x2, y2 + 1/n) - noise(x2,y2))


    
def val_noise2(x, y):
    
    n = 100

    x2 = n*lerp(0, 1, x) 
    y2 = n*lerp(0, 1, y) 
    x3 = round(x2) # n(x) 
    y3 = round(y2) # n(y)
    left = ( x3 ) / n # xn(x) - [0,1], 1/n
    top  = ( y3 ) / n # yn(x) - [0,1], 1/n

    pointInQuadX = x - left
    pointInQuadY = y - top

    tx1 = pointInQuadX * 1 if pseudoRandom(left, top) % 3 + \
                        1 == 0 else -1 if pseudoRandom(left, top) % 3 + 1 == 2 else 0 + \
                        pointInQuadY * 1 if pseudoRandom(left, top) % 3 == 2 else -1 if pseudoRandom(left, top) % 3 + 1 == 4 else 0

    tx2 = (pointInQuadX - 1/n) * 1 if pseudoRandom(left + 1/n, top) % 3 + \
                        1 == 0 else -1 if pseudoRandom(left + 1/n, top) % 3 + 1 == 2 else 0 + \
                        pointInQuadY * 1 if pseudoRandom(left + 1/n, top) % 3 == 2 else -1 if pseudoRandom(left + 1/n, top) % 3 + 1 == 4 else 0

    bx1 = pointInQuadX * 1 if pseudoRandom(left, top + 1/n) % 3 + \
                        1 == 0 else -1 if pseudoRandom(left, top + 1/n) % 3 + 1 == 2 else 0 + \
                        (pointInQuadY - 1/n) * 1 if pseudoRandom(left, top + 1/n) % 3 == 2 else -1 if pseudoRandom(left, top + 1/n) % 3 + 1 == 4 else 0

    bx2 = (pointInQuadX - 1/n) * 1 if pseudoRandom(left + 1/n, top + 1/n) % 3 + \
                        1 == 0 else -1 if pseudoRandom(left + 1/n, top + 1/n) % 3 + 1 == 2 else 0 + \
                        (pointInQuadY - 1/n) * 1 if pseudoRandom(left + 1/n, top + 1/n) % 3 == 2 else -1 if pseudoRandom(left + 1/n, top + 1/n) % 3 + 1 == 4 else 0

    pointInQuadX = QFunc(pointInQuadX)
    pointInQuadY = QFunc(pointInQuadY)

    tx = lerp(tx1, tx2, pointInQuadX)
    bx = lerp(bx1, bx2, pointInQuadX)
    tb = lerp(tx, bx, pointInQuadY)
    
    #print(bx1, tx2, pointInQuadX)

    return tb

def func(x, y):
    x += 0
    y += 0
    #val = noise(x, y)
    val = val_noise2(x, y)
    return val, val, val


label = tk.Label()
img = tk.PhotoImage(data=pyshader(func, 256, 256)).zoom(3, 3)
label.pack()
label.config(image=img)
tk.mainloop()