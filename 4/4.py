sum = 0
copies = {i+1: 1 for i in range(200)}

with open ("c:/Users/tk/ref/python_projects/advent_of_code/4/input2.txt") as my_file:

    for line in my_file:
        # print(f"{copies=}")
        # print(f"{line=}")

        card_num = int(line.split("|")[0].strip().split()[1].split(":")[0])

        # for _ in range(copies[card_num]):
        # print(f"{card_num=}")
        card_sum = 0

        card = line.split("|")[0].strip().split()[1:]
        nums = line.split("|")[1].strip().split()

        for num in nums:
            if num in card:
                # print(f"{num=} {card[0][:2]=}")
                card_sum += 1

        # print(f"{card_sum=}")

        for i in range(1, card_sum+1):
            # print(f"{card_num+i=}")
            copies[card_num+i] = copies[card_num+i] + copies[card_num]
            # print(f"{copies[card_num+i]=}")

        # sum += card_sum * copies[card_num]
        sum += copies[card_num]
        print(f"{sum=}")

print(f"{card=} {nums=} {sum=}")