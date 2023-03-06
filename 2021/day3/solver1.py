import sys
f = open(sys.argv[1], "r")

line = f.readline().strip()
array = [1 if i == '1' else -1 for i in line]
for line in f:
    line = line.strip()
    for i in range(len(line)):
        if line[i] == '1':
            array[i] += 1
        else:
            array[i] -= 1
most = ""
least = ""
for i in array:
    if i > 0:
        most += '1'
        least += '0'
    else:
        most += '0'
        least += '1'

print(most, int(most, 2))
print(least, int(least, 2))
print(int(most, 2)*int(least, 2))
