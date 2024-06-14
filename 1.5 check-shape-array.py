#calculating shape

import numpy as np
n1= np.array([[1,2,4,5],[3,5,6,6]])
print(n1.shape)


#changing shape

n1.shape =(4,2)   #n1.reshape(4,2)
print(n1.shape)


#make vector
n1.shape = (8,1)
print(n1)

#also you can check dimentions of the array


import numpy as np
n2= np.array([[1,2,4,5],[3,5,6,6]])
print(n2.ndim)