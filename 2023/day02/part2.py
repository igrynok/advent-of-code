import re
from collections import defaultdict

input_file = "input"

data = open(input_file).read()

answer = []
template = 'Game (.*): (.*)'
colors = {'red':12, 'green':13, 'blue':14}

for line in data.strip().split("\n"):
    m = re.match(template, line)
    game_num = int(m.group(1))
    cube_sets = m.group(2).split(';')
    game_possible = True
    colors_min = defaultdict(int)
    for cube_set in cube_sets:
        cubes = cube_set.split(',')
        for cube in cubes:
            match = re.match(r'(\d+)\s+(\w+)', cube.strip())
            number = int(match.group(1))
            color = match.group(2).lower()
            if colors_min[color] < number:
                colors_min[color] = number
    set_power = 1
    for key in colors_min.keys():
        set_power *= colors_min[key]
    answer.append(set_power)

print(sum(answer))