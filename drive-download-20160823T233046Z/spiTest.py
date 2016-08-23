#First program with MCP23017
import wiringpi2 as wiringpi
import time

pin_base = 65                   #lowest available starting number
ic_addr = 0x10                 #IC address with i2cdetect -y 1

wiringpi.wiringPiSetup()        #initializes wiringpi 
wiringpi.mcp23s17Setup(pin_base, 0, ic_addr)    #initializes this IC to these pins on this CE0
wiringpi.mcp23s17Setup(81, 1, 0x10)             #initializing second SPI chip

#Address function for LED One (MANUALLY ENTER PINs HERE)
def adrOne() :
    red = 73
    green = 74
    blue = 75
    power = 72

    wiringpi.pinMode(red, 1)   #Red set as output
    wiringpi.pinMode(green, 1) #Green set as output
    wiringpi.pinMode(blue, 1)  #Blue set as output
    wiringpi.pinMode(power, 1) #Power set as output

    return red, green, blue, power

#Writing function to prompt user input
def prompt(promptStr) :
    x = raw_input(promptStr)
    return x

#Function to assign certain LED to specific color
def color(r, g, b, p, color) :
    red = r
    green = g
    blue = b
    power = p

    #supplys 5v to anode
    wiringpi.digitalWrite(power, 1)
    
    if color == 'R' :
        wiringpi.digitalWrite(red, 0)
        wiringpi.digitalWrite(green, 1)
        wiringpi.digitalWrite(blue, 1)

    elif color == 'G':
        wiringpi.digitalWrite(red, 1)
        wiringpi.digitalWrite(green, 0)
        wiringpi.digitalWrite(blue, 1)

    elif color == 'B':
        wiringpi.digitalWrite(red, 1)
        wiringpi.digitalWrite(green, 1)
        wiringpi.digitalWrite(blue, 0)

    elif color == 'Y' :
        wiringpi.digitalWrite(red, 0)
        wiringpi.digitalWrite(green, 0)
        wiringpi.digitalWrite(blue, 1)

    elif color == 'P' :
        wiringpi.digitalWrite(red, 0)
        wiringpi.digitalWrite(green, 1)
        wiringpi.digitalWrite(blue, 0)

    elif color == 'C' :
        wiringpi.digitalWrite(red, 1)
        wiringpi.digitalWrite(green, 0)
        wiringpi.digitalWrite(blue, 0)

    elif color == 'W' :
        wiringpi.digitalWrite(red, 0)
        wiringpi.digitalWrite(green, 0)
        wiringpi.digitalWrite(blue, 0)

    else :
        print "Are you autistic?"
        wiringpi.digitalWrite(power, 0) #Sets power OUTPUT to LOW
        wiringpi.pinMode(power, 0)      #Sets power PIN to
#Main Function#
#initializing pins as outputs
wiringpi.pinMode(72, 1)
wiringpi.pinMode(88, 1)
#Making both outputs high
wiringpi.digitalWrite(72, 1)
wiringpi.digitalWrite(88, 1)
#sleep
time.sleep(8)
#cleanup
wiringpi.digitalWrite(72, 0)
wiringpi.digitalWrite(88, 0)
wiringpi.pinMode(72, 0)
wiringpi.pinMode(88, 0)
