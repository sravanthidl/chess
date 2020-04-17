import piece_obstacles

'''moves a piece'''
def update(board, s_row, s_col, d_row, d_col) :
 board[d_row][d_col] = board[s_row][s_col]
 board[s_row][s_col] = '_'

'''kills a piece'''
def kill(board, s_row, s_col, d_row, d_col) :
 if(ord(board[s_row][s_col]) < 90 and ord(board[d_row][d_col]) > 97) :		#White kills Black
  update(board, s_row, s_col, d_row, d_col)
 elif(ord(board[d_row][d_col]) < 90 and ord(board[s_row][s_col]) > 97) :	#Black kills White
  update(board, s_row, s_col, d_row, d_col)
 else :										#WKW or BKB
  print("You Cant Kill Your Own Army!")

'''moves of a rook'''
def rook(board, s_row, s_col, d_row, d_col) :
 obs = piece_obstacles.rook_obs(board, s_row, s_col, d_row, d_col)
 if(obs == -1):					#Invalid travelling path
  print("Rook Does'nt Move Crossly!")
 elif(obs == 0) :				#No obstacles
  if(board[d_row][d_col] == '_') :		#move
   update(board, s_row, s_col, d_row, d_col)
  else :					#kill
   kill(board, s_row, s_col, d_row, d_col)
 else :						#obstacle
  print("OOPS!OBSTACLE!")
 return board

'''moves of a knight'''
def knight(board, s_row, s_col, d_row, d_col) :
 if(abs(d_row - s_row) == 2 and abs(d_col - s_col) == 1) or (abs(d_row - s_row) == 1 and abs(d_col - s_col) == 2) :						#Valid travelling path
  if(board[d_row][d_col] == '_') :		#move
   update(board, s_row, s_col, d_row, d_col)
  else :					#kill
   kill(board, s_row, s_col, d_row, d_col)
 else :						#Invalid travelling path
  print("Invalid!Knight moves in an L-shape!")
 return board

'''moves of a bishop'''
def bishop(board, s_row, s_col, d_row, d_col) :
 obs = piece_obstacles.bishop_obs(board, s_row, s_col, d_row, d_col)
 if(obs == -1) :				#Invalid travelling path
  print("Invalid Move!Bishops Move Crossly!")
 elif(obs == 0) :				#No obstacles
  if(board[d_row][d_col] == '_') :		#move
   update(board, s_row, s_col, d_row, d_col)
  else :					#kill
   kill(board, s_row, s_col, d_row, d_col)
 else :						#obstacle
   print("OOPS!OBSTACLE!")
 return board

'''moves of a queen(rook or bishop)'''
def queen(board, s_row, s_col, d_row, d_col) :
 if(s_row == d_row or s_col == d_col) :						#straight
  obs = piece_obstacles.rook_obs(board, s_row, s_col, d_row, d_col)
  if(obs == 0) :								#No obstacle
   if(board[d_row][d_col] == '_') :						#move
    update(board, s_row, s_col, d_row, d_col)
   else :									#kill
    kill(board, s_row, s_col, d_row, d_col)
  else :									#Obstacle
   print("OOPS!OBSTACLE!")
 elif(abs(d_row - s_row) == abs(d_col - s_col)) :				#Cross
  obs = piece_obstacles.bishop_obs(board, s_row, s_col, d_row, d_col)
  if(obs == 0) :								#No obstacle
   if(board[d_row][d_col] == '_') :						#move
    update(board, s_row, s_col, d_row, d_col)
   else :									#kill
    kill(board, s_row, s_col, d_row, d_col)
  elif(obs == 1) :								#Obstacle
   print("OOPS!OBSTACLE!")
 else :										#Invalid travelling path
  print("Invalid Move!Queen Moves Either Crossly Or Straight")
 return board

'''moves of a king'''
def king(board, s_row, s_col, d_row, d_col) :
 if(abs(d_row - s_row) == abs(d_col - s_col) and abs(d_row - s_row) == 1) or (abs(d_row - s_row) == 1 and s_col == d_col) or (abs(d_col - s_col) == 1 and s_row == d_row) :		#Valid move
  if(board[d_row][d_col] == '_') :					#move
   update(board, s_row, s_col, d_row, d_col)
  else :								#kill
   kill(board, s_row, s_col, d_row, d_col)
 else :									#Invalid move
  print("Invalid move!King moves only 1 step!")
 return board

'''first move of a pawn'''
def pawn_first_move(board, s_row, s_col, d_row, d_col):
 if(board[s_row][s_col] == 'P' and (d_row == 5 or d_row == 6)):		#White 1/2 steps ahead
  if(piece_obstacles.pawn_obs(board, s_row, s_col, d_row, d_col) == 0):	#No obstacles
   update(board, s_row, s_col, d_row, d_col)
  else:									#Obstacle
   print("OOPS!OBSTACLE!")
 elif(board[s_row][s_col] == 'p' and (d_row == 3 or d_row == 4)):	#Black 1/2 steps ahead
  if(piece_obstacles.pawn_obs(board, s_row, s_col, d_row, d_col) == 0):	#No Obstacles
   update(board, s_row, s_col, d_row, d_col)
  else:									#Obstacle
   print("OOPS!OBSTACLE!")
 else:									#More than 2 steps ahead
  print("INVALID MOVE!")

'''moves of a pawn from its second move'''
def pawn_move(board, s_row, s_col, d_row, d_col):
 if(board[s_row][s_col] == 'P' and d_row == s_row - 1):          		#White 1 step ahead
  if(board[s_row - 1][s_col] == '_'):
   update(board, s_row, s_col, d_row, d_col)
  else:
   print("PAWN KILLS CROSSLY!")
 elif(board[s_row][s_col] == 'p' and d_row == s_row + 1):        		#Black 1 step ahead
  if(board[s_row + 1][s_col] == '_'):
   update(board, s_row, s_col, d_row, d_col)
  else:
   print("PAWN KILLS CROSSLY!")
 else:                                                          #More than 1 step ahead
  print("INVALID MOVE!")

'''moves of any pawn'''
def pawn(board, s_row, s_col, d_row, d_col) :
 if(s_col == d_col):						#Straight move
  if(board[s_row][s_col] == 'P' and s_row == 7):			#White's first move
   pawn_first_move(board, s_row, s_col, d_row, d_col)
  elif(board[s_row][s_col] == 'p' and s_row == 2):		#Black's first move
   pawn_first_move(board, s_row, s_col, d_row, d_col)
  else:								#From second move
   pawn_move(board, s_row, s_col, d_row, d_col)
 elif(abs(s_row - d_row) == 1):					#cross move
  if(board[s_row][s_col] == 'P' and d_row == s_row - 1):	#White pawn kills
   kill(board, s_row, s_col, d_row, d_col)
  elif(board[s_row][s_col] == 'p' and d_row == s_row + 1):	#Black pawn kills
   kill(board, s_row, s_col, d_row, d_col)
  else:
   print("INVALID MOVE!")
 else:
  print("INVALID MOVE!")
