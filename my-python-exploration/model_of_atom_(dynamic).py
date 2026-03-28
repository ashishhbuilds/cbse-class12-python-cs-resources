import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
ax.set_xlim(-30,30)
ax.set_ylim(-30,30)

# Nucleus
ax.scatter(0,0, color="red", s=600)

# Electron initialization
num_orbits=3
electron_counts = [2,4,6]
radii = [5,10,15]
electrons = []

for orbit, count in enumerate(electron_counts):
    for i in range(count):
        electron, = plt.plot([], [], "go")
        electrons.append((electron, orbit))

def init():
    for electron, _ in electrons:
        electron.set_data([], [])
    return [electron for electron, _ in electrons]

def update(frame):
    for electron, orbit in electrons:
        theta_offset = 4 * np.pi/electron_counts[orbit]
        theta = 2 * np.pi * frame/(100*(orbit+1))+electron_counts[orbit]*theta_offset
        x=radii[orbit]*np.cos(theta)
        y=radii[orbit]*np.sin(theta)
        electron.set_data(x,y)
    return[electron for electron, _ in electrons]

ani = FuncAnimation(fig, update, frames=100, init_func=init, blit=True, repeat=True)

plt.show()
