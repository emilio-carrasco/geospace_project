import pandas as pd
import json
import geopandas

from lib_calculus import latlon_dist



def list2pandas(lista):
    df=dict()
    for key,value in lista[0].items():
        df[key]=list()
        for l in lista:
            df[key].append(l[key])
    return pd.DataFrame(df)

def create_distance_df(la,lb):
    d = pd.DataFrame(float(0), index=range(len(lb)), columns=range(len(la))) 
    return d

def calculate_inv_distances_df(la,lb,nombre,auto=False): 
    l_out=la
    
    df = create_distance_df(la,lb)
    for ir,r in enumerate(lb):
        for ic, c in enumerate(la):
            if auto and r == c:
                df[ir][ic] = 0 
            else:
                try:
                    a = [c['latitud'],c['longitud']]           
                    b = [r['latitud'],r['longitud']]         
                    d = latlon_dist(a,b)
                    df[ic][ir] = round(100/(d+1)**2,1)
                   
                except:
                    df[ic][ir] = 0
    
    
    lista_datos=list(df.sum(axis = 0))

    for i,dato in enumerate(lista_datos):
        l_out[i][nombre]= round(dato,2)
    return l_out

def calculate_inv_distances_indv(ofi,lb): 
    l_out=list()
    for r in lb:
        a = [ofi['latitud'],ofi['longitud']]           
        b = [r['latitud'],r['longitud']]         
        d = latlon_dist(a,b)
        score = round(100/(d+1)**2,1)
        l_out.append(score)
    return round(sum(l_out),2)

def lee_geodf(data):

    df=list2pandas(data)
    df.rename(columns={'latitud':'latitude','longitud':'longitude'},inplace=True)
    gdf = geopandas.GeoDataFrame(df, geometry=geopandas.points_from_xy(df.latitude, df.longitude))
    return gdf