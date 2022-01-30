import csv
import math
with open("data4.csv", newline = '') as f:
    reader = csv.reader(f)
    data = list(reader)

data1 = data[0]

def mean(data):
    m = len(data)
    total = 0
    for x in data:
        total += int(x)

    mean = total/m
    
    return mean

squaredList = []
for number in data1:
    a = int(number) - mean(data1)
    a = a**2
    squaredList.append(a)

sum = 0
for i in squaredList:
    sum = sum + i

result = sum/(len(data1) - 1)
standardDerivation = math.sqrt(result)
print("Standard Deviation is " + str(standardDerivation))
print("Mean is " + str(mean(data1)))