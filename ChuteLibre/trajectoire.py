__author__ = 'euphrasieservant'
from tkinter import*

# trace des billes à la suite en suivant la trajectoire de chute libre

fen = Tk()
can = Canvas(fen, bg='white', height=400, width=1000)
can.pack(side=TOP, padx=10, pady=10)


# conditions initiales
x = 10
y = 200
t = 0
dt = 0.1
vx = 10
vy = -10
g = 9.81

while t < 60:

    x = x + vx * t
    y = y + vy * t + 0.5 * g * t*t
    bille = can.create_oval(x-5, y-5, x+5, y+5, fill='red')
    t = t + dt

fen.mainloop()