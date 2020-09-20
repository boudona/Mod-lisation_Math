#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np




cheval1 = plt.imread('chevaux.png', 'PNG') # import dans un tableau numpy
cheval2 = plt.imread('chevaux.png', 'PNG')


chevaux1 = np.concatenate((cheval1,cheval2),axis=0)

plt.imshow(chevaux1)
plt.show()
plt.imsave('doubleHorizontal.png', chevaux1)

chevaux2 = np.concatenate((cheval1,cheval2),axis=1)
plt.imshow(chevaux2)
plt.show()
plt.imsave('doubleVertical.png', chevaux2)

chevaux21 = plt.imread('doubleVertical.png', 'PNG') # import dans un tableau numpy
chevaux22 = plt.imread('doubleVertical.png', 'PNG')

chevaux3 = np.concatenate((chevaux21,chevaux22),axis=0)
plt.imshow(chevaux3)
plt.show()
plt.imsave('quadruple.png', chevaux2)

