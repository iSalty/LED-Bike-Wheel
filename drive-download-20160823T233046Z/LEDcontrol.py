import wiringpi2 as wiringpi
import RPi.GPIO as GPIO
import time
import io
import glob
import os

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

c0 = wiringpi.wiringPiSPISetup(0, 8000000)
c1 = wiringpi.wiringPiSPISetup(1, 8000000)

#Read in the Text files which contains the all of the colors for the image
path = '/home/pi/Desktop/Playlist/Playlist3'
frameTime = 1   #How long (in seconds) each frame is displayed for

fileNames = []
for filename in sorted(glob.glob(os.path.join(path, '*.txt'))) :
    print filename
    fileNames.append(filename)

frames = []
i = 0
while i<len(fileNames) :
    frames.append(open(fileNames[i], 'r').read())
    i = i+1

numFrames = len(frames)
print "NumFrames: ",numFrames
print "Frame Time : ",frameTime,"seconds"

#Hall Sensors
HALL_ADDR1 = 5
HALL_ADDR2 = 6
HALL_ADDR3 = 13
HALL_ADDR4 = 21
GPIO.setup(HALL_ADDR1, GPIO.IN)
GPIO.setup(HALL_ADDR2, GPIO.IN)
GPIO.setup(HALL_ADDR3, GPIO.IN)
GPIO.setup(HALL_ADDR4, GPIO.IN)

#Making array each IC is addressed by pin_base[IC#-1]
PIN_BASE = 65
pin_base = [PIN_BASE, PIN_BASE+16, PIN_BASE+32, PIN_BASE+48, PIN_BASE+64, PIN_BASE+80, PIN_BASE+96, PIN_BASE+112, PIN_BASE+128, PIN_BASE+144, PIN_BASE+160, PIN_BASE+176]

#doing setup for each individual IC
wiringpi.mcp23s17Setup(pin_base[0], 0, 0x10)    #IC 0  (LEDs 1-4)   (Pins 65-80)
wiringpi.mcp23s17Setup(pin_base[1], 0, 0x11)    #IC 1  (LEDs 5-8)   (Pins 81-96)
wiringpi.mcp23s17Setup(pin_base[2], 0, 0x12)    #IC 2  (LEDs 9-12)  (Pins 97-112)
wiringpi.mcp23s17Setup(pin_base[3], 0, 0x13)    #IC 3  (LEDs 13-16) (Pins 113-128)
wiringpi.mcp23s17Setup(pin_base[4], 0, 0x14)    #IC 4  (LEDs 17-20) (Pins 129-144)
wiringpi.mcp23s17Setup(pin_base[5], 0, 0x15)    #IC 5  (LEDs 21-24) (Pins 145-160)
wiringpi.mcp23s17Setup(pin_base[6], 1, 0x10)    #IC 6  (LEDs 25-28) (Pins 161-176)
wiringpi.mcp23s17Setup(pin_base[7], 1, 0x11)    #IC 7  (LEDs 29-32) (Pins 177-192)
wiringpi.mcp23s17Setup(pin_base[8], 1, 0x12)    #IC 8  (LEDs 33-36) (Pins 193-208)
wiringpi.mcp23s17Setup(pin_base[9], 1, 0x13)    #IC 9  (LEDs 37-40) (Pins 209-224)
wiringpi.mcp23s17Setup(pin_base[10], 1, 0x14)   #IC 10 (LEDs 41-44) (Pins 225-240)
wiringpi.mcp23s17Setup(pin_base[11], 1, 0x15)   #IC 11 (LEDs 45-48) (Pins 241-256)


frameOffset = 4320
decimalOffset = frameOffset/2 #in colorsDecimal how long a frame is [0:frameOffset/2]


#colorList array -- Frame1 = [0:4320], Frame2 = [4320, 2*4320] ...
colorList = []
j = 0
while j < numFrames :
    i = 0
    while i < len(frames[j]) :       #creating a List of all the relevant colors (each 12 represents the colors for a stick for 1 degree)
        colorList.append(frames[j][i])
        i = i+2
    j = j + 1
#BREAKPOINT HERE
print "ColorList length: ", len(colorList)

#make the file into hex numbers and then finally into decimals
colorsHex = []
i = 1
while i < len(colorList) :
    color2 = colorList[i]
    color1 = colorList[i-1]
    #color2     read color 2 first because of how data is passed into wiringPiSPIDataRW
    #Have 0 after the hex number because these are the MS4Bits
    if color2 == 'K' :
        colorsHex.append("00")
    elif color2 == 'R' :
        colorsHex.append("D0")
    elif color2 == 'Y' :
        colorsHex.append("90")
    elif color2 == 'G' :
        colorsHex.append("B0")
    elif color2 == 'C' :
        colorsHex.append("30")
    elif color2 == 'B' :
        colorsHex.append("70")
    elif color2 == 'P' :
        colorsHex.append("50")
    elif color2 == 'W' :
        colorsHex.append("10")
    else :
        print "Error color2 not read properly at i=", i
        print "color2 = ", color2
    #color1
    if color1 == 'K' :
        colorsHex.append('0')
    elif color1 == 'R' :
        colorsHex.append('D')
    elif color1 == 'Y' :
        colorsHex.append('9')
    elif color1 == 'G' :
        colorsHex.append('B')
    elif color1 == 'C' :
        colorsHex.append('3')
    elif color1 == 'B' :
        colorsHex.append('7')
    elif color1 == 'P' :
        colorsHex.append('5')
    elif color1 == 'W' :
        colorsHex.append('1')
    else :
        print "Error color1 not read properly at i=", i
        print "Color1 = ", color1
    #increment i by 2
    i = i+2

#Array containing decimal equivalent of hex values, is half of length of colorList becuase each hex (0xab) represents 2 LEDs
colorsDecimal = []      
i = 0
while i < len(colorsHex) :
    x = int(colorsHex[i], 16)   #First Hex Digit (Represents colors of first two LEDs of a given IC)
    y = int(colorsHex[i+1], 16) #Second Hex Digit (Representes colors of last two LEDs of a given IC)
    z = x+y
    colorsDecimal.append(z)

    #increment i by 2
    i = i+2

#Prints for prntScrn
##print "Color List:   ",colorList[0:12]
##print "Hex List:     ",colorsHex[0:12]
##print "Decimal List: ",colorsDecimal[0:6]
#-------------      Reading Picture File       ----------------------------------------------#
    
#-- Various parameters for the buffer to be passed into wiringPiSPIDataRW --#
IC0 = int("0x40", 16)   #converting hex values into integers
IC1 = int("0x42", 16)
IC2 = int("0x44", 16)
IC3 = int("0x46", 16)
IC4 = int("0x48", 16)
IC5 = int("0x4A", 16)
ICaddr = [IC0, IC1, IC2, IC3, IC4, IC5]

GPIOA = int("0x12", 16)

buff = [0,0,0,0]  

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
        print "Error in cleanup."
#---------------- Clean Output -----------------------------------------------------------#

#--------------- Prompt Function ---------------------------------------------------------#
def prompt(promptStr) :
    x = raw_input(promptStr)
    return x
#--------------- Prompt Function ---------------------------------------------------------#

#--------------   Degree(theta) Function -------------------------------------------------#
#input(theta)= the angle of stick 1
#output(allColors)= 4 element List containing colors for 4 sticks
def Degree(theta,frame) :
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
    allColors.append(colorsDecimal[(decimalOffset*(frame-1))+theta1*6:(decimalOffset*(frame-1))+(theta1*6)+6])      #mult by 6 because each hex number = 2 LEDs of color
    allColors.append(colorsDecimal[(decimalOffset*(frame-1))+theta2*6:(decimalOffset*(frame-1))+(theta2*6)+6])
    allColors.append(colorsDecimal[(decimalOffset*(frame-1))+theta3*6:(decimalOffset*(frame-1))+(theta3*6)+6])
    allColors.append(colorsDecimal[(decimalOffset*(frame-1))+theta4*6:(decimalOffset*(frame-1))+(theta4*6)+6])
    
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

#Implementing RPM tracking
#Defing variables outside of while loop
RPM = 1.0
RPS = RPM / 60.0
DegPS = RPS * 360.0
SPDeg = 1 / DegPS
theta_1 = 0
count = 0

frameTimer = time.time() #This will be updated after switching frames 
frameUpdateTimer = frameTimer + frameTime
frame = 1

time1 = time.time()     #Time of last reading
time2 = time.time()     #Time of passing magnet (now)
timeUpdate = time2 + 2*SPDeg

#Entering while loop
try :
    while True :
        if ("%.4f", time.time()) >= ("%.4f", frameUpdateTimer) :
            frameTimer = frameUpdateTimer
            frameUpdateTimer = frameTimer + frameTime
            frame = frame + 1
        if frame > numFrames :
            frame = 1
        if GPIO.input(5) == False :  #Stick 1 passes Magnet @ 170deg (LEFT)
            time2 = time.time()
            dt = time2 - time1
            if dt > 0.1 and dt < 1000 :
                RPS = 0.25/dt
                RPM = 60 * RPS
                SPDeg = 1.0 / (RPS*360)
                time1 = time2
		print "Hall 1 read"
            if dt > 1000 :
                #shut off??
                print "Too slow Hall 1!"
            elif dt < 0.1 :
                print "Too fast Hall 1! "
            theta_1 = 170

        if GPIO.input(6) == False :  #Stick 2 passes Magnet (stick 1 is now at 80deg, BOTTOM)
            time2 = time.time()
            dt = time2 - time1
            if dt > 0.1 and dt < 1000 :
                RPS = 0.25/dt
                RPM = 60 * RPS
                SPDeg = 1.0 / (RPS*360)
                time1 = time2
		print "Hall 2 read"
            if dt > 1000 :
                #shut off??
                print "Too slow Hall 2!"
            elif dt < 0.1 :
                print "Too fast Hall 2! "
            theta_1 = 80

        if GPIO.input(13) == False :  #Stick 3 passes Magnet (stick 1 is now at 350deg, RIGHT)
            time2 = time.time()
            dt = time2 - time1
            if dt > 0.1 and dt < 1000 :
                RPS = 0.25/dt
                RPM = 60 * RPS
                SPDeg = 1.0 / (RPS*360)
                time1 = time2
		print "Hall 3 read"
            if dt > 1000 :
                #shut off??
                print "Too slow Hall 3!"
            elif dt < 0.1 :
                print "Too fast Hall 3! "
            theta_1 = 350

        if GPIO.input(21) == False :  #Stick 4 passes Magnet (stick 1 is now at 260deg, TOP)
            time2 = time.time()
            dt = time2 - time1
            if dt > 0.1 and dt < 1000 :
                RPS = 0.25/dt
                RPM = 60 * RPS
                SPDeg = 1.0 / (RPS*360)
                time1 = time2
		print "Hall 4 read"
            if dt > 1000 :
                #shut off??
                print "Too slow Hall 4!"
            elif dt < 0.1 :
                print "Too fast Hall 4! "
            theta_1 = 260

        #When the bike goes 2 degree, update theta and assign all LEDs proper colors
        if ("%.4f" % time.time()) >= ("%.4f" % timeUpdate) :
           # count =  count + 1
           # if count%1000==1 :
           #     print ("%.4f" % time.time())
            theta_1 = theta_1 - 1   #minus one because way i defined angles (CCW = negative)
            if theta_1 < 0 :      #changes -1degree to 359degrees
                theta_1 = theta_1 + 360
            timeUpdate = timeUpdate + SPDeg
            
            #Update Buffer with appropriate integer values
            degreeColors = Degree(theta_1,frame)
            
            #Assigning LEDs the colors from degreeColors list
            i = 0
            while i < 3 :
                #LED Stick 1
                buff_1 = ''.join(chr(x) for x in [ICaddr[i], GPIOA, degreeColors[0][2*i], degreeColors[0][2*i+1]])
                result = wiringpi.wiringPiSPIDataRW(0, buff_1)
                #LED Stick 2
                buff_2 = ''.join(chr(x) for x in [ICaddr[i+3], GPIOA, degreeColors[1][2*i], degreeColors[1][2*i+1]])
                result = wiringpi.wiringPiSPIDataRW(0, buff_2)
                #LED Stick 3
                buff_3 = ''.join(chr(x) for x in [ICaddr[i], GPIOA, degreeColors[2][2*i], degreeColors[2][2*i+1]])
                result = wiringpi.wiringPiSPIDataRW(1, buff_3)
                #LED Stick 4
                buff_4 = ''.join(chr(x) for x in [ICaddr[i+3], GPIOA, degreeColors[3][2*i], degreeColors[3][2*i+1]])
                result = wiringpi.wiringPiSPIDataRW(1, buff_4)
                i = i+1
                
except KeyboardInterrupt :
    pass

#----  Cleanup  ----#
cleanOutput()
buff_clean = ''.join(chr(x) for x in [ICaddr[0], GPIOA, 0x00, 0x00])
result = wiringpi.wiringPiSPIDataRW(1,buff_clean)
buff_clean1 = ''.join(chr(x) for x in [ICaddr[1], GPIOA, 0x00, 0x00])
result = wiringpi.wiringPiSPIDataRW(1,buff_clean1)
buff_clean2 = ''.join(chr(x) for x in [ICaddr[4], GPIOA, 0x00, 0x00])
result = wiringpi.wiringPiSPIDataRW(1, buff_clean2)
GPIO.cleanup

