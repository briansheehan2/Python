# Figure 75
def udfAverage(dataSum, dataCount):
    return dataSum/dataCount

data = [1,2,3,4,5,6,7,8,9,10]
intLength = len(data)
print("Data Length =",intLength)
intSum = sum(data)
print("Data Sum =",intSum)
fltAverage=udfAverage(intSum,intLength)
print("Data Average =",fltAverage)
