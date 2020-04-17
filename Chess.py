import piece_obstacles
import piece
import check
#BUILDING THE CHESS BOARD
def initial_board() :
 l = [[' ', 1, 2, 3, 4, 5, 6, 7, 8], [1, 'r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'], [2, 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'], [3, '_', '_', '_', '_', '_', '_', '_', '_'], [4, '_', '_', '_', '_', '_', '_', '_', '_'], [5, '_', '_', '_', '_', '_', '_', '_', '_'], [6, '_', '_', '_', '_', '_', '_', '_', '_'],[7, 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],[8, 'R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']]
 return l

def print_board(board) :
 for i in board:
  print('                      ', end = "")
  print('  '.join([str(elem) for elem in i]))

'''s_row = source row.Row in which the piece is standing'''
'''s_col = source column.Column in which the piece is standing'''
'''d_row = destination row.Row to which the player wants to move the piece'''
'''d_col = destination column.Column to which the player wants to move the piece'''

'''check_move checks for basic invalid moves'''
def check_move(in_board, s_row, s_col, d_row, d_col) :
 if(s_row == d_row and s_col == d_col) :		#Moving to the same place it is
  print("Invalid Move!")
 elif(s_row > 8 or s_col > 8 or d_row > 8 or d_col > 8) :	#Out of the board
  print("You Are Out Of The Board!")
 else :
  check_piece(in_board, s_row, s_col, d_row, d_col)

'''check_piece finds the piece the player is trying to move and processess the move accordingly'''
'''p = pawn, r = rook, b = bishop, n = knight, q = queen, k = king'''
''' uppercase denotes the WHITES and lowercase denotes the BLACKS'''
def check_piece(board, s_row, s_col, d_row, d_col) :
 if(board[s_row][s_col] == 'p' or board[s_row][s_col] == 'P') :
  piece.pawn(board, s_row, s_col, d_row, d_col)
 elif(board[s_row][s_col] == 'r' or board[s_row][s_col] == 'R') :
  piece.rook(board, s_row, s_col, d_row, d_col)
 elif(board[s_row][s_col] == 'b' or board[s_row][s_col] == 'B') :
  piece.bishop(board, s_row, s_col, d_row, d_col)
 elif(board[s_row][s_col] == 'n' or board[s_row][s_col] == 'N') :
  piece.knight(board, s_row, s_col, d_row, d_col)
 elif(board[s_row][s_col] == 'q' or board[s_row][s_col] == 'Q') :
  piece.queen(board, s_row, s_col, d_row, d_col)
 elif(board[s_row][s_col] == 'k' or board[s_row][s_col] == 'K') :
  piece.king(board, s_row, s_col, d_row, d_col)
 else :
  print("INVALID PIECE!!!")
 print_board(board)

in_board = initial_board()
print_board(in_board)
turn = 1
while True : 	
 s_row = int(input("Source Row:"))
 s_col = int(input("Source Column:"))
 d_row = int(input("Dest Row:"))
 d_col = int(input("Dest Column:"))
 if(turn % 2 == 1) :						#White's turn
  if(ord(in_board[s_row][s_col]) < 90) :			#White moves
   check_move(in_board, s_row, s_col, d_row, d_col)
   if(in_board[s_row][s_col] == '_'):				#White moved
    turn = turn + 1
  else :							#Black moves
   print("Its White's Turn!")
 else :								#Black's turn
  if(ord(in_board[s_row][s_col]) > 90) :			#Black moves
   check_move(in_board, s_row, s_col, d_row, d_col)
   if(in_board[s_row][s_col] == '_'):				#Black moved
    turn = turn + 1
  else :							#White moves
   print("Its Black's Turn!")
 if((turn - 1) % 2 == 1):
  check_for_king = 'k'
 else:
  check_for_king = 'K'
 if(check.check_check_mate(in_board, check_for_king)):
  print("CHECKMATE!")
  exit(0)
 if(check.check_check(in_board, check_for_king)):
  print("CHECK!") 
