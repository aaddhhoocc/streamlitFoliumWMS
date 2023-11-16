import streamlit as st

import streamlit_folium as st_folium
import folium
from folium.plugins import MousePosition, Fullscreen, Draw


st.set_page_config(layout = 'wide')

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden !important;}
            [data-testid="stToolbar"] {visibility: hidden !important;}
            .css-1rs6os {visibility: hidden;}
            .css-17ziqus {visibility: hidden;}
            .block-container {
                    padding-top: 0rem;
                    padding-bottom: 0rem;
                    padding-left: 0rem;
                    padding-right: 0rem;
                }
            """
st.markdown(hide_st_style, unsafe_allow_html=True)


map_geo = folium.Map(location=[52.0,19.0], zoom_start=6, control_scale=True, prefer_canvas=True) #.add_child(folium.LatLngPopup())

MousePosition().add_to(map_geo)
Fullscreen().add_to(map_geo)
Draw(export=True).add_to(map_geo)

#folium.Figure(width='100%')

# folium.raster_layers.WmsTileLayer(url ='https://mapy.geoportal.gov.pl/wss/service/PZGIK/NMT/WMS/SkorowidzeUkladEVRF2007?',
#                 layers = 'SkorowidzeNMT2023',
#                 transparent = True, 
#                 control = True,
#                 fmt="image/png",
#                 name = 'SkorowidzeNMT2023',
#                 overlay = True,
#                 show = True,
#                 CRS = 'EPSG:2180',
#                 version = '1.3.0',
#                 opacity=0.35,
#                 ).add_to(map_geo)

# folium.raster_layers.WmsTileLayer(url ='https://mapy.geoportal.gov.pl/wss/service/PZGIK/NMT/WMS/SkorowidzeUkladEVRF2007?',
#                 layers = 'SkorowidzeNMT2022',
#                 transparent = True, 
#                 control = True,
#                 fmt="image/png",
#                 name = 'SkorowidzeNMT2022',
#                 overlay = True,
#                 show = True,
#                 CRS = 'EPSG:2180',
#                 version = '1.3.0',
#                 opacity=0.35,
#                 ).add_to(map_geo)
#
# folium.raster_layers.WmsTileLayer(url ='https://mapy.geoportal.gov.pl/wss/service/PZGIK/NMT/WMS/SkorowidzeUkladEVRF2007?',
#                 layers = 'SkorowidzeNMT2021',
#                 transparent = True, 
#                 control = True,
#                 fmt="image/png",
#                 name = 'SkorowidzeNMT2021',
#                 overlay = True,
#                 show = True,
#                 CRS = 'EPSG:2180',
#                 version = '1.3.0',
#                 opacity=0.35,
#                 ).add_to(map_geo)
#
# folium.raster_layers.WmsTileLayer(url ='https://mapy.geoportal.gov.pl/wss/service/PZGIK/NMT/WMS/SkorowidzeUkladEVRF2007?',
#                 layers = 'SkorowidzeNMT2020iStarsze',
#                 transparent = True, 
#                 control = True,
#                 fmt="image/png",
#                 name = 'SkorowidzeNMT2020iStarsze',
#                 overlay = True,
#                 show = True,
#                 CRS = 'EPSG:2180',
#                 version = '1.3.0',
#                 opacity=0.35,
#                 ).add_to(map_geo)
                
folium.raster_layers.WmsTileLayer(url ='https://mapy.geoportal.gov.pl/wss/service/PZGIK/ORTO/WMS/StandardResolution?',
                layers = 'Raster',
                transparent = True, 
                control = True,
                fmt="image/png",
                name = 'Ortofotomapa standardowa',
                overlay = True,
                show = True,
                #CRS = 'EPSG:2180',
                version = '1.3.0',
                opacity=0.4,
                ).add_to(map_geo)
                         
folium.raster_layers.WmsTileLayer(url ='https://mapy.geoportal.gov.pl/wss/service/PZGIK/ORTO/WMS/HighResolution?',
                layers = 'Raster',
                transparent = True, 
                control = True,
                fmt="image/png",
                name = 'Ortofotomapa o wysokiej rozdzielczości',
                overlay = True,
                show = False,
                #CRS = 'EPSG:2180',
                version = '1.3.0',
                opacity=0.4,
                ).add_to(map_geo)
                
                                                  
folium.LayerControl().add_to(map_geo)

#with st.expander("", expanded=True):
with st.empty():
    st_data = st_folium.st_folium(map_geo, width='100%', height=500, use_container_width=True)
    #st_data = st_folium.folium_static(map_geo, width=1000, height=800)

#st_data