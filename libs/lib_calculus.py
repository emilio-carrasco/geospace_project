from math import radians
from math import sin, cos, atan2, sqrt

def celda_latlon2pnt(lista):
    return[{"type":"Point", "coordinates": d} for d in lista]

def latlon2pnt(flat_list):
    return list(map(celda_latlon2pnt, flat_list))

def flat_latlon(list_):
    lista=[]
    for sublist in list_:            
            for item in sublist:
                if item!=[] and (item['latitude'] is not None) and  (item['longitude'] is not None):
                    tipo_point = {"type":"Point", "coordinates": [item['latitude'], item['longitude']]}
                    lista.append(tipo_point)
    lista_coordenadas = [{'tipo_p':l}    for l in lista]
    
    return lista_coordenadas


def latlon_dist(latlon1,latlon2):
    """
    This functions returns the distance between 2 points with its coordinates
    in lat long.
    latlon1,latlong2: list[lat,long]
    
    return distance in km
    """
  
    lat1=radians(latlon1[0])
    lon1=radians(latlon1[1])

    lat2=radians(latlon2[0])
    lon2=radians(latlon2[1])

    R = 6373.0

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    return R * c 

def une_rate_oficinas(list_oficinas,list_ranking,name_):
    for i,r in enumerate(list_ranking):
        list_oficinas[i][name_]=round(r,2)

    return(list_oficinas)