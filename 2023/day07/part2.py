import functools
from collections import Counter

input_file = "input"

data = open(input_file).readlines()
hands = [tuple(elem.strip().split()) for elem in data]

points = {(5,): 7, (4, 1): 6, (3, 2): 5, (3, 1, 1): 4, (2, 2, 1): 3, (2, 1, 1, 1): 2, (1, 1, 1, 1, 1): 1}
values = {"A": 14, "K": 13, "Q": 12, "T": 11, "9": 10, "8": 9, "7": 8, "6": 7, "5": 6, "4": 5, "3": 4, "2": 3, "J": 2}


def compare(x, y):
    hand1, hand2 = x[0], y[0]
    points1_max, points2_max = 0, 0
    for ch in values.keys():
        hand1_replaced, hand2_replaced = hand1.replace('J', ch), hand2.replace('J', ch)
        counter1, counter2 = Counter(hand1_replaced), Counter(hand2_replaced)
        points1 = points[tuple(sorted(counter1.values(), reverse=True))]
        points2 = points[tuple(sorted(counter2.values(), reverse=True))]
        points1_max, points2_max = max(points1_max, points1), max(points2_max, points2)

    if points1_max > points2_max:
        return 1
    elif points1_max < points2_max:
        return -1
    else:
        for h1, h2 in zip(hand1, hand2):
            if values[h1] > values[h2]:
                return 1
            elif values[h1] < values[h2]:
                return -1
    return 0


sorted_hand = sorted(hands, key=functools.cmp_to_key(compare))
print(sorted_hand)
print(sum([int(sorted_hand[i][1])*(i + 1) for i in range(len(sorted_hand))]))