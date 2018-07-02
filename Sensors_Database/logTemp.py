import time
import sqlite3
import serial
dbname='sensorsData.db'
sampleFreq = 1*30 # time in seconds ==> Sample each 30 s
ser = serial.Serial(port='/dev/ttyACM0', baudrate=9600, parity=serial.PARITY_NONE,
stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS, timeout=1)

# get data from DHT sensor
def getTempdata():
    x=ser.readline()#dump the first reading
    x=ser.readline()
    temp=x.decode('utf-8')#decode to numbers
    if temp is not None:
        temp = round(float(temp), 2)
        return temp
# log sensor data on database
def logData (temp):
        conn=sqlite3.connect(dbname)
        curs=conn.cursor()
        curs.execute("INSERT INTO Temp_data values(datetime('now'), (?))", (temp,))
        conn.commit()
        conn.close()
# main function
def main():
        while True:
            temp = getTempdata()
            logData (temp)
            time.sleep(sampleFreq)
# ------------ Execute program 
main()
