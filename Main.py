import math
from numpy import zeros
import math

InputArr = []

print("Enter number of points!")
n = int(input())

InterArr = zeros(n)
for i in range(n):
    InterArr[i] = zeros(n)

#constant
k = int(n / 2)

print("Write Distances of points!(Write - for unconnected point) \n")
for i in range(n):
    str1 = input()
    arr1 = str1.split()
    InputArr.append(arr1)

#set inf to math.inf
for i in range(n):
    for j in range(n):
        if(InputArr[i][j] == "inf"):
            InputArr[i][j] = math.inf
for i in range (n):
    for j in range(n):
        if(InputArr[i][j] == 0):
            InterArr[i][j] = 0
        elif(InputArr[i][j] > (InputArr[i][k] + InputArr[k][j])):
            InterArr[i][j] = (InputArr[i][k] + InputArr[k][j])
        else:
            InterArr[i][j] = "*"
