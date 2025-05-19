from py2neo import Graph
import geopandas as gpd
import matplotlib.pyplot as plt
from shapely.geometry import Point, LineString

# Neo4j bağlantısı
graph = Graph(""))

# Ülkelerin enlem, boylam ve seyahat kısıtlaması bilgilerini çekme
query = """
MATCH (a:Country)-[r:TRAVEL_RESTRICTION]->(b:Country)
RETURN a.name AS from_country, a.latitude AS from_latitude, a.longitude AS from_longitude,
       b.name AS to_country, b.latitude AS to_latitude, b.longitude AS to_longitude,
       r.status AS travel_restriction
"""
results = graph.run(query).data()

# Ülkelerin enlem ve boylam bilgileri (manuel olarak girilmiştir)
country_coords = {
    "Turkey": (38.9637, 35.2433),
    "Germany": (51.1657, 10.4515),
    "France": (46.6034, 1.8883),
    "Greece": (39.0742, 21.8243),
    "Bulgaria": (42.7339, 25.4858),
    "Georgia": (32.1656, -82.9001),
    "Iraq": (33.2232, 43.6793),
    "Syria": (34.8021, 38.9968),
    "Iran": (32.4279, 53.6880),
    "Armenia": (40.0691, 45.0382),
    "Azerbaijan": (40.1431, 47.5769)
}

# Verileri işleme
countries = []
connections = []

for record in results:
    from_country = record['from_country']
    to_country = record['to_country']

    # Enlem ve boylam bilgilerini manuel olarak ekleme
    from_latitude, from_longitude = country_coords.get(from_country, (None, None))
    to_latitude, to_longitude = country_coords.get(to_country, (None, None))

    if from_latitude is not None and from_longitude is not None and to_latitude is not None and to_longitude is not None:
        from_point = Point(from_longitude, from_latitude)
        to_point = Point(to_longitude, to_latitude)

        if from_country not in [country['name'] for country in countries]:
            countries.append({
                'name': from_country,
                'geometry': from_point
            })

        if to_country not in [country['name'] for country in countries]:
            countries.append({
                'name': to_country,
                'geometry': to_point
            })

        connections.append({
            'from': from_point,
            'to': to_point,
            'status': record['travel_restriction']
        })

# GeoDataFrame oluşturma
countries_gdf = gpd.GeoDataFrame(countries)
connections_gdf = gpd.GeoDataFrame(connections)

# Dünya haritasını yükleme
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

# Harita üzerinde ülkeleri işaretleme ve seyahat kısıtlamalarını gösterme
fig, ax = plt.subplots(1, 1, figsize=(15, 10))
world.plot(ax=ax, color='lightgrey')

# Ülkelerin merkezlerini işaretleme ve adlarını yazma
countries_gdf.plot(ax=ax, color='red', markersize=50, label='Country Centers')
for idx, row in countries_gdf.iterrows():
    plt.text(row.geometry.x, row.geometry.y, row['name'], fontsize=9, ha='right')

# Seyahat kısıtlamalarını çizme
for idx, row in connections_gdf.iterrows():
    line = LineString([row['from'], row['to']])
    color = 'green' if row['status'] == 'open' else 'orange' if row['status'] == 'partially restricted' else 'red'
    gpd.GeoSeries([line]).plot(ax=ax, color=color, linewidth=2)

# Legendi ayarlama
handles, labels = ax.get_legend_handles_labels()
by_label = dict(zip(labels, handles))
ax.legend(by_label.values(), by_label.keys())

plt.title("World Map with Travel Restrictions")
plt.show()
