from copy import deepcopy
import common
map_file = common.load_day(6, False)
time = common.Timer()
class Vector():
    def __init__(self, y, x):
        self.x = x
        self.y = y
    
    def __add__(self, vector):
        return Vector(self.y + vector.y, self.x + vector.x)
    
    def __str__(self):
        return f"({self.x}, {self.y})"
    
    def __repr__(self):
        return str(self)
    
    def __eq__(self, other):
        return self.y == other.y and self.x == other.x

facings = (Vector(-1, 0), Vector(0, 1), Vector(1, 0), Vector(0, -1))
facing_blocks = ("↑", "→", "↓", "←", "+")

for y, line in enumerate(map_file):
    map_file[y] = list(map_file[y].rstrip())
    if "^" in line:
        x = line.index("^")
        file_position = Vector(y, x)
        file_facing = 0
    for x, item in enumerate(map_file[y]):
        map_file[y][x] = [map_file[y][x]]

def stringify_map(map_data):
    map_data = deepcopy(map_data)
    output = []
    for line in map_data:
        for i in range(len(line)):
            if isinstance(line[i], list):
                line[i] = "O" if "O" in line[i] else \
                    ("+" if len(line[i]) > 1 else \
                    (facing_blocks[line[i][0]] if isinstance(line[i][0], int) else line[i][0]))
        output += [''.join(line).rstrip()]
    return output
    
def print_map(map_data):
    for line in stringify_map(map_data):
        print(line)
    print()

# part 1
guard_position = deepcopy(file_position)
guard_facing = deepcopy(file_facing)
map = deepcopy(map_file)
distance = 0
visited_positions = []
while True:
    new_position = guard_position + facings[guard_facing]
    if (not (0 <= new_position.y < len(map))) or (not (0 <= new_position.x < len(map[0]))):
        break
    while map[new_position.y][new_position.x] == ["#"]:
        guard_facing = guard_facing+1 if guard_facing < 3 else 0
        new_position = guard_position + facings[guard_facing]
        if (not (0 <= new_position.y < len(map)-1)) or (not (0 <= new_position.x < len(map[0])-1)):
            break
    guard_position = new_position
    if not guard_position in visited_positions:
        visited_positions += [Vector(guard_position.y, guard_position.x)]
    if map[guard_position.y][guard_position.x] == ["."]:
        map[guard_position.y][guard_position.x] = [guard_facing]
    else:
        map[guard_position.y][guard_position.x] += [guard_facing]
for line in stringify_map(map):
    for arrow in facing_blocks:
        distance += ''.join(line).count(arrow)
common.print_result(distance)
time.stop()
time.restart()
# part 2
loops = 0
for position in visited_positions:
    imaginary_map = deepcopy(map_file)
    guard_position = deepcopy(file_position)
    guard_facing = deepcopy(file_facing)
    imaginary_map[position.y][position.x] = ["#"]
    found_loop = False
    while True:
        new_position = guard_position + facings[guard_facing]
        if (not (0 <= new_position.y < len(imaginary_map))) or (not (0 <= new_position.x < len(imaginary_map[0]))):
            break
        while imaginary_map[new_position.y][new_position.x] == ["#"]:
            guard_facing = guard_facing+1 if guard_facing < 3 else 0
            new_position = guard_position + facings[guard_facing]
            if (not (0 <= new_position.y < len(imaginary_map)-1)) or (not (0 <= new_position.x < len(imaginary_map[0])-1)):
                break
        guard_position = new_position
        if guard_facing in imaginary_map[guard_position.y][guard_position.x]:
            found_loop = True
            break
        if imaginary_map[guard_position.y][guard_position.x] == ["."]:
            imaginary_map[guard_position.y][guard_position.x] = [guard_facing]
        else:
            imaginary_map[guard_position.y][guard_position.x] += [guard_facing]
    if found_loop:
        loops += 1
common.print_result(loops)
time.stop()