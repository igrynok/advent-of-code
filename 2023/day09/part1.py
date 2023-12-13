input_file = "input"

data = open(input_file).readlines()

history = []
for line in data:
    arr = list(map(int, line.strip().split()))
    arr_sum = arr[-1]
    while not all(x == 0 for x in arr):
        arr = [arr[i] - arr[i-1] for i in range(1, len(arr))]
        arr_sum += arr[-1]
    history.append(arr_sum)

print(sum(history))