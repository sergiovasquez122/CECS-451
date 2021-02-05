from board import *
from timeit import default_timer as timer

def hill(initial_state : Board):
    current = Board(initial_state.n_queen)
    current.map = deepcopy(initial_state.get_map())
    current.fitness()
    restarts = 0
    while True:
        neighbor = current.succ() # returns best of all neighbors
        neighbor.fitness()
        if current.get_fit() <= neighbor.get_fit(): # we checked
            if current.get_fit() == 0: # found global optima
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

    start = timer()
    best_found, restarts = hill(test1)
    end = timer()
    formatted_time = "{:.2f}".format((end - start) * 1000)
    print("running time:", formatted_time, "ms")
    print("# of restarts:", restarts)
    best_found.show()
