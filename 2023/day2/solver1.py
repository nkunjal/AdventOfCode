answer = 0
f = open("input.txt", "r")
for line in f.readlines():
    lines = line.split(" ")
    idNum = int(lines[1][:-1])
    line = " ".join(lines[2:])
    rounds = line.split(";")
    possible = True
    for r in rounds:
        items = r.split(",")
        for l in items:
            item = l.split()
            if item[1] == "green" and int(item[0]) > 13:
                possible = False
                break
            elif item[1] == "red" and int(item[0]) > 12:
                possible = False
                break
            elif item[1] == "blue" and int(item[0]) > 14:
                possible = False
                break
    if possible:
        answer += idNum

print(answer)
