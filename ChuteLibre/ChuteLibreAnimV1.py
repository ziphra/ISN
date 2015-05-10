from tkinter import*

# définition d'une animation qui fait suivre à une bille la trajectoire de la chute libre .
# 1ere version : simple boucle, l'affichage n'est pas synchronisé avec le temps réel

#sur Terre
def anime1():
    global g
    g = 9.81
    anime()



#sur la Lune
def anime2():
    global g
    g = 1.62
    anime()

def anime():
    global x,y,t

    while (y < 400) : # 400 est la hauteur de la fenêtre : si y > 400, la bille est sortie de la fenêtre. On peut s'arrêter !
        # déplacement suivant x et y
        x = x0+vx0*t
        y = y0+vy0*t+0.5*g*t*t
        canevas.coords(bille,x-20,y-20,x+20,y+20)
        canevas.update() # on a besoin de cet appel dans certaines versions de python / tkinter
        t = t + dt # temps suivant
        
    # la bille est sortie de la fenêtre : remise à zéro de la position de la bille
    x = x0
    y = y0
    t = 0
    canevas.coords(bille,x-20,y-20,x+20,y+20)
    canevas.update() # on a besoin de cet appel dans certaines versions de python / tkinter


fen = Tk()

# création d'une fenêtre

canevas=Canvas(fen, bg='gray',height=400,width=700)
canevas.pack()


# coordonnées initiales (1 pixel = 1m)
x0 = 30
y0 = 100
# vitesse initiale
vx0 = 10
vy0 = -10 # négatif, donc vers le haut
# accroissement du temps à chaque itération (en s)
dt = 0.1
t = 0
x = x0
y = y0


#création d'une bille
bille=canevas.create_oval(x-20,y-20,x+20,y+20,fill='red')


#création des boutons dirigeant l'animation
b1=Button(fen,text="Terre", command=anime1)
b1.pack(side=LEFT)

b2=Button(fen,text="Lune", command=anime2)
b2.pack(side=LEFT)

b3=Button(fen,text="Quitter", command=fen.destroy)
b3.pack(side=RIGHT)

fen.mainloop()


