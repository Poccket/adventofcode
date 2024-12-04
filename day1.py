location_lists = [[], []]
with open('inputs/day1.txt', 'r') as f:
    for line in f:
        line = line.split()
        location_lists[0].append(int(line[0]))
        location_lists[1].append(int(line[1]))

location_lists[0].sort()
location_lists[1].sort()

# part 1
distance = 0
for i in range(len(location_lists[0])):
    distance += abs(location_lists[0][i] - location_lists[1][i])

print(distance)

# part 2
similarity = 0
for location in location_lists[0]:
    similarity += location * location_lists[1].count(location)

print(similarity)