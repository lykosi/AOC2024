data = open('Inputs\day2.txt', 'r').read().split('\n')
reports = []
for sReports in data:
    reports.append(list(map(int, sReports.split())))

unsafe = 0
safe = 0
for report in reports:
     bIs_decreasing = report == sorted(report, reverse=True)
     for index, level in enumerate(report):
        if index != 0:
            previous_number  = report[index - 1]
            if bIs_decreasing:
                if previous_number - 4 >= level or previous_number < level or previous_number == level:
                    unsafe += 1
                    break
            else:
                if previous_number + 4 <= level or previous_number > level or previous_number == level:
                    unsafe += 1
                    break     
            if index  == len(report) - 1:
                safe += 1 
print(safe, "reports are safe") #287

def IsDecreasing(nums):
    return nums == sorted(nums, reverse=True)
