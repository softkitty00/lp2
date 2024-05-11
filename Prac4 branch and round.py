def is_safe(board, row, col, N):
    # Check if there is a queen in the same column or diagonals
    for i in range(row):
        if board[i] == col or \
                board[i] == col - (row - i) or \
                board[i] == col + (row - i):
            return False
    return True

def solve_n_queens(board, row, N, solution):
    if row >= N:
        solution.append(board[:])
        return
    for col in range(N):
        if is_safe(board, row, col, N):
            board[row] = col
            solve_n_queens(board, row + 1, N, solution)

def n_queens_branch_and_bound(N):
    solution = []
    board = [-1] * N
    solve_n_queens(board, 0, N, solution)
    if not solution:
        print("Solution does not exist")
        return False
    for sol in solution:
        for col in sol:
            row_str = ['.'] * N
            row_str[col] = 'Q'
            print(' '.join(row_str))
        print()
    return True

# Example usage:
n_queens_branch_and_bound(4)
