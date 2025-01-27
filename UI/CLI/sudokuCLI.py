from sys import *
from os import getcwd
path.append(getcwd())
from setup import*

def fill_path_in_board(board, path:list[Node]):
  for node in path:
      row, col, value = node.value[0], node.value[1], node.value[2][0]
      board[row][col] = value
      print(board)
      ui_step()