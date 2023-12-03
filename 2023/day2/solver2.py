answer = 0
f = open("input.txt", "r")
for line in f.readlines():
    lines = line.split(" ")
    idNum = int(lines[1][:-1])
    line = " ".join(lines[2:])
    rounds = line.split(";")
    r, b, g = 0, 0, 0
    for roundStr in rounds:
        items = roundStr.split(",")
        for l in items:
            item = l.split()
            if item[1] == "green":
                g = max(int(item[0]), g)
            elif item[1] == "red":
                r = max(int(item[0]), r)
            elif item[1] == "blue":
                b = max(int(item[0]), b)
    answer += r*b*g

print(answer)
