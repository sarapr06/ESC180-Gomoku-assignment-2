##modified detect rows and detect row

"""Gomoku starter code
You should complete every incomplete function,
and add more functions and variables as needed.

Note that incomplete functions have 'pass' as the first statement:
pass is a Python keyword; it is a statement that does nothing.
This is a placeholder that you should remove once you modify the function.

Author(s): Michael Guerzhoy with tests contributed by Siavash Kazemian.  Last modified: Nov. 1, 2023
"""
def print_board(board): #guerzhoy's'

    s = "*"
    for i in range(len(board[0])-1):
        s += str(i%10) + "|"
    s += str((len(board[0])-1)%10)
    s += "*\n"

    for i in range(len(board)):
        s += str(i%10)
        for j in range(len(board[0])-1):
            s += str(board[i][j]) + "|"
        s += str(board[i][len(board[0])-1])

        s += "*\n"
    s += (len(board[0])*2 + 1)*"*"

    print(s)

def make_empty_board(sz): #guerzhoy's'
    board = []
    for i in range(sz):
        board.append([" "]*sz)
    return board

def is_empty(board): #done
    '''This function returns True iff there are no stones on the board board'''
    count = 0
    for rows in range(len(board)):
        for cols in range(len(board[0])):
            if board[rows][cols]==" ":
                count+=1
    return count == len(board)*len(board[0]) #number of places on any size board

# def length_seq(board, y_end, x_end, d_y, d_x):
#     for i in range():
#         coords = []
#         coords.append(y_end - d_y*i)
#         coords.append(x_end-d_x*i)
#         L.append(coords)
#     return len(L)

def is_bounded(board, y_end, x_end, length, d_y, d_x):
    y_start = y_end - (length - 1) * d_y
    x_start = x_end - (length - 1) * d_x

    # Check if start and end points are within the board
    if not (0 <= y_start < len(board) and 0 <= x_start < len(board)):
        return "CLOSED"
    if not (0 <= y_end < len(board) and 0 <= x_end < len(board[0])):
        return "CLOSED"

    # Check spaces adjacent to the sequence
    start_adj_y, start_adj_x = y_start - d_y, x_start - d_x
    end_adj_y, end_adj_x = y_end + d_y, x_end + d_x

    start_open = (0 <= start_adj_y < len(board) and 0 <= start_adj_x < len(board[0]) and board[start_adj_y][start_adj_x] == " ")
    end_open = (0 <= end_adj_y < len(board) and 0 <= end_adj_x < len(board[0]) and board[end_adj_y][end_adj_x] == " ")

    if start_open and end_open:
        return "OPEN"
    elif start_open or end_open:
        return "SEMIOPEN"
    else:
        return "CLOSED"

def is_col(col, y_end, board, x_end, d_y, d_x, length): #done
    L=[]
    for i in range(length):
        coords = []
        if y_end - d_y*i>=len(board) or y_end - d_y*i<0 or x_end - d_x*i>=len(board) or x_end - d_x*i<0:
            return False
        coords.append(y_end - d_y*i)
        coords.append(x_end-d_x*i)
        L.append(coords)
    for e in range(len(L)):
        if board[L[e][0]][L[e][1]] != col:
            return False
    return True

def detect_row(board, col, y_start, x_start, length, d_y, d_x): #done
    open_seq_count = 0
    semi_open_seq_count = 0

    y, x = y_start, x_start
    while 0 <= y < len(board) and 0 <= x < len(board[0]):
        # Check for a sequence of the required length and correct color
        is_sequence = all(
            0 <= y + i * d_y < len(board) and
            0 <= x + i * d_x < len(board[0]) and
            board[y + i * d_y][x + i * d_x] == col
            for i in range(length)
        )

        # If we found a valid sequence, check its boundedness
        if is_sequence:
            y_end, x_end = y + (length - 1) * d_y, x + (length - 1) * d_x
            bound_status = is_bounded(board, y_end, x_end, length, d_y, d_x)

            if bound_status == "OPEN":
                open_seq_count += 1
            elif bound_status == "SEMIOPEN":
                semi_open_seq_count += 1

            # Move y, x to the end of this sequence to avoid overlap
            y, x = y_end + d_y, x_end + d_x
        else:
            y += d_y
            x += d_x

    return open_seq_count, semi_open_seq_count

    return open_seq_count, semi_open_seq_count

def detect_rows(board, col, length):
    open_seq_count, semi_open_seq_count = 0, 0

    for y in range(len(board)):
        open_seq, semi_open_seq = detect_row(board, col, y, 0, length, 0, 1)  # Horizontal
        open_seq_count += open_seq
        semi_open_seq_count += semi_open_seq

    for x in range(len(board[0])):
        open_seq, semi_open_seq = detect_row(board, col, 0, x, length, 1, 0)  # Vertical
        open_seq_count += open_seq
        semi_open_seq_count += semi_open_seq

    for y in range(len(board)):
        open_seq, semi_open_seq = detect_row(board, col, y, 0, length, 1, 1)  # Diagonal /
        open_seq_count += open_seq
        semi_open_seq_count += semi_open_seq

    for x in range(len(board[0])):
        open_seq, semi_open_seq = detect_row(board, col, 0, x, length, 1, 1)  # Diagonal /
        open_seq_count += open_seq
        semi_open_seq_count += semi_open_seq

    for y in range(len(board)):
        open_seq, semi_open_seq = detect_row(board, col, y, len(board[0]) - 1, length, 1, -1)  # Diagonal \
        open_seq_count += open_seq
        semi_open_seq_count += semi_open_seq

    for x in range(len(board[0])):
        open_seq, semi_open_seq = detect_row(board, col, 0, x, length, 1, -1)  # Diagonal \
        open_seq_count += open_seq
        semi_open_seq_count += semi_open_seq

    return open_seq_count, semi_open_seq_count
def search_max(board): #done?
    '''uses the function score() (provided) to find the optimal move for black. finds the location (y,x), such that (y,x) is empty and putting a black stone on (y,x) maximizes the score of the board as calculated by score().
    returns a tuple (y, x) such that putting a black stone in coordinates (y, x) maximizes the potential score (if there are several such tuples, you can
return any one of them).
    After the function returns, the contents of board must remain the same.'''

    empty_places = []
    max_score=0
    move_y=0
    move_x=0
    for y in range(len(board)):
        for x in range(len(board[0])):
            L=[]
            if board[y][x]==" ":
                L.append(y)
                L.append(x)
                empty_places.append(L)
    for e in range(len(empty_places)): #tries all the empty spaces
        board[empty_places[e][0]][empty_places[e][1]] = "b"
        if score(board)>max_score:
            max_score = score(board)
            move_y=empty_places[e][0]
            move_x=empty_places[e][1]
        board[empty_places[e][0]][empty_places[e][1]] = " "

    return move_y, move_x

def score(board): #guerzhoy's'
    MAX_SCORE = 100000

    open_b = {}
    semi_open_b = {}
    open_w = {}
    semi_open_w = {}

    for i in range(2, 6):
        open_b[i], semi_open_b[i] = detect_rows(board, "b", i)
        open_w[i], semi_open_w[i] = detect_rows(board, "w", i)


    if open_b[5] >= 1 or semi_open_b[5] >= 1:
        return MAX_SCORE

    elif open_w[5] >= 1 or semi_open_w[5] >= 1:
        return -MAX_SCORE

    return (-10000 * (open_w[4] + semi_open_w[4])+
            500  * open_b[4]                     +
            50   * semi_open_b[4]                +
            -100  * open_w[3]                    +
            -30   * semi_open_w[3]               +
            50   * open_b[3]                     +
            10   * semi_open_b[3]                +
            open_b[2] + semi_open_b[2] - open_w[2] - semi_open_w[2])
def empty_slots(board):
    empty_slots = []
    for rows in range(len(board)):
        for cols in range(len(board[0])):
            slot = []
            if board[rows][cols]==" ":
                slot.append(rows)
                slot.append(cols)
                empty_slots.append(slot)
    return empty_slots
def is_win(board):
    '''determines the current status of the game, and returns one of["White won", "Black won", "Draw", "Continue playing"], depending on the current status
on the board. The only situation where "Draw" is returned is when board is full'''

    open_w, semi_open_w = detect_rows(board, "w", 5)
    open_b, semi_open_b = detect_rows(board, "b", 5)
    if open_w ==1 or semi_open_w ==1:
        return "White won"
    elif open_b ==1 or semi_open_b ==1:
        return "Black won"
    elif len(empty_slots(board))>0:
        return "Continue playing"
    else:
        return "Draw"

##GUERZHOY FUNCTIONS START HERE
def analysis(board):
    for c, full_name in [["b", "Black"], ["w", "White"]]:
        print("%s stones" % (full_name))
        for i in range(2, 6):
            open, semi_open = detect_rows(board, c, i);
            print("Open rows of length %d: %d" % (i, open))
            print("Semi-open rows of length %d: %d" % (i, semi_open))

def play_gomoku(board_size):
    board = make_empty_board(board_size)
    board_height = len(board)
    board_width = len(board[0])

    while True:
        print_board(board)
        if is_empty(board):
            move_y = board_height // 2
            move_x = board_width // 2
        else:
            move_y, move_x = search_max(board)

        print("Computer move: (%d, %d)" % (move_y, move_x))
        board[move_y][move_x] = "b"
        print_board(board)
        #analysis(board)

        game_res = is_win(board)
        if game_res in ["White won", "Black won", "Draw"]:
            return game_res

        print("Your move:")
        move_y = int(input("y coord: "))
        move_x = int(input("x coord: "))
        board[move_y][move_x] = "w"
        print_board(board)
        #analysis(board)

        game_res = is_win(board)
        if game_res in ["White won", "Black won", "Draw"]:
            return game_res

def put_seq_on_board(board, y, x, d_y, d_x, length, col):
    for i in range(length):
        board[y][x] = col
        y += d_y
        x += d_x

if __name__ == '__main__':
    board = make_empty_board(8)
    print_board(board)
    print(play_gomoku(8))