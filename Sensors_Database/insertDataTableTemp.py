import sqlite3
import sys
conn=sqlite3.connect('sensorsData.db')
curs=conn.cursor()
# function to insert data on a table
def add_data (temp):
    curs.execute("INSERT INTO Temp_data values(datetime('now'), (?))", (temp,))
    conn.commit()
# call the function to insert data
add_data (20.5)
add_data (25.8)
add_data (30.3)
# print database content
print ("\nEntire database contents:\n")
for row in curs.execute("SELECT * FROM Temp_data"):
    print (row)
# close the database after use
conn.close()
