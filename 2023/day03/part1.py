input_file = "input"

data = open(input_file).read()

matrix = [[ch for ch in line] for line in data.strip().split("\n")]

rows = len(matrix)
columns = len(matrix[0])


def get_neighbours(cell):
    neighbours = []
    deltas = [(0, 1), (1, 0), (-1, 0), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
    for delta in deltas:
        if 0 <= cell[0] + delta[0] < rows and 0 <= cell[1] + delta[1] < columns:
            neighbours.append((cell[0] + delta[0], cell[1] + delta[1]))
    return neighbours


visited = set()
answer = []

for row in range(rows):
    for column in range(columns):
        cell = (row, column)
        if matrix[row][column] == '.' or not matrix[row][column].isdigit() or cell in visited:
            continue
        adjacent = False
        for neighbour in get_neighbours(cell):
            if neighbour in visited:
                continue
            if matrix[neighbour[0]][neighbour[1]] != '.' and not matrix[neighbour[0]][neighbour[1]].isdigit():
                adjacent = True
                break

        if adjacent:
            i = cell[1]
            number = ''
            while 0 <= i < columns and matrix[row][i].isdigit():
                visited.add((row, i))
                number += matrix[row][i]
                i += 1
            i = cell[1] - 1
            while 0 <= i < columns and matrix[row][i].isdigit():
                visited.add((row, i))
                number = matrix[row][i] + number
                i -= 1
            answer.append(int(number))

print(sum(answer))
