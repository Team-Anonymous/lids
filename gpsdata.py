import serial
import pynmea2
def loc():
	z=0;
	while z<=5:
		serialStream = serial.Serial("/dev/ttyS0", 9600, timeout=1)
		sentence = serialStream.readline()
		z+=1
		if sentence.find('GGA') > 0:
			data = pynmea2.parse(sentence)
 			return([str(data.latitude),str(data.longitude)])
