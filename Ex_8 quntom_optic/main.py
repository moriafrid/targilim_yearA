from numpy import cos,sin, cosh,sinh,pi,exp,sqrt
import numpy as np
import matplotlib.pyplot as plt
import cmath
r=1
theta=np.arange(0,2*pi,0.1)
deltaX2=0.5*(cosh(r)**2+sinh(r)**2-cos(theta)*sinh(2*r))
deltaP2=0.5*(cosh(r)**2+sinh(r)**2+cos(theta)*sinh(2*r))
theta0=[0,0.5*exp(-2*r)]
theta_pi=[pi,0.5*exp(2*r)]
theta_2pi=[2*pi,exp(-2*r)]

plt.figure()
plt.title('deltaX^2 Q1')
plt.plot(theta,deltaX2,'.')
plt.plot(0,0.5*exp(-2*r),'ro')
plt.plot(pi,0.5*exp(2*r),'bo')
plt.plot(2*pi,0.5*exp(-2*r),'ro')
plt.legend(['deltaX^2','0.5*exp(-2*r)','0.5*exp(2*r)','0.5*exp(-2*r)'])

deltaX2=0.5*(cosh(r)**2+sinh(r)**2-cos(theta)*sinh(2*r)+0.5)
deltaP2=0.5*(cosh(r)**2+sinh(r)**2+cos(theta)*sinh(2*r)+0.5)
plt.figure()
plt.title('deltaX^2 AND deltaP^2 Q2')
plt.plot(theta,deltaX2,'.')
plt.plot(theta,deltaP2,'.')
plt.plot([0,0],[0.5*exp(-2*r),0.5*exp(-2*r)+0.5],'ro')
plt.plot([pi,pi],[0.5*exp(2*r),0.5*exp(2*r)+0.5],'bo')
plt.plot([2*pi,2*pi],[0.5*exp(-2*r),0.5*exp(-2*r)+0.5],'ro')
plt.legend(['deltaX^2','deltaP^2','0.5*exp(-2*r)'+u"\u00B1"+'0.5','0.5*exp(2*r)'+u"\u00B1"+'0.5','0.5*exp(-2*r)'+u"\u00B1"+'0.5'],loc='upper right')

N=0.5
b=[]
for a in theta: b.append(complex(cmath.cos(a),-cmath.sin(a)*(1-2*N)) )
deltaX2=sqrt(N*(1-N))*cosh(2*r)-0.5*sinh(2*r)*np.array(b)
deltaP2=sqrt(N*(1-N))*cosh(2*r)+0.5*sinh(2*r)*np.array(b)
plt.figure()
plt.title('not ideal beam splite Q3')
plt.plot(theta,deltaX2,'.')
#plt.plot(theta,deltaP2,'.')
plt.plot(0,(1-N)*exp(-2*r),'ro')
plt.plot(pi,N*exp(2*r),'bo')
plt.plot(2*pi,(1-N)*exp(-2*r),'ro')
plt.legend(['deltaX^2','0.5*exp(-2*r)','0.5*exp(2*r)','0.5*exp(-2*r)'],loc='upper right')
plt.show()
a=1

