import pandas as pd

from lib_calculus import latlon_dist

def create_distance_df(la,lb):
    d = pd.DataFrame(float(0), index=range(len(lb)), columns=range(len(la))) 
    return d


def calculate_inv_distances_df(la,lb,auto):
    df = create_distance_df(la,lb)
    for ir,r in enumerate(lb):
        for ic, c in enumerate(la):
            if auto and r == c:
                df[ir][ic] = 0 ###hay que quitarlo
            else:
                try:
                    a = c['tipo_p']['coordinates']              
                    b = r['tipo_p']['coordinates']
                    d = latlon_dist(a,b)
                    df[ic][ir] = 10/(d+1)
                except:
                    df[ic][ir] = 0
    
    if len(la)>1:
        return list(df.sum(axis = 0))
    else:
        return float(df.sum(axis = 0))

