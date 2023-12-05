input_file = "input"

data = open(input_file).read()

answer = 0
for card in data.strip().split("\n"):

    inputs = card.split(':')[1].strip().split('|')
    winner = inputs[0].strip().split()
    winner_set = set(map(int, winner))
    mine = inputs[1].strip().split()
    mine_set = set(map(int, mine))

    inter = winner_set.intersection(mine_set)
    points = 2 ** (len(inter) - 1) if inter else 0
    answer += points

print(answer)

