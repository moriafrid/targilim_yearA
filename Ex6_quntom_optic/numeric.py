import numpy as np
import random
import matplotlib.pyplot as plt
realization_nam=10000
NW=(np.array([111,158,180,201,234,321,490,635,810,1014,1500,1800,2000,3000])-111)/700
realization_vec=np.arange(realization_nam)

g2 = []
g22=[]
g23=[]
for lambde in NW:
    ex_photon = []
    ats = []
    ars = []
    for i in realization_vec:
        print(i)
        at=0
        ar=0
       # photons=1+epsilon
        epsilon = np.random.poisson(lam=lambde)
        ex_photon.append(epsilon)
        for pothon in np.arange(epsilon): #number of photon that pass the gate
            coin = random.randint(1, 2)
            if coin==1:
                at+=1
                as2=1
            else:
                ar+=1
                ar2=1
        ats=np.append(ats,at)
        ars=np.append(ars,ar)


    maxepsilon=np.max(ex_photon)
    #ydata=[]
    #ars_True=(ars>0)
    #ats_True=(ats>0)
    index=np.where(ars==ats)
    index_True=np.where(ars[index]>0)
    #index=np.where(ars==True)
    #a=(ars_True[index]==ats_True[index])
    b = np.shape(np.where((np.array(ex_photon) > 0) == True))[1]
    if b==0:
        b=1
    #aqual=np.shape(np.where(a==True))[1]
    aqual=np.shape(index_True)[1]
    g22.append(aqual/b)
    mechane=np.mean(abs(ars)) * np.mean(abs(ats))
    if mechane==0:
        mechane=1
    g23.append((np.mean(abs(ars) * abs(ats))) / mechane)

plt.figure()
plt.title('numeric correlation g22')
plt.ylabel('g2')
plt.xlabel('NW')
plt.plot(NW,g22,'.',)

plt.figure()
plt.title('numeric correlation g23')
plt.ylabel('g2')
plt.xlabel('NW')
plt.plot(NW,g23,'.')
plt.show()
a=1
