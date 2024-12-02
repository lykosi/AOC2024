result = []
right_column = []
left_column = []

data = open('Inputs\day1.txt', 'r').read().split('\n')
for sDistances in data:
    iDistances = list(map(int, sDistances.split()))
    left_column.append(iDistances[0])
    right_column.append(iDistances[1])

for index in range(len(data)):
    iMin_right_column = min(right_column)
    right_column.remove(iMin_right_column)
    
    iMin_left_column = min(left_column)
    left_column.remove(iMin_left_column)

    iMin = min(iMin_right_column, iMin_left_column)
    iMax = max(iMin_right_column, iMin_left_column)
    result.append(iMax - iMin)

response = sum(result)
print("The total distance between the lists is:", response) #2430334