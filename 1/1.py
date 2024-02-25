import numpy as np

nums = []
nums_dict = {"ONE": "O1E", "TWO": "T2O", "THREE": "T3E", "FOUR": "F4R", "FIVE": "F5E", "SIX": "S6X", "SEVEN": "S7N", "EIGHT": "E8T", "NINE": "N9E", "ZERO": "Z0O"}

with open("c:/Users/tk/ref/python_projects/advent_of_code/1/input.txt") as my_file:
    for line in my_file:
        # print(line)
        first_pos_dict = {}
        last_pos_dict = {}

        # get the positions of the keys from nums_dict in the line
        for key in nums_dict:
            first_pos_dict[key] = line.upper().find(key) if line.upper().find(key)!=-1 else np.inf
            last_pos_dict[key] = line.upper().rfind(key)

        # print(first_pos_dict)
        # print(last_pos_dict)

        # print(min(first_pos_dict, key=first_pos_dict.get))
        # print(max(last_pos_dict, key=last_pos_dict.get))

        min_key = min(first_pos_dict, key=first_pos_dict.get)
        max_key = max(last_pos_dict, key=last_pos_dict.get)

        line = line.upper().replace(min_key, nums_dict[min_key])
        line = line.upper().replace(max_key, nums_dict[max_key])

        # print(line)
        num = ""
        for i in range(len(line)):
            if line[i].isdigit():
                num += line[i]
                break
        for i in range(len(line)-1, -1, -1):
            if line[i].isdigit():
                num += line[i]
                break

        nums.append(int(num))

print(nums)
print(sum(nums))