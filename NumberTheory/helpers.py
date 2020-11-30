import numpy as np

def points_count(d, j):
    return d/(np.gcd(d, j))

def find_totients(m):
    return [x for x in range(1,m) if np.gcd(x,m) == 1]