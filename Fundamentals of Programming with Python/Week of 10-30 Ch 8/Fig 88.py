#creating a new file as a readme.txt
import os
print("Displaying Python current working directory (CWD) =",os.getcwd())
os.chdir("C:\\MyPython")
wFile = open("readme.txt","w")
wFile.write("First line\n")
wFile.write("Second line\n")
wFile.write("Third line\n")
print("File Name: ",wFile.name)
print("Mode of Opening: ",wFile.mode)
print("Is wFile closed: ",wFile.closed)
wFile.close()
print("Is wFile closed: ",wFile.closed)
         
