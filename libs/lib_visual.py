import sys
sys.path.append('./libs')
import pandas as pd
from lib_api import foursquare_visual
from folium import  Marker, Icon, Map

def imprime_mapa(lat,lon):
    lista=["starbucks","estadio de baloncesto", "restaurante vegano","escuelas primaria","peluqueria perros","aeropuerto"]
   
    tipo=list()
    latitud=list()
    longitud=list()
    for q in lista:
        resultado=foursquare_visual({'latitud':lat, 'longitud':lon},q)
        for r in resultado:
            tipo.append(q.replace(" ","_"))
            latitud.append(r['latitud'])
            longitud.append(r['longitud'])
        

    df=pd.DataFrame({'tipo':tipo,'latitud':latitud,'logitud':longitud})

    

    map_2 = Map(location=[lat,lon],zoom_start=15)

    establecimiento = {
            "location":[lat, lon ],
            "tooltip" : "Empresa"
        }
    icon = Icon(color = "beiredge",
                        prefix = "fa",
                        icon = "dot-circle",
                        icon_color = "white"
            )

    Marker(**establecimiento,icon = icon ).add_to(map_2)
    for i, row in df.iterrows():
        
        establecimiento = {
            "location":[row["latitud"], row["logitud"]],
            "tooltip" : row["tipo"]
        }


        if row["tipo"] == "starbucks":
            icon = Icon(color = "beige",
                        prefix = "fa",
                        icon = "coffee-togo",
                        icon_color = "black"
            )
            
        elif row["tipo"] == "restaurante_vegano":
            icon = Icon(color = "green",
                        prefix = "fa",
                        icon = "leaf",
                        icon_color = "black"
            )

        elif row["tipo"] == "escuelas_primaria":
            icon = Icon(color = "blue",
                        prefix = "fa",
                        icon = "child",
                        icon_color = "black"
            )
        
        elif row["tipo"] == "peluqueria_perros":
            icon = Icon(color = "red",
                        prefix = "fa",
                        icon = "dog",
                        icon_color = "black"
            )

        elif row["tipo"] == "estadio_de_baloncesto":
            icon = Icon(color = "orange",
                        prefix = "fa",
                        icon = "basketball-ball",
                        icon_color = "black"
            )

        elif row["tipo"] == "aeropuerto":
            icon = Icon(color = "grey",
                        prefix = "fa",
                        icon = "plane",
                        icon_color = "black"
            )
            
        else:
                        prefix = "fa",
                        icon = "briefcase",
                        icon_color = "black"
            
        Marker(**establecimiento,icon = icon ).add_to(map_2)
    map_2