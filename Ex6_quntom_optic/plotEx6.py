import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

def fit2(x,a,c):
    return c-a**2/(a+x)**2

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
#X=x
plt.plot(X,Y,'.', linewidth=3)

popt2, pcov = curve_fit(fit2, X, Y,bounds=((0, 0), (6, 1.1)))
print('for c-a^2/(a+x)^2 a=' + str(popt2[0]) +' ,c=' + str(popt2[1]) )
plt.plot(X, fit2(X, *popt2), '-', linewidth=3)
plt.title('g2 for targil 6')
plt.xlabel('NW')
plt.ylabel('corelatoin_chance')
plt.show()
a=1