answer = 0
f = open("input.txt", "r")
mapStrToNum = {"one":1, "two":2, "three": 3, "four": 4, "five": 5, "six": 6, "seven":7, "eight": 8, "nine":9}
for line in f.readlines():
    lst = []
    for i in range(len(line)):
        c = line[i]
        word3 = line[i:i+3]
        word4 = line[i:i+4]
        word5 = line[i:i+5]
        if c.isdigit():
            lst += [int(c)]
        elif word3 in mapStrToNum.keys():
            lst += [mapStrToNum[word3]]
        elif word4 in mapStrToNum.keys():
            lst += [mapStrToNum[word4]]
        elif word5 in mapStrToNum.keys():
            lst += [mapStrToNum[word5]]
    answer += lst[0]*10 + lst[-1]

print(answer)
