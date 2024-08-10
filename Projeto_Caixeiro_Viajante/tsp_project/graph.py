import networkx as nx

def create_graph(cities):
    """
    Cria o módulo que representa as cidades e calcula as distâncias
    """
    G = nx.Graph()
    coords = list(cities.values())

    for i, (city, coord) in enumerate(cities.items()):
        G.add_node(i, name=city, pos=coord)

    for i in range(len(coords)):
        for j in range(i + 1, len(coords)):
            distance = ((coords[i][0] - coords[j][0])**2 + (coords[j][1] - coords[i][1])**2)**0.5
            G.add_edge(i, j, weight=distance)

    return G
