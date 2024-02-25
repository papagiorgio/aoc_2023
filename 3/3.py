import re

table = []
nums = {}
symbols = []
gears = {}

def check_nums(nums, symbols): # check for every number if there is a symbol directly above, below or next to it and return the sum
    sum = 0
    for i, positions in nums.items():
        # print(f"{i=}, {positions=}")
        for pos in positions:
            # print(f"{i=}, {pos=}")
            r1, c1 = pos[0]
            r2, c2 = pos[1]
            found = False

            # check if there is a symbol directly next to the number
            if (r1, c1-1) in symbols: # left
                if (r1, c1-1) not in gears:
                    gears[(r1, c1-1)] = []
                gears[(r1, c1-1)].append(i)
                sum += int(i)
                found = True
                sum += int(i)
                found = True
            if not found and (r1, c2) in symbols: # right
                if (r1, c2) not in gears:
                    gears[(r1, c2)] = []
                gears[(r1, c2)].append(i)
                sum += int(i)
                found = True
            
            breaker = False
            if not found:
                # check if there is a symbol directly above the number
                for c in range(c1-1, c2+1):
                    if (r1-1, c) in symbols:
                        if (r1-1, c) not in gears:
                            gears[(r1-1, c)] = []
                        gears[(r1-1, c)].append(i)
                        sum += int(i)
                        found = True
                        break
            if not found:
                # check if there is a symbol directly below the number
                for c in range(c1-1, c2+1):
                    if (r2+1, c) in symbols:
                        if (r2+1, c) not in gears:
                            gears[(r2+1, c)] = []
                        gears[(r2+1, c)].append(i)
                        sum += int(i)
                        found = True
                        break
      
    return sum


sum = 0

with open("c:/Users/tk/ref/python_projects/advent_of_code/3/input.txt") as my_file:
    # lines.append(my_file.readlines())
    lines  = my_file.readlines()
    # print(f"{len(lines)=}")

for i, line in enumerate(lines):
    res = re.findall(r'\d+', line)
    # print(f"{res.start()=}, {res.end()=}")

    for match in re.finditer(r'\d+', line):
        # print("i", i, "match", match.group(), "start index", match.start(), "End index", match.end())
        if match.group() not in nums:
            nums[match.group()] = []
        
        nums[match.group()].append(((i, match.start()), (i, match.end())))
        # nums[match.group()] = ((i, match.start()), (i, match.end()))

    for match in re.finditer(r'[*]+', line.strip()):
        if match.group() != ".":
            # print("i", i, "match", match.group(), "start index", match.start(), "End index", match.end())
            symbols.append((i, match.start()))
    
    # print(f"{symbols=}")

print(f"{check_nums(nums, symbols)=}")
prods = 0
for gear in gears:
    # print(f"{gears[gear]=}")
    if len(gears[gear]) == 2:
        prods += int(gears[gear][0]) * int(gears[gear][1])
# print(f"{gears=}")
print(f"{prods=}")
# print(f"{table=}")
# print(f"{nums=}")
# print(f"{symbols=}")
# print(f"{table.find(nums[0, 0])=}")
