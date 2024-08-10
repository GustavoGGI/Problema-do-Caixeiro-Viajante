import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

def plot_route(graph, route, cities):
    fig, ax = plt.subplots(figsize=(15, 15))

    m = Basemap(
        projection='merc',
        llcrnrlat=20,
        urcrnrlat=50,
        llcrnrlon=-130,
        urcrnrlon=-60,
        lat_ts=0,
        resolution='i',
        ax=ax
    )
    m.drawcoastlines()
    m.drawcountries()
    m.drawstates()

    for cidade, (lat, lon) in cities.items():
        x, y = m(lon, lat)
        plt.plot(x, y, marker='o', color='red', markersize=5)
        plt.text(x, y, cidade, fontsize=8)

    for i in range(len(route) - 1):
        start_pos = graph.nodes[route[i]]['pos']
        end_pos = graph.nodes[route[i + 1]]['pos']
        start_x, start_y = m(start_pos[1], start_pos[0])
        end_x, end_y = m(end_pos[1], end_pos[0])
        plt.annotate(
            '',
            xy=(end_x, end_y),
            xytext=(start_x, start_y),
            arrowprops=dict(arrowstyle='->', color='blue', linestyle='--', lw=1)
        )

    ax.set_title('Rota do Caixeiro Viajante entre as Capitais dos Estados Unidos')
    ax.set_xlabel('Longitude')
    ax.set_ylabel('Latitude')

    plt.show()
