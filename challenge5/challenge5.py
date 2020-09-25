#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt


# ------------------ ENVELOPPE ----------------------------------------------

bleu = np.array([0,0,180], dtype = np.uint8) # initialisation de la couleur bleu
gris = np.array([150, 150, 150], dtype = np.uint8) # initilation de la couleur gris
orange = np.array([250,120,0], dtype = np.uint8) # initialisation de la couleur orange 
vert = np.array([0,150,0], dtype = np.uint8) # initialisation de la couleur vert


lenvel = np.zeros((200, 300, 3), dtype = np.uint8) # création de la matrice sur laquelle nous allons travailler 


I, J = np.meshgrid(\
                    np.arange(200, dtype=np.int64),\
                    np.arange(300, dtype = np.int64),\
                    indexing = 'ij') # on associe à chaque pixel un certain i qui défini sa ligne et un certain j qui défini sa colonne pour pouvoir l'identifier.


lenvel[ (I <= J*2/3) & (I<=200-J*2/3)]  = bleu # on sélectionne le triangle du haut et on le met en bleu 
lenvel[ (I >= J*2/3) &  (I<=200-J*2/3) ] = gris # on sélectionne le triangle de gauche et on le met en gris
lenvel[ (I > J*2/3) &  (I > 200-J*2/3) ] = vert # on sélectionne le triangle du bas et on le met en vert
lenvel[ (I <= J*2/3) & (I > 200-J*2/3) ] = orange # on sélectionne le triangle de droite et on le met en vert


plt.imshow(lenvel)
plt.show()
plt.imsave('lenveloppe.png', lenvel)


# --------------------- SEYCHELLES ------------------------------------------