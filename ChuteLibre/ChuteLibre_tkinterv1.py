__author__ = 'euphrasieservant'
from tkinter import*
from math import*
# tracer avec tkinter un corp en chute libre
# j'ai écrit dans la fonction chute libre on a pris l'équation du mouvement dans un repère mathématiques habituels
# et pour l'afficher correctement dans le repère de la fenetre on est obligé d'effectuer un changement de variable.
# ce qui fait qu'on a plein d'arguments lié à ca


# tracer un repère
# @param fenHeight hauteur de la fenêtre
# @param fenWidth largeur de la fenêtre
# @param xorigine position de l'origine par rapport à la fenêtre
# @param yorigine position de l'origine par rapport à la fenêtre
# note : pour tk, l'origine est en haut à gauche,
# width correspond à l'axe des X, height à celui des Y,
def repere(fenWidth, fenHeight, xorigine, yorigine):
    # les absisses : ligne horizontale
    can.create_line(xorigine, 0, xorigine, fenWidth, fill="black")
    # les ordonnées : ligne verticale
    can.create_line(0, yorigine, fenHeight, yorigine, fill="black")

# transformation d'une ascisse dans le repère vers coordonnée en X dans la fenêtre
# @param xerpere une abscisse dans le repère du dessin
# @param xorigine voir définition de la focntion repere
# @param echelle pour convertir les m en unités au sein de la fenêtre
def xRepereVersxFenetre(xrepere, xorigine, echelle):
    return echelle*xrepere + xorigine

# transformation d'une ordonnée dans le repère vers coordonnée en Y dans la fenêtre
# (remarque : dans la fenêtre, les y augmentent en allant vers le bas
# (alors que dans notre repère, c'est dans l'autre sens)
def yRepereVersyFenetre(yrepere, yorigine, echelle):
    return yorigine - echelle*yrepere


# Trace la chute libre d'un corp lancé avec une vitesse initiale
# @param g : gravitation au lieu considéré en N/kg
# @param x0 : absisse initiale (dans le repère tracé)
# @param y0 : ordonnée initiale (dans le repère tracé)
# @param vx0 : vitesse initiale selon x (en m/s)
# @param vy0 : vitesse initiale selon y (en m/s)

def chuteLibre(g, x0, y0, vx0, vy0, xorigine, yorigine, echelle):
    # intervalle de temps entre deux points de la courbe
    deltaT = 0.1
    t=0 # temps au moment du lancer
    x = x0
    y = y0

    # tant qu'on n'est pas retombé par terre...
    while t < 5:
        t=t+deltaT
        # je n'arrive pas à tracer un point avec Canvas,
        # je vais donc tracer la ligne entre (x,y) et (new, ynew), nouvelle position apres
        # l'intervalle de temps deltaT

        # les formules de la chute libre donne la position (xnew,ynew)
        # à l'instant t
        xnew = x0 + vx0 * t
        # y(t)=vy × t − gt22
        ynew = y0 + vy0 * t - 0.5 * g * t*t

        # on trace de l'ancienne position à la nouvelle
        # mais attention, il faut se placer dans le repère de tkinter


        can.create_line(xRepereVersxFenetre(x, xorigine, echelle),
                        yRepereVersyFenetre(y, yorigine, echelle),
                        xRepereVersxFenetre(xnew, xorigine, echelle),
                        yRepereVersyFenetre(ynew, yorigine, echelle),
                        fill="red")

        # on prepare la suite
        x = xnew
        y = ynew

# dimensions de la fenêtre
fenHeight = 500
fenWidth = 700

fen1 = Tk()
can = Canvas(fen1, bg='white', height=fenHeight, width=fenWidth)
can.pack(side = TOP, padx=10, pady=10)

# position de l'origine du repère dans la fenêtre, et échelle
xorigine = 100
yorigine = 400
echelle = 20 # un mètre est représenté par "echelle" pixels
repere(fenHeight, fenWidth, xorigine, yorigine)

# définition des paramètres
# gravitation au lieu considéré en N/kg
g = 9.81 # sur terre

# le lancé a lieu à l'origine
x0 = 0
y0 = 0
vx0 = 10
vy0 = 10

boutoncourbe = Button(fen1, text = "courbe", command = chuteLibre(g,x0,y0,vx0,vy0,xorigine, yorigine, echelle))
boutoncourbe.pack(side = LEFT, padx = 10, pady=10)

fen1.mainloop()