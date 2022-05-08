# -*- coding: utf-8 -*-

import sqlite3

con = sqlite3.connect("test_database")
cur = con.cursor()

cur.execute('''
          CREATE TABLE IF NOT EXISTS lieux
          (commune TEXT, 
           departement TEXT,
           region TEXT)
          ''')

cur.execute('''
          CREATE TABLE IF NOT EXISTS personnes
          (prenom TEXT, 
           nom TEXT,
           date_naissance DATE,
           commune TEXT)
          ''')

con.commit()
con.close()
