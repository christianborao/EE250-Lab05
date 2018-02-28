
import time

# Import SPI library (for hardware SPI) and MCP3008 library.
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008

# Hardware SPI configuration:
SPI_PORT   = 0
SPI_DEVICE = 0
mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))

led_pin = 2 #pin LED is connected to
light_pin = 0 #pin light sensor is connected to
sound_pin = 1 #pin that sound sensor is connected to

def Main():

	while True: 
	
		for x in range(10):
			#turn the LED on and off five times
			if (x % 2 == 0):
				GPIO.output(led_pin, GPIO.HIGH) #LED on
		
			else: 
				GPIO.output(led_pin, GPIO.LOW)

			time.sleep(0.25) #delay for 250 ms

		for x in range(50): #read light sensor every 100ms for 5 seconds

			#obtain the output of the Grove light sensor:
			light_data = mcp.read_adc(light_pin)

			#print out the output:
			print("Light level: " + str(light_data))

			#if output is less than 400 threshold, print "dark"
			if (light < 400):
				print("dark")
		
			#else, print "bright"
			else:
				print("bright")

			#delay 100ms
			time.sleep(0.1)

		for x in range(8):
			if (x % 2 == 0):
				GPIO.output(led_pin, GPIO.HIGH) #turn LED on
			else:
				GPIO.output(led_pin, GPIO.LOW) #turn LED off

			#delay 100ms
			time.sleep(0.1)

		for x in range(50):

			#read output of sound sensor:
			sound_data = mcp.read_adc(sound_pin)

			#print output:
			print("Sound level: " + str(sound_data))

			if (sound_data > 300):
				GPIO.output(led_pin, GPIO.HIGH) #LED on
				time.sleep(0.1) #delay for 100ms
				GPIO.output(led_pin, GPIO.LOW) #LED off
			else:
				time.sleep(0.1) #delay for 100ms

		for x in range(8):
			if (x % 2 == 0):
				GPIO.output(led_pin, GPIO.HIGH) #LED on
			else:
				GPIO.output(led_pin, GPIO.LOW) #LED off
			time.sleep(0.1) #delay 100ms

if __name__ == '__main__':
		Main()

