input_file = "input"

data = open(input_file).read()

answer = []
for codes in data.strip().split("\n"):

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
