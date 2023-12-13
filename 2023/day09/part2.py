from functools import reduce

input_file = "input"

data = open(input_file).readlines()

history = []
for line in data:
    arr = list(map(int, line.strip().split()))
    arr_sum = [arr[0]]
    while not all(x == 0 for x in arr):
        arr = [arr[i] - arr[i-1] for i in range(1, len(arr))]
        arr_sum.append(arr[0])
    arr_sum = arr_sum[::-1]
    history.append(reduce(lambda a, b: b-a, arr_sum))

print(sum(history))