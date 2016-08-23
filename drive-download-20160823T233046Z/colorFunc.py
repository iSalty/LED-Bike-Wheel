#Program that addresses 2 LEDs and a cetain sequence of colors RYGCBP
import RPi.GPIO as GPIO
import io
import time
import curses
import subprocess

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

#Functions which contain BCM Addresses for LEDs
def adrOne() :
    red = 16   
    green = 20
    blue = 21
    power = 12

    GPIO.setup(red, GPIO.OUT)   #Red
    GPIO.setup(green, GPIO.OUT) #Green
    GPIO.setup(blue, GPIO.OUT)  #Blue
    GPIO.setup(power, GPIO.OUT) #Power

    return red, green, blue, power

def adrTwo() :
    red = 2     
    green = 3
    blue = 4
    power = 17

    GPIO.setup(red, GPIO.OUT)   #Red
    GPIO.setup(green, GPIO.OUT) #Green
    GPIO.setup(blue, GPIO.OUT)  #Blue
    GPIO.setup(power, GPIO.OUT) #Power

    return red, green, blue, power

#Defining functions for each color
def Red(r, g, b, p) :
    red = r
    green = g
    blue = b
    power = p

    GPIO.output(power, 1)
    GPIO.output(red, 0)
    GPIO.output(green, 1)
    GPIO.output(blue, 1)

def Green(r, g, b, p) :
    red = r
    green = g
    blue = b
    power = p

    GPIO.output(power, 1)
    GPIO.output(red, 1)
    GPIO.output(green, 0)
    GPIO.output(blue, 1)

def Blue(r, g, b, p) :
    red = r
    green = g
    blue = b
    power = p

    GPIO.output(power, 1)
    GPIO.output(red, 1)
    GPIO.output(green, 1)
    GPIO.output(blue, 0)

def Yellow(r, g, b, p) :
    red = r
    green = g
    blue = b
    power = p

    GPIO.output(power, 1)
    GPIO.output(red, 0)
    GPIO.output(green, 0)
    GPIO.output(blue, 1)

def Purple(r, g, b, p) :
    red = r
    green = g
    blue = b
    power = p

    GPIO.output(power, 1)
    GPIO.output(red, 0)
    GPIO.output(green, 1)
    GPIO.output(blue, 0)

def Cyan(r, g, b, p) :
    red = r
    green = g
    blue = b
    power = p

    GPIO.output(power, 1)
    GPIO.output(red, 1)
    GPIO.output(green, 0)
    GPIO.output(blue, 0)

def White(r, g, b, p) :
    red = r
    green = g
    blue = b
    power = p

    GPIO.output(power, 1)
    GPIO.output(red, 0)
    GPIO.output(green, 0)
    GPIO.output(blue, 0)

def Off(r, g, b, p) :
    red = r
    green = g
    blue = b
    power = p

    GPIO.output(power, 0)
    GPIO.output(red, 0)
    GPIO.output(green, 0)
    GPIO.output(blue, 0)

#We are going to have LED at address one do the color first then at address two follow it
[r1, g1, b1, p1] = adrOne()
[r2, g2, b2, p2] = adrTwo()

print "Press CTR-C to quit"
#setting LED 1 to red
Red(r1, g1, b1, p1)
time.sleep(.5)
try :
    while True :
        
        #Now LED 2 will follow and LED 1 will change colors and so on
        Red(r2, g2, b2, p2)
        Yellow(r1, g1, b1, p1)
        time.sleep(.5)

        Yellow(r2, g2, b2, p2)
        Green(r1, g1, b1, p1)
        time.sleep(.5)

        Green(r2, g2, b2, p2)
        Cyan(r1, g1, b1, p1)
        time.sleep(.5)

        Cyan(r2, g2, b2, p2)
        Blue(r1, g1, b1, p1)
        time.sleep(.5)

        Blue(r2, g2, b2, p2)
        Red(r1, g1, b1, p1)
        time.sleep(.5)
except KeyboardInterrupt:
    pass

GPIO.cleanup()
