nodes = {}
steps = 0
sources = []
targets = []
curs = []

with open ("./8/input.txt") as file:

    instructions = file.readline().strip()
    
    for line in file:
        start = line.strip().split('=')[0].strip()
        left = line.strip().split('=')[1].split(",")[0].strip(" (")
        right = line.strip().split('=')[1].split(",")[1].strip(" )")

        nodes[start] = {
            "left": left,
            "right": right
        }

        if start.endswith("A"):
            sources.append(start)
        if start.endswith("Z"):
            targets.append(start)

instructions = instructions * 1000

# print(f"{instructions=}")

cycles = []

for source in sources:    
    steps = 0
    cur = source
    for instruction in instructions:
        # print(f"{cur=}")
        # print(f"{targets=}")
        # print(f"{instruction=}")
        # print(f"{nodes[cur]['left']=}")
        # print(f"{nodes[cur]['right']=}")

        if instruction == 'L':
            cur = nodes[cur]['left']
            steps += 1
        elif instruction == 'R':
            cur = nodes[cur]['right']
            steps += 1
        if cur in targets:
            break
    cycles.append(steps)

print(f"{cycles=}")
# print(f"{nodes=}")