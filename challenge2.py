
import matplotlib.pyplot as plt
import numpy as np



cheval1 = plt.imread('chevaux.png', 'PNG') # import dans un tableau numpy

chevaux1 = np.flip((cheval1),axis=0)


plt.imshow(chevaux1)
plt.show()
plt.imsave('simpleflip.png', chevaux1)



cheval2 = plt.imread('doubleVertical.png', 'PNG') # import dans un tableau numpy

chevaux2 = np.flip((cheval2),axis=0)


plt.imshow(chevaux2)
plt.show()
plt.imsave('doubleflip.png', chevaux2)


cheval3 = plt.imread('doubleflip.png', 'PNG') # import dans un tableau numpy

chevaux3 = np.concatenate((cheval2,cheval3),axis=0)


plt.imshow(chevaux3)
plt.show()
plt.imsave('doubleflip.png', chevaux3)


#plt.imsave('retourner.png', chevaux1)


