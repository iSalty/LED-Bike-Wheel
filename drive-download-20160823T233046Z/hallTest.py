import RPi.GPIO as GPIO
import io
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(5, GPIO.IN)
[red, green, blue, power] = [16, 20, 21, 12]
GPIO.setup(red, GPIO.OUT)   #Red
GPIO.setup(green, GPIO.OUT) #Green
GPIO.setup(blue, GPIO.OUT)  #Blue
GPIO.setup(power, GPIO.OUT) #Power

GPIO.output(red, 0)
GPIO.output(green, 1)
GPIO.output(blue, 1)
GPIO.output(power, 1)
time.sleep(1)
try :
    print "Entered Loop."
    while True :
        GPIO.output(red, 0)
        GPIO.output(green, 1)
        GPIO.output(blue, 1)
        GPIO.output(power, 1)
        
        if GPIO.input(5) == False : #if sensor goes LOW shut off LED for 1 sec
            GPIO.output(power, 0)
            time.sleep(.05)

        print GPIO.input(5)
        time.sleep(.05)
        
except KeyboardInterrupt :
    pass

GPIO.cleanup()
