# we can join two numoy array by vstack() and hstack() and column_stack()

#vstack: verticllay stack
import numpy as np
n1= np.array([1,2,4,5])
n2= np.array([50,80,99,50])
n3 =np.vstack((n1,n2))
print(n3)



#hstack: horizonatally stack
import numpy as np
n4= np.array([1,2,4,5])
n5= np.array([50,80,99,50])
n6 =np.hstack((n4,n5))
print(n6)

#hstack: column stack
import numpy as np
n7= np.array([1,2,4,5])
n8= np.array([50,80,99,50])
n9 =np.column_stack((n7,n8))
print(n9)