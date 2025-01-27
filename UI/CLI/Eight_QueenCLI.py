from sys import*
from os import getcwd
path.append(getcwd())
from setup import*
from Algorithms import*
from Eight_Queens_solver.Eight_Queen import *


def show_eqeen_path(path:list):
    for board in path:
        board = get_board_string(board.value)
        print(board, '\n')
        ui_step()
    