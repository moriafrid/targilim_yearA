import numpy as np
from scipy.fft import fft, ifft
import matplotlib.pyplot as plt

#function for the plots
def plots(x,y, titly, xlab='n_index',ylab='intensity'):
    plt.figure()
    plt.title(titly)
    plt.plot(x,y,'.')
    plt.ylabel(ylab)
    plt.savefig(titly+'.png')


#fit functions
def exp(x,A,N0):
    return A*np.exp(-x/N0)

def sinc(x,a,b,c):
    return c+(np.sinc(a*(x-b))**2)

def one_toX(x,A,b):
    return A*(x**b)