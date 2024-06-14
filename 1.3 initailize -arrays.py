import numpy as np

#initalize an array of 1 row and 2 colums of zeroes

#syntax : np.zeros((r,c)) #r=row and c=column

n1= np.zeros((1,2))
print(n1)


#initalize an array of 5 cross 5 of zeroes
n2= np.zeros((5,5))
print(n2)



#initalize an array of 5 cross 5  of specifice number

#syntax : np.full((r,c),s) #s=specific no.

n3= np.full((2,2),5)
print(n3)



#initalize numpy array within a range

n4= np.arange(10,20)
print(n4)


#initalize numpy array within a range with step size=5

n5= np.arange(10,60,5)
print(n5)