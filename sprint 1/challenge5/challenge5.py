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


bleu = np.array([0, 50, 100], dtype = np.uint8)
jaune = np.array([240, 255, 60], dtype = np.uint8)
rouge = np.array([200, 20, 50], dtype = np.uint8)
vert = np.array([60, 140, 70], dtype = np.uint8)
blanc = np.array([240, 240, 240], dtype = np.uint8)


seychelles = np.zeros((150, 300, 3), dtype = np.uint8)


I, J = np.meshgrid(\
                    np.arange(150, dtype=np.int64),\
                    np.arange(300, dtype = np.int64),\
                    indexing = 'ij')


seychelles[(I<=150-J*4/3)] = bleu
seychelles[ (I>=150-J*4/3) & (I<=150-J*2/3)] = jaune
seychelles[ (I>=150-J*2/3) & (I<=150-J*1/3)] = rouge
seychelles[ (I>=150-J*1/3) & (I<=150-J*1/6)] = blanc
seychelles[ (I>=150-J*1/6)] = vert


plt.imshow(seychelles)
plt.show()
plt.imsave('drapeau_seychelles.png', seychelles)


# --------------------- TRINIDAD ET TOBAGO ----------------------------------


rouge = np.array([200, 20, 50], dtype = np.uint8)
blanc = np.array([255, 255, 255], dtype = np.uint8)
noir = np.array([0, 0, 0], dtype = np.uint8)


trinidad = np.zeros((300, 500, 3), dtype = np.uint8)


I, J = np.meshgrid(\
                    np.arange(300, dtype=np.int64),\
                    np.arange(500, dtype = np.int64),\
                    indexing = 'ij')


trinidad[ I>=J*6/7 ] = rouge # rouge gauche
trinidad[ I<=J*6/7 ] = blanc # blanc gauche
trinidad[ I*7/6<=J-25 ] = noir
trinidad[ I*7/6<=J-125 ] = blanc # blanc droite
trinidad[ I*7/6<=J-150 ] = rouge # rouge droite


plt.imsave('drapeau_trinidad.png', trinidad)
plt.imshow(trinidad)
plt.show()
