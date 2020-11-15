#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np


bleu = np.array([0,0,180], dtype = np.uint8) # initialisation de la couleur bleu
gris = np.array([150, 150, 150], dtype = np.uint8) # initilation de la couleur gris
orange = np.array([250,120,0], dtype = np.uint8) # initialisation de la couleur orange 
vert = np.array([0,150,0], dtype = np.uint8) # initialisation de la couleur vert


t0 = np.zeros((200, 300, 3), dtype = np.uint8) # création de la matrice sur laquelle nous allons travailler 

t0[:,:]= gris #selection de toute les lignes et colonnes de la matrice et le met en gris (fond du tetris)
t0[:,0:50] = bleu 
t0[0:150,50:100] = orange
t0[50:100,100:150] = orange
t0[100:150,200:300] = vert
t0[150:200,150:250] = vert
plt.imshow(t0) 
plt.show()
plt.imsave('tetris_1.png', t0)

 
#stratégie: division de la matrice en 3 partie, modification du millieu de la matrice, puis concaténation de matrice


tgauche=t0[:,0:50] # isole la partie bleu (partie gauche)

tdroite = t0[:,200:300] #isole la partie droite de l'image (reste le même)


#--------------------constructieu bloc orange etape2----------------------------------

tgris=t0[0:50,100:250] #fond gris qui sera au-dessus du bloc orange


hautBlocOrange1=t0[50:100,50:150] #construction du haut du bloc oronge retourner (1/3)
hautBlocOrange2=t0[50:100,50:100] #construction du haut du bloc orange retourner (2/3)
hautBlocOrange=np.concatenate((hautBlocOrange1,hautBlocOrange2),axis=1)#haut du bloc retourner (3/3)


basBlocOrange1=t0[150:200,50:100] #construction du bas du bloc oronge retourner (1/3)
basBlocOrange2=t0[100:150,50:150]#construction du bas du bloc oronge retourner (2/3)
basBlocOrange=np.concatenate((basBlocOrange1,basBlocOrange2),axis=1) #bas du bloc retourner(3/3)

torange= np.concatenate((hautBlocOrange,basBlocOrange),axis=0) #bloc orange assembler

tfondbas1 = t0[150:200,50:200] #construction du fond en bas du bloc orange (etape2)

tmillieu1=np.concatenate((np.concatenate((tgris,torange),axis=0),tfondbas1),axis=0)

#--------------------construction bloc orange l'étape 3-------------------------------

basBlocOrangeVert2=t0[150:200,150:200] #construction du bas du bloc oronge (1/3)
basBlocOrangeVert1=basBlocOrange2[:,::-1] #construction du bas du bloc oronge (2/3)
basBlocOrangeVert=np.concatenate((basBlocOrangeVert1,basBlocOrangeVert2),axis=1) #bas du bloc oronge (3/3)

torange2=np.concatenate((hautBlocOrange,basBlocOrangeVert),axis=0) #bloc orange (le bloc a le meme haut)


tmillieu2=np.concatenate((np.concatenate((tgris,tgris),axis=0),torange2),axis=0)
#millieu de l'étape 3

#-------------------------------------------------------------------------------

#----assemblages des parties----

tetris1 = np.concatenate((np.concatenate((tgauche,tmillieu1),axis=1),tdroite),axis=1)
plt.imshow(tetris1) 
plt.show()
plt.imsave('Etape2.png', tetris1)

tetris2 = np.concatenate((np.concatenate((tgauche,tmillieu2),axis=1),tdroite),axis=1)
plt.imshow(tetris2) 
plt.show()
plt.imsave('Etape3.png', tetris2)





