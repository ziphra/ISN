from tkinter import*
import time

# Définition d'une animation qui fait suivre à une bille la trajectoire de la chute libre .
# 3eme version : affiche la bille dès que possible, à l'endroit où elle est censée se trouver, en fonction du temps réel passé
# depuis le lancé de la bille.
# Contrairement à ChuteLibreAnimV1 et V2, il n'y a pas d'incrément de temps dt fixé entre 2 affichages :
# on affiche la bille en fonction du temps effectivement passé depuis le lancé
# Ainsi, on est sûr que l'animation se fasse à la bonne vitesse, tout en ayant
# le plus d'affichage possible de la bille (puisqu'on le fait dès que possible, en fonction des capacités de l'ordinateur)
# C'est ainsi qu'on peut avoir la meilleure fluidité pour le mouvement

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
    # heure système du lancé
    start_time = time.time()
    while (y < 400) : # 400 est la hauteur de la fenêtre : si y > 400, la bille est sortie de la fenêtre. On peut s'arrêter !
        # temps depuis le lancé
        t = time.time() - start_time
        # déplacement suivant x et y
        x = x0+vx0*t
        y = y0+vy0*t+0.5*g*t*t
        canevas.coords(bille,x-20,y-20,x+20,y+20)
        canevas.update() # on a besoin de cet appel dans certaines versions de python / tkinter

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
dt = 0.01
t = 0
x = x0
y = y0

NN = 0

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


