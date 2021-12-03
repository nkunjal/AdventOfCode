import sys
f = open(sys.argv[1], "r")

first = int(f.readline()) 
second = int(f.readline())
third = int(f.readline())
increaseNumber = 0
for x in f:
    number = int(x)
    previousSum = first + second + third
    currentSum = second + third + number
    if previousSum < currentSum: 
        increaseNumber += 1
    first = second
    second = third
    third = number
print(increaseNumber)
