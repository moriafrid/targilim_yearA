# import libraries
import math
import matplotlib.pyplot as plt
import numpy as np

p= np.arange(-2*math.pi,2*math.pi,0.1)
#j=math.sqrt(-1)
# create data of complex numbers
#data = np.array([1 + 2j, 2 - 4j, -2j, -4, 4 + 1j, 3 + 8j, -2 - 6j, 5])
data =np.cos(p) + math.j*np.sin(p)
x=[]
# extract real part using numpy array
x = np.cos(p)
# extract imaginary part using numpy array
y = np.sin(p)

# plot the complex numbers
plt.plot(x, y, 'g*')
plt.ylabel('Imaginary')
plt.xlabel('Real')
plt.show()

