import math
import random
import cmath
import numpy as np
from scipy.fft import fft, ifft
import matplotlib.pyplot as  plt
from scipy.optimize import curve_fit
import pickle
from scipy.optimize import curve_fit
from scipy.signal import chirp, find_peaks, peak_widths
from plot import plots, exp, sinc, one_toX

# run over r experiments
def run(realization_num,size):
    intense = []
    detector500_2 = []
    sun = np.zeros(1024, dtype=complex)
    for r in np.arange(realization_num):
        # creat random realization for th esun vector
        for i in np.arange(480,480+size):
            theta=np.random.uniform(0,2*math.pi)
            sun[i]=cmath.exp(complex(0,theta))
        # calculation of the electric field
        E_earth=fft(sun)
        # calculation of the intensity on earth
        inty= (E_earth * E_earth.conj()).real
        intense=np.append(intense,inty)
        # the detector on place 500
        decty500_2= (E_earth[500] * E_earth[500].conj()).real
        detector500_2=np.append(detector500_2,decty500_2)

    intense=intense.reshape(realization_num,1024)
    detector500_2=np.expand_dims(detector500_2, axis=0)
    momentum2_2=((np.matmul(detector500_2,intense)).mean(0))/(intense.mean(0)*intense.mean(0))
    return sun,E_earth,inty,intense,detector500_2,momentum2_2


def run_diffrent_sun_mass(new_realization_num,sun_mass):
    widths = []
    for i in sun_mass:
        sun, E_earth, inty, intense, detector500_2, momentum24 = run(new_realization_num, i)
        xdata = np.arange(1024)
        ydata = momentum24 / new_realization_num
        #plots(xdata, ydata, 'The momentum 2 g2(n) plot2 run '+str(i), xlab='n', ylab='intensity')
        popt, pcov = curve_fit(sinc, xdata, ydata, bounds=((0.01, 495, 0.9), (0.05, 505, 1.1)))
        peaks, properties = find_peaks(ydata, prominence=0.5)
        width, width_heights, left_ips, right_ips = peak_widths(ydata, peaks, rel_height=0.5)
        widths=np.append(widths,width)
    return widths





def run5(realization_num,sun_mass):
    intense = []
    detector500_2 = []
    mean_intense=[]
    mean_detector500=[]
    sun = np.zeros(1024, dtype=complex)
    for r in np.arange(realization_num):
        for i in np.arange(480,520):
            theta=np.random.uniform(0,2*math.pi)
            sun[i]=cmath.exp(complex(0,theta))

        E_earth=fft(sun)
        inty= (E_earth * E_earth.conj()).real
        intense=np.append(intense,inty)
        decty500_2= (E_earth[500] * E_earth[500].conj()).real
        detector500_2=np.append(detector500_2,decty500_2)
        if (r+1)%10==0 and r>0:
            mean_intense=np.append(mean_intense,np.mean(intense.reshape(10,1024),0))
            intense=[]
            mean_detector500=np.append(mean_detector500,np.mean(detector500_2))
            detector500_2=[]

    intense=mean_intense.reshape(realization_num//10,1024)
    detector500_2=np.expand_dims(mean_detector500, axis=0)
    momentum2=((np.matmul(detector500_2,intense)).mean(0))/(intense.mean(0)*intense.mean(0))
    return sun,E_earth,inty,intense,detector500_2,momentum2

if __name__ == '__main__':
    sun,E_earth,inty,intense,detector500_2,momentum2=run(10000,40)
    f = open('store.pckl', 'wb')
    pickle.dump([sun, E_earth, inty, intense, detector500_2, momentum2], f)
    f.close()

