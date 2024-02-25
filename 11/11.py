import numpy as np
import pandas as pd

with open ("./11/input.txt") as my_file:
    lines = my_file.readlines()
    
    galaxies = {}

    empty_rows = [True]*len(lines)
    empty_cols = [True]*len(lines[0].strip())
    
    count = 1

    # build the universe
    for i in range(len(lines)):
        for j in range(len(lines[0].strip())):
            if lines[i][j] == '#':
                galaxies[count] = (j, i)
                count += 1
                empty_rows[i] = False
                empty_cols[j] = False

    # expand the universe
    for galaxy, pos in galaxies.items():
        galaxies[galaxy] = (galaxies[galaxy][0]+(999999*sum(empty_cols[:pos[0]])), 
                            galaxies[galaxy][1]+(999999*sum(empty_rows[:pos[1]])))

    # print(f"{galaxies=}")

    # measure distances
    sum = 0

    for i in range(len(galaxies)):
        for j in range(i+1, len(galaxies)):
            sum += abs(galaxies[i+1][0] - galaxies[j+1][0]) + abs(galaxies[i+1][1] - galaxies[j+1][1])

    print(f"{sum=}")

