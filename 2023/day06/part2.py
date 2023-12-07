
times = [53916768]
dist = [250133010811025]

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