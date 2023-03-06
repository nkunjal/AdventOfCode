import sys
f = open(sys.argv[1], "r")

horizontal = 0
depth = 0
aim = 0
for line in f:
    array = line.split(" ")
    if (array[0] == "forward"):
        horizontal += int(array[1])
        depth += int(array[1])*aim
    elif (array[0] == "down"):
        aim += int(array[1])
    else:
        aim -= int(array[1])
print(horizontal*depth)
