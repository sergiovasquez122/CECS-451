from board import *
from math import factorial

def encode(b : Board):
    the_map = b.get_map()
    result = ""
    for m in the_map:
        index = m.index(1)
        result += str(index)
    return result

def combination(n, r):
    return factorial(n) / ((factorial(r)) * factorial(n - r))

def decode(s : str):
    matrix = [[0 for _ in range(len(s))] for _ in range(len(s))]
    for m, c in zip(matrix, s):
        idx = int(c)
        m[idx] = 1

    b = Board(len(s))
    b.map = deepcopy(matrix)
    b.fitness()
    return b

if __name__ == '__main__':
    s = "31034"
    b = decode(s)
    b.show()


