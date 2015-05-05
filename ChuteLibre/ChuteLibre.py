__author__ = 'euphrasieservant'

from tkinter import*
import time

# définition d'une animation qui fait suivre à une bille la trajectoire de la chute libre .

def conditionsInitiales():
    global x0,y0,vx0,vy0
    # coordonnées initiales (en m)
    x0 = 0
    y0 = 40
    # vitesse initiale (en m/s)
    vx0 = 10
    vy0 = -10  # négatif pour aller vers le haut
    

def animation(imageFile):
    global t, x, y
    global bille
    global dt

    # affichage d'une photo de fond
    photo = PhotoImage(file=imageFile)
    canvas.create_image(0,0,image=photo, anchor=NW)

    conditionsInitiales()

    # création de la bille
    bille=createBille(x0,y0)

    # intervalle de temps (en s) entre 2 affichages (utilisé par animeV0 à V3)
    dt = 0.1
    
    # valeurs initiales de t,x,y
    t = 0
    x = x0
    y = y0

    # décommenter ces lignes pour lancer animeV0 :
    # global appelAnimeV0
    # appelAnimeV0 = 0
    # animeV0()
    
    # animeV1()
    # animeV2()
    # animeV3()
    anime()

# Affiche la bille dès que possible, à l'endroit où elle est censée se trouver, en fonction du temps réel passé
# depuis le lancé de la bille.
# Contrairement à animeV1, V2 et V3, il n'y a pas d'incrément de temps dt fixé entre 2 affichages :
# On affiche la bille en fonction du temps effectivement passé depuis le lancé
# Ainsi, on est sûr que l'animation se fasse à la bonne vitesse, tout en ayant
# le plus d'affichage possible de la bille (puisqu'on le fait dès que possible, en focntion des capacités de l'ordinateur)
# C'est ainsi qu'on peut avoir la meilleure fluidité pour le mouvement
def anime():
    # valeur max de y (sortie de la fenêtre)
    ymax = hauteurFen+tailleBille
    start_time = time.time() # temps du lancé de la bille
    while (y <= ymax):
        t = time.time() - start_time
        drawBilleAtTime(t)

# Affiche la bille tous les temps dt, en utilisant une simple boucle
# Tente que l'affichage soit en temps réel, en attendant ce qu'il faut avant de dessiner la bille
def animeV3():
    global t,dt,y
    
    # valeur max de y (sortie de la fenêtre)
    ymax = hauteurFen+tailleBille
    t = 0
    while (y <= ymax):
        # on note le moment où on affiche la bille
        start_time = time.time()
        drawBilleAtTime(t)
        t = t + dt
        # le temps passé depuis le moment où on a affiché la bille
        elapsed_time = time.time() - start_time
        # attendre dt - elapsed_time avant de réafficher la bille
        # (mais attention, vérifier que elapsed_time est bien positif : en effet,
        # il n'est pas sûr que l'ordinateur soit assez rapide pour faire drawBilleAtTime
        # en un temps inférieur à dt ! (cela dépend de la valeur dt)
        if (elapsed_time > 0):
            time.sleep(dt-elapsed_time)

# Affiche la bille tous les temps dt, en utilisant une simple boucle.
# Dans animeV0 et V1, on utilise fen.after - qui est un mécanisme puissant
# Aurions-nous pu nous passer de ce mécanisme, et faire les choses plus simplement ?
# Après tout, il s'agit juste, tous les temps dt, d'afficher la bille là où elle se troune :
# une simple boucle doit suffire. C'est ce que fait animeV2
#
# Mais le problème dans cette implémentation, c'est que ce n'est pas une animation "en temps réel" :
# l'intervalle de temps dt ne correspond pas au temps réel passé.
# La courbe est correcte, mais la chute ne va pas à la bonne vitesse
# animeV3 tente de résoudre ce problème
def animeV2():
    global t,dt,y
    
    # valeur max de y (sortie de la fenêtre)
    ymax = hauteurFen+tailleBille
    t = 0
    while (y <= ymax):
        drawBilleAtTime(t)
        t = t + dt

# affiche la bille tous les temps dt
# en utilisant fen.after
# Par rapport à animeV0, se préoccupe d'appeler l'affichage de la bille après un temps égal à dt
# de façon à ce que l'affichage soit en "temps réel" : que l'animation aille vraiement à la bonne vitesse
# -- au moins, approximativement
def animeV1():
    global t, y
    if y<=hauteurFen+tailleBille:
        drawBilleAtTime(t)
        t = t + dt
        # fen.affer permet d'attendre un temps donné (en milliseconde) avant que ne s'execute de nouveau animeV1
        # Si on néglige le temps passé dans drawBilleAtTime, il faut qu'on attende dt*1000 pour afficher
        # la bille au bon moment 
        fen.after(round(1000*dt),animeV1)  # vitesse du mouvement

# affiche la bille tous les temps dt
# (Ici, on ne se préoccupe pas de la durée réelle dt: redemande un affichage de la bille dès que possible)
#
# Utilise fen.after pour ce faire
# fen.after permet de demander à ce que la fonction passée en argument soit exécutée après un certain délai
# 
# On peut se demander ce qui se passe vraiment dans cet appel à fen.after : 
# fen.after(1,animeV0)
# est-ce que le programme s'arrête sur cette ligne, attend le temps demandé, puis appelle la fonction passée en argument (animeV0) ?
# comme si on avait quelque chose tel que :
#    attendre (le temps demandé, 1 ms par exemple)
#    animeV0
# Cela serait ennuyeux : on aurait en effet animeV0 qui s'appelle elle-même (avec des appels qui s'empilent)
# Ou bien : est-ce que l'appel à fen.after est juste une "note" postée à fen (rien ne se passe réellement durant son exécution)
# et plus tard, fen lance l'exécution de animeV0 ?
# On peut regarder ce qui se passe en faisant printer un message à l'entrée de animeV0, et un autre à la sortie
# On constate que chaque entrée dans animeV0 est suivi d'une sortie :
# C'est la 2eme hypothèse qui est la bonne


def animeV0():
    global t, y
    global appelAnimeV0
    appelAnimeV0 = appelAnimeV0 + 1 # le N° de l'appel à animeV0
    print("Entrée de animeV0, appel N° " + str(appelAnimeV0))
    if y<=hauteurFen+tailleBille:
        drawBilleAtTime(t)
        t = t + dt
        # fen.affer permet d'attendre un temps donné (en milliseconde) avant que ne s'execute de nouveau animeV0
        # Ici, on demande de réafficher la bille immédiatement (après 1 milliseconde)
        # on ne se préoccupe pas de laisser s'écouler exactement le temps dt
        fen.after(1,animeV0)  # vitesse du mouvement
    print("Sortie de animeV0, appel N° " + str(appelAnimeV0))


#
#
#

# dessine la bille à l'endroit où elle se trouve après un temps t depuis le lancé
def drawBilleAtTime(t):
    global x,y
    # position (x et y) au temps t
    x = x0 + vx0*t
    y = y0 + vy0*t + 0.5*g*t*t
    print("position au temps " + str(t) + " : " + str(x) + " , " + str(y))
    drawBilleAtPosition(x,y)

# dessine la bille en x,y
def drawBilleAtPosition(x,y):
    canvas.coords(bille,x,y,x+tailleBille,y+tailleBille)
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
def createBille(x,y) :
    bille = canvas.create_oval(x,y,x+tailleBille,y+tailleBille,fill='red')
    return bille


Tk=fen = Tk()
hauteurFen = 400
largeurFen = 700
tailleBille = 20

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


