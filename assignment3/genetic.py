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

def generate_initial_population(states=8,n_queens_size = 5):
    populations = []
    n_choose_2 = combination(n_queens_size, 2)
    for _ in range(states):
        b = Board(n_queens_size)
        b.fitness()
        b.fit = n_choose_2 - b.fit
        b.fit = int(b.fit)
        populations.append(b)
    return populations


def set_probability_of_population(population):
    fitnesses = [p.get_fit() for p in population]
    total_fitness = sum(fitnesses)
    probabilities = [(f / total_fitness for f in fitnesses)]
    return probabilities

def selection(population):
    probabilities = set_probability_of_population(population)
    running_sum = 0
    r = random.uniform(0, 1)
    for i in range(len(probabilities)):
        running_sum += probabilities[i]
        if r < running_sum:
            return population[i]
    return population[-1]

def cross_over(parent1, parent2):
    parent1_encoded = encode(parent1)
    parent2_encoded = encode(parent2)
    idx = random.randint(0, len(parent1_encoded) - 1)
    child1 = parent1_encoded[:idx] + parent2_encoded[idx:]
    child2 = parent2_encoded[:idx] + parent1_encoded[idx:]
    return child1, child2

if __name__ == '__main__':
    boards = generate_initial_population()
    for b in boards:
        b.show()
        print()
