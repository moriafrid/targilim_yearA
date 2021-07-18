import numpy as np
from scipy.fft import fft, ifft
import pickle
import math
import random
import cmath
from plot import plots
import matplotlib.pyplot as  plt

def run(realization_num,mu,sigma, size):
    intense = []
    detector500_2 = []
    sun=[]
    sun = np.zeros(1024, dtype=np.complex)
    Wrange=np.linspace(mu+4*sigma,mu-4*sigma,size)
    w0=30
    E = {}
    for r in np.arange(realization_num):
        i=0
        print('run is: '+str(r))
        for wi in Wrange:
            theta=np.random.uniform(0,2*math.pi)
            sun[480+i]=1/(np.sqrt(2*np.pi*(sigma**2)))*np.exp(-((wi-w0)**2)/(2*sigma**2))*cmath.exp(complex(0,theta))
            i+=1
            #sun[i]=random.gauss(mu,sigma)*cmath.exp(complex(0,theta))
#        plots(np.arange(size),abs(sun ),'random gauss')
 #       data = list(E.values())
 #       sun = np.array(data)
        E_earth = fft(sun)
        inty = (E_earth * E_earth.conj()).real
        intense = np.append(intense, inty)
        decty500_2 = (E_earth[500] * E_earth[500].conj()).real
        detector500_2 = np.append(detector500_2, decty500_2)

    intense = intense.reshape(realization_num, 1024)
    detector500_2 = np.expand_dims(detector500_2, axis=0)
    momentum2_2 = ((np.matmul(detector500_2, intense)).mean(0)) / (intense.mean(0) * intense.mean(0))
    return sun, E_earth, inty, intense, detector500_2, momentum2_2


def run1(realization_num,mu,sigma, size):
    intense = []
    detector500_2 = []

    sun = np.zeros(1024, dtype=np.complex)
    sun1 = np.zeros(1024, dtype=np.complex)

    for r in np.arange(realization_num):
        print('run is: '+str(r))
        for i in np.arange(size):
            theta=np.random.uniform(0,2*math.pi)
            sun[480+i]=random.gauss(mu,sigma)*cmath.exp(complex(0,theta))
            sun1[480+i]=random.gauss(mu,sigma)

        E_earth = fft(sun)
        inty = (E_earth * E_earth.conj()).real
        intense = np.append(intense, inty)
        decty500_2 = (E_earth[500] * E_earth[500].conj()).real
        detector500_2 = np.append(detector500_2, decty500_2)

    intense = intense.reshape(realization_num, 1024)
    detector500_2 = np.expand_dims(detector500_2, axis=0)
    momentum2_2 = ((np.matmul(detector500_2, intense)).mean(0)) / (intense.mean(0) * intense.mean(0))
    return sun1, E_earth, inty, intense, detector500_2, momentum2_2

if __name__ == '__main__':
    sun,E_earth,inty,intense,detector500_2,momentum2=run(10000,100,5,1024)
    f = open('store2.pckl', 'wb')
    pickle.dump([sun, E_earth, inty, intense, detector500_2, momentum2], f)
    f.close()