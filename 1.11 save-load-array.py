import numpy as np

#saving numpy array
n1= np.array([1,2,4,5,60])
np.save("my_numpy_array",n1)



#loading numpy array
s=np.load("my_numpy_array.npy")
print(s)