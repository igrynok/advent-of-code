import os

AOC_SESSION = ''
year = '2023'
day = '1'
folder = '2023/day01'

command = f'curl --cookie "session={AOC_SESSION}" https://adventofcode.com/{year}/day/{day}/input -o "{folder}/input"'

os.system(command)