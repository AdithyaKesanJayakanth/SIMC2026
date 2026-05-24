import math
import numpy as np
import random

# ── Parameters ───────────────────────────────────────────────────
sigma = 0.02



def apply_noise_toelement(x, sigma):
    """Apply Gaussian noise to a single element."""
    noise_multiplier = random.gauss(1, sigma)


    upper_bound = 1.05 * abs(x)
    lower_bound = 0.95 * abs(x)

    output = abs(x) * noise_multiplier
    output = min(output, upper_bound)
    output = max(output, lower_bound)
    output = float(np.sign(x) * output)  # Preserve the original sign of x
    #print(f"Noise multiplier: {noise_multiplier:.4f}, Output: {output:.4f} (Bounds: [{lower_bound:.4f}, {upper_bound:.4f}])")
    return output

def apply_noise_tovector(vec, sigma):
    """Apply Gaussian noise to each element of the vector."""
    output = []
    for x in vec:
        element = apply_noise_toelement(x, sigma)
        output.append(element)
    return output

if __name__ == "__main__":
    number_test = apply_noise_toelement(100, sigma)
    print(f"Original: 100, Noisy: {number_test}")
    vector_test = [-1, 2, 3 , 5 , 0]
    vector_noisy = apply_noise_tovector(vector_test, sigma)
    print(f"Original: {vector_test}, Noisy: {vector_noisy}")
