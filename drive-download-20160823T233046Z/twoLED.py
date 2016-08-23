import RPi.GPIO as GPIO
import io
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

#Making different functions to address the different LEDs
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

#Print a givin promptStr and records input
def prompt(promptStr) :
    x = raw_input(promptStr)
    return x

#Function to assign certain LED to specific color
def color(r, g, b, p, color) :
    red = r
    green = g
    blue = b
    power = p

    #supplys 3.3v to anode
    GPIO.output(power, 1)
    
    if color == 'R' :
        GPIO.output(red, 0)
        GPIO.output(green, 1)
        GPIO.output(blue, 1)
        #Blink
        blink()
    elif color == 'G':
        GPIO.output(red, 1)
        GPIO.output(green, 0)
        GPIO.output(blue, 1)
        #Blink
        blink()
    elif color == 'B':
        GPIO.output(red, 1)
        GPIO.output(green, 1)
        GPIO.output(blue, 0)
        #Blink
        blink()
    elif color == 'Y' :
        GPIO.output(red, 0)
        GPIO.output(green, 0)
        GPIO.output(blue, 1)
        #Blink
        blink()
    elif color == 'P' :
        GPIO.output(red, 0)
        GPIO.output(green, 1)
        GPIO.output(blue, 0)
        #Blink
        blink()
    elif color == 'C' :
        GPIO.output(red, 1)
        GPIO.output(green, 0)
        GPIO.output(blue, 0)
        #Blink
        blink()
    elif color == 'W' :
        GPIO.output(red, 0)
        GPIO.output(green, 0)
        GPIO.output(blue, 0)
        #Blink
        blink()
    else :
        print "Are you autistic?"
        GPIO.output(power, 0)

#Blink function ~ Prompt user to ask if they want that color blinking
def blink() :
    blinkPrompt = "Would you like it to blink (y/n)? "
    response = raw_input(blinkPrompt)
    response = response.lower()
    if response == 'y' :
        while True:
            GPIO.output(power, 0)
            time.sleep(.3)
            GPIO.output(power, 1)
            time.sleep(.3)
    else :
        return 0

#Choose which LED you are talking to
ledAdr = prompt("Which LED are you talking to (1,2,3...)? ")

#Switch Statement
if ledAdr == '1' :
    [red, green, blue, power] = adrOne()
    #Now choose which color you want
    colorChar = prompt("Which color would you like (R,G,B,Y,P,C,W)? ")
    colorChar = colorChar.upper()
    color(red, green, blue, power, colorChar)
elif ledAdr == '2' :
    [red, green, blue, power] = adrTwo()
    #Now choose which color you want
    colorChar = prompt("Which color would you like (R,G,B,Y,P,C,W)? ")
    colorChar = colorChar.upper()
    color(red, green, blue, power, colorChar)
else :
    print "Nope"

GPIO.cleanup()

    
