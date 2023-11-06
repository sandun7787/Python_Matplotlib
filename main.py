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

import matplotlib.pyplot as plt
import numpy as np

plt.plot([1,2,3,4,5,6,7,9],[2,3,4,5,6,7,8,10])
bottom,top=plt.ylim(bottom=2,top=9)
print(bottom)
print(top)
plt.show()

