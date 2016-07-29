# Extra exercise in Chapter 1
# Task 1.4.10
from image import *
from plotting import *

data = file2image("img01.png")
height = len(data)
width = len(data[0])
img = data
pts = {x+(height-y)*1j for x in range(width) for y in range(height) if img[y][x][2] < 120}
plot(pts, height)

# Task 1.4.11
def f(z): return  (z.real - width/2) + (z.imag - height/2)*1j
pts = {f(z) for z in pts}
plot(pts, height)

# Task 1.4.17
import math
w = [math.e**(math.pi*1j/n) for n in range(20)[1:]]
plot(w, 10)

# Task 1.4.19
def rotate(z): return z*math.e**(1j*math.pi/4)
plot({rotate(z) for z in pts}, height)

