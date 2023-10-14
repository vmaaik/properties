import json
import logging

import folium
from folium.plugins import Draw


class Map:

    def __init__(self, zoom_start=10):
        self.zoom_start = zoom_start
        self.map = folium.Map(["53.482816189990764", "-2.2266877586490175"], zoom_start=self.zoom_start,
                              png_enabled=True)
        Draw().add_to(self.map)

    def add_marker(self, coordinates, color='red'):
        folium.Marker(
            location=coordinates,
            icon=folium.Icon(color=color, icon=''),
        ).add_to(self.map)

    def add_geojson(self, geojson_data):
        logging.info("llaalalal")
        geojson_data_dict = json.loads(geojson_data)

        for feature in geojson_data_dict.get("features", []):
            popup_content = self.generate_popup_content(feature)
            popup_text = folium.Html(popup_content, script=True)
            folium.GeoJson(
                data=feature,
                popup=folium.Popup(html=popup_text, parse_html=True)
            ).add_to(self.map)

    def render(self):
        return self.map.get_root().render()

    def generate_popup_content(self, feature):
        popup_content = "<div style='min-width: 250px;'>"
        properties = feature.get("properties", {})

        for key, value in properties.items():
            if key == "location":
                popup_content += f"<a href={value} target='_blank' rel='noopener noreferrer'>View on Google Maps</a><br>"
            if key == "url":
                popup_content += f"<a href={value} target='_blank' rel='noopener noreferrer'>Property Link</a><br>"
            if key in ["lat", "long", "id", "location", "url"]:
                continue
            else:
                popup_content += f"<strong>{key}:</strong> {value}<br>"

        popup_content += "</div>"
        return popup_content
