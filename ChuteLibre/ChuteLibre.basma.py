# Créé par Omar, le 25/02/2015 en Python 3.2
from tkinter import*

# définition d'une animation qui fait suivre à une bilel la trajectoire de la chute libre .
def anime():
    global x,y,t
    if x<=200:
        t = t + dt
        x = x0+vx0*t
        y = y0+vy0*t+0.5*g*t*t # déplacement suivant x et y
        print(x)
        print(y)
        canevas.coords(bille,x*3,y*3,x*3+50,y*3+50)
        fen.after(50,anime)  #vitesse du mouvement


fen=Tk()

# création d'une fenetre
canevas=Canvas(fen,bg='gray',height=400,width=700)
canevas.pack()

# coordonées initiales

g = 6 # constante de gravitation
vx0 = 10
vy0 = -10 # négatif, donc vers le haut
t = 0
dt = 0.1
x0 = 10
y0 = 100

x = x0
y = y0

#création d'une bille
bille=canevas.create_oval(x,y,x+50,y+50,fill='red')

anime()

fen.mainloop()


