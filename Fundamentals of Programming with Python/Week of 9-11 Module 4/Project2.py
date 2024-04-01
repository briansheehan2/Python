#Program: VitalSigns
#Author: Brian Sheehan
#Version: 1
#Release: 1

#Inputs
print("Vital Signs Program - By Brian Sheehan")
strFirst = input("Enter first name : ")
strLast = input("Enter last name : ")
fltFahrenheit = float(input("Enter Temperature in Fahrenheit degrees : "))
intPulse = int(input("Enter Pulse/Minute : "))
intRespiration = int(input("Enter Respiration/Minute : "))
strBloodPressure = str(input("Enter Blood Pressure (Systolic/Diastolic) : "))

#Processing
print("\nCalculating Celcius from Fahrenheit degrees! \n")
fltCelsius = (fltFahrenheit-32)/1.8 #Calculating Celsius Degrees

#Output
print("*******Vital Signs - Intake Report******* \n")
print("Welcome "+strFirst+" "+strLast)
print("Temperature in Fahrenheit degrees = ",fltFahrenheit)
print("Temperature in Celsius degrees = %0.2f" %fltCelsius)
print("Pulse/Minute = ",intPulse)
print("Respiration/Minute = ",intRespiration)
print("Blood Pressure (Systolic/Diastolic) = ",strBloodPressure)

