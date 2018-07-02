# appTemp
Using LM35 as the analog temperature sensor;

Through the internal 10-bit ADC of Arduino Uno;

Transferring the temperature data to a Rapsberry Pi 3 B;

Logging the data into a SQLite 3 database.

**logTemp.py** ------ Main file
**sensorsData.db** ------ Database file
**out.csv** ------ csv file, contains all the temperature data that logged in my lab from June 30th to July 1st, 2018.  

Shawn@mtu, June 2018

*Modified from this link: http://www.instructables.com/id/From-Data-to-Graph-a-Web-Jorney-With-Flask-and-SQL/
