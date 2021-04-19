from lib_mongo import companies_tec_1M_mongo, companies_design 
from lib_calculus import  quita_office_null, quita_repes
from lib_pandas import calculate_inv_distances_df,calculate_inv_distances_indv
from lib_api import foursquare


def ranking1M(nombre):
    """
    lee de la bd de mongo todas las empresas de 1M y valora cuanto de cerca está de otras empresas
    el valor lo almacena en el campo "nombre"

    nombres es una string
    """
    lcompanies = companies_tec_1M_mongo("geoproyect",nombre)
    loffices  = quita_office_null(lcompanies)
    loffice_norepe = quita_repes(loffices)
    l_roffice = calculate_inv_distances_df(loffice_norepe,loffices,nombre.strip())

    return(l_roffice)

def ranking_design(lista_oficinas,nombre):
    """
    Esta fución toma la lista  de oficinas y consulta la base de datos las empresas de diseño y las compara 
    asigna a cada oficina de la lista un valor en  el campo "nombre"
    
    lista_oficinas: lista de oficinas con sus coordenadas
    nombre:nombre que le damos al campo.
    develve la misma lista con el campo actualizado.
    """
    ldesign = companies_design("geoproyect","companies")
    ldesign_no_null = quita_office_null(ldesign)
    l_rdesign = calculate_inv_distances_df(lista_oficinas,ldesign_no_null,nombre.strip())   
    return l_rdesign

def ranking_foursquares(candidatos,busqueda,n): 
    """
    esta función toma la lista candidatos, realiza una búsqueda en Fs con "n" máxio resultados.
    pondera estos resultados en función de la distancia a cada candidato y añade un nuevo campo con el mismo nombre de busqueda
    con este valor
    candidatos: lista con coordenadas.
    busqueda: string 
    n: int
    devuelve la lista de candidatos actualizada con el campo "busqueda"
    """
    for i, ofi in enumerate(candidatos):
        lista_fs=foursquare(ofi,busqueda,n) 
        busque_no_espacios=busqueda.replace(" ","_")
        candidatos[i][busque_no_espacios]=calculate_inv_distances_indv(ofi,lista_fs)
        
    
    return candidatos
