from tkinter import *
from tkinter import colorchooser
import random

tk = Tk()
canvas = Canvas(tk, width=500, height=500)
canvas.pack()

def random_rectangle(width, height, fill_color):
    x1 = random.randrange(width)
    y1 = random.randrange(height)
    x2 = random.randrange(x1 + random.randrange(width))
    y2 = random.randrange(y1 + random.randrange(height))
    canvas.create_rectangle(x1, y1, x2, y2, fill=fill_color)

# color = colorchooser.askcolor()

# for x in range(0, 100):
#     random_rectangle(400, 400, color[1])

canvas.create_arc(10,10,500,500, extent=180, style=ARC)



tk.mainloop()
