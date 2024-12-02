result = []
right_column = []
left_column = []

data = open('Inputs\day1.txt', 'r').read().split('\n')
for sDistances in data:
    iDistances = list(map(int, sDistances.split()))
    left_column.append(iDistances[0])
    right_column.append(iDistances[1])

for value in left_column:
    occurrence = right_column.count(value)
    result.append(value * occurrence)

response = sum(result)
print("The similarity score is:", response) #28786472