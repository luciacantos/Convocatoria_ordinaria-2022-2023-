# ejercicio 1
def solve_nonogram(clues):

    col_clues, row_clues = clues

    matrix = [['_' for _ in range(5)] for _ in range(5)]

    for col, clues in enumerate(col_clues):
        current_clue_index = 0
        current_clue = clues[current_clue_index]
        current_clue_count = 0
        for row in range(5):
            if matrix[row][col] == '_':
                matrix[row][col] = '0'
                current_clue_count += 1
                if current_clue_count == current_clue:
                    current_clue_index += 1
                    if current_clue_index < len(clues):
                        current_clue = clues[current_clue_index]
                        current_clue_count = 0
                    else:
                        break

    for row, clues in enumerate(row_clues):
        current_clue_index = 0
        current_clue = clues[current_clue_index]
        current_clue_count = 0
        for col in range(5):
            if matrix[row][col] == '_':
                matrix[row][col] = '0'
                current_clue_count += 1
                if current_clue_count == current_clue:
                    current_clue_index += 1
                    if current_clue_index < len(clues):
                        current_clue = clues[current_clue_index]
                        current_clue_count = 0
                    else:
                        break

    for row in range(5):
        for col in range(5):
            if matrix[row][col] == '_':
                matrix[row][col] = '1'
    return matrix

clues = ([2, 1], [1, 1, 1], [2, 1], [1, 1, 1], [2, 1]), ([1, 1], [2, 2], [3, 1], [2, 2], [1, 1])

solved_nonogram = solve_nonogram(clues)

for row in solved_nonogram:
    print(row)
