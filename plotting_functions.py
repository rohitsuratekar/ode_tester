import numpy as np
import matplotlib.pyplot as plt
#from mpl_toolkits.mplot3d import Axes3D
#import pylab

#fig = pylab.figure()
#ax = Axes3D(fig)

with open("xyz.txt") as original_parameters:
    k1 = [[float(digit) for digit in line.split()] for line in original_parameters]
k1 = np.asarray(k1)

fig, ax1 = plt.subplots()
ax2 = ax1.twinx()
ax1.scatter(k1[:,0],k1[:,1], color='g')
ax2.scatter(k1[:,0],k1[:,2], color='b')
ax1.set_xlabel('Vplc')
ax1.set_ylabel('Fractional Error', color='g')
ax2.set_ylabel('PIP2 steady state', color='b')
plt.title('Parameter space for PLC reaction velocity')
ax2.axhline()
ax1.axhline()
ax1.axvline()
plt.show()
