from math import log2

def B(q): return -(q * log2(q) + (1 - q) * log2(1 - q))

def B_g(q): return 2 * q *  (1 - q)
