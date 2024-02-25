import re

dp = {}

def count_arrangements(springs, c, last=""):
    conditions = c

    print(f"{springs=}, {conditions=}, {last=}")

    # print(springs, conditions, last)
    # print(f"{dp=}")
    # print(f"{springs[0]=}")

    if springs == "" and conditions == ():
        print("here")
        return 1
    if springs == "" and conditions != ():
        return 0
    
    if springs[0] == ".":
        print("bish")
        if (springs[1:], conditions[:]) not in dp.keys():
            dp[(springs[1:], conditions[:])] = count_arrangements(springs[1:], conditions[:])
        return dp[(springs[1:], conditions[:])]
    
    if springs[0] == "?":
        print("bosh")
        c1 = c2 = 0
        if last != "#":
            if ("#"+springs[1:], conditions[:]) not in dp.keys():
                c1 = count_arrangements("#"+springs[1:], conditions[:])
                dp["#"+springs[1:], conditions[:]] = c1
            else:
                c1 = dp[("#"+springs[1:], conditions[:])]
        if ("."+springs[1:], conditions[:]) not in dp.keys():
            c2 = count_arrangements("."+springs[1:], conditions[:])
            dp["."+springs[1:], conditions[:]] = c2
        else:
            c2 = dp[("."+springs[1:], conditions[:])]
        return c1 + c2
    
    if springs[0] == "#" and conditions!=() and last != "#":
        print("bash")
        # print(f"{springs=}, {conditions=}")

        n = conditions[0]
        # print(f"{n=}")
        if "." not in springs[:n] and len(springs)>=n:
            if (springs[n:], conditions[1:]) not in dp.keys():
                dp[(springs[n:], conditions[1:])] = count_arrangements(springs[n:], conditions[1:], "#")
            return dp[(springs[n:], conditions[1:])]
        else:
            if (springs[n:], conditions[1:]) not in dp.keys():
                dp[(springs[n:], conditions[1:])] = count_arrangements(springs[n:], conditions[1:], "#")
            return dp[(springs[n:], conditions[1:])]        
    return 0
        

with open ("./12/input3.txt") as my_file:
    lines = my_file.read().splitlines()

# print(f"{lines=}")

sum = 0

for line in lines:
    # print(f"{line=}")

    springs = line.split()[0]
    # springs = ((springs + '?')*4 ) + springs

    # springs = "?".join(springs)
    # springs = springs

    conds = tuple(map(int, line.split()[1].split(",")))
    # c = " ".join(line.split()[1].split(","))
    # conds = tuple(map(int, (c + " " + c + " " + c + " " + c + " " + c).split()))
    # print(f"{c=}")
    # print(f"{springs[0]=}")
    # print(f"{str('#' + springs[1:])=}")
    # print(f"{conds=}")


    sum += count_arrangements(springs, conds)

print(f"{sum=}")

# 7857 is the answer for part 1


# test = "0001000" # does not match
# test = "0011000" # does not match
# test = "0101000" # matches
# test = "0111000" # does not match
# test = "1001000" # does not match
# test = "1011000" # does not match
# test = "1101000" # does not match
# test = "1111000" # does not match

# r = "1*(?:0{1})+1+(?:0{1})+1+(?:0{3})+1*"

# print(f"{re.fullmatch(r, test)}")

'1*(?:0{1})+1+(?:0{1})+1+(?:0{3})+1+*'
'1*(?:0{1})+1+(?:0{1})+1+(?:0{3})+1*'
'1*(?:0{1})+1+(?:0{1})+1+(?:0{3})+1*'