import numpy as np
n1= np.array([1,2,4,5,60])
n2= np.array([50,80,99,50,1])


#intersect
n3 =np.intersect1d(n1,n2)
print(n3)



#intersect
n4 =np.setdiff1d(n1,n2)
print(n4)