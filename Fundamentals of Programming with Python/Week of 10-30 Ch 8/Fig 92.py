print("****************Vital Signs - Intake Form**********\n")
strFirst = input("Enter First Name: ")
strLast = input("Enter Last Name: ")
fltFahrenheit = float(input("Enter Temp in Deg F: "))
intPulse = int(input("Enter Pulse/min: "))
intRespiration = int(input("Enter Respiration/min: "))
strBloodPressure = str(input("Enter BP (sys/Dia): "))

print("\nCalculating Celcius from F deg!\n")
fltCelsius = (fltFahrenheit -32)/1.8

print("**********Vital Signs - Intake Report **********")
print("Welcome "+strFirst+" "+strLast)
print("Temp in F: ",fltFahrenheit)
print("Temp in C: %0.2f", fltCelsius)
print("Pulse/min: ",intPulse)
print("Respiration: ",intRespiration)
print("Blood pressure: ",strBloodPressure)
