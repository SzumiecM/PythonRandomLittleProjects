import pygame as py
from random import randrange
from time import sleep
import sys

#DEFAULT/DEFINED
N = 400
speed = 0.1
try:
    N = int(sys.argv[1])
    speed = float(sys.argv[2])
except:
    pass
###########################

def pause():
    cont = False
    while not cont:
        pressed = py.key.get_pressed()
        if pressed[py.K_ESCAPE]: cont = True
        sleep(0.005)


py.init()
screen = py.display.set_mode((N, N))
done = False
t = 0
points = 1
coo = [(N/2, N/2)]
drc = (0, -N/20)
up = False

while not done:
    screen.fill((0,0,0))
    color = (randrange(0, 255), randrange(0, 255), randrange(0, 255))
    while color == (0,0,0):     color = (randrange(0, 255), randrange(0, 255), randrange(0, 255))

    # DIRECTIONS
    for event in py.event.get():
        if event.type == py.QUIT: done = True
        if event.type == py.KEYDOWN and event.key == py.K_a: drc = (-N/20, 0)
        if event.type == py.KEYDOWN and event.key == py.K_w: drc = (0, -N/20)
        if event.type == py.KEYDOWN and event.key == py.K_s: drc = (0, N/20)
        if event.type == py.KEYDOWN and event.key == py.K_d: drc = (N/20, 0)

    # GENERATE NEW EATABLE
    if not up:
        x = randrange(0, N-N/20, N/20)
        y = randrange(0, N-N/20, N/20)
        while (x, y) in coo:
            x = randrange(0, N - N / 20, N / 20)
            y = randrange(0, N - N / 20, N / 20)
        up = True
    py.draw.rect(screen, color, py.Rect(x, y, N/20, N/20))

    # MOVE SNAKE
    for i in reversed(range(len(coo))):
        if i == len(coo)-1:
            a = coo[i][0]
            b = coo[i][1]
        coo[i] = list(coo[i])
        if i > 0:
            coo[i] = list(coo[i-1])
            coo[i] = tuple(coo[i])
        else:
            coo[i][0] += list(drc)[0]
            coo[i][1] += list(drc)[1]

            if coo[i][0] > N-N/20: coo[i][0] = 0
            if coo[i][0] < 0: coo[i][0] = N-N/20
            if coo[i][1] > N-N/20: coo[i][1] = 0
            if coo[i][1] < 0: coo[i][1] = N-N/20

            coo[i] = tuple(coo[i])

            if up == True and x == coo[i][0] and y == coo[i][1]:
                points += 1
                coo.append((a, b))
                py.draw.rect(screen, (255, 255, 255), py.Rect(a, b, N/20, N/20))
                up = False
            if any(coo.count(x) > 1 for x in coo): done = True

        py.draw.rect(screen, (255,255,255), py.Rect(coo[i][0], coo[i][1], N/20, N/20))

    # ESC
    pressed = py.key.get_pressed()
    if pressed[py.K_ESCAPE]: done = True
    if pressed[py.K_SPACE]: pause()

    py.display.flip()
    sleep(speed)

print(str("{0:.2f}".format(points*N/20*N/20/N/N*100)) + '%')
