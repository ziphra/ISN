__author__ = 'euphrasieservant'

from tkinter import*
import time

# définition d'une animation qui fait suivre à une bille la trajectoire de la chute libre .

def conditionsInitiales():
    global x0,y0,vx0,vy0
    # coordonnées initiales (en m)
    x0 = convertirPixelsEnMetres(10)
    y0 = convertirPixelsEnMetres(40)
    # vitesse initiale (en m/s)
    vx0 = 1
    vy0 = 0 # négatif pour aller vers le haut
    

def animation(imageFile):
    global t, x, y
    global bille
    global ymax

    # affichage d'une photo de fond
    photo = PhotoImage(file=imageFile)
    canvas.create_image(0,0,image=photo, anchor=NW)

    conditionsInitiales()

    repere(largeurFen, hauteurFen, convertirMetresEnPixels(x0), convertirMetresEnPixels(y0))

    # création de la bille
    bille=createBille(x0,y0)

    # valeurs initiales de t,x,y
    t = 0
    x = x0
    y = y0

    # valeur max de y, en m (sortie de la fenêtre)
    # (attention, hauteurFen et tailleBille sont en pixels)
    ymax = convertirPixelsEnMetres(hauteurFen+tailleBille)

    anime()

# Affiche la bille dès que possible, à l'endroit où elle est censée se trouver, en fonction du temps réel passé
# depuis le lancé de la bille.
# Contrairement à animeV1, V2 et V3, il n'y a pas d'incrément de temps dt fixé entre 2 affichages :
# On affiche la bille en fonction du temps effectivement passé depuis le lancé
# Ainsi, on est sûr que l'animation se fasse à la bonne vitesse, tout en ayant
# le plus d'affichage possible de la bille (puisqu'on le fait dès que possible, en focntion des capacités de l'ordinateur)
# C'est ainsi qu'on peut avoir la meilleure fluidité pour le mouvement
def anime():
    start_time = time.time()
    while (y <= ymax):
        t = time.time() - start_time
        drawBilleAtTime(t)


#
#
#

# dessine la bille à l'endroit où elle se trouve après un temps t depuis le lancé
def drawBilleAtTime(t):
    # position (x et y) au temps t, en mètres
    x = x0 + vx0*t
    y = y0 + vy0*t + 0.5*g*t*t
    print("position au temps " + str(t) + " : " + str(x) + " , " + str(y))
    drawBilleAtPosition(x,y)

# dessine la bille en x,y (en m)
def drawBilleAtPosition(x,y):
    # il faut convertir les m en pixels
    xpixel = convertirMetresEnPixels(x)
    ypixel = convertirMetresEnPixels(y)
    canvas.coords(bille,xpixel,ypixel,xpixel+tailleBille,ypixel+tailleBille)
    canvas.update() # on a besoin de cet appel dans certaines versions de python / tkinter

#
#
#
 
#sur Terre
def animationTerre():
    global g
    g = 9.81
    print("ici la terre")
    animation("desert2.gif")


#sur la Lune
def animationLune():
    global g
    g = 1.63
    print("ici la lune")
    animation("lune.gif")

# crée une nouvelle bille dans le canvas et la retourne
# x et y en pixels
def createBille(x,y) :
    bille = canvas.create_oval(x,y,x+tailleBille,y+tailleBille,fill='red')
    return bille

def convertirMetresEnPixels(xMetre): 
    # il faut retourner un nombre entier, d'où l'appel à round
    return round(xMetre / echelle)

def convertirPixelsEnMetres(xPixel): 
    return xPixel * echelle

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
    canvas.create_line(xorigine, 0, xorigine, fenWidth, fill="black", dash=(4, 4))
    # les ordonnées : ligne verticale
    canvas.create_line(0, yorigine, fenHeight, yorigine, fill="black", dash=(4, 4))
    
Tk=fen = Tk()
hauteurFen = 400 # en pixels
largeurFen = 700 # en pixels
tailleBille = 20 # en pixels
hauteurFenMetre = 4
# dimension en m représentée par un pixel
echelle = hauteurFenMetre / hauteurFen

fen.configure(width=largeurFen,height=hauteurFen)
canvas = Canvas(fen,width=largeurFen,height=hauteurFen)
photo = PhotoImage(file="brasil.gif")
canvas.create_image(0,0,image=photo, anchor=NW)
canvas.pack()

#création des boutons dirigeant l'animation
bTerre=Button(fen,text="Terre", command=animationTerre)
bTerre.pack(side=LEFT)

bLune=Button(fen,text="Lune", command=animationLune)
bLune.pack(side=LEFT)

bQuit=Button(fen,text="Quitter", command=fen.destroy)
bQuit.pack(side=RIGHT)

fen.mainloop()


