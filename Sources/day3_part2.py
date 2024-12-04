import re

def main():
    data = open('Inputs\day3.txt', 'r').read()
    result = retreive_matches(data)
    print("The results of the enabled multiplications is:", result) #127092535
    
def retreive_matches(data):
    regex = r"([don't]{5}\(\))|([do]{2}\(\))|(?<=mul\()\d+(?:,)\d+(?=\))"
    matches_regex = re.finditer(regex, data, re.MULTILINE)

    result = 0
    bCanExe = True
    for number, match in enumerate(matches_regex, start=1):
        values = str(match.group()).split(',')
        if(values[0] == 'do()'):
            bCanExe = True
            continue
        elif(values[0] == 'don\'t()'):
            bCanExe = False
            continue
        
        if(bCanExe):
            mul = int(values[0]) * int(values[1])
            result += mul
    return result

if __name__ == "__main__":
    main()
