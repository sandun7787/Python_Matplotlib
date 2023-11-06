"""print(numpy.__version__)"""
import numpy as np

"""x=np.array([1,2,3,4,5,6])
print(x)"""

n=np.array([1,2,3,4,5,6,7,8,9],ndmin=9)
print(n)
print(n.ndim)

y=np.array([[[1,2],[3,4]],[[7,8],[9,10]]],)
print(y[1,0,1])




