# -*- coding: utf-8 -*-

import sqlite3, json

con = sqlite3.connect("test_database")
cur = con.cursor()

### SQL queries ###

query_departement = '''
                    SELECT departement, count(*) 
                    from personnes left join lieux 
                    on personnes.commune = lieux.commune 
                    group by departement 
                    order by departement ASC;
                    '''

query_region = '''
                SELECT region, count(*) 
                from personnes left join lieux 
                on personnes.commune = lieux.commune 
                group by region 
                order by region ASC;
                '''


def query_to_result(query):
    """
    Transformation of the result of the sql query into a dictionary 
    for ingestion in json file

    Parameters
    ----------
    query : str
        SQL query

    Returns
    -------
    result : dict
        dict of the query results, where keys = region/departement
        and values = birth count

    """

    dict_result = {}

    def tup_to_dict(tup, dic):
        dic = dict(tup)
        return dic

    cur.execute(query)
    data = cur.fetchall()
    result = tup_to_dict(data, dict_result)
    return result


def write_to_json(file_name, result):
    """
    Write dict results to json file

    Parameters
    ----------
    file_name : str
        Name of the output json file 

    result : dict
        Use query_to_result function that returns a dictionary 
        from the result of the sql query

    Returns
    -------
    None.

    """
    with open("target\\"+file_name+".json", 'w', encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False)


write_to_json("departement", query_to_result(query_departement))
write_to_json("region", query_to_result(query_region))

con.commit()
con.close()
