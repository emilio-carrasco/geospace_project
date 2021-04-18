from math import radians
from math import sin, cos, atan2, sqrt
from functools import reduce


def latlon2pnt(flat_list):
    return list(map(celda_latlon2pnt, flat_list))



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


def score_normalizer(lista,*filtros):
    for f in filtros:
        maximo=reduce(lambda x,y:max(x,y),[l[f] for l in lista])
        for l in lista:
            f_Strip=f.strip()
            l[f]=round(100*l[f]/(maximo+1),2)

    return lista       

def selector(lista,**pesos):
    lista_out=[]
    for i,l in enumerate(lista):
        score=0

        for k,v in pesos.items():

            score+=round(l[k]*v/100,2)  
        l['score']=score
        lista_out.append(l)

    return(score_normalizer(lista_out,"score"))

def top(n,l,campo):
    l_ordenata = sorted(l, reverse=True, key=lambda k: k[campo]) 
    return l_ordenata[0:n]

def quita_office_null(lista):
    lista_out=list()
    for l in lista:  
        for i,oficina in enumerate(l['offices']):
            if  (oficina['latitude'] != None)  and  (oficina['longitude'] != None):
                lista_out.append({'name':l['name'], 'office_numb':i+1, 'latitud': oficina['latitude'], 'longitud':oficina['longitude'] })

    return(lista_out)

def quita_repes(lista):
    l_out=[lista[0]]
    for l in lista:

        esta= False
        for k in l_out:
            if (abs(l['latitud']-k['latitud']))<0.3 and (abs(l['longitud']-k['longitud']))<0.3:
                esta= True
                break
        
        if not esta :
            l_out.append(l)
    return l_out









