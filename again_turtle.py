import turtle
import time

t = turtle.Pen()

for x in range(1, 9):
    t.forward(100)
    t.left(225)

t.left(180)
t.up()
t.forward(150)
t.left(180)
t.down()

for x in range(1, 38):
    t.forward(100)
    t.left(175)

t.right(90)
t.up()
t.forward(200)
t.left(90)
t.down()

for x in range(1, 20):
    t.forward(100)
    t.left(95)



t.up()
t.forward(400)
t.right(90)
t.forward(100)
t.left(90)
t.down()

for x in range(1, 19):
    t.forward(100)
    if x % 2 == 0:
        t.left(175)
    else:
        t.left(225)


time.sleep(5)