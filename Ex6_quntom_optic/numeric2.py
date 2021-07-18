import numpy as np
import random
import matplotlib.pyplot as plt
from numpy import random as randy
from scipy.optimize import curve_fit

#fitting function
def fit2(x,a,c):
    return c-a**2/(a+x)**2
plt.figure()
plt.title('g2 for targil 6')
plt.xlabel('NW')
plt.ylabel('corelatoin_chance')

#convert point to data
x=np.array([158,201,234,321,490,635,810,1014])
y=np.array([539,507,479,431,368,333,303,289])
#find the 0,0 axis and correct by this all the dots
x0=111
y0=590
y=y0-y
x=x-x0
#use the pixal size to correct x'y
pixalX=1/700
pixalY=2.63e-3
X=x*pixalX
Y=y*pixalY
#data plot
plt.plot(X,Y,'+', markersize=10)

#add some point
NW=(np.array([111,146,158,180,201,234,321,490,635,810,1014,1500,1800])-111)/700

#fitting to theory
popt2, pcov = curve_fit(fit2, X, Y,bounds=((0, 0), (6, 1.1)))
print('for c-a^2/(a+x)^2 a=' + str(popt2[0]) +' ,c=' + str(popt2[1]) )
plt.plot(NW, fit2(NW, *popt2), 'b-', linewidth=1)

#numeric
realization_nam=100
NW=(np.array([111,146,158,180,201,234,321,490,635,810,1014,1500,1800])-111)/700
realization_vec=np.arange(realization_nam)
g2 = []
for lambde in NW:
    ex_photon = []
    ats = []
    ars = []
    for i in realization_vec:
        print(i)
        at=0
        ar=0
        epsilon = 1+np.random.poisson(lambde)
        ex_photon.append(epsilon)
        for pothon in np.arange(epsilon): #number of photon that pass the gate
            coin = random.randint(1, 2)
            if coin==1:
                at+=1
            else:
                ar+=1
        ats=np.append(ats,at)
        ars=np.append(ars,ar)

    mechane=np.mean(abs(ars)) * np.mean(abs(ats))
    print(mechane)
    g2.append((np.mean(abs(ars) * abs(ats))) / mechane)
plt.plot(NW,g2,'.', color='red',markersize=4)
plt.legend(['data','theory','numeric'])
plt.show()
a=1
