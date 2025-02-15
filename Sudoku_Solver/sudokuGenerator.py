#from setup import*
from sys import *
from os import getcwd
path.append(getcwd())
from setup import*
possible_moves = defaultdict(list)


def get_possible_numbers(row_idx, col_idx, board):
    '''
    returns a list of possible numbers for the given position
    '''
    if board[row_idx][col_idx] != 0:
        return None

    possible_numbers = [i for i in range(1,10)]
    
    # check the row and column constraints
    for cell in board[row_idx]:
        if cell in possible_numbers: possible_numbers.remove(cell)

    for row in board:
        if row[col_idx] in possible_numbers: possible_numbers.remove(row[col_idx])

    # check the 3x3 box constraints
    box_row, box_col = (3 * (row_idx //3), 3 * (col_idx//3))
    for row in range(3):
        for col in range(3):
            if board[box_row + row][box_col + col] in possible_numbers: possible_numbers.remove(board[box_row + row][box_col + col])
          
    return tuple(possible_numbers)


def preprocess(board):
    '''
    preprocess the board to get the possible numbers for each cell
    '''
    global possible_moves
    possible_moves = defaultdict(list)
    ROWS = len(board)
    COLS = len(board[0])
    # iterate over all the cells
    for row in range(ROWS):
        for col in range(COLS):
            # update the possible numbers for the current cell
            possible_numbers = get_possible_numbers(row, col, board)
            if possible_numbers:
                possible_moves[(row, col)] = possible_numbers


def get_sudoku_node(value):
   coordinates = (value[0], value[1])
   # distance to the last cell
   heuristic = dist(coordinates, (8, 8))
   cost = randint(0,20)
   # return the new node 
   return Node(value = value,children = [], cost = cost, heuristic = heuristic)
   

def solved(board: list[list[int]]):
  '''
  checks if the board is solved by checking if there is any 0 in the board
  '''
  for row in board:
    for cell in row:
      if cell == 0:
        return False
  return True



def try_node(node:Node, board:list[list[int]]):
  row = node.value[0]
  col = node.value[1] 
  board[row][col] = node.value[2][0]


def get_new_choice_tree(board) -> Node:

    global possible_moves
    preprocess(board)
    
    # Construct all possible nodes
    nodes = []
    for pos, possible_nums in possible_moves.items():
      if possible_nums:
          nodes.append(get_sudoku_node(value =(pos[0], pos[1], possible_nums)))

    # Assign each node to its children
    if nodes : root = Node.get_choices_root(nodes)

    # return the root as the first element of the list of nodes   
    return root if nodes else None









