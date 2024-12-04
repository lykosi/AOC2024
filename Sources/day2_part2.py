def main():
    data = open('Inputs\day2.txt', 'r').read().split('\n')
    reports = []
    for sReports in data:
        reports.append(list(map(int, sReports.split())))
    part2(reports)

def part2(reports):
    valid_reports = 0     
    for report in reports:
        if is_valid(report):
            valid_reports += 1
            continue
        
        bDampener = False
        for index_len in range(len(report)): 
            modified_report = [level for index, level in enumerate(report) if index != index_len]
            
            if is_valid(modified_report):
                bDampener = True
                break

        if bDampener:
            valid_reports += 1

    print(valid_reports, "reports are safe") #354


def is_valid(report):
    is_increasing = is_increasing_sequence(report)
    is_decreasing = is_decreasing_sequence(report)

    if not is_increasing and not is_decreasing:
        return False
    
    for index, level in enumerate(report):
        if index != 0:
            previous_number  = report[index - 1]
            if is_decreasing:
                if previous_number - 4 >= level or previous_number < level or previous_number == level:
                    return False           
            else:
                if previous_number + 4 <= level or previous_number > level or previous_number == level:
                    return False 
    return True

def is_decreasing_sequence(report):
    return  report == sorted(report, reverse=True)
def is_increasing_sequence(report):
    return  report == sorted(report, reverse=False)

if __name__ == "__main__":
    main()