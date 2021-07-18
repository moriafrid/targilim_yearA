import math
from random import random
import cmath
import numpy as np
from scipy.fft import fft, ifft
import matplotlib.pyplot as  plt
from scipy.optimize import curve_fit
from plot import plots, exp,sinc,one_toX
import pickle
from scipy.signal import chirp, find_peaks, peak_widths
from experiment2 import run,run1


if __name__ == '__main__':

    realization_num = 10000
    widths=[]
    #sun,E_earth,inty,intense,detector500,momentum2=run(1000,0,5,1024)
    sun,E_earth,inty,intense,detector500,momentum2=run(50,50,20,1024)
    plots(np.arange(1024),abs(sun),'the sun absoluteb Q2 100 runs')

    file = open("store2.pckl", 'rb')
    sun, E_earth, inty, intense, detector500, momentum2 = pickle.load(file)
    file.close()

    #1
    print("q1")
    plots(np.arange(1024),inty,'the intensity Q2')
    plots(np.arange(1024),abs(sun),'the sun absoluteb Q2')
    plots(np.arange(1024),abs(E_earth)**2,'the E_earth absoluteb Q2')

    #2
    print("q2")
    plt.figure()
    plt.title('Histogram of the intensity Q2')
    plt.xlabel='intensity'
    bin_num = 20
    histy1 = plt.hist(detector500.T, bins=bin_num, density=True)

    #3
    print("q3")
    xdata = np.arange(1024)
    ydata = momentum2 / realization_num
    plots(xdata, ydata, 'The momentum2 g2(n) Q2', xlab='n', ylab='intensity')
#    popt2, pcov = curve_fit(sinc, xdata, ydata, bounds=((0.1, 495, 0.5), (0.3, 505, 1.1)))
#    print('for g2=c+sinc(a(x-b))^2 the fitting is: a=' + str(popt2[0]) + ' ,b=' + str(popt2[1]) + ' ,c=' + str(popt2[2]))
    #plt.plot(xdata, sinc(xdata, *popt2), 'b-', linewidth=3)
    peaks, properties = find_peaks(ydata, prominence=(0.6), width=10, height=(0.6, 3))
    plt.hlines(y=properties["width_heights"], xmin=properties["left_ips"], xmax=properties["right_ips"], color="C1")
    plt.show()