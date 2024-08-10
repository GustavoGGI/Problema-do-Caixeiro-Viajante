from tsp_project.cities import get_city_coordinates
from tsp_project.graph import create_graph
from tsp_project.tsp_solver import nearest_neighbor_tsp
from tsp_project.visualizer import plot_route


if __name__ == "__main__":
    cities = get_city_coordinates()
    graph = create_graph(cities)

    route = nearest_neighbor_tsp(graph)

    route_names = [graph.nodes[i]['name'] for i in route]
    total_distance = sum(
        graph[route[i]][route[i + 1]]['weight'] for i in range(len(route) - 1)
    )

    print("Distâncias entre as cidades:")
    for i in range(len(route) - 1):
        start_city = route_names[i]
        end_city = route_names[i + 1]
        distance = graph[route[i]][route[i + 1]]['weight']
        print(f"De {start_city} para {end_city}: {distance:.2f} unidades de distância.")

    print(f"\nDistância total percorrida: {total_distance:.2f} unidades de distância.")


    plot_route(graph, route, cities)
