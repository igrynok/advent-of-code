matches = [len(set(line[:40].split()) & set(line[42:].split())) for line in open('input')]

cards = [1] * len(matches)
for i, n in enumerate(matches):
    for j in range(n):
        cards[i + j + 1] += cards[i]

print(sum(cards))