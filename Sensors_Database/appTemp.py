import time
import sqlite3
import serial

dbname = 'sensorsData.db'
sampleFreq = 1 # time in seconds
ser = serial.Serial(port='/dev/ttyACM0', baudrate=9600, parity=serial.PARITY_NONE,
stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS, timeout=1)

# get data from DHT sensor
def getTempdata():
    x=ser.readline()#dump the first reading
    x=ser.readline()
    temp=x.decode('utf-8')#decode to numbers
    if temp is not None:
        temp = round(float(temp), 2)
        logData (temp)

# log sensor data on database
def logData (temp):
    conn=sqlite3.connect(dbname)
    curs=conn.cursor()
    curs.execute("INSERT INTO Temp_data values(datetime('now'), (?))", (temp,))
    conn.commit()
    conn.close()

# display database data
def displayData():
    conn=sqlite3.connect(dbname)
    curs=conn.cursor()
    print ("\nEntire database contents:\n")
    for row in curs.execute("SELECT * FROM Temp_data"):
        print (row)
    conn.close()

# main function
def main():
    for i in range (0,10):
        getTempdata()
        time.sleep(sampleFreq)
displayData()

# Execute program 
main()
