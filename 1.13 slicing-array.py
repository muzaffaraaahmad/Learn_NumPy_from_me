#slicing is extracing particular set of elements from an array
import numpy as np

n2= np.array([[1,3,4],[33,45,66]])

print(n2[0])  #ist list

print(n2[0][1])  #ist list ka 2nd elemtnt


n3= np.array([[1,3,4],[33,45,66], [313,415,616],[22,33,4]])

#all rows and columns
print(n3)

#first column only
print(n3[:,0:1])