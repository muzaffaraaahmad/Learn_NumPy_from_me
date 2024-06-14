import numpy as np

n3= np.array([[1,3,4],[33,45,66], [313,415,616],[22,33,4]])

#all rows and columns
print(n3)



print(50*"-")


#first column only
print(n3[:,0:1])


print(50*"-")


#first column as in row
print(n3[:,0])


print(50*"-")

#last column as in row
print(n3[:,-1])

print(50*"-")



#last column of first two rows
print(n3[0:2,-1])
