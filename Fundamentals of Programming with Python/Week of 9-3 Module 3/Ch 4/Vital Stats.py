"""
Program: VitalSigns.py - Sequence Algorithm
Author: Brian Sheehan
Version: 1
Release: 1
"""

#Inputs
print("*******Vital Signs - Intake Form******\n")
strFirst = input("Enter First Name: ")
strLast = input("Enter Last Name: ")
fltFahrenheit=float(input("Enter Temperature in Fahrenheight"))
intPulse = int(input("Enter Pulse/Min: "))
intRespiration= int(input("Enter Respiration/min: "))
strBloodPressure = str(input("Enter Blood Pressure (Sys/Dia): "))

#Processing
print("\nCalculating Celsium from Fahrenheit degrees! \n")
fltCelsius = (fltFahrenheit - 32)/1.8 #calc celcius

      #Outputs
print("*******Vital Signs - Intake Report******* \n")
print("Welcome "+strFirst+" "+strLast)
print("Temp in F = ",fltFahrenheit)
print("Temp in C = %0.2f" %fltCelsius)
print("Pulse/Min = ",intPulse)
print("Resp/Min = " ,intRespiration)
print("Blood Pressire (Sys/Dia) = ", strBloodPressure)
