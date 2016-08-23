#First program with MCP23017
import wiringpi2 as wiringpi
import time

pin_base = 65                   #lowest available starting number
i2c_addr = 0x20                 #IC address with i2cdetect -y 1

wiringpi.wiringPiSetup()        #initializes wiringpi
wiringpi.mcp23017Setup(pin_base, i2c_addr)

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
        wiringpi.pinMode(power, 0)      #Sets power PIN to INPUT

#Main function - Asks user to input color and display for 2 seconds
[r1, g1, b1, p1] = adrOne()
inpChar = prompt("What color would you like the LED (RGBYCPW)? ")
inpChar = inpChar.upper()

    #Call color using inputchar to tell which color to turn on
color(r1, g1, b1, p1, inpChar)
time.sleep(2)

    #- Clean up -#
wiringpi.digitalWrite(p1, 0)    #sets power to LOW
wiringpi.pinMode(p1, 0)         #sets power back to input Mode
wiringpi.digitalWrite(r1, 0)    #sets red to LOW
wiringpi.pinMode(r1, 0)         #sets red back to input Mode
wiringpi.digitalWrite(g1, 0)    #sets green to LOW
wiringpi.pinMode(g1, 0)         #sets green back to input Mode
wiringpi.digitalWrite(b1, 0)    #sets blue to LOW
wiringpi.pinMode(b1, 0)         #sets blue back to input Mode
