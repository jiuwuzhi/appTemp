import sqlite3 as lite
import sys
con = lite.connect('sensorsData.db')
with con: 
    cur = con.cursor() 
    cur.execute("DROP TABLE IF EXISTS Temp_data")
    cur.execute("CREATE TABLE Temp_data(timestamp DATETIME, temp NUMERIC)")
