

from lib_api import foursquare_visual

from folium import  Marker, Icon, Map
import pandas as pd
from keplergl import KeplerGl

def imprime_mapa(lat,lon):
    """
    imprime un mapa carto de los serviciones que estamos estudiando
    lo hace centrado en lat long y. para realizar el mapa consulta en FS los resultados.

    tokens tiene que estar en .env

    devuelve el mapa
    """

    lista=["colegio", "starbucks","estadio de baloncesto", "bar","restaurante vegano","peluqueria perros","aeropuerto"]
   
    tipo=list()
    latitud=list()
    longitud=list()

    for q in lista:
        resultado=foursquare_visual({'latitud':lat, 'longitud':lon},q)
       
        for r in resultado:
            tipo.append(q.replace(" ","_"))
            latitud.append(r['latitud'])
            longitud.append(r['longitud'])
        #if q == "colegio" or q == "peluqueria perros":
        #    print(pd.DataFrame({'tipo':tipo,'latitud':latitud,'logitud':longitud}))
        #    raise
        
    
    df=pd.DataFrame({'tipo':tipo,'latitud':latitud,'logitud':longitud})

    

    mapa = Map(location=[lat,lon],zoom_start=15)

    empresa = {
            "location":[lat, lon ],
            "tooltip" : "Empresa"
        }
    icon = Icon(color = "red",
                        prefix = "fa",
                        icon = "fa-dot-circle-o",
                        icon_color = "white"
            )
    Marker(**empresa,icon = icon ).add_to(mapa)


    for i, row in df.iterrows():
        establecimiento = {
            "location":[row["latitud"], row["logitud"]],
            "tooltip" : row["tipo"].replace("_"," ").capitalize()
        }

        if row["tipo"] == "starbucks":
            icon = Icon(color = "green",
                        prefix = "fa",
                        icon = "fa-coffee",
                        icon_color = "white"
            )
            
        elif row["tipo"] == "restaurante_vegano":
            icon = Icon(color = "green",
                        prefix = "fa",
                        icon = "leaf",
                        icon_color = "black"
            )

        elif row["tipo"] == "colegio":
            icon = Icon(color = "blue",
                        prefix = "fa",
                        icon = "fa-graduation-cap ",
                        icon_color = "black"
            )
        
        elif row["tipo"] == "peluqueria_perros":
            icon = Icon(color = "red",
                        prefix = "fa",
                        icon = "fa-paw",
                        icon_color = "black"
            )

        elif row["tipo"] == "estadio_de_baloncesto":
            icon = Icon(color = "orange",
                        prefix = "fa",
                        icon = "fa-futbol-o ",
                        icon_color = "black"
            )

        elif row["tipo"] == "aeropuerto":
            icon = Icon(color = "white",
                        prefix = "fa",
                        icon = "fa-plane",
                        icon_color = "black"
            )
        elif row["tipo"] == "bar":
            icon = Icon(color = "pink",
                        prefix = "fa",
                        icon = "fa-glass",
                        icon_color = "white"
            )
            
        else:
                        prefix = "fa",
                        icon = "briefcase",
                        icon_color = "black"            
        Marker(**establecimiento,icon = icon ).add_to(mapa)
    return mapa

def imprime_kepler(df):
    """
    no lo he podido utilizar
    """
    map_kepler= KeplerGl(height=700, weight = 500, data={'Empresas': df})
    map_kepler
#show the map