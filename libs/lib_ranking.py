from lib_mongo import companies_tec_1M_mongo, companies_design 
from lib_calculus import  quita_office_null, quita_repes
from lib_pandas import calculate_inv_distances_df,calculate_inv_distances_indv
from lib_api import foursquare


def ranking1M(nombre):
    lcompanies = companies_tec_1M_mongo("geoproyect","companies")
    loffices  = quita_office_null(lcompanies)
    loffice_norepe = quita_repes(loffices)
    l_roffice = calculate_inv_distances_df(loffice_norepe,loffices,nombre.strip())

    return(l_roffice)

def ranking_design(lista_oficinas,nombre):
    ldesign = companies_design("geoproyect","companies")
    ldesign_no_null = quita_office_null(ldesign)
    l_rdesign = calculate_inv_distances_df(lista_oficinas,ldesign_no_null,nombre.strip())   
    return l_rdesign

def ranking_foursquares(candidatos,busqueda,n): 
    for i, ofi in enumerate(candidatos):
        lista_fs=foursquare(ofi,busqueda,n) 
        busque_no_espacios=busqueda.replace(" ","_")
        candidatos[i][busque_no_espacios]=calculate_inv_distances_indv(ofi,lista_fs)
        
    
    return candidatos
