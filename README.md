# ISN
projet isn de Euphrasie Servant et Basma Rezki

#Projet ISN : animations en Python sur le thème de la chute libre

## Présentation
### Introduction
Nous avons voulu suivre la spécialité ISN parce que c’était l’occasion de découvrir la programmation, un sujet qui nous était jusqu’alors quasiment inconnu. Il nous semblait en effet  important et intéressant d’apprendre comment programmer un ordinateur, parce que l’informatique est un outil puissant, qui est aujourd’hui absolument nécessaire et incontournable dans la plupart des domaines.
Au fil de l'année, nous avons appris un peu du langage Python, et nous avons utilisé quelques outils qui nous ont permis de réaliser de petits programmes simples. Pour la réalisation de ce projet, nous avons utilisé ces outils vus en classe, et d'autres que nous avons découverts au fil du travail sur ce projet. 

### Thème et objectifs du projet
La première question pour le projet était de trouver un sujet à la fois intéressant et réalisable vu notre niveau. Nous avions envie de faire quelque chose avec du graphique et de l’animation. Après plusieurs hésitations, nous nous sommes dit que nous pourrions essayer de faire une animation d’un personnage en train de sauter, et de comparer les sauts sur la terre et sur la lune : cela permettrait de combiner animation et cours de physique. Disons le tout de suite, nous nous sommes heurtés à des difficultés que nous n’avons pas pu surmonter, en particulier en ce qui concerne l’animation d’un personnage. Nous avons du revoir nos ambitions à la baisse : nous nous sommes finalement contentés d’animer une balle. Mais, en déviant de notre but initial, nous avons découvert de nouvelles choses, et nous avons eu de nouvelles idées.

### Ce projet sur Github
nous avons regardé comment utiliser Github pour gérer le code source de notre projet. 
Comme l’explique Wikipedia, http://fr.wikipedia.org/wiki/GitHub Github est un service web d'hébergement et de gestion de développement de logiciels, qui utilise le logiciel de gestion de versions Git. C’est un outil très utilisé par les développeurs de logiciels open-source, qui leur permet :
de partager leur code
de conserver toutes les étapes de leurs développement
de participer à des développements en commun

Pour nous, cela nous a permis :
de publier notre code
de nous échanger nos versions (même si, en pratique, nous avons plutôt échangé par mail)
d’être assurés d’avoir une sauvegarde de notre projet (pas question de tout perdre si notre ordinateur tombe en panne !)


L’ensemble des programmes - et ce rapport - sont de ce fait accessibles à l’adresse :
https://github.com/ziphra/ISN

### Environnement de développement
Pour programmé, nous avons utilisé deux outils différents. L’une d’entre nous a utilisé Édupython, c’est avec ce programme que nous avons débuté la programmation en classe d’ISN. L’autre à utilisé Pycharm, car édupython n’est pas compatible sur les Macintosh. 
1ere étape : tracer la trajectoire d’un corps en chute libre
Avant de penser faire une animation, voyons comment tracer la trajectoire d’un corps en train de tomber en chute libre

Un peu de physique
Comme on l’apprend en cours de physique, un corps en chute libre, lancé en (x0, y0) avec une vitesse initiale (Vx0, Vy0) suit une trajectoire dont les cordonnées sont données par les formules :
x = x0 + Vx0 * t 
et
y = y0 + Vy0 * t - 1/2*g*t^2

### Tracé de la courbe
Pour tracer une courbe, on a besoin d’une bibliothèque permettant de faire des graphiques. Nous nous sommes servis pour ça de matplotlib et de Tkinter qui sont deux bibliothèques du langage python. Pour ce qui est de dessiner une courbe, matplotlib est le mieux adapté, mais nous l’avons fait aussi avec Tkinter, parce que c’est l’outil que nous avons utilisé ensuite pour réaliser nos animations.

Tracé de la courbe avec Matplotlib
Matplotlib http://matplotlib.org est une bibliothèque permettant de faire des graphiques 2D en python.
Installation de matplotlib
Avec Python 3.4 l’utilitaire d’installation “pip” est disponible. Pour installer matplotlib, il suffit de faire :
pip install matplotlib
Utilisation de la méthode plot
Une fois installée, il est assez simple de tracer notre courbe, en utilisant la fonction plot de matplotlib, qui permet de tracer des points dans un repère. Le principe est le suivant : on détermine les coordonnées de tous les points à afficher, sous forme de deux tableaux, l’un contenant les abscisses des points, l’autre les ordonnées. 
La fonction plot prend en argument ces tableaux de valeurs, et affiche les points dans un repère, à l’échelle adaptée.
Voir programme :
Tracer de la courbe avec Tkinter
Tkinter est une bibliothèque pour réaliser des interfaces graphiques avec Python (donc par exemple, pour créer une fenêtre et y mettre des boutons, des images ou des objets graphiques, etc.) C’est pour ces fonctionnalités, que nous avions vues en classe, que nous avons décidé d’utiliser Tkinter : on peut en effet afficher des formes géométriques à l’écran, et les faire bouger, donc réaliser des animations.

On peut donc aussi s’en servir pour tracer des courbes, même si ce n’est pas vraiment adapté à cela, comme peut l’être matplotlib. Ce que Matplotlib fait tout seul, comme par exemple tracer des repères, il faut le faire “à la main” avec Tkinter. Mais essayer de tracer la trajectoire de la chute libre avec Tkinter était l’occasion de nous faire la main sur cette bibliothèque. Cela dit, nous n’avons pas non plus tenté de faire tout ce qu’on avait pu obtenir sans effort avec matplotlib. Il s’agissait plutôt de voir comment utiliser les “canevas” (sorte de toile de fond dans laquelle on place boutons, images, etc.), comment faire réagir des boutons par exemple…
Dans le programme :
https://github.com/ziphra/ISN/blob/master/ChuteLibre/ChuteLibre_tkinterv2.py
nous traçons un repère (mais sans graduation) et un bouton permet de demander de tracer la courbe (les valeurs pour les conditions initiales, la valeur de la constate de gravitation, etc. sont définies dans le programme : on ne peut pas les choisir dans cette version).

La réalisation de ce petit programme a nécessité la mise en place d’une fonction (“ChuteLibre”), avec à l’intérieur une boucle correspondant à l’accroissement du temps d’un petit intervalle de temps dt fixé (comme dans le tracé avec matplotlib, en définitive) : à chaque tour de boucle correspond une valeur de t (égal à n * dt lors de la nième itération), et on calcule les valeurs correspondantes de x et de y. La différence avec matplotlib, c’est que, au lieu de calculer la position de tous les points de la trajectoire, puis de les afficher, on les affiche au fur et à mesure de leur calcul (c’est à dire à l’intérieur de la boucle).
Ne pouvant pas créer de point avec Tkinter, nous avons choisi de tracer un segment de la position (x,y) à (xnew,ynew) (nouvelles valeurs de x et y après un tour de boucle, c’est à dire après le temps dt).

Noter que le repère de la fenêtre, dans Tkinter, n’est pas défini de la manière habituelle en mathématique : l’origine est dans le coin supérieur gauche, et l’axe des y est orienté vers le bas : les valeurs de y augmentent en allant vers le bas (l’axe des x lui est bien orienté vers la droite). Si bien que pour pouvoir avoir une courbe cohérente, nous avons modifié l’équation de la trajectoire (en changeant le signe du terme 1/2 * g * t**2)


Ce premier cap étant franchi, nous avons cherché à faire suivre cette trajectoire à un objet.
Animation d’une bille
Grâce à la bibliothèque Tkinter, nous avons créé une bille dans une fenêtre, et nous lui avons  fait suivre la trajectoire de la chute libre.

Tkinter : principes
Tkinter permet de créer une fenêtre, via l’appel:
fen = Tk()
fenêtre à laquelle on ajoute un “canevas” :
canevas=Canvas(fen, bg=‘gray',height=400,width=700)
sorte de “toile de fond” sur laquelle  on place des objets telles que les images.
On peut ajouter divers types d’objets à la fenêtre, en particulier des boutons, et définir les actions qui sont exécutées quand on clique sur un bouton.
La commande 
fen.mainLoop()
qu’on appelle une fois les éléments de la fenêtre mis en place, est spéciale. Même si elle est (apparemment) la dernière commande du programme, l’exécution continue : elle donne la main à l’utilisateur, dont elle attend les actions (par exemple les clics sur les boutons).
Pour définir ce qui se passe quand on clique sur un bouton, on l’indique lors de la création du bouton, sous forme du nom d’une fonction qui sera appelée quand l’utilisateur clique. Par exemple :
b3=Button(fen,text="Quitter", command=fen.destroy)

Affichage d’une forme géométrique 
Tkinter permet de créer une forme géométrique, de l’afficher dans un canevas.
Par exemple, étant donné un canevas, on crée une bille rouge de rayon 5 pixels en (x,y) par :
bille=canevas.create_oval(x-5, y-5, x+5, y+5, fill=‘red’)
C’est ainsi qu’en créant une bille à sa position à chaque intervalle de temps dt, on peut visualiser la trajectoire et l’accroissement de la vitesse (les billes étant de plus en plus espacées).
Voici l’exemple : https://github.com/ziphra/ISN/blob/master/ChuteLibre/trajectoire.py 




Animation d’une bille 
On peut également sur Tkinter changer la position de la bille en changeant ses coordonnées. C’est ainsi que l’on peut réaliser une animation comme dans : 

https://github.com/ziphra/ISN/blob/master/ChuteLibre/ChuteLibreAnimV1.py

Deux boutons, “Terre” et “Lune”, permettent de lancer l’animation en fixant la valeur correspondante de g, la constante de gravitation intervenant dans l’équation de la trajectoire. Cette constante vaut 9,81 sur Terre, et 1,62 sur la Lune. C’est à cause de la différence de cette valeur, qu’on observe des trajectoires différentes.
Chacun des boutons fixe donc la valeur de g adéquate, puis lance l’animation (fonction “anime”)

Fonctionnement de la fonction anime, 1ère idée
il s’agit d’afficher “en boucle” la bille à la bonne position, que nous calculons grâce aux équations, en fonction du temps.

En suivant ce qu’on a fait pour l’affichage de la trajectoire, on fait varier le temps à partir de t = 0, en augmentant d’un temps dt fixé à chaque fois. La première idée, c’est donc une boucle du genre :
while (t < 60) :
	# coordonnées au temps t
	x = x0+vx0*t
	y = y0+vy0*t+0.5*g*t*t
	# affichage de la bille en (x,y)
  canevas.coords(bille,x-5,y-5,x+5,y+5)
  canevas.update()
	t = t + dt # temps suivant

C’est ce qui a été fait dans 
https://github.com/ziphra/ISN/blob/master/ChuteLibre/ChuteLibreAnimV1.py
Remarque : plutôt que de réaliser l’affichage pendant un certain temps, avec une boucle du type 
while (t < 60) :
on a en fait mis une condition sur y : on boucle, tant que la bille ne sort pas de la fenêtre (400, hauteur de la fenêtre).

Le problème, c’est que l’affichage ne se fait pas au bon rythme (pas en temps réel). En effet, dans la boucle, dès qu’on a affiché la bille à sa position, on augmente la variable t de dt, et on boucle immédiatement. Mais le temps que prend le programme pour effectuer une boucle ne correspond pas au temps dt réel : la chute suit la bonne trajectoire, mais n’est pas à la bonne vitesse.

Synchronisation : utilisation de la méthode after
Tkinter nous fournit un moyen de palier ce problème. La fonction after permet d’attendre un certain temps (en millisecondes) avant de lancer une action. 
Si on néglige le temps que prend effectivement l’affichage de la bille, il suffit d’attendre le temps dt avant de demander l’affichage suivant.
C’est ce qui est fait dans 
https://github.com/ziphra/ISN/blob/master/ChuteLibre/ChuteLibreAnimV2.py
Il faut noter que la fonction “anime” ne contient alors plus de boucle à proprement parler (il n’y a plus le “while”) : c’est le fait d’appeler
fen.after(round(1000*dt),anime)
qui provoque l’affichage suivant de la bille.
On remarque aussi que cet appel n’est pas bloquant : l’exécution du programme se poursuit. En fait, l’appel à after est une sorte de commande à retardement : il indique au système qu’il devra appeler de nouveau «anime()» après un certain temps.

Affichage en temps réel : autre méthode
Mais nous nous sommes rendu compte qu’il y avait un moyen plus simple d’obtenir un affichage en temps réel, au lieu d’essayer d’afficher la bille tous les temps dt, il suffit d’afficher la bille là où elle est doit se trouver en fonction du temps réellement écoulé depuis le lancé.

Ainsi, on est sûr que l'animation se fait à la bonne vitesse, tout en ayant le plus d'affichage possible de la bille (puisque chaque affichage est fait dès que possible. C'est ainsi qu'on peut avoir la meilleure fluidité pour le mouvement.

Cela nécessite d’utiliser la fonction time.time(), qui donne “l’heure système”. On note dans une variable start_time la valeur de time.time() au moment du lancé, et on fait :
time.time() - start_time 
pour obtenir la valeur du temps t pour l’affichage à réaliser.

C’est ainsi que fonctionne :
https://github.com/ziphra/ISN/blob/master/ChuteLibre/ChuteLibreAnimV3.py

C’est la méthode que nous allons retenir pour la suite.

Etape suivante : paysage, échelle, réorganisation du code

Question d’échelle
A l’exécution, la chute semble lente. C’est normal : c’est une question d’échelle de la fenêtre. Un pixel représente 1 m, ce qui donne une chute de 400m : ça prend du temps ! Il faut pouvoir régler l’échelle. Cela passe par la définition d’un rapport d’échelle, et des fonctions pour convertir une dimension en pixels en une dimension en mètres et réciproquement :
convertirMetresEnPixels(xMetre)
convertirPixelsEnMetres(xPixel)


Paysage
Comme l'on souhaitait rendre bien apparent le fait que le mouvement suivi soit sur Terre ou sur la Lune, nous avons voulu mettre une image de fond différente selon le cas. Tkinter permet de mettre une image de fond, et de la changer : on va donc afficher une image différente selon que l’on clique sur le bouton “Terre” ou le bouton “Lune”

La création d’une image de fond se fait ainsi :
photo = PhotoImage(file=“nomFichierImage.gif")
photoOnCanvas = canvas.create_image(0,0,image=photo, anchor=NW)

et ensuite, pour changer l’image affichée, on fait :
photo = PhotoImage(file=“nomAutreImage.gif”)
canvas.itemconfig(photoOnCanvas,image=photo)

Nous avons eu du mal à faire fonctionner ça correctement, parce qu’il arrive que l’image disparaisse au bout d’un certain temps, ou dans certaines circonstances, sans que l’on comprenne bien pourquoi. Google nous a indiqué qu’une solution est de déclarer photo en global ce que nous avons fait.

Réorganisation du code
Afin d'optimiser notre programme, le rendre plus clair et faciliter les changements, nous avons modifié l'allure de notre code. Ainsi, nous obtenons plusieurs fonctions contenant les différentes informations nécessaires à l’exécution de notre fonction principale qui gère l’animation. 

Détermination interactive des conditions initiales
Dans ce qu’on a fait jusqu’à présent, les conditions initiales (position et vitesse au temps t = 0) sont écrites dans le programme : ce sont des variables, mais leurs valeurs ne peuvent être choisies par l’utilisateur.

On peut penser les faire saisir, mais dans l’idée de rendre notre animation plus interactive, nous avons introduit la possibilité de cliquer sur la fenêtre pour indiquer le point de départ de la chute, et de garder le bouton de la souris enfoncé pour déterminer la vitesse initiale.

Cela nécessite de récupérer l’endroit où l’utilisateur clique. Tkinter permet de le faire. Par exemple l’appel :
canvas.bind(“<ButtonPress-1>",mouseButtonDown)
fait que la fonction mouseButtonDown va être appelée quand on clique sur le canevas, et on peut y récupérer les coordonnées du clic
def mouseButtonDown(event):
	# les coordonnées du clic sont données par
  # event.x et event.y
  # (exprimés en pixel, dans le repère de la fenêtre)

https://github.com/ziphra/ISN/blob/master/ChuteLibre/ChuteLibreOnClick.py

Chute avec rebond
Pour faire rebondir la balle, il suffit de changer le sens de sa vitesse selon y lorsqu’elle atteint le base de la fenêtre. Pour ce faire, on relance un appel à anime, avec de nouvelles conditions initiales.
Pour plus de réalisme dans le rendu, on ne fait pas rebondir exactement au bas de la fenêtre, mais un peu au dessus, pour donner l’illusion que la bille est dans le paysage.
 
https://github.com/ziphra/ISN/blob/master/ChuteLibre/ChuteLibreRebond.py

Apollo
Toutes les animations précédentes souffrent d’un manque de réalisme, parce que la balle est mal intégrée au paysage. La question de l’échelle est importante.
On a voulu essayer de faire une animation, sinon plus réaliste, du moins de meilleure qualité.
Nous avons appris que lors d’une des missions Apollo sur la lune (Apollo 15), les Américains ont réalisé, devant une caméra de télévision, l’expérience de la chute libre sur la lune, avec un marteau et une plume, pour montrer qu’ils tombent à la même vitesse.

Nous avons décidé d’intégrer notre bille rouge à cette “expérience” célèbre - la bille allait-elle tomber à la même vitesse ?

Nous avons récupéré les images de la séquence sur internet :

et suivi les explications qui sont données. Ces explications nous ont fourni la solution pour réaliser notre animation : l’idée repose sur le fait que l’on connait le nombre d’images par seconde à la télévision. Cela dépend de la norme utilisée, mais dans le cas d’images américaines de cette époque, il s’agit d’un format appelé NTSC qui compte 29,97 images par secondes. On est donc capable de savoir exactement à quel temps chaque image de la séquence se produit, et la durée totale de la chute, ce qui nous donne sa hauteur. Avec ça, on a les éléments pour calculer où doit se trouver la bille, sur chaque image.

Nous avons donc une boucle de 1 à 36 (le nombre d’images de la séquence). Pour chaque image (donc chaque temps), nous affichons l’image correspondante, nous calculons à quelle hauteur doit se trouver la bille, et nous la traçons sur l’image.

