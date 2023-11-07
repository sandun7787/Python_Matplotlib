"""import matplotlib .pyplot as plt

plt.plot([1,2,3,4,5,6,7,8],[1,2,3,4,5,6,7,8])
plt.xlabel('X axies')
plt.ylabel('Y axies')
plt.title('first plot')
plt.show()
"""

"""import matplotlib.pyplot as plt
import numpy as np
"""
"""x=[2,3,4,5,6,7,8,9]
plt.plot(x,np.power(x,2),'k^-.',x,np.power(x,3),'c+:')
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.title('show')
plt.show()"""
"""
import matplotlib.pyplot as plt
import numpy as np

plt.plot([1,2,3,4,5,6,7,9],[2,3,4,5,6,7,8,10])
bottom,top=plt.ylim(bottom=2,top=9)
print(bottom)
print(top)
plt.show()

"""

"""import matplotlib.pyplot as plt
import numpy as np

x=np.arange(1,10,0.1)
y1=x
y2=np.sqrt(x)
y3=np.power(x,2)
y4=np.power(x,3)
plt.figure()

plt.subplot(2,2,1)
plt.plot(x,y1,'ro')
plt.title('y1=x')

plt.subplot(2,2,2)
plt.plot(x,y2,'g--')
plt.title('y1=x')

plt.subplot(2,2,3)
plt.plot(x,y3,'b^')
plt.title('$y3=x^2$')
plt.show()

plt.subplot(2,2,4)
plt.plot(x,y4,'ks')
plt.title('$y4=x^3$')
plt.show()"""

