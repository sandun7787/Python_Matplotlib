"""from array import *

x=array('i'[1,2,-3,4,5,6,7,8])
print(x)
x.extend([2,3,4,5,6,8])
x.insert(2,7)
x.pop(8)
x.remove(-3)
print(x[1:3]

      for i in range(len(5)):
"""


"""list ={1,2,3,4,5,6,7}
iter = iter(list)

while True:
    try:
    print(next(iter))
    except StopIteration:
    break
"""

class iter:
    def __init__(self):
        self.y=2

    def __iter__(self):
        return self

    def __next__(self, val=None):
        value=self.y
        self.y+=2
        return val

    myobj = iter()
    iter=iter(myobj)
    print(next(iter))




