# ESC180-Gomoku-assignment-2
Creating a gomuku game for a user against a computer. Credits go to ESC180, instructor Michael Guerzhoy, and functions not described here are pre-written by Michael Guerzhoy

# Assignment Description: 
In this assignment you will implement a simple (and imperfect) AI engine for the game Gomoku, played on a 8 × 8 board. In Gomoku, there are two players. One player plays with black stones and the other player plays with white stones. A player moves by placing a stone on an empty square on the board. The player who plays with black stones always moves first. After the first move, the players alternate. A player wins if she has placed five of her stones in a sequence, either horizontally, or vertically, or diagonally. Please read http://en.wikipedia.org/wiki/Gomoku for more information about Gomoku. We will be playing the standard variant.

The computer (which plays with the black stones) always moves first. After the first move, the user’s and the computer’s moves alternate. The computer determines its move by finding the move that maximises the return value of the score function (which is provided). Functions in gomoku.py accepts board as one of its arguments. This is the representation of the Gomoku board. The square (y,x) on the board is stored in board[y][x]. The value of the square is:

 " ", if the square is empty,

 "b", if the square has a black stone on it, and

 "w", if the square has a white stone on it.

An important part of the Gomoku AI engine is finding contiguous sequences of stones of the same colour on the Gomoku board. There are four possible directions for a sequence: left-to-right, top-to-bottom, upper-left-to-lower-right, and upper-right-to-lower-left. Note that we do not consider, for example, the direction right-lo-left, since a right-to-left sequence can be represented as a left-to-right sequence. The
direction of a sequence can be represented by a pair of numbers (d_y, d_x) as follows:
 
- (0,1): direction left-to-right. For example, the sequence of stones of the same colour on coordinates (5,2), (5,3), (5,4), (5,5) is a sequence in direction left-to-right. Note that we say that the last stone in the sequence is at location (5,5), not at location (5,2).
 
- (1,0): direction top-to-bottom. For example, a sequence of stones of the same colour on coordinates (3,1), (4,1), (5,1) is a top-to-bottom sequence. Note that we say that the last stone in the sequence is at location (5,1), not at location (3,1).
 
- (1,1): direction upper-left-to-lower-right. For example, a sequence of stones of the same colour on coordinates (2,3), (3,4), (4,5) is an upper-left-to-lower-right sequence. Note that we say that the last stone in the sequence is at location (4,5), not at location (2,3). (1,-1): direction upper-right-to-lower-left. For example, a sequence of stones of the same colour on coordinates (5,5), (6,4), (7,3) is an upper-right-to-lower-left sequence. Note that we say that the last stone in the sequence is at location (7,3), not at location (5,5).

A sequence can be:
1. open: a stone can be put on a square at either side of the sequence.
 
2. closed: the sequence is blocked on both sides, so that no stone can be placed on either side of the sequence. This can occur either because the sequence begins/ends near the border of the board, or because there is a stone of a different colour in the location immediately next to the beginning/end of the sequence.

3. semi-open: the sequence is neither open nor closed.

The AI engine uses the following functions:

- is_empty(board): This function returns True iff there are no stones on the board board.
 
- is_bounded(board, y_end, x_end, length, d_y, d_x): This function analyses the sequence of length length that ends at location (y end, x end). The function returns "OPEN" if the sequence is open, "SEMIOPEN" if the sequence if semi-open, and "CLOSED" if the sequence is closed. Assume that the sequence is complete (i.e., you are not just given a subsequence) and valid, and contains stones of only one colour.
 
- detect row(board, col, y start, x start, length, d y, d x): This function analyses the row (let’s call it R) of squares that starts at the location (y start,x start) and goes in the direction (d y,d x). Note that this use of the word row is different from “a row in a table”. Here the word row means a sequence of squares, which are adjacent either horizontally, or vertically, or diagonally. The function returns a tuple whose first element is the number of open sequences of colour col of length length in the row R, and whose second element is the number of semi-open sequences of colour col of length length in the row R. Assume that (y start,x start) is located on the edge of the board. Only complete sequences count.  Assume length is an integer greater or equal to 2.
 
- detect rows(board, col, length): This function analyses the board board. The function returns a tuple, whose first element is the number of open sequences of colour col of length lengthon the entire board, and whose second element is the number of semi-open sequences of colour col of length length on the entire board. Only complete sequences count.  Assume length is an integer greater or equal to 2.
 
- search max(board): This function uses the function score() (provided) to find the optimal move for black. It finds the location (y,x), such that (y,x) is empty and putting a black stone on (y,x) maximizes the score of the board as calculated by score(). The function returns a tuple (y, x) such that putting a black stone in coordinates (y, x) maximizes the potential score (if there are several such tuples, you can return any one of them). After the function returns, the contents of board must remain the same.

- is win(board): This function determines the current status of the game, and returns one of ["White won", "Black won", "Draw", "Continue playing"], depending on the current status on the board. The only situation where "Draw" is returned is when board is full.



























































































































































