# C = 100 units.
# D(t) = 2 - t/4



# This script compares two approaches:
#   1. Exact (integral) solution:  V(t) = C - 2t + t²/8
#   2. Numerical (Euler method) approximation using small time steps



C = 100        # initial volume in the tank
dt = 0.01      # time step for the numerical method

# Integral Approach
# For t < 8 the drain is active; at t >= 8 total drained = 8 units.
def volume_integral(t, C):
    if t < 8:
        return C - 2 * t + (t ** 2) / 8
    else:
        return C - 8




# Numerical Approach
# Subtracts D(t)*dt each step until the drain rate reaches zero or t_end is reached.
def volume_numerical(t_end, C, dt):
    volume = float(C)
    t = 0.0

    while t < t_end:
        d = (2 - t / 4)        # current drain rate at time t
        if d == 0:              # drain stops when rate hits zero
            break
        volume -= d * dt        # Euler step: subtract drained amount
        volume = max(0.0, volume)  # volume cannot go negative
        t += dt

    return volume


# --- Output: compare both methods for t = 1 to 8 ---
print("-" * 65)

for t in range(1, 9):
    integral  = volume_integral(t, C)
    numerical = volume_numerical(t, C, dt)
    print(f"{t:<6} {integral:<20.6f} {numerical:<25.6f}")
