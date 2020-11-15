 #!/usr/bin/env python2
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt



# ------------------ demi-cercle ----------------------------------------------

# definition des couleurs utilisées, codées en R, V, B
rouge = np.array([188, 0, 60], dtype = np.uint8)

# Création de l'image avec un fond blanc
demicercle = np.ones((200, 200, 3), dtype = np.uint8) * 255

# rayon du cercle 
r = 60

# Création de la grille des pixels
x = np.linspace(-0, 60, 200)
y = np.linspace(60, -0, 200)
X, Y  = np.meshgrid(x,y, indexing = 'xy')




# affectation de la zone

demicercle[ (X*X+Y*Y) <= (r*r) , :] = rouge

#probleme
#demicercle[ (X*X+Y*Y) <= (r*r) & ((X*X) >= (r*r)) , :] = rouge


# affichage
plt.imshow(demicercle)
plt.show()


# ------------------ Donut ----------------------------------------------

# definition des couleurs utilisées, codées en R, V, B
rouge = np.array([188, 0, 60], dtype = np.uint8)
blanc = np.array([255, 255, 255], dtype = np.uint8)
# Création de l'image avec un fond blanc
donut = np.ones((200, 200, 3), dtype = np.uint8) * 255

# rayon du cercle 
r =60

# Création de la partie exterieur du cercle rouge
xrouge = np.linspace(-60, 60, 200)
yrouge = np.linspace(60, -60, 200)
Xrouge, Yrouge  = np.meshgrid(xrouge,yrouge, indexing = 'xy')

# Création de la partie interieur du cercle rouge
xblanc = np.linspace(-125, 125, 200)
yblanc = np.linspace(125, -125, 200)
Xblanc, Yblanc  = np.meshgrid(xblanc,yblanc, indexing = 'xy')

# affectation de la zone

#         plus petit que le rouge                             plus grand que le blanc
donut[ ( (Xrouge*Xrouge+Yrouge*Yrouge) <= (r*r)  ) & ( (Xblanc*Xblanc+Yblanc*Yblanc) > (r*r) ), :] = rouge

#xb = np.linspace(-100, 100, 200)
#yb = np.linspace(100, -100, 200)
#Xb, Yb  = np.meshgrid(xb,yb, indexing = 'xy')
#japon[ (Xb*Xb+Yb*Yb) <= (r*r) , :] = blanc


# affichage
plt.imshow(donut)
plt.show()


# ------------------ Double Donut ----------------------------------------

# on travaille sur un repère orthonormé (en bas gauche)


rouge = np.array([188, 0, 60], dtype = np.uint8)
blanc = np.array([255, 255, 255], dtype = np.uint8)
noir = np.array([0,0,0], dtype = np.uint8)
# Création de l'image avec un fond blanc
DoubleDonut = np.ones((400, 600, 3), dtype = np.uint8) * 255


x = np.linspace(0, 6, 600)
y = np.linspace(4, 0, 400)
X, Y  = np.meshgrid(x,y, indexing = 'xy')


rG =2
rP=1


DoubleDonut[ ( (X-2)*(X-2)+(Y-2)*(Y-2) > (rP*rP)  ) & ( (X-2)*(X-2)+(Y-2)*(Y-2) < (rG*rG) ), :] = rouge
DoubleDonut[ ( (X-4)*(X-4)+(Y-2)*(Y-2) > (rP*rP)  ) & ( (X-4)*(X-4)+(Y-2)*(Y-2) < (rG*rG) ), :] = noir
DoubleDonut[ ( (X-4)*(X-4)+(Y-2)*(Y-2) > (rP*rP)  ) & ( (X-4)*(X-4)+(Y-2)*(Y-2) < (rG*rG) ) & ((X-2)*(X-2)+(Y-2)*(Y-2) > (rP*rP)  ) & ( (X-2)*(X-2)+(Y-2)*(Y-2) < (rG*rG) ) & (Y>2), :] = rouge



plt.imshow(DoubleDonut)
plt.show()