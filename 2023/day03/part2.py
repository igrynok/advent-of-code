input_file = "input"

data = open(input_file).read()

matrix = [[ch for ch in line] for line in data.strip().split("\n")]

rows = len(matrix)
columns = len(matrix[0])


def get_neighbours(cell):
    numbers = []
    deltas = [(0, 1), (1, 0), (-1, 0), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
    visited = set()
    for delta in deltas:
        if 0 <= cell[0] + delta[0] < rows and 0 <= cell[1] + delta[1] < columns:
            row, column = cell[0] + delta[0], cell[1] + delta[1]
            if (row, column) not in visited and matrix[row][column].isdigit():
                i = column
                number = ''
                while 0 <= i < columns and matrix[row][i].isdigit():
                    visited.add((row, i))
                    number += matrix[row][i]
                    i += 1
                i = column - 1
                while 0 <= i < columns and matrix[row][i].isdigit():
                    visited.add((row, i))
                    number = matrix[row][i] + number
                    i -= 1
                numbers.append(int(number))
    return numbers


answer = []

for row in range(rows):
    for column in range(columns):
        cell = (row, column)
        if matrix[row][column] == '*':
            nums = get_neighbours(cell)
            if len(nums) == 2:
                answer.append(nums[0] * nums[1])

print(sum(answer))
