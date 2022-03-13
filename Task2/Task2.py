# Напишите программу, которая рассчитывает положение точки относительно окружности.
# Координаты центра окружности и его радиус считываются из файла1.
import math
with open('file1.txt') as f1:
    x = f1.read(1)
    x=float(x)
    y = f1.read(3).strip()
    y = float(y)
    r = f1.readline()
    r = float(r)
data = []
with open('file2.txt') as f2:
    while True:
        line = f2.readline().strip()
        if line:
            data.append(line.split('\n'))
        if not line:
            break
data = [[float(n) for n in y[0].split(' ')] for y in data]

def pointposition(a,b):
    h = math.sqrt((x - a) ** 2 + (y - b) ** 2)
    if h == r:
        print('0 - Точка лежит на окружности')
    elif h < r:
        print('1 - Точка внутри')
    else:
        print('2 - Точка снаружи')
    return 

for point in data:
    x1 = point[0]
    y1 = point[1]
    pointposition(x1,y1)

