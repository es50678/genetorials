import numpy as np

def points_count(d, j):
    return d/(np.gcd(d, j))