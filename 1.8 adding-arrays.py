import numpy as np
n1= np.array([1,2,4,5,60])
n2= np.array([50,80,99,50,1])


#total sum numbers
n3 =np.sum([n1,n2])
print(n3)



# #column wise addition
n4 =np.sum([n1,n2], axis =0)
print(n4)



# row wise addition
n5 =np.sum([n1,n2], axis =1)
print(n5)