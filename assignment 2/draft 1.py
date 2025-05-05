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

def is_bounded(board, y_end, x_end, length, d_y, d_x): #done
    #rmbr that d_y and d_x are couples that show in which way the sequence is advancing (e.g. up/down, diagonally left/right)
    '''analyses the sequence of length length that ends at location (y_end, x_end). returns "OPEN" if the sequence is open, "SEMIOPEN" if the sequence if semi-open, and "CLOSED"
if the sequence is closed.
Assume that the sequence is complete (i.e., you are not just given a subsequence) and valid, and contains stones of only one colour.'''
    L=[]
    for i in range(length):
        coords = []
        coords.append(y_end - d_y*i)
        coords.append(x_end-d_x*i)
        L.append(coords)
    print(L)
    print_board(board)
    if (x_end ==7 and (d_x==-1 or d_x==1)) or (y_end == 7 and d_y == 1) or (x_end == 0 and (d_x == -1 or d_x==1)) or (y_end == 0 and d_y == 1):
        if L[len(L)-1][0]-d_y<0 or L[len(L)-1][1]-d_x<0:
            return "CLOSED"
        else:
            return "SEMIOPEN"

        return "SEMIOPEN"
    elif board[y_end+d_y][x_end+d_x] == " " and board[L[len(L)-1][0]-d_y][L[len(L)-1][1]-d_x] == " ":
        if y_end+d_y<0 or x_end+d_x<0 or L[len(L)-1][0]-d_y<0 or L[len(L)-1][1]-d_x<0:
            return "SEMIOPEN"
        return "OPEN"
    elif board[y_end+d_y][x_end+d_x] == " " or board[L[len(L)-1][0]-d_y][L[len(L)-1][1]-d_x] == " ":
            return "SEMIOPEN"
    else:
        return "CLOSED"


def detect_row(board, col, y_start, x_start, length, d_y, d_x):
    '''analyses the row (let’s call it R) of squares that starts at the location (y_start,x_start) and in the direction (d_y,d_x).Returns a tuple whose first element is the number of open sequences of colour col of length length in the row R, and whose second element is the number of semi-open sequences of colour col of length length in the row R.
    This use of the word row is different from “a row in a table”. Here, row means a sequence of squares, adjacent either horizontally,or vertically, or diagonally.
    Assume that (y_start,x_start) is located on the EDGE of the board. Only complete sequences count. Assume length is an integer greater or equal to 2.
'''
    open_seq_count = 0
    semi_open_seq_count = 0

    if is_bounded(board, y_start, x_start, length, -d_y, -d_x) == "OPEN":
        open_seq_count+=1
    elif is_bounded(board, y_start, x_start, length, -d_y, -d_x) == "SEMIOPEN":
        semi_open_seq_count+=1

    return open_seq_count, semi_open_seq_count

def detect_rows(board, col, length):
    '''analyses the board board. returns a tuple, whose first element is the number of open sequences of colour col of length length on the entire board, and whose second element is the number of semi-open sequences of colour col of length length on the entire board.
    Only complete sequences count. For example, Fig. 1 is considered to contain one open row of length 3, and no other rows. Assume length is an integer greater or equal to 2.'''
    open_seq_count, semi_open_seq_count = 0, 0
    for i in range(len(board)): #change range value
        for j in range(len(board[0])):
            if board[i][j]==col:
                for d_y in [0,1]:
                    if d_y==1:
                        LenX=[0,-1,1]
                    else:
                        LenX=[0,1]
                    for d_x in LenX:
                        L=detect_row(board, col, i, j, length, d_y, d_x)
                        print(L)
                        if L[0]!=0:
                            open_seq_count+=1
                            print("Open seq: " + str(open_seq_count))
                        elif L[1]!=0:
                            semi_open_seq_count +=1
                            print("semiopen seq: " + str(semi_open_seq_count))
    return open_seq_count, semi_open_seq_count

if __name__ == '__main__':
    board = make_empty_board(8)
    print_board(board)
    board[4][1]="Y"
    board[5][1]="Y"
    board[6][1]="Y"
    print_board(board)
    print(detect_row(board, "Y", 0, 0, 3, 0, 1))
    print(detect_rows(board, "Y", 2))