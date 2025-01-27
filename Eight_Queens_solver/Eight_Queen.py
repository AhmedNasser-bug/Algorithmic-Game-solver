from sys import*
from os import getcwd
path.append(getcwd())
from Eight_Queens_solver.Game_Tree_Generator import*
from setup import *


class Eight_Queen:

    def __init__(self):
        self.board_start = get_board()
        self.board_string = get_string_board(self.board_start)
        self.root = get_tree_root(self.board_start)

    
    def joint_condition(self, node:Node):
        return  node.heuristic == 4    
         
    # Correct
    @staticmethod
    def evaluation_function(node):
                                # turns into a 2d matrix
        return is_solved_board(get_board_string(node.value))