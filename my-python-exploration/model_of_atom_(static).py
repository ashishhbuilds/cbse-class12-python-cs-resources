import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Nucleus
ax.scatter(0,0,0, color="red", s=5000)

# Orbiting Electrons
num_electrons = 4
theta = np.linspace(0,2 * np.pi, num_electrons)
r=5
x=r * np.cos(theta)
y=r * np.sin(theta)
z= np.zeros_like(x)
ax.scatter(x,y,z, color="black")

ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

plt.show()
