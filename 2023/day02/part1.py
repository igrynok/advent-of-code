import re

input_file = "input"

data = open(input_file).read()

answer = []
template = 'Game (.*): (.*)'
colors = {'red': 12, 'green': 13, 'blue': 14}

for game in data.strip().split("\n"):

    line_match = re.match(template, game)
    game_num = int(line_match.group(1))
    cube_sets = line_match.group(2).split(';')
    game_possible = True

    for cube_set in cube_sets:
        cubes = cube_set.split(',')
        for cube in cubes:
            match = re.match(r'(\d+)\s+(\w+)', cube.strip())
            number = int(match.group(1))
            color = match.group(2).lower()
            if number > colors[color]:
                game_possible = False
                break
        if not game_possible:
            break

    if game_possible:
        answer.append(game_num)

print(sum(answer))
