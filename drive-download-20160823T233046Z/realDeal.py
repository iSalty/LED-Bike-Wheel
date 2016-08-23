import wiringpi2 as wiringpi
import RPi.GPIO as GPIO
import time
import io

GPIO.setmode(GPIO.BCM)      #Need GPIO for Hall Sensors
GPIO.setwarnings(False)

wiringpi.wiringPiSetup()

#Hall Sensors
HALL_ADDR1 = 5
HALL_ADDR2 = 6
HALL_ADDR3 = 13
HALL_ADDR4 = 26
GPIO.setup(HALL_ADDR1, GPIO.IN)
GPIO.setup(HALL_ADDR2, GPIO.IN)
GPIO.setup(HALL_ADDR3, GPIO.IN)
GPIO.setup(HALL_ADDR4, GPIO.IN)

#Making array each IC is addressed by pin_base[IC#-1]
PIN_BASE = 65
pin_base = [PIN_BASE, PIN_BASE+16, PIN_BASE+32, PIN_BASE+48, PIN_BASE+64, PIN_BASE+80, PIN_BASE+96, PIN_BASE+112, PIN_BASE+128, PIN_BASE+144, PIN_BASE+160, PIN_BASE+176]

#doing setup for each individual IC
wiringpi.mcp23s17Setup(pin_base[0], 0, 0x10)    #IC 1  (LEDs 1-4)   (Pins 65-80)
wiringpi.mcp23s17Setup(pin_base[1], 0, 0x11)    #IC 2  (LEDs 5-8)   (Pins 81-96)
wiringpi.mcp23s17Setup(pin_base[2], 0, 0x12)    #IC 3  (LEDs 9-12)  (Pins 97-112)
wiringpi.mcp23s17Setup(pin_base[3], 0, 0x13)    #IC 4  (LEDs 13-16) (Pins 113-128)
wiringpi.mcp23s17Setup(pin_base[4], 0, 0x14)    #IC 5  (LEDs 17-20) (Pins 129-144)
wiringpi.mcp23s17Setup(pin_base[5], 0, 0x15)    #IC 6  (LEDs 21-24) (Pins 145-160)
wiringpi.mcp23s17Setup(pin_base[6], 1, 0x10)    #IC 7  (LEDs 25-28) (Pins 161-176)
wiringpi.mcp23s17Setup(pin_base[7], 1, 0x11)    #IC 8  (LEDs 29-32) (Pins 177-192)
wiringpi.mcp23s17Setup(pin_base[8], 1, 0x12)    #IC 9  (LEDs 33-36) (Pins 193-208)
wiringpi.mcp23s17Setup(pin_base[9], 1, 0x13)    #IC 10 (LEDs 37-40) (Pins 209-224)
wiringpi.mcp23s17Setup(pin_base[10], 1, 0x14)   #IC 11 (LEDs 41-44) (Pins 225-240)
wiringpi.mcp23s17Setup(pin_base[11], 1, 0x15)   #IC 12 (LEDs 45-48) (Pins 241-256)


#Read in the Text file which contains the all of the colors for the image
colorFile = open('/home/pi/Desktop/Playlist/LEDcolor.txt', 'r')
readList = colorFile.read()

colorList = []
i = 0
while i < len(readList) :       #creating a List of all the relevant colors (each 12 represents the colors for a stick for 1 degree)
    colorList.append(readList[i])
    i = i+2
#-------------      Reading Picture File       ----------------------------------------------#


#-------------   Address functions for LED    -----------------------------------------------#
def addr_1() :
    [power, red, green, blue] = [pin_base[0], pin_base[0]+1, pin_base[0]+2, pin_base[0]+3] 
    
    wiringpi.pinMode(red, 1)   #Red set as output
    wiringpi.pinMode(green, 1) #Green set as output
    wiringpi.pinMode(blue, 1)  #Blue set as output
    wiringpi.pinMode(power, 1) #Power set as output

    return power, red, green, blue

def addr_2() :
    [power, red, green, blue] = [pin_base[0]+4, pin_base[0]+5, pin_base[0]+6, pin_base[0]+7] 
    
    wiringpi.pinMode(red, 1)   #Red set as output
    wiringpi.pinMode(green, 1) #Green set as output
    wiringpi.pinMode(blue, 1)  #Blue set as output
    wiringpi.pinMode(power, 1) #Power set as output

    return power, red, green, blue

def addr_3() :
    [power, red, green, blue] = [pin_base[0]+8, pin_base[0]+9, pin_base[0]+10, pin_base[0]+11] 
    
    wiringpi.pinMode(red, 1)   #Red set as output
    wiringpi.pinMode(green, 1) #Green set as output
    wiringpi.pinMode(blue, 1)  #Blue set as output
    wiringpi.pinMode(power, 1) #Power set as output

    return power, red, green, blue

def addr_4() :
    [power, red, green, blue] = [pin_base[0]+12, pin_base[0]+13, pin_base[0]+14, pin_base[0]+15] 
    
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
    [power, red, green, blue] = [pin_base[1]+4, pin_base[1]+5, pin_base[1]+6, pin_base[1]+7] 
    
    wiringpi.pinMode(red, 1)   #Red set as output
    wiringpi.pinMode(green, 1) #Green set as output
    wiringpi.pinMode(blue, 1)  #Blue set as output
    wiringpi.pinMode(power, 1) #Power set as output

    return power, red, green, blue

def addr_7() :
    [power, red, green, blue] = [pin_base[1]+8, pin_base[1]+9, pin_base[1]+10, pin_base[1]+11] 
    
    wiringpi.pinMode(red, 1)   #Red set as output
    wiringpi.pinMode(green, 1) #Green set as output
    wiringpi.pinMode(blue, 1)  #Blue set as output
    wiringpi.pinMode(power, 1) #Power set as output

    return power, red, green, blue
def addr_8() :
    [power, red, green, blue] = [pin_base[1]+12, pin_base[1]+13, pin_base[1]+14, pin_base[1]+15] 
    
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
    [power, red, green, blue] = [pin_base[2]+4, pin_base[2]+5, pin_base[2]+6, pin_base[2]+7] 
    
    wiringpi.pinMode(red, 1)   #Red set as output
    wiringpi.pinMode(green, 1) #Green set as output
    wiringpi.pinMode(blue, 1)  #Blue set as output
    wiringpi.pinMode(power, 1) #Power set as output

    return power, red, green, blue

def addr_11() :
    [power, red, green, blue] = [pin_base[2]+8, pin_base[2]+9, pin_base[2]+10, pin_base[2]+11] 
    
    wiringpi.pinMode(red, 1)   #Red set as output
    wiringpi.pinMode(green, 1) #Green set as output
    wiringpi.pinMode(blue, 1)  #Blue set as output
    wiringpi.pinMode(power, 1) #Power set as output

    return power, red, green, blue

def addr_12() :
    [power, red, green, blue] = [pin_base[2]+12, pin_base[2]+13, pin_base[2]+14, pin_base[2]+15] 
    
    wiringpi.pinMode(red, 1)   #Red set as output
    wiringpi.pinMode(green, 1) #Green set as output
    wiringpi.pinMode(blue, 1)  #Blue set as output
    wiringpi.pinMode(power, 1) #Power set as output

    return power, red, green, blue

def addr_13() :
    [power, red, green, blue] = [pin_base[3], pin_base[3]+1, pin_base[3]+2, pin_base[3]+3] 
    
    wiringpi.pinMode(red, 1)   #Red set as output
    wiringpi.pinMode(green, 1) #Green set as output
    wiringpi.pinMode(blue, 1)  #Blue set as output
    wiringpi.pinMode(power, 1) #Power set as output

    return power, red, green, blue

def addr_14() :
    [power, red, green, blue] = [pin_base[3]+4, pin_base[3]+5, pin_base[3]+6, pin_base[3]+7] 
    
    wiringpi.pinMode(red, 1)   #Red set as output
    wiringpi.pinMode(green, 1) #Green set as output
    wiringpi.pinMode(blue, 1)  #Blue set as output
    wiringpi.pinMode(power, 1) #Power set as output

    return power, red, green, blue

def addr_15() :
    [power, red, green, blue] = [pin_base[3]+8, pin_base[3]+9, pin_base[3]+10, pin_base[3]+11] 
    
    wiringpi.pinMode(red, 1)   #Red set as output
    wiringpi.pinMode(green, 1) #Green set as output
    wiringpi.pinMode(blue, 1)  #Blue set as output
    wiringpi.pinMode(power, 1) #Power set as output

    return power, red, green, blue

def addr_16() :
    [power, red, green, blue] = [pin_base[3]+12, pin_base[3]+13, pin_base[3]+14, pin_base[3]+15] 
    
    wiringpi.pinMode(red, 1)   #Red set as output
    wiringpi.pinMode(green, 1) #Green set as output
    wiringpi.pinMode(blue, 1)  #Blue set as output
    wiringpi.pinMode(power, 1) #Power set as output

    return power, red, green, blue

def addr_17() :
    [power, red, green, blue] = [pin_base[4], pin_base[4]+1, pin_base[4]+2, pin_base[4]+3] 
    
    wiringpi.pinMode(red, 1)   #Red set as output
    wiringpi.pinMode(green, 1) #Green set as output
    wiringpi.pinMode(blue, 1)  #Blue set as output
    wiringpi.pinMode(power, 1) #Power set as output

    return power, red, green, blue

def addr_18() :
    [power, red, green, blue] = [pin_base[4]+4, pin_base[4]+5, pin_base[4]+6, pin_base[4]+7] 
    
    wiringpi.pinMode(red, 1)   #Red set as output
    wiringpi.pinMode(green, 1) #Green set as output
    wiringpi.pinMode(blue, 1)  #Blue set as output
    wiringpi.pinMode(power, 1) #Power set as output

    return power, red, green, blue

def addr_19() :
    [power, red, green, blue] = [pin_base[4]+8, pin_base[4]+9, pin_base[4]+10, pin_base[4]+11] 
    
    wiringpi.pinMode(red, 1)   #Red set as output
    wiringpi.pinMode(green, 1) #Green set as output
    wiringpi.pinMode(blue, 1)  #Blue set as output
    wiringpi.pinMode(power, 1) #Power set as output

    return power, red, green, blue

def addr_20() :
    [power, red, green, blue] = [pin_base[4]+12, pin_base[4]+13, pin_base[4]+14, pin_base[4]+15] 
    
    wiringpi.pinMode(red, 1)   #Red set as output
    wiringpi.pinMode(green, 1) #Green set as output
    wiringpi.pinMode(blue, 1)  #Blue set as output
    wiringpi.pinMode(power, 1) #Power set as output

    return power, red, green, blue

def addr_21() :
    [power, red, green, blue] = [pin_base[5], pin_base[5]+1, pin_base[5]+2, pin_base[5]+3] 
    
    wiringpi.pinMode(red, 1)   #Red set as output
    wiringpi.pinMode(green, 1) #Green set as output
    wiringpi.pinMode(blue, 1)  #Blue set as output
    wiringpi.pinMode(power, 1) #Power set as output

    return power, red, green, blue

def addr_22() :
    [power, red, green, blue] = [pin_base[5]+4, pin_base[5]+5, pin_base[5]+6, pin_base[5]+7] 
    
    wiringpi.pinMode(red, 1)   #Red set as output
    wiringpi.pinMode(green, 1) #Green set as output
    wiringpi.pinMode(blue, 1)  #Blue set as output
    wiringpi.pinMode(power, 1) #Power set as output

    return power, red, green, blue

def addr_23() :
    [power, red, green, blue] = [pin_base[5]+8, pin_base[5]+9, pin_base[5]+10, pin_base[5]+11] 
    
    wiringpi.pinMode(red, 1)   #Red set as output
    wiringpi.pinMode(green, 1) #Green set as output
    wiringpi.pinMode(blue, 1)  #Blue set as output
    wiringpi.pinMode(power, 1) #Power set as output

    return power, red, green, blue

def addr_24() :
    [power, red, green, blue] = [pin_base[5]+12, pin_base[5]+13, pin_base[5]+14, pin_base[5]+15] 
    
    wiringpi.pinMode(red, 1)   #Red set as output
    wiringpi.pinMode(green, 1) #Green set as output
    wiringpi.pinMode(blue, 1)  #Blue set as output
    wiringpi.pinMode(power, 1) #Power set as output

    return power, red, green, blue

def addr_25() :
    [power, red, green, blue] = [pin_base[6], pin_base[6]+1, pin_base[6]+2, pin_base[6]+3] 
    
    wiringpi.pinMode(red, 1)   #Red set as output
    wiringpi.pinMode(green, 1) #Green set as output
    wiringpi.pinMode(blue, 1)  #Blue set as output
    wiringpi.pinMode(power, 1) #Power set as output

    return power, red, green, blue

def addr_26() :
    [power, red, green, blue] = [pin_base[6]+4, pin_base[6]+5, pin_base[6]+6, pin_base[6]+7] 
    
    wiringpi.pinMode(red, 1)   #Red set as output
    wiringpi.pinMode(green, 1) #Green set as output
    wiringpi.pinMode(blue, 1)  #Blue set as output
    wiringpi.pinMode(power, 1) #Power set as output

    return power, red, green, blue

def addr_27() :
    [power, red, green, blue] = [pin_base[6]+8, pin_base[6]+9, pin_base[6]+10, pin_base[6]+11] 
    
    wiringpi.pinMode(red, 1)   #Red set as output
    wiringpi.pinMode(green, 1) #Green set as output
    wiringpi.pinMode(blue, 1)  #Blue set as output
    wiringpi.pinMode(power, 1) #Power set as output

    return power, red, green, blue

def addr_28() :
    [power, red, green, blue] = [pin_base[6]+12, pin_base[6]+13, pin_base[6]+14, pin_base[6]+15] 
    
    wiringpi.pinMode(red, 1)   #Red set as output
    wiringpi.pinMode(green, 1) #Green set as output
    wiringpi.pinMode(blue, 1)  #Blue set as output
    wiringpi.pinMode(power, 1) #Power set as output

    return power, red, green, blue

def addr_29() :
    [power, red, green, blue] = [pin_base[7], pin_base[7]+1, pin_base[7]+2, pin_base[7]+3] 
    
    wiringpi.pinMode(red, 1)   #Red set as output
    wiringpi.pinMode(green, 1) #Green set as output
    wiringpi.pinMode(blue, 1)  #Blue set as output
    wiringpi.pinMode(power, 1) #Power set as output

    return power, red, green, blue

def addr_30() :
    [power, red, green, blue] = [pin_base[7]+4, pin_base[7]+5, pin_base[7]+6, pin_base[7]+7] 
    
    wiringpi.pinMode(red, 1)   #Red set as output
    wiringpi.pinMode(green, 1) #Green set as output
    wiringpi.pinMode(blue, 1)  #Blue set as output
    wiringpi.pinMode(power, 1) #Power set as output

    return power, red, green, blue

def addr_31() :
    [power, red, green, blue] = [pin_base[7]+8, pin_base[7]+9, pin_base[7]+10, pin_base[7]+11] 
    
    wiringpi.pinMode(red, 1)   #Red set as output
    wiringpi.pinMode(green, 1) #Green set as output
    wiringpi.pinMode(blue, 1)  #Blue set as output
    wiringpi.pinMode(power, 1) #Power set as output

    return power, red, green, blue

def addr_32() :
    [power, red, green, blue] = [pin_base[7]+12, pin_base[7]+13, pin_base[7]+14, pin_base[7]+15] 
    
    wiringpi.pinMode(red, 1)   #Red set as output
    wiringpi.pinMode(green, 1) #Green set as output
    wiringpi.pinMode(blue, 1)  #Blue set as output
    wiringpi.pinMode(power, 1) #Power set as output

    return power, red, green, blue

def addr_33() :
    [power, red, green, blue] = [pin_base[8], pin_base[8]+1, pin_base[8]+2, pin_base[8]+3] 
    
    wiringpi.pinMode(red, 1)   #Red set as output
    wiringpi.pinMode(green, 1) #Green set as output
    wiringpi.pinMode(blue, 1)  #Blue set as output
    wiringpi.pinMode(power, 1) #Power set as output

    return power, red, green, blue

def addr_34() :
    [power, red, green, blue] = [pin_base[8]+4, pin_base[8]+5, pin_base[8]+6, pin_base[8]+7] 
    
    wiringpi.pinMode(red, 1)   #Red set as output
    wiringpi.pinMode(green, 1) #Green set as output
    wiringpi.pinMode(blue, 1)  #Blue set as output
    wiringpi.pinMode(power, 1) #Power set as output

    return power, red, green, blue

def addr_35() :
    [power, red, green, blue] = [pin_base[8]+8, pin_base[8]+9, pin_base[8]+10, pin_base[8]+11] 
    
    wiringpi.pinMode(red, 1)   #Red set as output
    wiringpi.pinMode(green, 1) #Green set as output
    wiringpi.pinMode(blue, 1)  #Blue set as output
    wiringpi.pinMode(power, 1) #Power set as output

    return power, red, green, blue

def addr_36() :
    [power, red, green, blue] = [pin_base[8]+12, pin_base[8]+13, pin_base[8]+14, pin_base[8]+15] 
    
    wiringpi.pinMode(red, 1)   #Red set as output
    wiringpi.pinMode(green, 1) #Green set as output
    wiringpi.pinMode(blue, 1)  #Blue set as output
    wiringpi.pinMode(power, 1) #Power set as output

    return power, red, green, blue

def addr_37() :
    [power, red, green, blue] = [pin_base[9], pin_base[9]+1, pin_base[9]+2, pin_base[9]+3] 
    
    wiringpi.pinMode(red, 1)   #Red set as output
    wiringpi.pinMode(green, 1) #Green set as output
    wiringpi.pinMode(blue, 1)  #Blue set as output
    wiringpi.pinMode(power, 1) #Power set as output

    return power, red, green, blue

def addr_38() :
    [power, red, green, blue] = [pin_base[9]+4, pin_base[9]+5, pin_base[9]+6, pin_base[9]+7] 
    
    wiringpi.pinMode(red, 1)   #Red set as output
    wiringpi.pinMode(green, 1) #Green set as output
    wiringpi.pinMode(blue, 1)  #Blue set as output
    wiringpi.pinMode(power, 1) #Power set as output

    return power, red, green, blue

def addr_39() :
    [power, red, green, blue] = [pin_base[9]+8, pin_base[9]+9, pin_base[9]+10, pin_base[9]+11] 
    
    wiringpi.pinMode(red, 1)   #Red set as output
    wiringpi.pinMode(green, 1) #Green set as output
    wiringpi.pinMode(blue, 1)  #Blue set as output
    wiringpi.pinMode(power, 1) #Power set as output

    return power, red, green, blue

def addr_40() :
    [power, red, green, blue] = [pin_base[9]+12, pin_base[9]+13, pin_base[9]+14, pin_base[9]+15] 
    
    wiringpi.pinMode(red, 1)   #Red set as output
    wiringpi.pinMode(green, 1) #Green set as output
    wiringpi.pinMode(blue, 1)  #Blue set as output
    wiringpi.pinMode(power, 1) #Power set as output

    return power, red, green, blue

def addr_41() :
    [power, red, green, blue] = [pin_base[10], pin_base[10]+1, pin_base[10]+2, pin_base[10]+3] 
    
    wiringpi.pinMode(red, 1)   #Red set as output
    wiringpi.pinMode(green, 1) #Green set as output
    wiringpi.pinMode(blue, 1)  #Blue set as output
    wiringpi.pinMode(power, 1) #Power set as output

    return power, red, green, blue

def addr_42() :
    [power, red, green, blue] = [pin_base[10]+4, pin_base[10]+5, pin_base[10]+6, pin_base[10]+7] 
    
    wiringpi.pinMode(red, 1)   #Red set as output
    wiringpi.pinMode(green, 1) #Green set as output
    wiringpi.pinMode(blue, 1)  #Blue set as output
    wiringpi.pinMode(power, 1) #Power set as output

    return power, red, green, blue

def addr_43() :
    [power, red, green, blue] = [pin_base[10]+8, pin_base[10]+9, pin_base[10]+10, pin_base[10]+11] 
    
    wiringpi.pinMode(red, 1)   #Red set as output
    wiringpi.pinMode(green, 1) #Green set as output
    wiringpi.pinMode(blue, 1)  #Blue set as output
    wiringpi.pinMode(power, 1) #Power set as output

    return power, red, green, blue

def addr_44() :
    [power, red, green, blue] = [pin_base[10]+12, pin_base[10]+13, pin_base[10]+14, pin_base[10]+15] 
    
    wiringpi.pinMode(red, 1)   #Red set as output
    wiringpi.pinMode(green, 1) #Green set as output
    wiringpi.pinMode(blue, 1)  #Blue set as output
    wiringpi.pinMode(power, 1) #Power set as output

    return power, red, green, blue

def addr_45() :
    [power, red, green, blue] = [pin_base[11], pin_base[11]+1, pin_base[11]+2, pin_base[11]+3] 
    
    wiringpi.pinMode(red, 1)   #Red set as output
    wiringpi.pinMode(green, 1) #Green set as output
    wiringpi.pinMode(blue, 1)  #Blue set as output
    wiringpi.pinMode(power, 1) #Power set as output

    return power, red, green, blue

def addr_46() :
    [power, red, green, blue] = [pin_base[11]+4, pin_base[11]+5, pin_base[11]+6, pin_base[11]+7] 
    
    wiringpi.pinMode(red, 1)   #Red set as output
    wiringpi.pinMode(green, 1) #Green set as output
    wiringpi.pinMode(blue, 1)  #Blue set as output
    wiringpi.pinMode(power, 1) #Power set as output

    return power, red, green, blue

def addr_47() :
    [power, red, green, blue] = [pin_base[11]+8, pin_base[11]+9, pin_base[11]+10, pin_base[11]+11] 
    
    wiringpi.pinMode(red, 1)   #Red set as output
    wiringpi.pinMode(green, 1) #Green set as output
    wiringpi.pinMode(blue, 1)  #Blue set as output
    wiringpi.pinMode(power, 1) #Power set as output

    return power, red, green, blue

def addr_48() :
    [power, red, green, blue] = [pin_base[11]+12, pin_base[11]+13, pin_base[11]+14, pin_base[11]+15] 
    
    wiringpi.pinMode(red, 1)   #Red set as output
    wiringpi.pinMode(green, 1) #Green set as output
    wiringpi.pinMode(blue, 1)  #Blue set as output
    wiringpi.pinMode(power, 1) #Power set as output

    return power, red, green, blue
#-------------   Addressing Functions for LEDs    ----------------------------------------#

#------ Wiringpi Cleanup Function --------------------------------------------------------#
def cleanOutput () :
    NumIC = 12      #Number of ICs that need to be cleaned up
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
#---------------- Clean Output -----------------------------------------------------------#

        
#------ Color Function - Assign certain LED a color  -------------------------------------#
def color(LEDaddr, color) :
    [power, red, green, blue] = LEDaddr

    if color == "K" :                   #K = Black
        wiringpi.digitalWrite(power, 0)
        wiringpi.digitalWrite(red, 0)
        wiringpi.digitalWrite(green, 0)
        wiringpi.digitalWrite(blue, 0)
        return
    
    #supplys 5v to anode
    wiringpi.digitalWrite(power, 1)
    
    if color == 'R' :                   #R = Red
        wiringpi.digitalWrite(red, 0)
        wiringpi.digitalWrite(green, 1)
        wiringpi.digitalWrite(blue, 1)

    elif color == 'G':                  #G = Green
        wiringpi.digitalWrite(red, 1)
        wiringpi.digitalWrite(green, 0)
        wiringpi.digitalWrite(blue, 1)

    elif color == 'B':                  #B = Blue
        wiringpi.digitalWrite(red, 1)
        wiringpi.digitalWrite(green, 1)
        wiringpi.digitalWrite(blue, 0)

    elif color == 'Y' :                 #Y = Yellow
        wiringpi.digitalWrite(red, 0)
        wiringpi.digitalWrite(green, 0)
        wiringpi.digitalWrite(blue, 1)

    elif color == 'P' :                 #P = Purple
        wiringpi.digitalWrite(red, 0)
        wiringpi.digitalWrite(green, 1)
        wiringpi.digitalWrite(blue, 0)

    elif color == 'C' :                 #C = Cyan
        wiringpi.digitalWrite(red, 1)
        wiringpi.digitalWrite(green, 0)
        wiringpi.digitalWrite(blue, 0)

    elif color == 'W' :                 #W = White
        wiringpi.digitalWrite(red, 0)
        wiringpi.digitalWrite(green, 0)
        wiringpi.digitalWrite(blue, 0)

    else :
        print "Not an available color?"
        wiringpi.digitalWrite(power, 0) #Sets power OUTPUT to LOW
        wiringpi.pinMode(power, 0)      #Sets power PIN to
#------ Function to assign certain LED to specific color ---------------------------------#

        
#--------------- Prompt Function ---------------------------------------------------------#
def prompt(promptStr) :
    x = raw_input(promptStr)
    return x
#--------------- Prompt Function ---------------------------------------------------------#


#--------------   Degree(theta) Function -------------------------------------------------#
#input(theta)= the angle of stick 1
#output(allColors)= 4 element List containing colors for 4 sticks
def Degree(theta) :
    theta1 = theta
    theta2 = theta + 90
    theta3 = theta + 180
    theta4 = theta + 270

    if theta1 >= 360 :
        theta1 = theta -360
    if theta2 >= 360 :
        theta2 = theta2 - 360
    if theta3 >= 360 :
        theta3 = theta3 - 360
    if theta4 >= 360 :
        theta4 = theta4 - 360
    
    allColors = []
    allColors.append(colorList[theta1*12:(theta1*12)+12])
    allColors.append(colorList[theta2*12:(theta2*12)+12])
    allColors.append(colorList[theta3*12:(theta3*12)+12])
    allColors.append(colorList[theta4*12:(theta4*12)+12])
    
    return allColors
#--------------   Degree(theta) Function -------------------------------------------------#

    
#__MAIN__
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
LED13 = [p13, r13, g13, b13] = addr_13()
LED14 = [p14, r14, g14, b14] = addr_14()
LED15 = [p15, r15, g15, b15] = addr_15()
LED16 = [p16, r16, g16, b16] = addr_16()
LED17 = [p17, r17, g17, b17] = addr_17()
LED18 = [p18, r18, g18, b18] = addr_18()
LED19 = [p19, r19, g19, b19] = addr_19()
LED20 = [p20, r20, g20, b20] = addr_20()
LED21 = [p21, r21, g21, b21] = addr_21()
LED22 = [p22, r22, g22, b22] = addr_22()
LED23 = [p23, r23, g23, b23] = addr_23()
LED24 = [p24, r24, g24, b24] = addr_24()
LED25 = [p25, r25, g25, b25] = addr_25()
LED26 = [p26, r26, g26, b26] = addr_26()
LED27 = [p27, r27, g27, b27] = addr_27()
LED28 = [p28, r28, g28, b28] = addr_28()
LED29 = [p29, r29, g29, b29] = addr_29()
LED30 = [p30, r30, g30, b30] = addr_30()
LED31 = [p31, r31, g31, b31] = addr_31()
LED32 = [p32, r32, g32, b32] = addr_32()
LED33 = [p33, r33, g33, b33] = addr_33()
LED34 = [p34, r34, g34, b34] = addr_34()
LED35 = [p35, r35, g35, b35] = addr_35()
LED36 = [p36, r36, g36, b36] = addr_36()
LED37 = [p37, r37, g37, b37] = addr_37()
LED38 = [p38, r38, g38, b38] = addr_38()
LED39 = [p39, r39, g39, b39] = addr_39()
LED40 = [p40, r40, g40, b40] = addr_40()
LED41 = [p41, r41, g41, b41] = addr_41()
LED42 = [p42, r42, g42, b42] = addr_42()
LED43 = [p43, r43, g43, b43] = addr_43()
LED44 = [p44, r44, g44, b44] = addr_44()
LED45 = [p45, r45, g45, b45] = addr_45()
LED46 = [p46, r46, g46, b46] = addr_46()
LED47 = [p47, r47, g47, b47] = addr_47()
LED48 = [p48, r48, g48, b48] = addr_48()

LEDaddr = [LED1, LED2, LED3, LED4, LED5, LED6, LED7, LED8, LED9, LED10, LED11, LED12, LED13, LED14, LED15, LED16, LED17, LED18, LED19, LED20, LED21, LED22, LED23, LED24, LED25, LED26, LED27, LED28, LED29, LED30, LED31, LED32, LED33, LED34, LED35, LED36, LED37, LED38, LED39, LED40, LED41, LED42, LED43, LED44, LED45, LED46, LED47, LED48]
#Implementing RPM tracking
#Defing variables outside of while loop
RPM = 0.0
RPS = RPM / 60.0
DegPS = RPS * 360.0
SPDeg = 1 / DegPS
DTS = SPDeg * deg
theta_1 = 0

time1 = time.time()     #Time of last reading
time2 = time.time()     #Time of passing magnet (now)

try :
    while True :
        if GPIO.input(5) == False :  #Stick 1 passes Magnet @ 180deg (LEFT)
            time2 = time.time()
            dt = time2 - time1
            if dt > 0.1 and dt < 1000 :
                RPS = 0.25/dt
                RPM = 60 * RPS
                SPDeg = 1.0 / (RPS*360)
                time1 = time2
            if dt > 1000 :
                #shut off??
                print "Too slow!"
            elif dt < 0.1 :
                print "Too fast! "
            theta_1 = 170

        if GPIO.input(6) == False :  #Stick 2 passes Magnet (stick 1 is now at 90deg, BOTTOM)
            time2 = time.time()
            dt = time2 - time1
            if dt > 0.1 and dt < 1000 :
                RPS = 0.25/dt
                RPM = 60 * RPS
                SPDeg = 1.0 / (RPS*360)
                time1 = time2
            if dt > 1000 :
                #shut off??
                print "Too slow!"
            elif dt < 0.1 :
                print "Too fast! "
            theta_1 = 80

        if GPIO.input(13) == False :  #Stick 3 passes Magnet (stick 1 is now at 0deg, RIGHT)
            time2 = time.time()
            dt = time2 - time1
            if dt > 0.1 and dt < 1000 :
                RPS = 0.25/dt
                RPM = 60 * RPS
                SPDeg = 1.0 / (RPS*360)
                time1 = time2
            if dt > 1000 :
                #shut off??
                print "Too slow!"
            elif dt < 0.1 :
                print "Too fast! "
            theta_1 = 350

        if GPIO.input(26) == False :  #Stick 4 passes Magnet (stick 1 is now at 270deg, TOP)
            time2 = time.time()
            dt = time2 - time1
            if dt > 0.1 and dt < 1000 :
                RPS = 0.25/dt
                RPM = 60 * RPS
                SPDeg = 1.0 / (RPS*360)
                time1 = time2
            if dt > 1000 :
                #shut off??
                print "Too slow!"
            elif dt < 0.1 :
                print "Too fast! "
            theta_1 = 260

        #When the bike goes 1 degree, update theta and assign all LEDs proper colors
        if ("%.4f" % time.time()) == ("%.4f" % time2 + SPDeg) :
            theta = theta - 1   #minus one because way i defined angles (CCW = negative)
            if theta < 0 :      #changes -1degree to 359degrees
                theta = theta + 360
            allColors = Degree(theta)
            time2 = time2 + SPDeg

            #Assigning LEDs the colors from allColors list
            #LED Stick 1
            i = 0
            while i < 12 :
                color(LEDaddr[i], allColors[0][i])
                i = i+1
            #LED Stick 2
            i = 0
            while i < 12 :
                color(LEDaddr[12+i], allColors[1][i])
                i = i+1
            #LED Stick 3
            i = 0
            while i < 12 :
                color(LEDaddr[24+i], allColors[2][i])
                i = i+1
            #LED Stick 4
            i = 0
            while i < 12 :
                color(LEDaddr[36+i], allColors[3][i])
                i = i+1

except KeyboardInterrupt :
    pass

#----  Cleanup  ----#
cleanOutput()
GPIO.cleanup
