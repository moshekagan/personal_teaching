def distance(row1, col1, row2, col2):
    rows = row1 - row2 if row1 > row2 else row2 - row1
    cols = col1 - col2 if col1 > col2 else col2 - col1
    return rows + cols


def add_tower(board, d, row, col):
    for i in range(row):
        if distance(i, board[i], row, col) <= d:
            return False

    board[row] = col
    return True


def n_tower_helper(board, d, row):
    if row == len(board):
        return True

    for i in range(len(board)):
        if add_tower(board, d, row, i):
            return n_tower_helper(board, d, row+1)

    return False


def n_tower(n, d):
    for i in range(n):
        board = [0] * n
        board[0] = i
        res = n_tower_helper(board, d, 1)
        if res:
            return board

    return []


if __name__ == '__main__':
    print(distance(5, 5, 4, 2))
    print(distance(3, 0, 2, 4))
    print(distance(5, 5, 0, 0))
    print()

    board = [0, 0, 0, 0, 0, 0]
    print(add_tower(board, 2, 0, 3))
    print(board)
    print()

    board = [0, 3, 5, 0, 0, 0]
    print(add_tower(board, 2, 3, 3))
    print(board)
    print()

    print(add_tower(board, 2, 3, 1))
    print(board)
    print()

    print(n_tower(4, 2))
    print(n_tower(3, 1))
    print(n_tower(6, 2))
    print(n_tower(6, 6))
