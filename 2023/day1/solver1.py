answer = 0
f = open("input.txt", "r")
for line in f.readlines():
    lst = []
    for c in line:
        if c.isdigit():
            lst += [int(c)]
    answer += lst[0]*10 + lst[-1]

print(answer)
