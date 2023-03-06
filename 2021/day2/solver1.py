import sys
f = open(sys.argv[1], "r")

horizontal = 0
vertical = 0
for line in f:
    array = line.split(" ")
    if (array[0] == "forward"):
        horizontal += int(array[1])
    elif (array[0] == "down"):
        vertical += int(array[1])
    else:
        vertical -= int(array[1])
print(horizontal*vertical)
