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
    vx0 = 2
    vy0 = -2 # négatif pour aller vers le haut
    

def animation(imageFile):
    global bille, photo
    global ymax

    # changement de la photo de fond
    photo = PhotoImage(file=imageFile)
    canvas.itemconfig(photoOnCanvas,image=photo)
    canvas.update()

    conditionsInitiales()

    # création de la bille, si elle n'a pas encore été créée
    # Non ! pas ici, parce que on peut appeler plusieurs fois animation
    # et on veut une seule bille
    # bille=createBille(x0,y0)

    # valeur max de y, en m (sortie de la fenêtre)
    # (attention, hauteurFen et rayonBille sont en pixels)
    ymax = convertirPixelsEnMetres(hauteurFen+2*rayonBille)

    anime()

# Affiche la bille dès que possible, à l'endroit où elle est censée se trouver, en fonction du temps réel passé
# depuis le lancé de la bille.
def anime():
    global x, y
    # valeurs initiales de x,y
    x = x0
    y = y0
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
    # (y doit être global, parce qu'on l'utilise dans le test de sortie de anime)
    global x,y
    x = x0 + vx0*t
    y = y0 + vy0*t + 0.5*g*t*t
    # print("position au temps " + str(t) + " : " + str(x) + " , " + str(y))
    drawBilleAtPosition(x,y)

# dessine la bille en x,y (en m)
def drawBilleAtPosition(x,y):
    # il faut convertir les m en pixels
    xpixel = convertirMetresEnPixels(x)
    ypixel = convertirMetresEnPixels(y)
    canvas.coords(bille,xpixel-rayonBille,ypixel-rayonBille,xpixel+rayonBille,ypixel+rayonBille)
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

# crée une bille dans le canvas et la retourne
# x et y en pixels
def createBille(x,y) :
    bille = canvas.create_oval(x-rayonBille, y-rayonBille ,x+rayonBille, y+rayonBille, fill='red')
    return bille

def convertirMetresEnPixels(xMetre): 
    # il faut retourner un nombre entier, d'où l'appel à round
    return round(xMetre / echelle)

def convertirPixelsEnMetres(xPixel): 
    return xPixel * echelle

#
#
#

Tk=fen = Tk()
hauteurFen = 400 # en pixels
largeurFen = 700 # en pixels
rayonBille = 10 # en pixels
# dimension en m représentée par un pixel
echelle = 0.1

fen.configure(width=largeurFen,height=hauteurFen)
canvas = Canvas(fen,width=largeurFen,height=hauteurFen)
photo = PhotoImage(file="brasil.gif")
photoOnCanvas = canvas.create_image(0,0,image=photo, anchor=NW)

canvas.pack()

# Création de la bille. Comme on ne sait pas encore où on voudra qu'elle apparaisse
# on la place iitialement en dehors de la fenêtre
bille = createBille(-100, -100)

#création des boutons dirigeant l'animation
bTerre=Button(fen,text="Terre", command=animationTerre)
bTerre.pack(side=LEFT)

bLune=Button(fen,text="Lune", command=animationLune)
bLune.pack(side=LEFT)

bQuit=Button(fen,text="Quitter", command=fen.destroy)
bQuit.pack(side=RIGHT)

fen.mainloop()


