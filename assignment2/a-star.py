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
    frontier = [(source, h[source])]
    cost = {source : 0}
    parent_pointer = {source : None}
    while len(frontier) != 0:
        frontier.sort(key=lambda x:x[1], reverse=True)
        current_node, node_cost = frontier.pop()
        node_cost -= h[current_node]
        if current_node == "Bucharest":
            path = []
            while current_node != None:
                path.append(current_node)
                current_node = parent_pointer[current_node]
            path.reverse()
            return path, cost["Bucharest"]

        for neighbor, g_cost in G[current_node]:
            if neighbor not in parent_pointer or node_cost + g_cost + h[neighbor] < cost[neighbor]:
                cost[neighbor] = node_cost + g_cost
                parent_pointer[neighbor] = current_node
                frontier.append((neighbor, cost[neighbor] + h[neighbor]))
    return None

if __name__ == '__main__':
    G, h = construct_graph()
    for source in G.keys():
        print(path_to_bucharest(G, h, source))
