from copy import deepcopy import random
import numpy as np


class Board:
    def __init__(self, n):
        self.n_queen = n
        self.map = [[0 for j in range(n)] for i in range(n)]
        self.fit = 0

        for i in range(self.n_queen):
            j = random.randint(0, self.n_queen - 1)
            self.map[i][j] = 1

    def fitness(self):
        # vertical and diagonal collisions only detected
        for i in range(self.n_queen):
            for j in range(self.n_queen):
                if self.map[i][j] == 1:
                    for k in range(1, self.n_queen - i):
                        if self.map[i + k][j] == 1:
                            self.fit += 1
                        if j - k >= 0 and self.map[i + k][j - k] == 1:
                            self.fit += 1
                        if j + k < self.n_queen and self.map[i + k][j + k] == 1:
                            self.fit += 1

    def show(self):
        print(np.matrix(self.map))
        print("Fitness: ",  self.fit)

    def valid(self, i, j):
        return i >= 0 and i < self.n_queen and j >= 0 and j < self.n_queen and self.map[i][j] == 0


    def find_coordinate_of_queen_to_move(self):
        queen_number = random.randint(0, self.n_queen - 1)
        for i in range(len(self.map)):
            for j in range(len(self.map)):
                    if self.map[i][j] == 1 and queen_number == 0:
                        return (i, j)
                    elif self.map[i][j] == 1:
                        queen_number -= 1
        return (None, None) # later change to throw exception, was given an invalid position

    def succ(self):
        (i, j) = self.find_coordinate_of_queen_to_move()
        return self.successor(i, j)

    def successor(self, i, j):
        # assumes that given a valid position
        possible_movements = [[1, 0], [0, 1], [-1, 0], [0, -1], [-1, -1], [-1, 1], [1, -1], [1, 1]] # moves all 8 eight directions
        possible_movements = [[0, i] for i in range(-self.n_queen, self.n_queen)] # columns of a particular row
        best_fit = float('inf')
        best_successor = Board(self.n_queen)
        best_successor.map = deepcopy(self.map)
        best_successor.fit = self.fit
        for movement in possible_movements:
            x_new = i + movement[0]
            y_new = j + movement[1]
            if self.valid(x_new, y_new):
                new_map = deepcopy(self.map)
                new_map[i][j] = 0
                new_map[x_new][y_new] = 1
                new_board = Board(self.n_queen)
                new_board.map = deepcopy(new_map)
                new_board.fitness()
                if new_board.get_fit() < best_fit:
                    best_fit = new_board.get_fit()
                    best_successor.map = deepcopy(new_board.map)
                    best_successor.fit = best_fit
        return best_successor

    def flip(self, i, j):
        if self.map[i][j] == 0:
            self.map[i][j] = 1
        else:
            self.map[i][j] = 0

    def get_map(self):
        return self.map
    
    def get_fit(self):
        return self.fit

    def set_map(self, map):
        self.map = map

if __name__ == '__main__':
    b = Board(4)
    b.set_map(deepcopy([[1, 1, 1, 1], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]))
    b.fitness()
    b.show()

    c = Board(2)
    c.fitness()
    c.show()

    d = Board(4)
    d.set_map(deepcopy([[1, 0, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0]]))
    d.fitness()
    d.show()

