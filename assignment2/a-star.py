import heapq as pq

def construct_graph(map_file = 'map.txt', distance_file = 'distances.txt'):
    h = {}
    f = open(distance_file, 'r')
    for line in f:
        split_index = line.find('-')
        current_city = line[:split_index]
        distance_to_bucharest = int(line[split_index + 1:])
        h[current_city] = distance_to_bucharest

    f = open(map_file, 'r')
    G = {}
    for line in f:
        split_index = line.find('-')
        current_city = line[:split_index]
        neighbors = line[split_index + 1:]
        adj_of_city = []
        for neighbor in neighbors.split(','):
            neighbor = neighbor.rstrip()
            left_brace_index = neighbor.find('(')
            neighbor_name = neighbor[:left_brace_index]
            neighbor_dist = int(neighbor[left_brace_index + 1 : len(neighbor) - 1])
            adj_of_city.append((neighbor_name, neighbor_dist))
        G[current_city] = adj_of_city
    return G, h

def path_to_bucharest(G, h, source):
    if source not in G: return None # if source is not in the graph no reason to traverse
    g = {source : 0} # distance traveled so far
    f = {source : h[source]} # estimated distance to travel
    frontier = [(f[source], source)]
    parent_pointer = {source : None} # used to find path from destination from source if possible
    while len(frontier) != 0:
        _, current_node = pq.heappop(frontier)
        if current_node == "Bucharest": # A* guarantees that once the target node has been dequeued the solution is optimal
            path = []
            while current_node != None:
                path.append(current_node)
                current_node = parent_pointer[current_node]
            path.reverse()
            return path, g["Bucharest"]

        for neighbor, g_cost in G[current_node]: # traverse nodes adjacent to current node and relax the edge if possible
            if neighbor not in parent_pointer or g[current_node] + g_cost + h[neighbor] < f[neighbor]: # did we find a better f(n), if so update
                g[neighbor] = g[current_node] + g_cost
                f[neighbor] = g[neighbor] + h[neighbor]
                parent_pointer[neighbor] = current_node
                pq.heappush(frontier, (f[neighbor], neighbor))

    return None # could not find a path to destination

def pretty_print(path, distance_traveled):
    print("From city:", path[0])
    print("To city:", path[len(path) - 1])
    pretty_path = ""
    for city in path[:len(path) - 1]:
        pretty_path += city + " - "
    pretty_path += path[len(path) - 1]
    print("Best route:", pretty_path)
    print("Total distance:", distance_traveled)

if __name__ == '__main__':
    G, h = construct_graph()
    for source in G.keys():
       path, distance_traveled = path_to_bucharest(G, h, source)
       pretty_print(path, distance_traveled)
       print()
