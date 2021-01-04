# -*- coding: utf-8 -*-


import numpy as np
import matplotlib.pyplot as plt
from scipy import *

imageDeBase = plt.imread('face.png', 'PNG')
plt.imshow(imageDeBase) 
plt.show()

translation2 = np.zeros((768, 1024, 3), dtype = np.uint8)
ratio = np.sqrt(2)
print 
for i in range(768):
    for y in range(1024):
        if((y*ratio<1024) and (i*ratio<768)):
            translation2[int(i/ratio)][int(y/ratio)]=imageDeBase[767-i][y]
            
inverse = translation2[::-1,:,:]


plt.imshow(inverse) 
plt.show()

##########################################################

translation2 = np.zeros((768, 1024, 3), dtype = np.uint8)
ratio = np.pi/6
for i in range(768):
    for y in range(1024):
        
            translation2[int(ratio*i)][y]=imageDeBase[i][y]
            
        
plt.imshow(translation2) 
plt.show()