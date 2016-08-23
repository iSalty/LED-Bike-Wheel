import wiringpi2 as wiringpi
import RPi.GPIO as GPIO
import time
import io

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

wiringpi.wiringPiSetup()

#Hall Sensors
HALL_ADDR1 = 5
GPIO.setup(HALL_ADDR1, GPIO.IN)

PIN_BASE = 65
#Making array each IC is addressed by pin_base[IC#-1]
pin_base = [PIN_BASE, PIN_BASE+16, PIN_BASE+32, PIN_BASE+48, PIN_BASE+64, PIN_BASE+80, PIN_BASE+96, PIN_BASE+112, PIN_BASE+128, PIN_BASE+144, PIN_BASE+160, PIN_BASE+176, PIN_BASE+192]

#doing setup for each individual IC
wiringpi.mcp23s17Setup(pin_base[0], 0, 0x10)    #IC 1  (LEDs 1-4)
wiringpi.mcp23s17Setup(pin_base[1], 0, 0x11)    #IC 2  (LEDs 5-8)
wiringpi.mcp23s17Setup(pin_base[2], 0, 0x12)    #IC 3  (LEDs 9-12)
wiringpi.mcp23s17Setup(pin_base[3], 0, 0x13)    #IC 4  (LEDs 13-16)
wiringpi.mcp23s17Setup(pin_base[4], 0, 0x14)    #IC 5  (LEDs 17-20)
wiringpi.mcp23s17Setup(pin_base[5], 0, 0x15)    #IC 6  (LEDs 21-24)
wiringpi.mcp23s17Setup(pin_base[6], 1, 0x10)    #IC 7  (LEDs 25-28)
wiringpi.mcp23s17Setup(pin_base[7], 1, 0x11)    #IC 8  (LEDs 29-32)
wiringpi.mcp23s17Setup(pin_base[8], 1, 0x12)    #IC 9  (LEDs 33-36)
wiringpi.mcp23s17Setup(pin_base[9], 1, 0x13)    #IC 10 (LEDs 37-40)
wiringpi.mcp23s17Setup(pin_base[10], 1, 0x14)   #IC 11 (LEDs 41-44)
wiringpi.mcp23s17Setup(pin_base[11], 1, 0x15)   #IC 12 (LEDs 45-48)

#-------------   Address functions for LED    -----------------------------------------------#
def addr_1() :
    [power, red, green, blue] = [pin_base[0], pin_base[0]+1, pin_base[0]+2, pin_base[0]+3] 
    
    wiringpi.pinMode(red, 1)   #Red set as output
    wiringpi.pinMode(green, 1) #Green set as output
    wiringpi.pinMode(blue, 1)  #Blue set as output
    wiringpi.pinMode(power, 1) #Power set as output

    return power, red, green, blue

def addr_2() :
    [power, red, green, blue] = [pin_base[0], pin_base[0]+1, pin_base[0]+2, pin_base[0]+3] 
    
    wiringpi.pinMode(red, 1)   #Red set as output
    wiringpi.pinMode(green, 1) #Green set as output
    wiringpi.pinMode(blue, 1)  #Blue set as output
    wiringpi.pinMode(power, 1) #Power set as output

    return power, red, green, blue

def addr_3() :
    [power, red, green, blue] = [pin_base[0], pin_base[0]+1, pin_base[0]+2, pin_base[0]+3] 
    
    wiringpi.pinMode(red, 1)   #Red set as output
    wiringpi.pinMode(green, 1) #Green set as output
    wiringpi.pinMode(blue, 1)  #Blue set as output
    wiringpi.pinMode(power, 1) #Power set as output

    return power, red, green, blue

def addr_4() :
    [power, red, green, blue] = [pin_base[0], pin_base[0]+1, pin_base[0]+2, pin_base[0]+3] 
    
    wiringpi.pinMode(red, 1)   #Red set as output
    wiringpi.pinMode(green, 1) #Green set as output
    wiringpi.pinMode(blue, 1)  #Blue set as output
    wiringpi.pinMode(power, 1) #Power set as output

    return power, red, green, blue

def addr_5() :
    [power, red, green, blue] = [pin_base[1], pin_base[1]+1, pin_base[1]+2, pin_base[1]+3] 
    
    wiringpi.pinMode(red, 1)   #Red set as output
    wiringpi.pinMode(green, 1) #Green set as output
    wiringpi.pinMode(blue, 1)  #Blue set as output
    wiringpi.pinMode(power, 1) #Power set as output

    return power, red, green, blue

def addr_6() :
    [power, red, green, blue] = [pin_base[1], pin_base[1]+1, pin_base[1]+2, pin_base[1]+3] 
    
    wiringpi.pinMode(red, 1)   #Red set as output
    wiringpi.pinMode(green, 1) #Green set as output
    wiringpi.pinMode(blue, 1)  #Blue set as output
    wiringpi.pinMode(power, 1) #Power set as output

    return power, red, green, blue

def addr_7() :
    [power, red, green, blue] = [pin_base[1], pin_base[1]+1, pin_base[1]+2, pin_base[1]+3] 
    
    wiringpi.pinMode(red, 1)   #Red set as output
    wiringpi.pinMode(green, 1) #Green set as output
    wiringpi.pinMode(blue, 1)  #Blue set as output
    wiringpi.pinMode(power, 1) #Power set as output

    return power, red, green, blue
def addr_8() :
    [power, red, green, blue] = [pin_base[1], pin_base[1]+1, pin_base[1]+2, pin_base[1]+3] 
    
    wiringpi.pinMode(red, 1)   #Red set as output
    wiringpi.pinMode(green, 1) #Green set as output
    wiringpi.pinMode(blue, 1)  #Blue set as output
    wiringpi.pinMode(power, 1) #Power set as output

    return power, red, green, blue

def addr_9() :
    [power, red, green, blue] = [pin_base[2], pin_base[2]+1, pin_base[2]+2, pin_base[2]+3] 
    
    wiringpi.pinMode(red, 1)   #Red set as output
    wiringpi.pinMode(green, 1) #Green set as output
    wiringpi.pinMode(blue, 1)  #Blue set as output
    wiringpi.pinMode(power, 1) #Power set as output

    return power, red, green, blue

def addr_10() :
    [power, red, green, blue] = [pin_base[2], pin_base[2]+1, pin_base[2]+2, pin_base[2]+3] 
    
    wiringpi.pinMode(red, 1)   #Red set as output
    wiringpi.pinMode(green, 1) #Green set as output
    wiringpi.pinMode(blue, 1)  #Blue set as output
    wiringpi.pinMode(power, 1) #Power set as output

    return power, red, green, blue

def addr_11() :
    [power, red, green, blue] = [pin_base[2], pin_base[2]+1, pin_base[2]+2, pin_base[2]+3] 
    
    wiringpi.pinMode(red, 1)   #Red set as output
    wiringpi.pinMode(green, 1) #Green set as output
    wiringpi.pinMode(blue, 1)  #Blue set as output
    wiringpi.pinMode(power, 1) #Power set as output

    return power, red, green, blue

def addr_12() :
    [power, red, green, blue] = [pin_base[2], pin_base[2]+1, pin_base[2]+2, pin_base[2]+3] 
    
    wiringpi.pinMode(red, 1)   #Red set as output
    wiringpi.pinMode(green, 1) #Green set as output
    wiringpi.pinMode(blue, 1)  #Blue set as output
    wiringpi.pinMode(power, 1) #Power set as output

    return power, red, green, blue
#-------------   Addressing Functions for LEDs    ----------------------------------------#


#--------------- Prompt Function ---------------------------------------------------------#
def prompt(promptStr) :
    x = raw_input(promptStr)
    return x
#--------------- Prompt Function ---------------------------------------------------------#


#------ Function to assign certain LED to specific color ---------------------------------#
def color(p, r, g, b, color) :
    power = p
    red = r
    green = g
    blue = b

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

    elif color == "Blk" :
        wiringpi.digitalWrite(power, 0)
        wiringpi.digitalWrite(red, 0)
        wiringpi.digitalWrite(green, 0)
        wiringpi.digitalWrite(blue, 0)

    else :
        print "Not an available color?"
        wiringpi.digitalWrite(power, 0) #Sets power OUTPUT to LOW
        wiringpi.pinMode(power, 0)      #Sets power PIN to
#------ Function to assign certain LED to specific color ---------------------------------#


#------ Wiringpi Cleanup Function --------------------------------------------------------#
def cleanOutput () :
    NumIC = 3      #Number of ICs that need to be cleaned up
    #First turn output to LOW, then turn pin to INPUT
    if NumIC >= 12 :
        i = pin_base[11]+15
        while i >= pin_base[11] :       #while loop to put output LOW then turn to input
            wiringpi.digitalWrite(i, 0)
            wiringpi.pinMode(i, 0)
            i = i - 1
    if NumIC >= 11 :
        i = pin_base[10]+15
        while i >= pin_base[10] :       #while loop to put output LOW then turn to input
            wiringpi.digitalWrite(i, 0)
            wiringpi.pinMode(i, 0)
            i = i - 1
    if NumIC >= 10 :
        i = pin_base[9]+15
        while i >= pin_base[9] :       #while loop to put output LOW then turn to input
            wiringpi.digitalWrite(i, 0)
            wiringpi.pinMode(i, 0)
            i = i - 1
    if NumIC >= 9 :
        i = pin_base[8]+15
        while i >= pin_base[8] :       #while loop to put output LOW then turn to input
            wiringpi.digitalWrite(i, 0)
            wiringpi.pinMode(i, 0)
            i = i - 1
    if NumIC >= 8 :
        i = pin_base[7]+15
        while i >= pin_base[7] :       #while loop to put output LOW then turn to input
            wiringpi.digitalWrite(i, 0)
            wiringpi.pinMode(i, 0)
            i = i - 1
    if NumIC >= 7 :
        i = pin_base[6]+15
        while i >= pin_base[6] :       #while loop to put output LOW then turn to input
            wiringpi.digitalWrite(i, 0)
            wiringpi.pinMode(i, 0)
            i = i - 1
    if NumIC >= 6 :
        i = pin_base[5]+15
        while i >= pin_base[5] :       #while loop to put output LOW then turn to input
            wiringpi.digitalWrite(i, 0)
            wiringpi.pinMode(i, 0)
            i = i - 1
    if NumIC >= 5 :
        i = pin_base[4]+15
        while i >= pin_base[4] :       #while loop to put output LOW then turn to input
            wiringpi.digitalWrite(i, 0)
            wiringpi.pinMode(i, 0)
            i = i - 1
    if NumIC >= 4 :
        i = pin_base[3]+15
        while i >= pin_base[3] :       #while loop to put output LOW then turn to input
            wiringpi.digitalWrite(i, 0)
            wiringpi.pinMode(i, 0)
            i = i - 1
    if NumIC >= 3 :
        i = pin_base[2]+15
        while i >= pin_base[2] :       #while loop to put output LOW then turn to input
            wiringpi.digitalWrite(i, 0)
            wiringpi.pinMode(i, 0)
            i = i - 1
    if NumIC >= 2 :
        i = pin_base[1]+15
        while i >= pin_base[1] :       #while loop to put output LOW then turn to input
            wiringpi.digitalWrite(i, 0)
            wiringpi.pinMode(i, 0)
            i = i-1
    if NumIC >= 1 :
        i = pin_base[0]+15
        while i >= pin_base[0] :       #while loop to put output LOW then turn to input
            wiringpi.digitalWrite(i, 0)
            wiringpi.pinMode(i, 0)
            i = i - 1
    else :
        print "Error invalid NumIC for cleanup."
    
#__MAIN__
#prompt user input for the RPM
RPM = 50.0

#Calculating RPM relevant parameters
RPS = RPM / 60.0        #rotations per second
DegPS = RPS * 360.0     #how many degrees go in 1 second
SPDeg = 1 / DegPS       #seconds it takes to go 1 degree

#Getting the addresses for the relevant LEDs (just 1 strip for the moment)
LED1  = [p1, r1, g1, b1]     = addr_1()
LED2  = [p2, r2, g2, b2]     = addr_2()
LED3  = [p3, r3, g3, b3]     = addr_3()
LED4  = [p4, r4, g4, b4]     = addr_4()
LED5  = [p5, r5, g5, b5]     = addr_5()
LED6  = [p6, r6, g6, b6]     = addr_6()
LED7  = [p7, r7, g7, b7]     = addr_7()
LED8  = [p8, r8, g8, b8]     = addr_8()
LED9  = [p9, r9, g9, b9]     = addr_9()
LED10 = [p10, r10, g10, b10] = addr_10()
LED11 = [p11, r11, g11, b11] = addr_11()
LED12 = [p12, r12, g12, b12] = addr_12()

#Turning on LEDs in RAINBOW (RYGCBP) when the Hall sensor is triggered
try :
    while True :
        if GPIO.input(HALL_ADDR1) == False :
            #Turns LEDs ON in rainbow colors
            color(p1, r1, g1, b1, 'P')  #LED 1 is nearest the center of the wheel
            color(p2, r2, g2, b2, 'P')
            color(p3, r3, g3, b3, 'B')
            color(p4, r4, g4, b4, 'B')
            color(p5, r5, g5, b5, 'C')
            color(p6, r6, g6, b6, 'C')
            color(p7, r7, g7, b7, 'G')
            color(p8, r8, g8, b8, 'G')
            color(p9, r9, g9, b9, 'Y')
            color(p10, r10, g10, b10, 'Y')
            color(p11, r11, g11, b11, 'R')
            color(p12, r12, g12, b12, 'R')

            onTime = 180.0 * SPDeg
            time.sleep(onTime)             #tells it to sleep for 180 degrees at this RPM

            #Turns LEDs OFF for other half of circle
            color(p1, r1, g1, b1, 'Blk')  #LED 1 is nearest the center of the wheel
            color(p2, r2, g2, b2, 'Blk')
            color(p3, r3, g3, b3, 'Blk')
            color(p4, r4, g4, b4, 'Blk')
            color(p5, r5, g5, b5, 'Blk')
            color(p6, r6, g6, b6, 'Blk')
            color(p7, r7, g7, b7, 'Blk')
            color(p8, r8, g8, b8, 'Blk')
            color(p9, r9, g9, b9, 'Blk')
            color(p10, r10, g10, b10, 'Blk')
            color(p11, r11, g11, b11, 'Blk')
            color(p12, r12, g12, b12, 'Blk')

            offTime = 180.0 * SPDeg
            time.sleep(offTime)
            
        #Turns off all LEDs
        color(p1, r1, g1, b1, 'Blk')  #LED 1 is nearest the center of the wheel
        color(p2, r2, g2, b2, 'Blk')
        color(p3, r3, g3, b3, 'Blk')
        color(p4, r4, g4, b4, 'Blk')
        color(p5, r5, g5, b5, 'Blk')
        color(p6, r6, g6, b6, 'Blk')
        color(p7, r7, g7, b7, 'Blk')
        color(p8, r8, g8, b8, 'Blk')
        color(p9, r9, g9, b9, 'Blk')
        color(p10, r10, g10, b10, 'Blk')
        color(p11, r11, g11, b11, 'Blk')
        color(p12, r12, g12, b12, 'Blk')
        print "One Pass"
except KeyboardInterrupt :
    pass

#----  Cleanup  ----#
cleanOutput()
GPIO.cleanup
