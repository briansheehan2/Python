#iteration algorithm to prompt for file name until sucessful or gracefully exit
while True:
    strFileName = input("Input a file name or press [Enter] to exit : ")
    if (strFileName == ""):
        print("You pressed [Enter] to exit. Thank you")
        break
    try:
        strFileName = open(strFileName, 'r')
    except FileNotFoundError:
        print("Wrong path and/or file name for ",strFileName)
    else:
        print("File name = ",strFileName," was found")
        break
print("goodbye")
