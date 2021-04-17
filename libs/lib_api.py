import requests
import json
from dotenv import load_dotenv
import os
from time import sleep
from functools import reduce
import operator

load_dotenv()

def getFromDict(diccionario,mapa):
    return reduce(operator.getitem,mapa,diccionario)

def foursquare(coord,query,limit):
    _id= os.getenv("fstoken1")
    secret= os.getenv("fstoken2")

    url_query = 'https://api.foursquare.com/v2/venues/explore'
    parametros = {
                    "client_id": _id,
                    "client_secret": secret,
                    "v": "20180323",
                    "ll": f"{coord['tipo_p']['coordinates'][0]},{coord['tipo_p']['coordinates'][1]}",
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
        dato=dict()
        paralista = {}
        paralista['type']="Point"
        paralista["coordinates"]= [getFromDict(dic, mapa_latitud), getFromDict(dic,mapa_longitud)]
        dato['tipo_p']=paralista
        lista_busqueda.append(dato)
    return lista_busqueda