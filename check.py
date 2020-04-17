def get_piece_pos(board, k_row, k_col):
 horizontal = [board[k_row][i] for i in range(1, 9) if(board[k_row][i] != '_')]
 vertical = [board[i][k_col] for i in range(1, 9) if(board[i][k_col] != '_')]
 cross_right = []
 row = k_row
 col = k_col
 while(row < 8 and col > 1):
  row = row + 1
  col = col - 1
 while(row >= 1 and col <= 8):
  if(board[row][col] != '_'):
   cross_right.append(board[row][col])
  row = row - 1
  col = col + 1
 cross_left = []
 while(k_row < 8 and k_col < 8):
  k_row = k_row + 1
  k_col = k_col + 1
 while(k_row >= 1 and k_col >= 1):
  if(board[k_row][k_col] != '_'):
   cross_left.append(board[k_row][k_col])
  k_row = k_row - 1
  k_col = k_col - 1
 return horizontal, vertical, cross_right, cross_left

def find_king(board, king):
 for i in range(1, 9):
  for j in range(1, 9):
   if(board[i][j] == king):
    return i, j
 return

def valid(k_row, k_col):
 if(k_row >= 1 and k_row <= 8 and k_col >= 1 and k_col <= 8):
  return True
 return False

def is_qr(king, piece):
 if((king == 'k' and (piece == 'Q' or piece == 'R')) or (king == 'K' and (piece == 'q' or piece == 'r'))):
  return True
 return False

def is_qb(king, piece):
 if((king == 'k' and (piece == 'Q' or piece == 'B')) or (king == 'K' and (piece == 'q' or piece == 'b'))):
  return True
 return False

def is_knight(king, piece):
 if((king == 'K' and piece == 'n') or (king == 'k' and piece == 'N')):
  return True
 return False

def is_pawn(king, piece):
 if((king == 'K' and piece == 'p') or (king == 'k' and piece == 'P')):
  return True
 return False

def check_by_ver_hor(lis, king):
 if(len(lis) == 1):
  return False
 pos = 0
 for i in range(0, len(lis)):
  if(lis[i] == king):
   pos = i
   break
 if(pos == 0):
  return is_qr(king, lis[pos + 1])
 if(pos == len(lis) - 1):
  return is_qr(king, lis[pos - 1])
 return (is_qr(king, lis[pos + 1]) or is_qr(king, lis[pos - 1]))

def check_by_cross(lis, king):
 if(len(lis) == 1):
  return False
 pos = 0
 for i in range(0, len(lis)):
  if(lis[i] == king):
   pos = i
   break
 if(pos == 0):
  return is_qb(king, lis[pos + 1])
 if(pos == len(lis) - 1):
  return is_qb(king, lis[pos - 1])
 return (is_qb(king, lis[pos + 1]) or is_qb(king, lis[pos - 1]))

def check_by_pawn(board, k_row, k_col):
 king = board[k_row][k_col]
 rows = [k_row + 1, k_row - 1]
 cols = [k_col + 1, k_col - 1]
 for i in rows:
  for j in cols:
   if(valid(i, j) and is_pawn(king, board[i][j])):
    return True
 return False

def check_by_knight(board, k_row, k_col):
 king = board[k_row][k_col]
 rows = [k_row + 1, k_row + 2, k_row - 1, k_row - 2]
 cols = [k_col + 1, k_col + 2, k_col - 1, k_col - 2]
 for i in range(4):
  for j in range(4):
   if(valid(rows[i], cols[j]) and is_knight(king, board[rows[i]][cols[j]])):
    if(i == 0 and (j == 0 or j == 3)):
     return True
    if(i == 1 and (j == 0 or j == 2)):
     return True
    if(i == 2 and (j == 1 or j == 2)):
     return True
    if(i == 3 and (j == 0 or j == 2)):
     return True
 return False

def check_check(board, king):
 k_row, k_col = find_king(board, king)
 hor, ver, cr, cl = get_piece_pos(board, k_row, k_col)
 h = check_by_ver_hor(hor, king)
 v = check_by_ver_hor(ver, king)
 c1 = check_by_cross(cr, king)
 c2 = check_by_cross(cl, king)
 knight = check_by_knight(board, k_row, k_col)
 pawn = check_by_pawn(board, k_row, k_col)
 return (h or v or c1 or c2 or knight or pawn)

def copy(board):
 res = []
 for i in board:
  lis = []
  for j in i:
   lis.append(j)
  res.append(lis)
 return res

def check_check_mate(board, king):
 k_row, k_col = find_king(board, king)
 c = 0
 tmp = copy(board)
 rows = [k_row,  k_row + 1, k_row - 1]
 cols = [k_col, k_col + 1, k_col - 1]
 for i in range(0, 3):
  for j in range(0, 3):
   tmp[k_row][k_col] = '_'
   if(valid(rows[i], cols[j])):
    tmp[rows[i]][cols[j]] = king
    if(check_check(tmp, king)):
     c = c + 1
   tmp = copy(board)
 return c == 8
