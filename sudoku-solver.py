def find_next_empty(puzzle):
    # finds the next row, column on the puzzle thats not filled yet (represented as '-1')
    # zero-indexing (0-8)
    for r in range(9):
        for c in range(9):
            if puzzle[r][c] == -1:
                return r, c
    return None, None
def is_valid(puzzle, guess, row, col):
    row_vals = puzzle[row]
    if guess in row_vals:
        return False

    col_vals = [puzzle[i][col] for i in range(9)]
    if guess in col_vals:
        return False

    row_start = (row // 3) * 3
    col_start = (col // 3) * 3

    for r in range(row_start, row_start + 3):
        for c in range(col_start, col_start + 3):
            if puzzle[r][c] == guess:
                return False

    return True


def solve_sudoku(puzzle):
    # solving sudoku puzzle using "backtracking"
    # where it is a list of lists, where each inner list is a row in this puzzle
    # mutating the puzzle to be the solution (if such exists)

    # 1.) choosing somewhere on the puzzle to make a guess
    row, col = find_next_empty(puzzle)

    # 2.) if theres nowhere left, then its done, because only valid inputs are allowed
    if row is None:
        return True

    # 3.) if theres a place to put a number, then make a guess between 1 and 9
    for guess in range(1, 10):
        # 4.) check if the guess is valid
        if is_valid(puzzle, guess, row, col):
            puzzle[row][col] = guess
            # 5.) recursively call fucntion
            if solve_sudoku(puzzle):
                return True

        # 6.) if not valid or if guess does not solve the puzzle, then
        # backtrack and try a new member
        puzzle[row][col] = -1

    # 7.) if none of the numbers that we try work, then this puzzle is unsolvable
    return False

if __name__ == '__main__':
    example_board = [
        [-1, -1, 6,   3, -1, 7,   -1, -1, -1],
        [-1, -1, 4,   -1, -1, -1,   -1, -1, 5],
        [1, -1, -1,   -1, -1, 6,   -1, 8, 2],

        [2, -1, 5,   -1, 3, -1,   1, -1, 6],
        [-1, -1, -1,   2, -1, -1,   3, -1, -1],
        [9, -1, -1,   -1, 7, -1,   -1, -1, 4],

        [-1, 5, -1,   -1, -1, -1,   -1, -1, -1],
        [-1, 1, -1,   1, -1, -1,   -1, -1, -1],
        [-1, -1, 8,   1, -1, 9,   -1, 4, -1]
    ]
    print(solve_sudoku(example_board))
    print(example_board)
