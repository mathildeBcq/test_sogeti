# -*- coding: utf-8 -*-

import csv, sqlite3

con = sqlite3.connect("test_database")
cur = con.cursor()


def get_data(file):
    """
    Gets data from CSV file

    Parameters
    ----------
    file : str
    The file location of the csv

    Returns
    -------
    data : orderedDict
    Each lines produce a dict where keys are column name

    """
    with open(file, "r", encoding="utf-8") as f:
        data = csv.DictReader(f)
        return data


personnes_data = get_data(
    "resources\\people.csv")
lieux_data = get_data(
    "resources\\lieux.csv")

### Values per field ###

to_personnes = [(i['prenom'],
                 i['nom'],
                 i["date-naissance"],
                 i["commune"])
                for i in personnes_data]

to_lieux = [(i['commune'],
             i['departement'],
             i["region"])
            for i in lieux_data]

### SQL ingestion instruction ###

cur.executemany('''
                INSERT INTO personnes 
                (prenom, nom, date_naissance, commune) 
                VALUES (?, ?, ?, ?);
                ''',
                to_personnes)

cur.executemany('''
                INSERT INTO lieux 
                (commune, departement, region) 
                VALUES (?, ?, ?);
                ''',
                to_lieux)

con.commit()
con.close()
