import sys
f = open(sys.argv[1], "r")

previous = int(f.readline())

increaseNumber = 0
for x in f:
    number = int(x)
    if previous < number: 
        increaseNumber += 1
    previous = number
print(increaseNumber)
