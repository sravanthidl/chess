'''rook_obs checks for obstacles in rook's travelling path'''
def rook_obs(board, s_row, s_col, d_row, d_col) :
 if(s_row == d_row) :			#horizontal
  if(s_col < d_col) :			#right
   for i in range (s_col + 1, d_col) :
    if(board[s_row][i] != '_') :
     return 1
   return 0
  else :				#left
   for i in range(d_col + 1, s_col) :
    if(board[s_row][i] != '_') :
     return 1
   return 0
 elif(s_col == d_col) :			#vertical
  if(s_row < d_row) :			#down
   for i in range (s_row + 1, d_row) :
    if(board[i][s_col] != '_') :
     return 1
   return 0
  else :				#up
   for i in range (d_row + 1, s_row) :
    if(board[i][s_col] != '_') :
     return 1
   return 0
 else :
  return -1

'''bishop_obs checks for obstacles in bishop's travelling path'''
def bishop_obs(board, s_row, s_col, d_row, d_col) :
 if(abs(d_row - s_row) != abs(d_col - s_col)) :
  return -1
 elif(s_row > d_row) :			#up 
  if(s_col < d_col) :			#right
   temp = s_row - 1
   for i in range(s_col + 1, d_col) :
    if(board[temp][i] != '_') :
     return 1
    temp = temp - 1
   return 0
  else :				#left
   temp = d_row + 1
   for i in range(d_col + 1, s_col) :
    if(board[temp][i] != '_') :
     return 1
    temp = temp + 1
   return 0
 else :					#down
  if(s_col < d_col) :			#right
   temp = s_row + 1
   for i in range(s_col + 1, d_col) :
    if(board[temp][i] != '_') :
     return 1
    temp = temp + 1
   return 0
  else :				#left
   temp = d_row - 1
   for i in range(d_col + 1, s_col) :
    if(board[temp][i] != '_') :
     return 1
    temp = temp - 1
   return 0

'''pawn_obs checks for obstacles in pawn's travelling path'''
def pawn_obs(board, s_row, s_col, d_row, d_col) :
 if(board[s_row][s_col] == 'P') :			#White pawn
  for i in range(d_row, s_row):
   if(board[i][s_col] != '_'):
    return 1
  return 0
 else:							#Black pawn
  for i in range(s_row + 1, d_row + 1):
   if(board[i][s_col] != '_'):
    return 1
  return 0
