import requests
import json
from dotenv import load_dotenv
import os
from time import sleep
from functools import reduce
import operator

load_dotenv()

def getFromDict(diccionario,mapa):
    """
    Nos permite bucear por el "diccionario" usando las strings contenidas en la lista "mapa"

    diccionario: dict
    mapa: lista de strings con la ruta a bucear


    return: elemento final tras la ruta.
    """
    return reduce(operator.getitem,mapa,diccionario)

def foursquare(coord,query,limit):
    """
    Esta funcion toma unas coordenadas y una petición para foursquare. La realiza con el límite que le pasemos.
    Tenemos que tener los tokens en el archivo .env 
                _id ---> fstoken1
            secret  ----> fstoken2
    Nos devuelve la lista con los resultados de latitus y longitus por campos.

    coord: diccionario con campos 'latitud' y 'longitud'
    query: string con la busqueda de foursquare
    limit: límite máximo de resultados a FS.

    """

    _id= os.getenv("fstoken1")
    secret= os.getenv("fstoken2")

    url_query = 'https://api.foursquare.com/v2/venues/explore'
    parametros = {
                    "client_id": _id,
                    "client_secret": secret,
                    "v": "20180323",
                    "ll": f"{coord['latitud']},{coord['longitud']}",
                    "query": query, 
                    "limit": limit   
                }
    
    sleep(1)
    resp = requests.get(url= url_query, params = parametros).json()

    data = resp.get("response").get("groups")[0].get("items")

    mapa_latitud = ["venue", "location", "lat"]
    mapa_longitud = ["venue", "location", "lng"]

    lista_busqueda = []

    for dic in data:
        paralista = {}
        #paralista['type']="Point"
        paralista["latitud"]= getFromDict(dic, mapa_latitud) 
        paralista["longitud"] =getFromDict(dic, mapa_longitud)
        lista_busqueda.append(paralista)
    return lista_busqueda


    
def foursquare_visual(coord,query):
    """
    Esta funcion toma unas coordenadas y una petición para foursquare. La realiza con el límite que le pasemos.
    Tenemos que tener los tokens en el archivo .env 
                _id ---> fstoken1
            secret  ----> fstoken2
    Nos devuelve la lista con los resultados de latitus y longitus por campos. Limitado a 25 y en un radio de 5km

    coord: diccionario con campos 'latitud' y 'longitud'
    query: string con la busqueda de foursquare


    """
    _id= os.getenv("fstoken1")
    secret= os.getenv("fstoken2")

    url_query = 'https://api.foursquare.com/v2/venues/explore'
    parametros = {
                    "client_id": _id,
                    "client_secret": secret,
                    "v": "20180323",
                    "radius":5000,
                    "ll": f"{coord['latitud']},{coord['longitud']}",
                    "query": query, 
                    "limit": 25  

                }
    
    sleep(1)
    resp = requests.get(url= url_query, params = parametros).json()
    data = resp.get("response").get("groups")[0].get("items")

    mapa_latitud = ["venue", "location", "lat"]
    mapa_longitud = ["venue", "location", "lng"]

    lista_busqueda = []

    for dic in data:
        paralista = {}
        #paralista['type']="Point"
        paralista["latitud"]= getFromDict(dic, mapa_latitud) 
        paralista["longitud"] =getFromDict(dic, mapa_longitud)
        lista_busqueda.append(paralista)
    return lista_busqueda