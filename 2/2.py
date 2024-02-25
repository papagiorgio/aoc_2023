RED_MAX = 12 
GREEN_MAX = 13
BLUE_MAX = 14


with open("c:/Users/tk/ref/python_projects/advent_of_code/2/input.txt") as my_file:
    sum = 0

    for game in my_file:
        min_red = 0
        min_green = 0
        min_blue = 0

        power = 0

        game_name, rounds = game.split(":") 
        game_num = int(game_name.split()[-1])
        rounds = rounds.strip().split(";")

        for round in rounds:
            for draw in round.split(","):
                # print(f"{draw.split()= }")
                if "red" in draw and int(draw.split()[0]) > min_red:
                    min_red = int(draw.split()[0])
                elif "green" in draw and int(draw.split()[0]) > min_green:
                    min_green = int(draw.split()[0])
                elif "blue" in draw and int(draw.split()[0]) > min_blue:
                    min_blue = int(draw.split()[0])
        power = min_red * min_green * min_blue
        print(f"{game_num=} {power=}")
        sum += power
    print(f"{sum}")