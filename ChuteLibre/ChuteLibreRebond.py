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
    

def animation():
    global t, x, y
    global bille
    global ymax

    # conditionsInitiales()

    # repere(largeurFen, hauteurFen, convertirMetresEnPixels(x0), convertirMetresEnPixels(y0))

    # création de la bille
    # bille=createBille(x0,y0)

    # valeurs initiales de t,x,y
    t = 0
    x = x0
    y = y0

    # valeur max de y, en m (sortie de la fenêtre)
    # (attention, hauteurFen et tailleBille sont en pixels)
    # ymax = convertirPixelsEnMetres(hauteurFen-tailleBille/2)
    ymax = convertirPixelsEnMetres(hauteurFen-70-tailleBille/2)

    anime()

# Affiche la bille dès que possible, à l'endroit où elle est censée se trouver, en fonction du temps réel passé
# depuis le lancé de la bille.
# Contrairement à animeV1, V2 et V3, il n'y a pas d'incrément de temps dt fixé entre 2 affichages :
# On affiche la bille en fonction du temps effectivement passé depuis le lancé
# Ainsi, on est sûr que l'animation se fasse à la bonne vitesse, tout en ayant
# le plus d'affichage possible de la bille (puisqu'on le fait dès que possible, en focntion des capacités de l'ordinateur)
# C'est ainsi qu'on peut avoir la meilleure fluidité pour le mouvement
def anime():
    global x0,y0,vx0,vy0,t
    
    start_time = time.time()
    while (animationOn):
        if (y >= ymax) : # il faut rebondir !
            # vitesse selon y :
            vy = vy0 + g * t
            if (vy > 0) : # (sinon, c'est qu'on est déjà en train de remonter)
                # si on prend comme nouvelle vitesse initiale l'opposé de vy,
                # on va remonter jusqu'à la hauteur du début
                vy0 = -vy
                vx0 = vx0 # ne change pas
                x0 = x
                y0 = y
                t = 0
                start_time = time.time()
            else :
                t = time.time() - start_time
        else :
            t = time.time() - start_time
        drawBilleAtTime(t)


#
#
#

# dessine la bille à l'endroit où elle se trouve après un temps t depuis le lancé
def drawBilleAtTime(t):
    # position (x et y) au temps t, en mètres
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
    canvas.coords(bille,xpixel-tailleBille/2,ypixel-tailleBille/2,xpixel+tailleBille/2,ypixel+tailleBille/2)
    canvas.update() # on a besoin de cet appel dans certaines versions de python / tkinter

#
#
#
 
#sur Terre
def initTerre():
    global g, photo
    g = 9.81
    print("ici la terre")
    # affichage d'une photo de fond
    # canvas.delete("image") # destruction de celle qui est affichée
    photo = PhotoImage(file="desert2.gif")
    canvas.create_image(0,0,image=photo, anchor=NW)
    canvas.update()

#sur la Lune
def initLune():
    global g, photo
    g = 1.63
    print("ici la lune")
    # affichage d'une photo de fond
    # canvas.delete("image") # destruction de celle qui est affichée
    photo = PhotoImage(file="lune.gif")
    canvas.create_image(0,0,image=photo, anchor=NW)
    canvas.update()

# crée une nouvelle bille dans le canvas et la retourne
# x et y en pixels
def createBille(x,y) :
    bille = canvas.create_oval(x-tailleBille/2,y-tailleBille/2,x+tailleBille/2,y+tailleBille/2,fill='red',tag="bille")
    return bille

def convertirMetresEnPixels(xMetre): 
    # il faut retourner un nombre entier, d'où l'appel à round
    return round(xMetre / echelle)

def convertirPixelsEnMetres(xPixel): 
    return xPixel * echelle

Tk=fen = Tk()
hauteurFen = 400 # en pixels
largeurFen = 700 # en pixels
tailleBille = 20 # en pixels
hauteurFenMetre = 10
# dimension en m représentée par un pixel
echelle = hauteurFenMetre / hauteurFen

fen.configure(width=largeurFen,height=hauteurFen)
canvas = Canvas(fen,width=largeurFen,height=hauteurFen)
photo = PhotoImage(file="brasil.gif")
canvas.create_image(0,0,image=photo, anchor=NW, tag="image")
canvas.pack()

#création des boutons dirigeant l'animation
bTerre=Button(fen,text="Terre", command=initTerre)
bTerre.pack(side=LEFT)

bLune=Button(fen,text="Lune", command=initLune)
bLune.pack(side=LEFT)

bQuit=Button(fen,text="Quitter", command=fen.destroy)
bQuit.pack(side=RIGHT)

def mouseButtonDown(event):
    #outputting x and y coords to console
    global x0pix,y0pix
    global x0, y0
    global bille
    global animationOn
    animationOn = FALSE
    x0pix = event.x
    y0pix = event.y
    x0 = convertirPixelsEnMetres(x0pix)
    y0 = convertirPixelsEnMetres(y0pix)
    # création de la bille (destruction d'abord si elle existe)
    canvas.delete("bille")
    bille = createBille(x0pix,y0pix)

def mouseButtonStillDown(event):
    #outputting x and y coords to console
    canvas.create_line(x0pix,y0pix,event.x,event.y,fill="red",tag="line")
    canvas.update()
    canvas.delete("line")
    canvas.create_line(x0pix,y0pix,event.x,event.y,fill="red",tag="line")
 
def mouseButtonUp(event):
    #outputting x and y coords to console
    #canvas.delete("line")
    #canvas.update()
    global x0,y0,vx0,vy0
    # avec ceci, la vitesse initiale est calculée en prenant le déplacement de la souris
    # converti en m. Mais risque d'être trop grande
    # On multiplie donc par un coefficient
    coef = 0.5 # 100/hauteurFenMetre
    vx0 = (convertirPixelsEnMetres(event.x) - x0) * coef
    vy0 = (convertirPixelsEnMetres(event.y) - y0) * coef

    canvas.delete("line")
    global animationOn
    animationOn = TRUE
    animation()

#mouseclick event
canvas.bind("<ButtonPress-1>",mouseButtonDown)
canvas.bind("<B1-Motion>",mouseButtonStillDown)
canvas.bind("<ButtonRelease-1>",mouseButtonUp)

fen.mainloop()


