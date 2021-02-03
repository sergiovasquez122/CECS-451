from board import *

def hill(initial_state : Board):
    current = Board(initial_state.n_queen)
    current.map = deepcopy(initial_state.get_map())
    current.fitness()
    restarts = 0
    while True:
        neighbor = current.succ()
        neighbor.fitness()
        if current.get_fit() <= neighbor.get_fit():
            if current.get_fit() == 0:
                return current, restarts
            else:
                current = Board(initial_state.n_queen)
                current.fitness()
                restarts += 1
        else:
            current = neighbor
            current.fitness()

if __name__ == '__main__':
    test1 = Board(5)
    test1.fitness()
    test1.show()

    best_found, restarts = hill(test1)
    best_found.show()
    print(restarts)
