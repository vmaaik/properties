from folium import GeoJsonTooltip

from map.map import Map


class BaseMap(Map):

    def __init__(self, geojson_data):

        super().__init__()
        self.geojson_data = geojson_data

        if geojson_data:
            super().add_geojson(self.geojson_data)
