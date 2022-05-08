# test_sogeti

This python project aims to :
- create within a database two tables: people and places
- feed these tables via csv files
- transform the queried data by sql query to count the number of births by region and by department, to finally write the result in a json file

For ease of implementation, we use the sqlite3 library for the sql part and the json library for writing to file