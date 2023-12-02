import re
from collections import defaultdict

input_file = "input"

data = open(input_file).read()

answer = []
template = 'Game (.*): (.*)'
color_limits = {'red': 12, 'green': 13, 'blue': 14}

for game in data.strip().split("\n"):

    line_match = re.match(template, game)
    game_num = int(line_match.group(1))
    cube_sets = line_match.group(2).split(';')
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