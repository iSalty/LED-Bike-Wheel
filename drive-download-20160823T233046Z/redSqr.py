#Program to hard code red square onto the bike wheel
import RPi.GPIO as GPIO
import io
import time
import subprocess

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

RPM = 130.0           #10 mph
#Calculating relevant values from the RPM
RPS = RPM / 60.0
DegPS = RPS * 360.0
SPDeg = 1 / DegPS

#Function to address LEDs
def addrOne() :
    red = 16
    green = 20
    blue = 21
    power = 12

    GPIO.setup(red, GPIO.OUT)   #Red
    GPIO.setup(green, GPIO.OUT) #Green
    GPIO.setup(blue, GPIO.OUT)  #Blue
    GPIO.setup(power, GPIO.OUT) #Power

    return red, green, blue, power

def addrTwo() :
    red = 2
    green = 3
    blue = 4
    power = 17

    GPIO.setup(red, GPIO.OUT)   #Red
    GPIO.setup(green, GPIO.OUT) #Green
    GPIO.setup(blue, GPIO.OUT)  #Blue
    GPIO.setup(power, GPIO.OUT) #Power

    return red, green, blue, power

#Function to prompt a user input given a prompt string
def prompt(promptStr) :
    x = raw_input(promptStr)
    return x

#Function to call a specific color for a given number of degrees of rotation
def Red(r, g, b, p, d) :
    red = r
    green = g
    blue = b
    power = p
    deg = d
    
    GPIO.output(power, 1)
    GPIO.output(red, 0)
    GPIO.output(green, 1)
    GPIO.output(blue, 1)
    
    sec = deg * SPDeg       #Calculates time in seconds for a given number of degrees d
    time.sleep(sec)

def Green(r, g, b, p, d) :
    red = r
    green = g
    blue = b
    power = p
    deg = d

    GPIO.output(power, 1)
    GPIO.output(red, 1)
    GPIO.output(green, 0)
    GPIO.output(blue, 1)

    sec = deg * SPDeg       #Calculates time in seconds for a given number of degrees d
    time.sleep(sec)

def Blue(r, g, b, p, d) :
    red = r
    green = g
    blue = b
    power = p
    deg = d

    GPIO.output(power, 1)
    GPIO.output(red, 1)
    GPIO.output(green, 1)
    GPIO.output(blue, 0)

    sec = deg * SPDeg       #Calculates time in seconds for a given number of degrees d
    time.sleep(sec)

def Yellow(r, g, b, p, d) :
    red = r
    green = g
    blue = b
    power = p
    deg = d

    GPIO.output(power, 1)
    GPIO.output(red, 0)
    GPIO.output(green, 0)
    GPIO.output(blue, 1)

    sec = deg * SPDeg       #Calculates time in seconds for a given number of degrees d
    time.sleep(sec)

def Purple(r, g, b, p, d) :
    red = r
    green = g
    blue = b
    power = p
    deg = d

    GPIO.output(power, 1)
    GPIO.output(red, 0)
    GPIO.output(green, 1)
    GPIO.output(blue, 0)

    sec = deg * SPDeg       #Calculates time in seconds for a given number of degrees d
    time.sleep(sec)

def Cyan(r, g, b, p, d) :
    red = r
    green = g
    blue = b
    power = p
    deg = d

    GPIO.output(power, 1)
    GPIO.output(red, 1)
    GPIO.output(green, 0)
    GPIO.output(blue, 0)

    sec = deg * SPDeg       #Calculates time in seconds for a given number of degrees d
    time.sleep(sec)

def White(r, g, b, p, d) :
    red = r
    green = g
    blue = b
    power = p
    deg = d

    GPIO.output(power, 1)
    GPIO.output(red, 0)
    GPIO.output(green, 0)
    GPIO.output(blue, 0)

    sec = deg * SPDeg       #Calculates time in seconds for a given number of degrees d
    time.sleep(sec)

def Off(r, g, b, p, d) :
    red = r
    green = g
    blue = b
    power = p
    deg = d

    GPIO.output(power, 0)
    GPIO.output(red, 0)
    GPIO.output(green, 0)
    GPIO.output(blue, 0)

    sec = deg * SPDeg       #Calculates time in seconds for a given number of degrees d
    time.sleep(sec)

#---- MAIN FUNCTION ----#
#get addresses of the LEDs and save into r#,g#,b#,p# vars
[r1, g1, b1, p1] = addrOne()
[r2, g2, b2, p2] = addrTwo()

print SPDeg
print "Use Ctrl-C to exit program"

try :
    while True :

        Red(r1, g1, b1, p1, 90)
        Yellow(r1, g1, b1, p1, 90)
        Green(r1, g1, b1, p1, 90)
        Cyan(r1, g1, b1, p1, 90)
        Blue(r1, g1, b1, p1, 90)
        Purple(r1, g1, b1, p1, 90)

except KeyboardInterrupt :
    pass

GPIO.cleanup()
