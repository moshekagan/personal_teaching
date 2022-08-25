NOT_VISITED = -1
LAND = 1
SEA = 0


def find_path(m):
    r = [NOT_VISITED] * len(m[0])
    visited = [r[:] for i in range(len(m))]
    res = find_path_helper(m, visited, 0, 0)

    print_mat(visited)

    return res


def print_mat(m):
    print()
    for i in range(len(m)):
        for j in range(len(m[0])):
            c = " "
            if m[i][j] == LAND:
                c = "#"
            if m[i][j] == SEA:
                c = "~"
            print(c, end=" | ")
        print()


def is_visited(v, row, col):
    return v[row][col] != NOT_VISITED


def find_path_helper(m, visited, row, col):
    if row == len(m) - 1 and col == len(m[-1]) - 1 and m[row][col] == LAND:
        visited[row][col] = LAND
        return True

    if m[row][col] == LAND:
        visited[row][col] = LAND

        res1 = find_path_helper(m, visited, row - 1, col) if row > 0 and                not is_visited(visited, row-1, col) else False  # Left
        res2 = find_path_helper(m, visited, row + 1, col) if row < len(m) - 1 and       not is_visited(visited, row+1, col) else False  # Down
        res3 = find_path_helper(m, visited, row, col - 1) if col > 0 and                not is_visited(visited, row, col-1) else False  # Up
        res4 = find_path_helper(m, visited, row, col + 1) if col < len(m[row]) - 1 and  not is_visited(visited, row, col+1) else False  # Right

        return res1 or res2 or res3 or res4

    visited[row][col] = SEA
    return False


if __name__ == '__main__':
    m1 = [[1]]

    m2 = [[1, 1, 1],
          [0, 0, 1],
          [0, 0, 1],
          [0, 0, 1]]

    m3 = [[0]]

    m4 = [[1, 1, 1, 1],
          [0, 0, 1, 0],
          [0, 0, 1, 0],
          [0, 0, 1, 1]]

    m5 = [[1, 1, 1, 1],
          [0, 0, 0, 1],
          [0, 0, 1, 1],
          [0, 0, 1, 0],
          [0, 0, 1, 1]]

    m6 = [[1, 1, 1, 1, 0],
          [0, 0, 0, 1, 0],
          [0, 0, 1, 1, 0],
          [0, 0, 1, 0, 0],
          [0, 0, 1, 1, 1]]

    m7 = [[1, 1, 1, 1, 0],
          [0, 0, 0, 1, 0],
          [0, 0, 0, 1, 0],
          [0, 0, 1, 0, 0],
          [0, 0, 1, 1, 1]]

    m8 = [[1, 1, 1, 1, 1],
          [1, 1, 1, 1, 1],
          [1, 1, 1, 1, 1],
          [1, 1, 1, 1, 1],
          [1, 1, 1, 1, 1]]

    m9 = [[1, 1, 1],
          [1, 0, 1],
          [1, 0, 1],
          [1, 1, 1]]

    m10 = [[1, 1, 1],
           [1, 0, 0],
           [1, 0, 0],
           [1, 1, 1]]

    print(find_path(m1))  # True
    print(find_path(m2))  # True
    print(find_path(m3))  # False
    print(find_path(m4))  # True
    print(find_path(m5))  # True
    print(find_path(m6))  # True
    print(find_path(m7))  # False
    print(find_path(m8))  # True
    print(find_path(m9))  # True
    print(find_path(m10))  # True
