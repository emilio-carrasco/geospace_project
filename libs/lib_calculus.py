from math import radians
from math import sin, cos, atan2, sqrt
from functools import reduce


def latlon2pnt(flat_list):
    return list(map(celda_latlon2pnt, flat_list))

def latlon_dist(latlon1,latlon2):
    """
    Devuelve la distancia entre dos puntos según su longitud y latitud.

    latlon1 y latlon2 listas [latitud y longitud] en grados.
    
    return distancia en kms.
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
    """
    esta función normaliza todos los valores de la lista cuyos campos se encuentren en "filtros".
    Escala el resultado a 100:valor máximo.

    devuelve la misma lista con valores escalados
    """
    for f in filtros:
        maximo=reduce(lambda x,y:max(x,y),[l[f] for l in lista])
        for l in lista:
            f_Strip=f.strip()
            l[f]=round(100*l[f]/(maximo+1),2)
    return lista       

def selector(lista,**pesos):
    """
    esta función pondera cada uno de los campos de lista por el contenido de "pesos"

    al salir realiza una nueva normalización.
    """
    lista_out=[]
    for i,l in enumerate(lista):
        score=0
        for k,v in pesos.items():
            score+=round(l[k]*v/100,2)  
        l['score']=score
        lista_out.append(l)

    return(score_normalizer(lista_out,"score"))

def top(n,l,campo):
    """
    esta función escoge los n mejores elementos de la lista l atendiendo al campo 

    devuelve una lista similar pero con n elementos
    """
    l_ordenata = sorted(l, reverse=True, key=lambda k: k[campo]) 
    return l_ordenata[0:n]

def quita_office_null(lista):
    """
    esta función elimina las oficinas cuyas coordenadas no están completas.

    devulve la misma lista pero desglosando cada empresa en  sus diferentes oficinas. para diferenciar
    cada oficina añade el campo "office_numb'
    """
    lista_out=list()
    for l in lista:  
        for i,oficina in enumerate(l['offices']):
            if  (oficina['latitude'] != None)  and  (oficina['longitude'] != None):
                lista_out.append({'name':l['name'], 'office_numb':i+1, 'latitud': oficina['latitude'], 'longitud':oficina['longitude'] })

    return(lista_out)

def quita_repes(lista):
    """
    esta función elimina las compañías que está muy cerca y se queda con una.

    en vez de hacer el calculo exacto de la distancia hacemos la aproximación 
    de que el radio de la tierra es mucho mayor que la distancia con la que trabajamos.

    lista: lista de empresas con campos de latitud y longitud.

    return la misma lista con la algunas oficinas muy cercanas filtradas
    """
    l_out=[lista[0]]
    for l in lista:
        esta= False
        for k in l_out:
            if (abs(l['latitud']-k['latitud']))<0.25 and (abs(l['longitud']-k['longitud']))<0.25:
                esta= True
                break
        
        if not esta :
            l_out.append(l)
    return l_out









