import streamlit as st
import streamlit_folium as st_folium
import folium

map_geo = folium.Map(location=[53.0,20.0], zoom_start=6)

folium.raster_layers.WmsTileLayer(url ='https://mapy.geoportal.gov.pl/wss/service/PZGIK/NMT/WMS/SkorowidzeUkladEVRF2007?',
                layers = 'SkorowidzeNMT2023',
                transparent = True, 
                control = True,
                fmt="image/png",
                name = 'SkorowidzeNMT2023',
                overlay = True,
                show = True,
                CRS = 'EPSG:2180',
                version = '1.3.0',
                opacity=0.3,
                ).add_to(map_geo)

folium.raster_layers.WmsTileLayer(url ='https://mapy.geoportal.gov.pl/wss/service/PZGIK/NMT/WMS/SkorowidzeUkladEVRF2007?',
                layers = 'SkorowidzeNMT2022',
                transparent = True, 
                control = True,
                fmt="image/png",
                name = 'SkorowidzeNMT2022',
                overlay = True,
                show = True,
                CRS = 'EPSG:2180',
                version = '1.3.0',
                opacity=0.3,
                ).add_to(map_geo)

folium.raster_layers.WmsTileLayer(url ='https://mapy.geoportal.gov.pl/wss/service/PZGIK/NMT/WMS/SkorowidzeUkladEVRF2007?',
                layers = 'SkorowidzeNMT2021',
                transparent = True, 
                control = True,
                fmt="image/png",
                name = 'SkorowidzeNMT2021',
                overlay = True,
                show = True,
                CRS = 'EPSG:2180',
                version = '1.3.0',
                opacity=0.3,
                ).add_to(map_geo)
                
folium.raster_layers.WmsTileLayer(url ='https://mapy.geoportal.gov.pl/wss/service/PZGIK/NMT/WMS/SkorowidzeUkladEVRF2007?',
                layers = 'SkorowidzeNMT2020iStarsze',
                transparent = True, 
                control = True,
                fmt="image/png",
                name = 'SkorowidzeNMT2020iStarsze',
                overlay = True,
                show = True,
                CRS = 'EPSG:2180',
                version = '1.3.0',
                opacity=0.3,
                ).add_to(map_geo)
                
folium.LayerControl().add_to(map_geo)
    
st_data = st_folium.st_folium(map_geo)