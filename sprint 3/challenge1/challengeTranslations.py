# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 12:07:52 2020

@author: Daniel
"""


import numpy as np
import matplotlib.pyplot as plt
from scipy import *

imageDeBase = plt.imread('face.png', 'PNG')
plt.imshow(imageDeBase) 
plt.show()

#########################################################

translation1 = np.zeros((768, 1024,3), dtype = np.uint8)
x = 149
y = 149

for i in range(768):  
    for o in range(1024):  
        if(o+150<1024 and i-150>0):
            translation1[i-150][o+150]=imageDeBase[i][o]    
plt.imshow(translation1) 
plt.imsave('translation1.png', translation1)
plt.show()


###################################################

translation2 = np.zeros((768, 1024, 3), dtype = np.uint8)
for i in range(768):
    for y in range(1024):
        if(y+300<1024 and i-150>0):
            translation2[i-150][y+300]=imageDeBase[i][y]
       
plt.imshow(translation2) 
plt.imsave('translation2.png', translation2)
plt.show()

######################################################

translation3 = np.zeros((768, 1024, 3), dtype = np.uint8)
for i in range(768):
    for y in range(1024):
        if(y+300<1024 and i-150>0):
            translation3[i][y]=imageDeBase[i-150][y+300]
plt.imshow(translation3) 
plt.imsave('translation3.png', translation3)
plt.show()

##########################################################
