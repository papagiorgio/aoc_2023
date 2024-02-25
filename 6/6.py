times = [34908986]
distances = [204171312101780]

# times = [71530]
# distances = [940200]
prod = 1

for i in range(1):
    count = 0
    unique = set()
    for j in range(times[i]):
        # print(f"{times[i]=}, {distances[i]=}, {j=}, {j * (times[i]-j)=}")
        distance = j * (times[i]-j)
        if distance > distances[i]:
            count += 1

    print(f"{count=}")
    prod *= count

print(prod)
    