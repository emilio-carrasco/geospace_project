
from lib_mongo import companies_tec_1M_mongo,companies_design

from lib_calculus import latlon2pnt, flat_latlon, latlon_dist,une_rate_oficinas
from lib_pandas import create_distance_df,calculate_inv_distances_df
from lib_api import foursquare
def ranking1M():
    list_companies = companies_tec_1M_mongo("geoproyect","companies")
    lista_officinas_latlon = flat_latlon(list_companies)
    list_rate_distance = calculate_inv_distances_df(lista_officinas_latlon,lista_officinas_latlon,True)
    return(une_rate_oficinas(lista_officinas_latlon,list_rate_distance,'dist1m'))

def ranking_design(lista_oficinas):
    lista_design = companies_design("geoproyect","companies")
    lista_design_latlon = flat_latlon(lista_design)
    list_design = calculate_inv_distances_df(lista_oficinas,lista_design_latlon,False)
    return(une_rate_oficinas(lista_oficinas,list_design,'design'))

def ranking_foursquares(lista_oficinas,busqueda):
    lista_fs_ranking=[]
    for i,ofi in enumerate(lista_oficinas):
        lista_fs=foursquare(ofi,"starbucks",50)
        lista_fs_ranking.append(calculate_inv_distances_df([ofi],lista_fs,False))

    return (une_rate_oficinas(lista_oficinas,lista_fs_ranking,busqueda))