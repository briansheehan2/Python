#Reading Files in python
import os
print("Python current working directory (CWD) =",os.getcwd())
os.chdir("C:\\MyPython")
print("Reading a file using with")
with open('readme.txt') as rFile:
    data = rFile.read()
    print(data)

print("Processing a text file one line at a time")
with open('readme.txt') as rFile:
    for line in rFile:
        print(line, end ='')
