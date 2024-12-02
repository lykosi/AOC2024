result = []
rightColumn = []
leftColumn = []

data = open('Inputs\day1.txt', 'r').read().split('\n')
for sDistances in data:
    iDistances = list(map(int, sDistances.split()))
    leftColumn.append(iDistances[0])
    rightColumn.append(iDistances[1])

for value in leftColumn:
    occurrence = rightColumn.count(value)
    result.append(value * occurrence)

response = sum(result)
print("The similarity score is:", response) #28786472