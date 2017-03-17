import serial
import MySQLdb
import time

#returns ms since the epoch
def millis():
        return time.time() * 1000


ser = serial.Serial('/dev/ttyACM0', 9600)

actual=millis()
ser.write("a");
ser.write("a");
ser.write("a");
ser.write("a");
ser.write("a");

while actual+5000>millis():
	print("ESPErando")

db = MySQLdb.connect("localhost", "root", "root", "experimientos")
curs=db.cursor()
actual=millis()
a=input("Ingrese el numero del experimento")
ser.write("b");
j=0
while actual+5000>millis():
	x=ser.readline()
	print x
	s=x.split(",")
	if len(s)==4:
		curs.execute("INSERT INTO ejemplo values("+str(a)+",'"+s[0]+"','"+s[1]+"','"+s[2]+"','"+s[3]+"')")
		db.commit()
		j=j+1
print str(j)
