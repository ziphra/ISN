__author__ = 'euphrasieservant'
from tkinter import*
from math import*
# tracer avec tkinter un corp en chute libre


# Trace la chute libre d'un corp lancé avec une vitesse initiale
# Les coordonnées et vitesses sont exprimées en m et m/s
# dans un repère lié à la fenêtre
# (orgigine en haut à gauche, axe des x vers la droite, axe des y vers le bas)
# @param g : gravitation au lieu considéré en N/kg
# @param x0 : absisse initiale en m
# @param y0 : ordonnée initiale en m
# @param vx0 : vitesse initiale en m/s
# @param vy0 : vitesse initiale en m/s (attention, valeur négative pour aller vers le haut !)
# @param echelle : conversion de m en pixels 1m = echelle * pixels

def chuteLibre(g, x0, y0, vx0, vy0, echelle):
    print("hello");
    # intervalle de temps entre deux points de la courbe
    deltaT = 0.1
    t=0 # temps au moment du lancer
    x = x0
    y = y0

    while t < 20: # durée de 20 secondes
        t=t+deltaT
        # je n'arrive pas à tracer un point avec Canvas,
        # je vais donc tracer la ligne entre (x,y) et (new, ynew), nouvelle position apres
        # l'intervalle de temps deltaT

        # les formules de la chute libre donne la position (xnew,ynew)
        # à l'instant t
        xnew = x0 + vx0 * t
        # attention, le repère en y est orienté vers le bas, d'où le + pour le terme en t^2
        # y(t)=vy × t + gt^2
        ynew = y0 + vy0 * t + 0.5 * g * t*t

        # on trace de l'ancienne position à la nouvelle


        can.create_line(echelle * x,
                        echelle * y,
                        echelle * xnew,
                        echelle * ynew,
                        fill="red")

        # on prepare la suite
        x = xnew
        y = ynew

# tracer un repère
# Le lancé aura lieu en son origine
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

#
# Afficher une fenêtre
#

# dimensions de la fenêtre
fenHeight = 500
fenWidth = 700

fen1 = Tk()
can = Canvas(fen1, bg='white', height=fenHeight, width=fenWidth)
can.pack(side = TOP, padx=10, pady=10)

#
# Dessiner un repère avec pour origine l'endroit du lancé
#

# position de l'origine du lancer dans la fenêtre
# (il s'agit de dimension en pixels)
xorigine = 100
yorigine = 400
repere(fenHeight, fenWidth, xorigine, yorigine)

#
# définition des paramètres de la chute libre
#

# gravitation au lieu considéré en N/kg
g = 9.81 # sur terre
echelle = 10 # un mètre est représenté par "echelle" pixels
# le lancé a lieu à l'origine du repère tracé
x0 = xorigine / echelle # en m
y0 = yorigine / echelle # en m
vx0 = 10 # en m/s
vy0 = -10 # en m/s négative pour lancer vers le haut

#
# Affichage
#

def courbe():
    chuteLibre(g,x0,y0,vx0,vy0,echelle)

# boutoncourbe = Button(fen1, text = "courbe", command = chuteLibre(g,x0,y0,vx0,vy0,echelle))
boutoncourbe = Button(fen1, text = "courbe", command = courbe)
boutoncourbe.pack(side = LEFT, padx = 10, pady=10)

fen1.mainloop()