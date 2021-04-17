from pymongo import MongoClient
import pandas as pd

def companies_tec_1M_mongo(database,col):  
    """
    This function takes a db and a collection as strings and returns a
    df with all names of companies with all it office coordinates.

    Some of them might be junk.

    database: string
    col: string
    
    returns df
    """
    client =MongoClient("localhost:27017")
    db = client.get_database(database)
    c = db.get_collection(col)
    db.list_collection_names()

    cond_tec = { "tag_list": { "$regex": "tech" } }
    cond_1M = { "total_money_raised": { "$regex": "M" } }
    cond_design = {"tag_list": { "$regex": "design" }}

    cond_no_muerta = {"deadpooled_year": { "$in": [{"type": 10}, None] }}

    cond_1M_and_tec_nomuerta={"$and": [cond_tec, cond_1M, cond_no_muerta]}
    cond_design_no_muerta={"$and": [cond_no_muerta,cond_design]}

    proy={"_id":0, "name":1, "offices.latitude":1, "offices.longitude":1}

    comp_1M_tec=list(c.find(cond_1M_and_tec_nomuerta,proy))    
    return [ c['offices'] for c in comp_1M_tec]

def companies_design(database,col):  
    """
    This function takes a db and a collection as strings and returns a
    df with all names of companies with all it office coordinates.

    Some of them might be junk.

    database: string
    col: string
    
    returns df
    """
    client =MongoClient("localhost:27017")
    db = client.get_database(database)
    c = db.get_collection(col)
    db.list_collection_names()
    cond_design = {"tag_list": { "$regex": "design" }}
    cond_no_muerta = {"deadpooled_year": { "$in": [{"type": 10}, None] }}
    cond_design_no_muerta={"$and": [cond_no_muerta,cond_design]}

    proy={"_id":0, "offices.latitude":1, "offices.longitude":1}
    comp_desgin=list(c.find(cond_design_no_muerta,proy))
    return [ c['offices'] for c in comp_desgin]