def parse():
  with open("input.txt", "r") as fp:
    moves = [int(i) for i in fp.readline().split(",")]
    board = []
    lst = []
    line = fp.readline()
    count = 0
    while (line):
      if (len(line) > 5):
        board.append([int(i.strip()) for i in line.split()])
        count += 1
      if (count%5 == 0): 
        lst.append(list(board))
        board = []
      line = fp.readline() 
  lst = [i for i in lst if len(i)]  
  return (lst, moves)

sum_board = lambda board: sum([sum(filter(lambda x: type(x) == int, i)) for i in board])

mark = lambda boards, num : list([[[("#" if k == num else k) for k in boards[i][j]] for j in range(len(boards[i]))] for i in range(len(boards))])

def board_won(board, char):
  width = len(board)
  for i in range(width):
    if width in (len([j for j in board[i] if j == char]), len([board[j][i] for j in range(width) if board[j][i] == char])):
      return True
  return False
  
def win_index(boards):
  for i in range(len(boards)):
    if board_won(boards[i], "#"):
      return i
  return -1

def process_one(ctx):
  boards, moves = ctx
  count = 0
  while (win_index(boards) == -1 and count < len(moves)):
    num = moves[count]
    boards = mark(boards, num)
    count += 1
  return sum_board(boards[win_index(boards)] * moves[count-1])

def process_two(ctx):
  boards, moves = ctx
  count = 0
  winners = []
  while (count < len(moves)):
    num = moves[count]
    boards = mark(boards, num)        
    wins = 0
    for i in range(len(boards)):
      if board_won(boards[i-wins], "#"):
        winners.append((boards.pop(i-wins), moves[count]))
        wins+=1
    count += 1
  return sum_board(winners[-1][0] * winners[-1][1])

a = parse()
print(process_one(a))
print(process_two(a))
