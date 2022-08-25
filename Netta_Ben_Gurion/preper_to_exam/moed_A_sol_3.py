FIRST_PLAYER = 0
SECOND_PLAYER = 1


def current_row(board):
    for i in range(len(board)):
        if board[i] != 0:
            return i
    return None


def do_move(board, move):
    res = board[:]
    res[current_row(board)] = move
    return res


# def play_helper(board, current_player):
#     res = [0, 0]
#     row = current_row(board)
#
#     if row is None:  # if row is None the board is empty
#         res[current_player] += 1
#         return res
#
#     pos_moves = board[row]
#
#     for move in range(pos_moves):
#         new_board = do_move(board, move)
#         new_current_player = FIRST_PLAYER if current_player == SECOND_PLAYER else SECOND_PLAYER
#
#         new_res = play_helper(new_board, new_current_player)
#         res[0] += new_res[0]
#         res[1] += new_res[1]
#
#     return res
#
# def play(board):
#     current_player = FIRST_PLAYER
#     res = play_helper(board, current_player)
#
#     return res


def play_helper(board, current_player, res):
    row = current_row(board)

    if row is None:  # if row is None the board is empty
        res[current_player] += 1
        return res

    pos_moves = board[row]

    for move in range(pos_moves):
        new_board = do_move(board, move)
        new_current_player = FIRST_PLAYER if current_player == SECOND_PLAYER else SECOND_PLAYER

        play_helper(new_board, new_current_player, res)

    return res


def play(board):
    res = [0, 0]
    current_player = FIRST_PLAYER
    res = play_helper(board, current_player, res)

    return res


def win(board):
    row = current_row(board)

    if row is None:  # if row is None the board is empty - Winning
        return True

    pos_moves = board[row]

    for move in range(pos_moves):
        new_board = do_move(board, move)
        is_next_move_win = not win(new_board)

        if not is_next_move_win:  # this move is loss
            return True

    return False  # im the losser


if __name__ == '__main__':
    print(play([0, 0]))
    print(play([1, 2]))
    print(play([4]))

