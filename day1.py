import common
location_input = common.load_day(1, False)

time = common.Timer()
location_lists = [[], []]
for line in location_input:
    line = line.split()
    location_lists[0].append(int(line[0]))
    location_lists[1].append(int(line[1]))

location_lists[0].sort()
location_lists[1].sort()

# part 1
distance = 0
for i in range(len(location_lists[0])):
    distance += abs(location_lists[0][i] - location_lists[1][i])

common.print_result(distance)
time.stop()
time.restart()
# part 2
similarity = 0
for location in location_lists[0]:
    similarity += location * location_lists[1].count(location)

common.print_result(similarity)
time.stop()