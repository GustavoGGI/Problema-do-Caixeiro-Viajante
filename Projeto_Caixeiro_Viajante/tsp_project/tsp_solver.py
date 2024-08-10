def nearest_neighbor_tsp(graph, start_node=0):
    """
    """
    unvisited = set(graph.nodes)
    current_node = start_node
    tour = [current_node]
    unvisited.remove(current_node)

    while unvisited:
        next_node = min(unvisited, key=lambda node: graph[current_node][node]['weight'])
        tour.append(next_node)
        unvisited.remove(next_node)
        current_node = next_node

    tour.append(start_node)  # Retorna ao ponto de partida
    return tour
