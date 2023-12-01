input_file = "input"

data = open(input_file).read()

answer = []
digits = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
map = {'one': '1e', 'two': '2o', 'three': '3e', 'four': '4', 'five': '5e', 'six': '6', 'seven': '7n', 'eight': '8t',
       'nine': '9e'}

for line in data.strip().split("\n"):

    i = 0
    while True:
        if not line[i].isdigit():
            for digit in digits:
                if line[i:].startswith(digit):
                    line = line.replace(digit, map[digit])
                    break
        i += 1
        if i >= len(line):
            break

    num = ''
    for ch in line:
        if ch.isdigit():
            num += ch
            break

    for ch in line[::-1]:
        if ch.isdigit():
            num += ch
            break

    answer.append(int(num))

print(sum(answer))
