import math

input_file = "input"

data = open(input_file).readlines()

times = list(map(int, data[0].split(':')[1].strip().split()))
dist = list(map(int, data[1].split(':')[1].strip().split()))

games = list(zip(times, dist))
answer = []
for game in games:
    t = game[0]
    d = game[1]
    ways = 0
    for i in range(t + 1):
        speed = i
        remind_t = t - i
        travel_d = speed*remind_t
        if travel_d > d:
            ways += 1
    answer.append(ways)

print(answer)
print(math.prod(answer))


