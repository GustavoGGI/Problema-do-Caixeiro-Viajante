def nearest_neighbor_tsp(graph):
    start_node = list(graph.keys())[0]  # Escolher o primeiro nó como ponto de partida
    unvisited = set(graph.keys())
    route = [start_node]
    unvisited.remove(start_node)

    current_node = start_node
    while unvisited:
        next_node = min(unvisited, key=lambda node: graph[current_node][node])
        route.append(next_node)
        unvisited.remove(next_node)
        current_node = next_node

    route.append(start_node)  # Retornar ao ponto de partida
    return route
