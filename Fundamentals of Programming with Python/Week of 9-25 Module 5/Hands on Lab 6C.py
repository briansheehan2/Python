#start by initalizing variables
import winsound
import random
intFrequency = 2000
intDuration = 1000
fltCelcius = 00.0
fltFahrenheit = 0.0
intMinimum = 1
intMaximum = 11
fltBattery = 100.0
#program developed by Brian Sheehan
print("Thermal Handheld Scanner - Converting Celcius to Fahrenheit degrees\n")
#input values
for intScans in range (intMinimum, intMaximum):
    print("Thermal Screening Counter =",intScans)
    fltBattery = fltBattery-intMinimum*10
    print("Battery charge = {:.2f}".format(fltBattery,2))
    if(intScans <= intMaximum):
        #winsound.Beep(intFrequency,intDuration)
        fltCelcius = random.uniform(35.9,38.3)
        print("Input (Celcius) : %.2f"%fltCelcius)
        fltFahrenheit=(fltCelcius*1.8)+32
        print("Processing-Calculating Fahrenheit")
        #output
        print("Formatted Output = %.2f"%fltFahrenheit)
        if(fltFahrenheit>98.6):
            print("Traveler may have fever!")
            intFrequency=1000
            intDuration=1000
            #winsound.Beep(intFrequency,intDuration)
            print("Ask for recent covid test. If not available quarentine")
        else:
            print("Traveler has normal temp. passed thermal")
            
    else:
          print("Please recharge your themal scanner")

print("Goodbye!")          
