import numpy as np
import matplotlib.pyplot as plt
x=np.arange(0,1,0.01)
a=1
plt.figure()
y1=a*(1-x)+0.5
plt.plot(x,y1)
plt.plot(x,x*a+0.5)
plt.plot(0.5,y1[np.where(x==0.5)],'o',ms=5)
plt.legend(['var(Xm)','var(Pm)','|r|^2=0.5,var(Xm)=1'],loc ="upper right")
plt.title('Xm Pm Varience')
plt.xlabel('|r|^2')
plt.ylabel('Var')

plt.figure()
y1=x
plt.plot(x,y1)
plt.plot(x,1-x)
plt.plot(0.5,y1[np.where(x==0.5)],'o',ms=5)
plt.legend(['Xin','Pin','|r|^2=0.5,efficiency=0.5'],loc ="upper right")
plt.title('Xin Pin Measurement Efficiency')
plt.xlabel('|r|^2')
plt.ylabel('efficiency')
plt.show()