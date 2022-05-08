# test_sogeti

This python project aims to :
- **create** within a database two tables: personnes and lieux = **create_tables.py**
- **feed** these tables via csv files = **insert_data.py**
- **transform** the queried data by sql to count the number of births by region and by department, to finally write the result in a json file = **data_transformation.py**

For ease of implementation, we use the **sqlite3** library for the sql part and the **json** library for writing to file

## Acknowledgments

There are cases where the **same city name** refers to cities in **different departments or regions** in the source data. 
e.g. Saint-Denis in Ile de France and Reunion
=> Risk of distorted results