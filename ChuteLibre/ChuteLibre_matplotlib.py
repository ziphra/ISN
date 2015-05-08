from pylab import *

# Trace la trajectoire d'un corps en chute libre, lancé avec une vitesse initiale
#
# Utilise matplotlib
# plot permet de tracer une courbe
#
# On sait écrire l'absisse et l'ordonnée du corps en focntion du temps t
# plot(x,y) permet d'afficher y en fonction de x
# On calcule pour chaque instant t
# les valeurs de x et de y correspondant

# LES VALEURS D'ENTREE
# vitesse initiale selon x (m/s)
vx0 = 10
# vitesse initiale selon y (m/s)
vy0 = 20
# absisse initiale
x0 = 0
# ordonnée initiale
y0 = 0
# gravitation au lieu considéré
g = 9.81

# le nombre de points utilisés pour tracer la courbe
nbPoints = 1000
# durée entre deux points consécutifs (en s)
dt = 0.01
# temps de la fin du tracé
tmax = nbPoints * dt # en s

# tableau des absisses, du temps 0 au temps tmax
x = [0] * nbPoints
# tableau des ordonnées, du temps 0 au temps tmax
y = [0] * nbPoints 

for i in range(0, nbPoints): 
    # temps correspondant au i ème point
    t = i*dt
    # vitesse constante selon x
    x[i] = x0 + vx0 * t
    # acceleration selon y
    y[i] = y0 + vy0 * t - 0.5 * g * t*t

plot(x, y)
show()