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
    return b

def generate_initial_population(states=8,n_queens_size = 5):
    populations = []
    for _ in range(states):
        b = Board(n_queens_size)
        populations.append(b)
    return populations

def set_fitness(population, states):
    n_choose_2 = combination(states, 2)
    for p in population:
        p.fitness()
        p.fit = n_choose_2 - p.fit

def set_probability_of_population(population):
    fitnesses = [p.get_fit() for p in population]
    total_fitness = sum(fitnesses)
    probabilities = [(f / total_fitness) for f in fitnesses]
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

def mutation(child):
    idx = random.randint(0, len(child))
    if idx == 0:
        return child
    altered_child = list(child)
    altered_child[idx - 1] = str(random.randint(0, len(child) - 1))
    return ''.join(child)

def cross_over(parent1, parent2):
    parent1_encoded = encode(parent1)
    parent2_encoded = encode(parent2)
    idx = random.randint(0, len(parent1_encoded) - 1)
    child1 = parent1_encoded[:idx] + parent2_encoded[idx:]
    child2 = parent2_encoded[:idx] + parent1_encoded[idx:]
    child1 = mutation(child1)
    child2 = mutation(child2)
    return decode(child1), decode(child2)

def next_generation(population):
    length = len(population) // 2
    children = []
    for _ in range(length):
        parent1 = selection(population)
        parent2 = selection(population)
        child1, child2 = cross_over(parent1, parent2)
        children.append(child1)
        children.append(child2)
    return children

def genetic_algorithm(states = 8, n_queen_size = 5):
    population = generate_initial_population(states, n_queen_size)
    n_choose_2 = combination(n_queen_size, 2)
    while True:
        set_fitness(population, states)
        for p in population:
            if p.get_fit() == n_choose_2:
                return p
        population = next_generation(population)


if __name__ == '__main__':
    b = genetic_algorithm()
    b.show()
