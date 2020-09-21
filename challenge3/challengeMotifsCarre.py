#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np

#créer C1 pour l'utiliser 

#piste de réflexion : base=np.zeros((100,100,3))
#                       base[75:,75:,:]=vert



#==> Ceci interdit
C1 = plt.imread('C1.png', 'PNG') # import dans un tableau numpy
C1FlipAbcisse = np.flip((C1),axis=0) 

C2MoitieGauche = np.concatenate((C1,C1FlipAbcisse),axis=0)
C2MoitieDroite = np.flip((C2MoitieGauche),axis=1)
C2 = np.concatenate((C2MoitieGauche,C2MoitieDroite),axis=1)

plt.imshow(C2)
plt.show()
plt.imsave('C2.png', C2)

C31 = np.concatenate((C2,C2),axis=0)
C32 = np.concatenate((C31,C31),axis=1)
C3 = np.concatenate((C32,C31),axis=1)

plt.imshow(C3)
plt.show()
plt.imsave('C3.png', C3)