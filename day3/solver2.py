import sys
f = open(sys.argv[1], "r")

def calculateOxygen(oxygen, i):
    if len(oxygen) == 1:
        return oxygen[0]
    counter = sum([1 if line[i] == '1' else -1 for line in oxygen])
    if counter >= 0:
        return calculateOxygen([line for line in oxygen if line[i] == '1'], i + 1)
    else:
        return calculateOxygen([line for line in oxygen if line[i] == '0'], i + 1)
def calculateCarb(carb, i):
    if len(carb) == 1:
        return carb[0]
    counter = sum([1 if line[i] == '1' else -1 for line in carb])
    if counter >= 0:
        return calculateCarb([line for line in carb if line[i] == '0'], i + 1)
    else:
        return calculateCarb([line for line in carb if line[i] == '1'], i + 1)
array = [line.strip() for line in f]

oxygen = calculateOxygen(array, 0)
carbo = calculateCarb(array, 0)

print("Oxygen ", oxygen, int(oxygen, 2))
print("Carbo ", carbo, int(carbo, 2))
print(int(oxygen, 2)*int(carbo, 2))
