import functools
from collections import Counter

input_file = "input"

data = open(input_file).readlines()
hands = [tuple(elem.strip().split()) for elem in data]

values = {"A": 14, "K": 13, "Q": 12, "J": 11, "T": 10, "9": 9, "8": 8, "7": 7, "6": 6, "5": 5, "4": 4, "3": 3, "2": 2}


def compare(x, y):
    hand1, hand2 = x[0], y[0]
    counter1, counter2 = Counter(hand1), Counter(hand2)
    points1, points2 = sorted(counter1.values(), reverse=True), sorted(counter2.values(), reverse=True)

    if points1 > points2:
        return 1
    elif points1 < points2:
        return -1
    else:
        for h1, h2 in zip(hand1, hand2):
            if values[h1] > values[h2]:
                return 1
            elif values[h1] < values[h2]:
                return -1
    return 0


sorted_hand = sorted(hands, key=functools.cmp_to_key(compare))
print(sum([int(sorted_hand[i][1])*(i + 1) for i in range(len(sorted_hand))]))
