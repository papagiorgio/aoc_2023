import math

seed_to_soil = []
soil_to_fertilizer = []
fertilizer_to_water = []
water_to_light = []
light_to_temp = []
temp_to_hum = []
hum_to_loc = []

locs = []

# print(my_file.read().split("\n"))
seeds = []
intervals = []

with open ("c:/Users/tk/ref/python_projects/advent_of_code/5/input.txt") as my_file:
    seedlist = list(map(int, my_file.readline().split()[1:]))

    for i in range(0, len(seedlist), 2):
        # for j in range(seedlist[i+1]):
        #     seeds.append(seedlist[i]+j)
        intervals.append((seedlist[i],seedlist[i]+seedlist[i+1]-1))

    # print(f"{seeds=}")
    print(f"{intervals=}")

    # print(f"{seeds=}")
    line = my_file.readline().strip()

    # read the maps
    while line!="EOF":
        if "seed-to-soil" in line:
            line = my_file.readline().strip()
            while line != "":
                seed_to_soil.append(list(map(int, line.split())))
                line = my_file.readline().strip()
            # print(f"{seed_to_soil=}")
        if "soil-to-fertilizer" in line:
            line = my_file.readline().strip()
            while line != "":
                soil_to_fertilizer.append(list(map(int, line.split())))
                line = my_file.readline().strip()
            # print(f"{soil_to_fertilizer=}")
        if "fertilizer-to-water" in line:
            line = my_file.readline().strip()
            while line != "":
                fertilizer_to_water.append(list(map(int, line.split())))
                line = my_file.readline().strip()
            # print(f"{fertilizer_to_water=}")
        if "water-to-light" in line:
            line = my_file.readline().strip()
            while line != "":
                water_to_light.append(list(map(int, line.split())))
                line = my_file.readline().strip()
            # print(f"{water_to_light=}")
        if "light-to-temperature" in line:
            line = my_file.readline().strip()
            while line != "":
                light_to_temp.append(list(map(int, line.split())))
                line = my_file.readline().strip()
            # print(f"{light_to_temp=}")
        if "temperature-to-humidity" in line:
            line = my_file.readline().strip()
            while line != "":
                temp_to_hum.append(list(map(int, line.split())))
                line = my_file.readline().strip()
            # print(f"{temp_to_hum=}")
        if "humidity-to-location" in line:
            line = my_file.readline().strip()
            while line != "EOF":
                hum_to_loc.append(list(map(int, line.split())))
                line = my_file.readline().strip()
            # print(f"{hum_to_loc=}")
            break
        line = my_file.readline().strip()
        # print(f"{line=}")
    
    # print(f"{seeds=}")

def split_interval(interval, orig, maps):
    min = interval[0]
    max = interval[1]

    # mapped = False

    for (d, map_min, t) in maps:
        map_max = map_min + t-1
        shift = d-map_min
        
        if min > map_max or max < map_min: # interval is fully outside map, nothing to do
            print("interval is fully outside map, nothing to do")
            continue 
        elif (min >= map_min and max <= map_max): # interval is fully inside map, no split, just return the mapped interval
            print("interval is fully inside map, no split, just return the mapped interval")
            return ([(min+shift, max+shift)], [orig])
        elif (min < map_min and max > map_max): # map is fully inside interval, split into three intervals, map the second and return them
            print("map is fully inside interval, split into three intervals, map the second and return them")
            return ([(min, map_min-1), (map_min+shift, map_max+shift), (map_max+1, max)], [(orig[0], orig[0]+map_min-min), (orig[0]+map_min-min, orig[0]+max-map_max), (orig[0]+max-map_max, orig[1])])
        elif (min >= map_min and max > map_max): # map overlaps interval from the left, split into two intervals, map the first and return them
            print("map overlaps interval from the left, split into two intervals, map the first and return them")
            return ([(min+shift, map_max+shift), (map_max+1, max)], [(orig[0], orig[0]+map_max-min), (orig[0]+map_max-min, orig[1])])
        elif (min < map_min and max <= map_max): # map overlaps interval from the right, split into two intervals, map the second and return them???
            print("map overlaps interval from the right, split into two intervals, map the second and return them??")
            return ([(min, map_min-1), (map_min+shift, max+shift)], [(orig[0], orig[0]+map_min-min), (orig[0]+map_min-min, orig[1])])
    return ([interval], [orig])

def split_intervals(intervals, origs, maps):
    new_intervals = []
    new_origs = []

    for interval, orig in zip(intervals, origs):
        tmp = split_interval(interval, orig, maps)
        # print(f"{tmp=}")
        for t in tmp[0]:
            new_intervals.append(t)
        for t in tmp[1]:
            new_origs.append(t)
    return (new_intervals, new_origs)
    
locs = []
orig_locs = []

i = 0

while True:

    if i%100000 == 0:
        print(f"{i=}")

    loc = i
    # print(f"{i=}")

    for map in hum_to_loc:
        if loc >= map[0] and loc < map[0]+map[2]:
            hum = loc - map[0] + map[1]
            break
    else:
        hum = loc
    
    for map in temp_to_hum:
        if hum >= map[0] and hum < map[0]+map[2]:
            temp = hum - map[0] + map[1]
            break
    else:
        temp = hum
    
    for map in light_to_temp:
        if temp >= map[0] and temp < map[0]+map[2]:
            light = temp - map[0] + map[1]
            break
    else:
        light = temp
    
    for map in water_to_light:
        if light >= map[0] and light < map[0]+map[2]:
            water = light - map[0] + map[1]
            break
    else:
        water = light
    
    for map in fertilizer_to_water:
        if water >= map[0] and water < map[0]+map[2]:
            fertilizer = water - map[0] + map[1]
            break
    else:
        fertilizer = water
    
    for map in soil_to_fertilizer:
        if fertilizer >= map[0] and fertilizer < map[0]+map[2]:
            soil = fertilizer - map[0] + map[1]
            break
    else:
        soil = fertilizer
    

    for map in seed_to_soil:
        if soil >= map[0] and soil < map[0]+map[2]:
            seed = soil - map[0] + map[1]
            break
    else:
        seed = soil
    
    # print(f"{seed=}, {soil=}, {fertilizer=}, {water=}, {light=}, {temp=}, {hum=}, {loc=}")


    breaker = False

    for interval in intervals:
        if seed >= interval[0] and seed <= interval[1]:
            print(f"{seed=}, {interval=}, {loc}")
            breaker = True
            break
    if breaker:
        break

    i += 1