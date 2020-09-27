#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np

t0=plt.imread('tetris_1.png','PNG')
plt.imshow(t0) 
plt.show() 

tgauche=t0[:,0:50] # isole la partie bleu (partie gauche)

tdroite = t0[:,200:300] #isole la partie gauche de l'image (reste le même)


#--------------------constructieu millieu etape2----------------------------------

tgris=t0[0:50,100:250] #fond gris qui sera au-dessus du bloc orange


thog1=t0[50:100,50:150] #construction du haut du bloc oronge retourner (1/3)
thog2=t0[50:100,50:100] #construction du haut du bloc orange retourner (2/3)
thog=np.concatenate((thog1,thog2),axis=1)#haut du bloc retourner (3/3)


tbog1=t0[150:200,50:100] #construction du bas du bloc oronge retourner (1/3)
tbog2=t0[100:150,50:150]#construction du bas du bloc oronge retourner (2/3)
tbog=np.concatenate((tbog1,tbog2),axis=1) #bas du bloc retourner(3/3)

torange= np.concatenate((thog,tbog),axis=0) #bloc orange assembler

tfondbas1 = t0[150:200,50:200] #construction du fond en bas du bloc orange (etape2)

tmillieu1=np.concatenate((np.concatenate((tgris,torange),axis=0),tfondbas1),axis=0)

#--------------------construction millieu l'étape 3-------------------------------

t2bog2=t0[150:200,150:200] #construction du bas du bloc oronge (1/3)
t2bog1=tbog2[:,::-1] #construction du bas du bloc oronge (2/3)
t2bog=np.concatenate((t2bog1,t2bog2),axis=1) #bas du bloc oronge (3/3)

torange2=np.concatenate((thog,t2bog),axis=0) #bloc orange (le bloc a le meme haut)


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





