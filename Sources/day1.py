result = []
rightColumn = []
leftColumn = []

data = open('Inputs\day1.txt', 'r').read().split('\n')
for sDistances in data:
    iDistances = list(map(int, sDistances.split()))
    leftColumn.append(iDistances[0])
    rightColumn.append(iDistances[1])

for index in range(len(data)):
    iMinRightColumn = min(rightColumn)
    rightColumn.remove(iMinRightColumn)
    
    iMinLeftColumn = min(leftColumn)
    leftColumn.remove(iMinLeftColumn)

    iMin = min(iMinRightColumn, iMinLeftColumn)
    iMax = max(iMinRightColumn, iMinLeftColumn)
    result.append(iMax - iMin)

response = sum(result)
print("The total distance between the lists is:", response) #2430334