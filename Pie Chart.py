import matplotlib.pyplot as plt
category=['food','transport','rent','other']
cost=[1000,1400,4000,2500]
plt.pie(cost,labels=category,radius=1.5,autopct='%0.1f%%',explode=[0,0.1,0.2,0])
plt.show()