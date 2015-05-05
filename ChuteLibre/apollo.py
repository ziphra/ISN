__author__ = 'euphrasieservant'

from tkinter import*
import time

# Animation basée sur les images Apollo 15 (expérience "du marteau et de la plume" en chute libre)
# On surimpose aux images de la NASA une bille qui, elle aussi, tombe en chute libre.

def conditionsInitiales():
    global x0,y0,vx0,vy0
    # coordonnées initiales (en m)
    x0 = convertirPixelsEnMetres(126)
    y0 = convertirPixelsEnMetres(163)
    # vitesse initiale (en m/s)
    vx0 = 0
    vy0 = 0 # négatif pour aller vers le haut
    

def animation():
    global bille

    conditionsInitiales()

    # si la bille n'a pas encore été créée, la créer
    # (c'est le cas si on clique sur "Go" sans faire "A vos marques")
    if (bille == None) :
        bille=createBille(x0,y0)


    anime()

def anime():
    for i in range(1, 37):
        print(str(i));
        drawFrame(i)


#
#
#

# affichage de la ieme image de la vidéo
def drawFrame(i):
    global photo
    # on affiche la ieme image de la vidéo : le fichier s'appelle apollo[i]
    photo = PhotoImage(file="apollo/apollo" + str(i) +".gif")
    canvas.itemconfig(photoOnCanvas,image=photo)
    # temps correspondant
    t = i / 29.97 # 29.97 images / seconde (NTSC)
    drawBilleAtTime(t)
    
# dessine la bille à l'endroit où elle se trouve après un temps t depuis le lancé
def drawBilleAtTime(t):
    # position (x et y) au temps t, en mètres
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

# définit la constante de gravitation. 
def initGravitation():
    global g
    g = 1.62 # Nous sommes sur la lune 

# crée une nouvelle bille dans le canvas et la retourne
# x et y en pixels
def createBille(x,y) :
    bille = canvas.create_oval(x-tailleBille/2,y-tailleBille/2,x+tailleBille/2,y+tailleBille/2,fill='red')
    return bille

def convertirMetresEnPixels(xMetre): 
    # il faut retourner un nombre entier, d'où l'appel à round
    return round(xMetre / echelle)

def convertirPixelsEnMetres(xPixel): 
    return xPixel * echelle

# ceci nous a servi pour repérer les coordonnées de l'endroit où placer la blle dans l'image
def mouseButtonDown(event):
    print(str(event.x) + " ; " +str(event.y))

# préparation du lancé, dessine la bille en haut
def aVosMarques():
    global bille, photo
    photo = PhotoImage(file="apollo/apollo0.gif")
    canvas.itemconfig(photoOnCanvas,image=photo)
    conditionsInitiales()
    # si la bille n'a pas encore été créée, la créer
    if (bille == None) :
        bille=createBille(x0,y0)
    drawBilleAtTime(0)
  
Tk=fen = Tk()
hauteurFen = 409 # en pixels
largeurFen = 270 # en pixels
tailleBille = 20 # en pixels
# valeurs mesurées sur l'image (en pixels) :
yFinChute = 384
yDepartChute = 163
# valeur réelle en m (calculée à partir du nombre d'images (36), et de la durée entre 2 images en video NTSC)
hauteurChuteEnM = 1.2
# dimension en m représentée par un pixel
echelle = hauteurChuteEnM / (yFinChute - yDepartChute)

initGravitation()

bille = None # pour pouvoir tester dans prepa si a déja été créée ou pas

fen.configure(width=largeurFen,height=hauteurFen)
canvas = Canvas(fen,width=largeurFen,height=hauteurFen)
# affichage de l'image "N° 0"
photo = PhotoImage(file="apollo/apollo0.gif")
photoOnCanvas = canvas.create_image(0,0,image=photo, anchor=NW)
canvas.pack()

bAVosMarques=Button(fen,text="A vos marques!", command=aVosMarques)
bAVosMarques.pack(side=LEFT)

bGo=Button(fen,text="Go!", command=animation)
bGo.pack(side=LEFT)

bQuit=Button(fen,text="Quitter", command=fen.destroy)
bQuit.pack(side=RIGHT)

# a servi à repérer où on va place la bille
canvas.bind("<ButtonPress-1>",mouseButtonDown)

fen.mainloop()


