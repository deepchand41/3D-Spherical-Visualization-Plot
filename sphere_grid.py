from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
import math as m


def cart2sph(x,y,z):
    XsqPlusYsq = x**2 + y**2
    r = m.sqrt(XsqPlusYsq + z**2)               # r
    elev = m.atan2(z,m.sqrt(XsqPlusYsq))     # theta
    az = m.atan2(y,x)                           # phi
    return r, elev, az

def sph2cart(r,theta,phi):
    x = np.sin(phi) * np.cos(theta)
    y = np.sin(phi) * np.sin(theta)
    z = np.cos(phi)
    return(x,y,z)

plt.ion()

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
u = np.linspace(0, 2 * np.pi, 100)
v = np.linspace(0, np.pi, 100)
x = 1 * np.outer(np.cos(u), np.sin(v))
y = 1 * np.outer(np.sin(u), np.sin(v))
z = 1 * np.outer(np.ones(np.size(u)), np.cos(v))
ax.plot_wireframe(x, y, z,  rstride=4, cstride=4, color='c')

for i in range(100):
    theta = np.random.randint(180,size=100)
    phi = np.random.randint(180,size=100)
    x,y,z = sph2cart(r=1, theta=theta[i], phi=phi[i])
    ax.scatter(x,y,z)
    plt.draw()
    plt.pause(0.1)

plt.show(block=True)
