
import matplotlib.pyplot as plt
import numpy as np



cheval1 = plt.imread('chevaux.png', 'PNG') # import dans un tableau numpy

plt.imshow(cheval1)
plt.show()


#♦----------------Inverse------------------------
chevalinverse = cheval1[::-1,:,:]
plt.imshow(chevalinverse)
plt.show()


#-----------------les 4 Chevaux-------------------------

chevauxdouble = np.concatenate((cheval1,cheval1),axis=1)
chevauxdoubleinverse = chevauxdouble[::-1,:,:]

chevaux2=np.concatenate((chevauxdouble,chevauxdoubleinverse),axis=0)


plt.imshow(chevaux2)
plt.show()



