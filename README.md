# test_sogeti

This python project aims to :
- **create** within a database two tables: personnes and lieux
- **feed** these tables via csv files
- **transform** the queried data by sql to count the number of births by region and by department, to finally write the result in a json file

For ease of implementation, we use the **sqlite3** library for the sql part and the **json** library for writing to file

## Acknowledgments

There are cases where the **same city name** refers to cities in **different departments or regions** in the source data. 
e.g. Saint-Denis in Ile de France and Reunion
=> Risk of distorted results