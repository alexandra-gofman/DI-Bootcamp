
def create_board() -> list:
    '''Creating a new board'''

    board = []
    for i in range(3):
        row = []
        for j in range(3):
            row.append('-')
        board.append(row)

    return board

def display_board(board):
    """Displaying a board as it is"""

    print(f'''|_{board[0][0]}_|_{board[1][0]}_|_{board[2][0]}_|
|_{board[0][1]}_|_{board[1][1]}_|_{board[2][1]}_|
|_{board[0][2]}_|_{board[1][2]}_|_{board[2][2]}_|''')

def get_position(position):
    """Comparing positions with coordinates of board"""

    board_dictionary = {
        1: (0, 0), 2: (1, 0), 3: (2, 0),
        4: (0, 1), 5: (1, 1), 6: (2, 1),
        7: (0, 2), 8: (1, 2), 9: (2, 2)
    }

    return board_dictionary[position]


def check_win(board, player):
    '''Checking who is winner'''

    moves_pl = []

    if player == 1:
        sign_of_player = 'X'

    elif player == 2:
        sign_of_player = 'O'

    for i, row in enumerate(board):
        for j, line in enumerate(board[i]):
            if line == sign_of_player:
                moves_pl.append([i, j])

    if len(moves_pl) > 2:
        list_j = []
        list_i = []
        for i, j in moves_pl:
            list_i.append(i)
            list_j.append(j)
        for i in list_i:
            if list_i.count(i) >= 3:
                print(f'Player{player} won!')
                return True
        for j in list_j:
            if list_j.count(j) >= 3:
                print(f'Player{player} won!')
                return True

        if [0, 0] in moves_pl and [1, 1] in moves_pl and [2, 2] in moves_pl:
            print(f'Player {player} won!')
            return True

        if [0, 2] in moves_pl and [1, 1] in moves_pl and [2, 0] in moves_pl:
            print(f'Player {player} won!')
            return True

    return False


def player_input(player, board):
    '''Players make their moves, and these are saved on the board'''

    while True:
        position = int(input(f'Player{player}: Please enter your next position: '))
        pos = get_position(position)

        if board[pos[0]][pos[1]] == '-':

            if player == 1:
                board[pos[0]][pos[1]] = 'X'

                if check_win(board, player) is True:
                    return True

            if player == 2:
                board[pos[0]][pos[1]] = 'O'

                if check_win(board, player) is True:
                    return True
            return

        else:
            print('This position is already used. Try again.')
            continue

def check_for_draw(board):

    for row in board:
        for line in row:
            if line == '-':
                return False
    return True

def play():
    playing_board = create_board()
    i = 0

    while True:

        if i % 2 == 0:
            if player_input(1, playing_board) is True:
                display_board(playing_board)
                return

        if i % 2 == 1:
            if player_input(2, playing_board) is True:
                display_board(playing_board)
                return

        display_board(playing_board)
        if check_for_draw(playing_board):
            print('it is a draw')
            return

        i += 1

play()