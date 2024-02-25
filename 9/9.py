
with open ("./9/input2.txt") as my_file:

    lines = my_file.readlines()

sum = 0

for line in lines:
    diffs = []
    diffs.append(list(map(int, line.strip().split()))[::-1]) # reverse for part 2
    all_zeroes = False

    while not all_zeroes:
        all_zeroes = True
        diffs.append([])

        for i in range(0, len(diffs[-2])-1):
            diffs[-1].append(int(diffs[-2][i+1]) - int(diffs[-2][i]))

            if int(diffs[-2][i+1]) - int(diffs[-2][i]) != 0:
                all_zeroes = False
        
        print(f"{diffs=}")

    for i in range(len(diffs)-1, 0, -1):
        diffs[i-1].append(diffs[i-1][-1] + diffs[i][-1])

    sum += diffs[0][-1]

# print(f"{diffs=}")
print(f"{sum=}")
