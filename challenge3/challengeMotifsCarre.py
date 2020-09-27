#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np

#créer C1 pour l'utiliser 

vert = (0,120,0)
orange = (255,120,0)

#------------------------
l, h = (20, 20)
carorange = orange * np.ones((h, l, 3), dtype = np.uint8)
carorange[15:, 15:,:] = vert
plt.imshow(carorange)
plt.show()
plt.imsave('C1.png', carorange)

#------------------------
# Solution de Paulin

l, h = (40, 40)
carorange = orange * np.ones((h, l,3), dtype = np.uint8)
carorange[15:25, 15:25,:] = vert


# Solution d'Arthur
#test1 =  np.concatenate((carorange,carorange[:,::-1,:]),axis=1)
#test2 = np.concatenate((carorange[::-1,:,:],carorange[::-1,::-1,:]),axis=1)
#carorange = np.concatenate((test1,test2),axis=0)

plt.imshow(carorange)
plt.show()
plt.imsave('C2.png', carorange)

#------------------------
carorange2 = np.concatenate((carorange,carorange),axis=0)
carorange3 = np.concatenate((carorange2,carorange2),axis=1)
carorangeFini = np.concatenate((carorange3,carorange2),axis=1)
plt.imshow(carorangeFini)
plt.show()
plt.imsave('C3.png', carorangeFini)
