import math
from random import random
import cmath
import numpy as np
from scipy.fft import fft, ifft
import matplotlib.pyplot as  plt
from scipy.optimize import curve_fit
from experiment import run, run_diffrent_sun_mass, run5
from plot import plots, exp,sinc,one_toX
import pickle
from scipy.signal import chirp, find_peaks, peak_widths

def calculate_xdata(band_width,bin_num):
    bin_edges = band_width
    width= (band_width[-1] - band_width[0]) / (bin_num)
    x_data = (np.arange( bin_num))*width + width/2
    return x_data

if __name__ == '__main__':
    realization_num = 10000
    widths=[]
    #sun,E_earth,inty,intense,detector500_2,momentum2=run(realization_num,40)
    file = open("store.pckl", 'rb')
    sun, E_earth, inty, intense, detector500_2, momentum2 = pickle.load(file)
    file.close()
    #1
    print("q1")
    # plots of the sun vector and earth intensity
    plots(np.arange(1024),abs(sun),'the sun  absolute')
    plots(np.arange(1024),inty,'the intensity')
    #2
    print("q2")
    # plots of the histogram of earth intensity
    plt.figure()
    plt.title('Histogram of the intensity')
    plt.xlabel='intensity'
    bin_num = 20
    histy1 = plt.hist(detector500_2.T, bins=bin_num, density=True)
    xdata = calculate_xdata(histy1[1], bin_num)
    #fit the histogram to exponent
    popt, pcov = curve_fit(exp, xdata, histy1[0], bounds=((0.018, 20), (0.04, 41)))
    print('the fitting: A*exp(-x/N0) A='+str(popt[0]) +' ,N0='+str(popt[1]))
    plt.plot(xdata, exp(xdata, *popt), 'b-', linewidth=3)
    plt.savefig('Histogram of the intensity.png')

    #3
    print("q3")
    #plot g2 function
    xdata = np.arange(1024)
    ydata = momentum2 / realization_num
    plots(xdata, ydata, 'The momentum2 g2(n)', xlab='n', ylab='intensity')
    #fit g2 to 1+sinc^2
    popt2, pcov = curve_fit(sinc, xdata, ydata, bounds=((0.01, 495, 0.9), (0.05, 505, 1.1)))
    print('for g2=c+sinc(a(x-b))^2 the fitting is: a=' + str(popt2[0]) + ' ,b=' + str(popt2[1]) + ' ,c=' + str(popt2[2]))
    plt.plot(xdata, sinc(xdata, *popt2), 'b-', linewidth=3)
    peaks, properties = find_peaks(ydata, prominence=(0.6), width=10, height=(0.6, 3))
    plt.hlines(y=properties["width_heights"], xmin=properties["left_ips"], xmax=properties["right_ips"], color="C1")
    #4
    print("q4")
    #plot FWHM
    sun_mass = np.array([5, 8, 10, 15, 20, 30, 40, 60, 100, 140])
    new_realization_num = 500
    widths = run_diffrent_sun_mass(new_realization_num, sun_mass)
    plots(sun_mass, widths, 'FWMH for diffrent sun mass', xlab='sun mass', ylab='FWHM')
    popt, pcov = curve_fit(one_toX, sun_mass, widths, bounds=((500, -3), (1200, 3)))
    print('for A*(x^b) fitting is: A=' + str(popt[0]) + ' ,b=' + str(popt[1]) )
    plt.plot(sun_mass, one_toX(sun_mass, *popt), 'g-', linewidth=1)
    #5
    print("q5")
    #calculation of g2 with mean on 10 trials- lead to less contrast
    plots(xdata, ydata, 'The g2 with and witoht mean on 10 realization', xlab='n', ylab='intensity')
    g2_high = properties['peak_heights'] - popt2[2]
    print('the contrast without mean is ' + str(g2_high))
    plt.plot(xdata, sinc(xdata, *popt2), 'b-', linewidth=3)
    realization_num = 10000
    sun, E_earth, inty, intense, detector500_2, momentum24 = run5(realization_num, 40)
    xdata = np.arange(1024)
    ydata = momentum24 / (realization_num // 10)
    plt.plot(xdata, ydata, '.')
    popt5, pcov = curve_fit(sinc, xdata, ydata, bounds=((0.01, 495, 0.9), (3, 507, 1.1)))
    peaks, properties5 = find_peaks(ydata, prominence=(0.1), width=1, height=(0.05, 3))
    g2_high_mean = properties5['peak_heights'] - popt5[2]
    print('the contrast with mean is ' + str(g2_high_mean))


plt.show()

a=1


