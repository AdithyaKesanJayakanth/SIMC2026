import math as m

# Represents a single grid cell in the drainage simulation.
# Each square has a terrain type that determines its hydrological properties.
class square:
    def __init__(self, row, col , name):
        self.row = row
        self.col = col
        self.name = name
        self.water0 = 0         # current water level in the cell
        self.rainfall = 0       # water added per time step
        self.capacity = 0       # max water before overflow/transfer
        self.drain_rate = 0     # water absorbed into ground per step
        self.transfer_rate = 0  # max water that can flow out per step

        # Set hydrological properties based on terrain type
        if self.name == "lowland":
            self.rainfall = 0.0
            self.capacity = 100.0
            self.drain_rate = 5.0
            self.transfer_rate = 1.0

        elif self.name == "mountain":
            self.rainfall = 100.0    # mountains receive rainfall
            self.capacity = 20.0     # low capacity — rocky terrain
            self.drain_rate = 10.0   # moderate ground absorption
            self.transfer_rate = 24.0  # steep slopes => fast runoff

        elif self.name == "ocean":
            self.rainfall = 0.0
            self.capacity = m.inf    # ocean never overflows
            self.drain_rate = 0.0
            self.transfer_rate = 0.0 # ocean does not push water out

        else:
            print("Error: unknown square name")

    def __repr__(self):
        return f"{self.name} ({self.row}-{self.col})"

    # Exponential decay model: V(t) = water0 * 0.5^t - 2
    # Returns the volume at time t based on current water level
    def volfn(self, t):
        return self.water0 * pow(0.5, t) - 2

    # Add one time-step's worth of rainfall to this cell
    def rainfall_apply(self):
        self.water0 += self.rainfall

    # Remove water via ground absorption (exponential decay model)
    def drain(self, t):
        drain_amount = max(0, self.volfn(t))
        if self.water0 > drain_amount:
            self.water0 -= drain_amount
        else:
            self.water0 = 0


# --- Grid Setup ---
# 3x3 terrain grid: mountain in the centre, ocean at bottom-right, lowland elsewhere
terrain = [
[
        square(0, 0, "lowland"),
        square(0, 1, "lowland"),
        square(0, 2, "lowland"),
    ],
    [
        square(1, 0, "lowland"),
        square(1, 1, "mountain"),
        square(1, 2, "lowland"),
    ],
    [
        square(2, 0, "lowland"),
        square(2, 1, "lowland"),
        square(2, 2, "ocean"),
    ],
]

def neighbour(row , col):
    neighbours = []
    for i in terrain:
        for j in i:
            if abs(j.row - row) + abs(j.col - col) == 1:
                neighbours.append(j)
    return neighbours

# Print the water level of every cell in a grid layout
def waterdisplay(terrain):
    for row in terrain:
        for col in row:
            print(f"|| {col.name} ({col.row}-{col.col} , {col.water0} ) ||", end=" ")
        print()

# Advance the simulation by the given number of time steps.
# Each step: (1) apply rainfall, (2) drain into ground, (3) transfer excess to neighbours.
def global_update(terrain, time):

    for t in range(time):

        # Phase 1: Rainfall — every cell receives its per-step rainfall
        for row in terrain:
            for sq in row:
                sq.rainfall_apply()

        # Phase 2: Drainage — each cell absorbs water into the ground
        for row in terrain:
            for sq in row:
                sq.drain(t)

        # Phase 3: Transfer — excess water flows to adjacent cells
        # A separate dict accumulates deltas so transfers don't cascade within one step
        transfer_changes = {}

        for row in terrain:
            for sq in row:
                transfer_changes[sq] = 0

        for row in terrain:
            for sq in row:

                # Only transfer if water exceeds capacity
                if sq.water0 <= sq.capacity:
                    continue

                neighbours = neighbour(sq.row, sq.col)

                # Water only flows downhill: mountain → lowland → ocean
                flow_targets = {"mountain": "lowland", "lowland": "ocean"}
                target_type = flow_targets.get(sq.name)
                if target_type is None:
                    continue
                valid = []
                for n in neighbours:
                    if n.name == target_type:
                        valid.append(n)

                if not valid:
                    continue

                excess = sq.water0 - sq.capacity
                max_transfer = max(0, sq.volfn(t))  # decay-based transfer limit
                transferable = min(excess, max_transfer)
                share = transferable / len(valid)

                for n in valid:
                    space = n.capacity - n.water0  # remaining capacity in neighbour
                    add = min(share, space)         # don't exceed neighbour's capacity

                    transfer_changes[sq] -= add
                    transfer_changes[n] += add

        # Apply all transfers at once (simultaneous update)
        for sq, delta in transfer_changes.items():
            sq.water0 += delta

# Run the simulation for 1000 time steps and display final water levels
global_update(terrain , 1)
waterdisplay(terrain)