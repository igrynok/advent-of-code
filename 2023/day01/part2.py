input_file = "input"

data = open(input_file).read()

answer = []
digits = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
map = {'one': '1e', 'two': '2o', 'three': '3e', 'four': '4', 'five': '5e', 'six': '6', 'seven': '7n', 'eight': '8t',
       'nine': '9e'}

for codes in data.strip().split("\n"):

    i = 0
    while True:
        if not codes[i].isdigit():
            for digit in digits:
                if codes[i:].startswith(digit):
                    codes = codes.replace(digit, map[digit])
                    break
        i += 1
        if i >= len(codes):
            break

    num = ''
    for ch in codes:
        if ch.isdigit():
            num += ch
            break

    for ch in codes[::-1]:
        if ch.isdigit():
            num += ch
            break

    answer.append(int(num))

print(sum(answer))
