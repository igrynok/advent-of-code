input_file = "input"

data = open(input_file).read()

answer = []
for lines in data.strip().split("\n"):

    num = ''

    for ch in lines:
        if ch.isdigit():
            num += ch
            break

    for ch in lines[::-1]:
        if ch.isdigit():
            num += ch
            break

    answer.append(int(num))

print(sum(answer))
