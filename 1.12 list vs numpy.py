""" 

numpy array is best than list bz of three reasons
      1. Less Mempry
      2. Fast 
      3. Convient


      """

#proving point-1. Less Mempry

import numpy as np
import time
import sys

l=list(range(100))

print("The total memmory occupaid by list : ",sys.getsizeof(l)*len(l))  #memory of one element * total elements

n= np.arange(100)
print("The total memmory occupaid by array : ",n.size*n.itemsize) 





#proving point-2. fast

size =10000000000

l1= list(range(size))
l2= list(range(size))


n1= np.arange(size)
n2= np.arange(size)

#addition of two lists
start = time.time()
result=[(x,y) for x,y in zip(l1,l2)]
print("Time taken by list", time.time()-start*1000) #miliseconds



#addition of two array
start = time.time()
result= n1+n2
print("Time taken by array", time.time()-start*1000)