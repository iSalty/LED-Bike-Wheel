import numpy as np
import os
import cv2
print "Version : " + cv2.__version__

#Loads a color image
readPath = '/home/pi/Desktop/Pictures/pacMan/'
writePath = '/home/pi/Desktop/Playlist/PlaylistTest/'
#Reads in all files in the read path
fileRead = []
print "Files to be read in:"
for filename in sorted(os.listdir(readPath)) :
    print filename
    fileRead.append(filename)
i=0
while i<len(fileRead) :
    fileRead[i] = readPath + fileRead[i]
    i = i+1

fileWrite = []
i=0
while i<len(fileRead) :
    fileWrite.append(fileRead[i][len(readPath):len(fileRead[i])-3])
    fileWrite[i] = writePath + fileWrite[i] + "txt"
    i = i+1

print "----File Write----"
print fileWrite
k = 0
while k<len(fileRead) :
    img1 = cv2.imread(fileRead[0],1)
    img2 = cv2.resize(img1, (360,360)) 
    img3 = cv2.linearPolar(img2, (img2.shape[0]/2, img2.shape[1]/2), 180, cv2.WARP_FILL_OUTLIERS)
    img4 = cv2.resize(img3, (300,300))

    #cv2.imshow('before',img1)
    #cv2.imshow('resized', img2)
    #cv2.imshow('linear-polar', img3)

    #Creates a 12*360 = 4320 element list of each LED (GRB) for each degree (360)
    img5 = []

    j = 0
    while j < img3.shape[0] :
        i = 0
        while i < 360-18-6 :
            img5.append(img3[j,6+i])
            i=i+28
        j = j+1

    #Finding color of each LED (4320 element list of color charachter, exe 'R')
    LEDcolor = []

    R = 0
    G = 0
    B = 0

    i = 0
    while i < len(img5) :
        B = img5[i][0]
        G = img5[i][1]
        R = img5[i][2]

        if R > 120 :
            if B <= 120 and G <= 120 :
                LEDcolor.append('R')
            elif B <= 120 and G >= 120:
                LEDcolor.append('Y')
            elif G <= 120 and B >= 120:
                LEDcolor.append('P')
            else :
                LEDcolor.append('W')
        elif B > 120 :
            if R <= 120 and G <= 120 :
                LEDcolor.append('B')
            elif R <= 120 and G > 120:
                LEDcolor.append('C')
        elif G > 120 :
            if R <= 120 and B <= 120 :
                LEDcolor.append('G')
        else :
            LEDcolor.append("K")

        i = i+1

    #Saving LEDcolor in a text file
    colorFile = open(fileWrite[k], 'w')
    for char in LEDcolor :
        print>>colorFile, char

    k = k+1

###Print the colors for each degree value
##i = 0
##while i < 360 :
##    print "Colors @ ",i,"deg : ", LEDcolor[i*12:(i*12)+12]
##    i = i+1
##
###------- Degree(theta) input degree of stick1, output colors for all LEDs -------#
##def Degree(theta) :
##    theta1 = theta
##    theta2 = theta + 90
##    theta3 = theta + 180
##    theta4 = theta + 270
##
##    if theta1 >= 360 :
##        theta1 = theta -360
##    if theta2 >= 360 :
##        theta2 = theta2 - 360
##    if theta3 >= 360 :
##        theta3 = theta3 - 360
##    if theta4 >= 360 :
##        theta4 = theta4 - 360
##    
##    allColors = []
##    allColors.append(LEDcolor[theta1*12:(theta1*12)+12])
##    allColors.append(LEDcolor[theta2*12:(theta2*12)+12])
##    allColors.append(LEDcolor[theta3*12:(theta3*12)+12])
##    allColors.append(LEDcolor[theta4*12:(theta4*12)+12])
##    
##    return allColors

##allColors = Degree(90)
##print ''
##print "---------------------- ---------------------"
##print "LEDStick1 : ", allColors[0]
##print "LEDStick2 : ", allColors[1]
##print "LEDStick3 : ", allColors[2]
##print "LEDStick4 : ", allColors[3]


#cv2.waitKey(0)
##cv2.destroyAllWindows()
