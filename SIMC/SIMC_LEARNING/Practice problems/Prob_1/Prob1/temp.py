import matplotlib.pyplot as plt
import numpy as np


T0 = 90        # initial temperature (°C)
T_room = 25    # room temperature (°C)
k = 0.05       # cooling constant
dt = 0.1       # time step (minutes)
t_end = 60     # simulate for 60 minutes

# dT/dt = -k * (T - T_room)
# T(t) = T_room + (T_initial - T_room) * e^(-kt)
x = []
y = []

i = 0
dT_dt = 0
while i < t_end/dt:
    x.append(i*dt)
    y.append(T0)
    i += 1
    dT_dt = -k * (T0 - T_room)
    T0 += dT_dt * dt

print(i*dt)

x_points = np.array(x)
y_points = np.array(y)
plt.xlabel('Time (minutes)')
plt.ylabel('Temperature (°C)')
plt.title('Cooling of Coffee Over Time')
plt.plot
plt.plot(x_points, y_points, marker='o', linestyle='-', color='b')

plt.show()
