def move(cur, last):
    i, j = cur
    last_i, last_j = last

    if lines[i][j] == "|":
        route[i][j] = "|"
        if last_i < i:
            return (i+1, j)
        else:
            return (i-1, j)
    elif lines[i][j] == "-":
        route[i][j] = "-"
        if last_j < j:
            return (i, j+1)
        else:
            return (i, j-1)
    elif lines[i][j] == "L":
        route[i][j] = "L"
        if last_i < i:
            return (i, j+1)
        else:
            return (i-1, j)
    elif lines[i][j] == "J":
        route[i][j] = "J"
        if last_i < i:
            return (i, j-1)
        else:
            return (i-1, j)
    elif lines[i][j] == "7":
        route[i][j] = "7"
        if last_j < j:
            return (i+1, j)
        else:
            return (i, j-1)
    elif lines[i][j] == "F":
        route[i][j] = "F"
        if last_i > i:
            return (i, j+1)
        else:
            return (i+1, j)

with open ("./10/input.txt") as file:
    
    lines = file.readlines()


max_x = len(lines[0].strip())
max_y = len(lines)

route = [["0" for i in range(max_x)] for j in range(max_y)]

for i in range(len(lines)):
    for j in range(len(lines[i])):
        if lines[i][j] == "S":
            start = (i, j)
            print(f"{start=}")

# input.txt
cur1 = (117, 63)
cur2 = (119, 63)
last1 = (118, 63)
last2 = (118, 63)
route[start[0]][start[1]] = "|"


# input2.txt
# cur1 = (1, 2)
# cur2 = (2, 1)
# last1 = (1, 1)
# last2 = (1, 1)
# route[start[0]][start[1]] = "F"


#input4.txt
# cur1 = (1, 2)
# cur2 = (2, 1)
# last1 = (1, 1)
# last2 = (1, 1)
# route[start[0]][start[1]] = "F"


# input5.txt
# cur1 = (4, 13)
# cur2 = (5, 12)
# last1 = (4, 12)
# last2 = (4, 12)
# route[start[0]][start[1]] = "F"


sum = 1

while cur1 != cur2:
    tmp1 = cur1
    tmp2 = cur2

    cur1 = move(cur1, last1)
    cur2 = move(cur2, last2)

    last1 = tmp1
    last2 = tmp2

    sum += 1

cur1 = move(cur1, last1)
cur2 = move(cur2, last2)

inner = 0
row_count = 0

for row in route:
    col_count = 0

    edge_up = False
    edge_down = False

    for col in row:
        if col == "0":
            if (col_count%2 != 0):
                inner += 1 
        elif col == "|":
            col_count += 1
            row_count += 1
        elif col == "F":
            edge_up = True
        elif col == "L":
            edge_down = True
        elif col == "J" and edge_up:
            col_count += 1
            edge_up = False
            edge_down = False
        elif col == "7" and edge_down:
            col_count += 1
            edge_up = False
            edge_down = False
        elif col == "J" and edge_down:
            edge_down = False
        elif col == "7" and edge_up:
            edge_up = False

print(f"{inner=}")

""""
1366 is too high (979 was too hight too...)



| is a vertical pipe connecting north and south.
- is a horizontal pipe connecting east and west.
L is a 90-degree bend connecting north and east.
J is a 90-degree bend connecting north and west.
7 is a 90-degree bend connecting south and west.
F is a 90-degree bend connecting south and east.
. is ground; there is no pipe in this tile.
S is the starting position of the animal; there is a pipe on this tile, but your sketch doesn't show what shape the pipe has.
"""