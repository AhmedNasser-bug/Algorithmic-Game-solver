from sys import*
from os import getcwd
path.append(getcwd())
from setup import*
from Sudoku_Solver.sudokuGenerator import*

class Sudoku:

    def __init__(self) -> None:
        self.board = [
            [5, 3, 0, 0, 7, 0, 0, 0, 0],
            [6, 0, 0, 1, 9, 5, 0, 0, 0],
            [0, 9, 8, 0, 0, 0, 0, 6, 0],
            [8, 0, 0, 0, 6, 0, 0, 0, 3],
            [4, 0, 0, 8, 0, 3, 0, 0, 1],
            [7, 0, 0, 0, 2, 0, 0, 0, 6],
            [0, 6, 0, 0, 0, 0, 2, 8, 0],
            [0, 0, 0, 4, 1, 9, 0, 0, 5],
            [0, 0, 0, 0, 8, 0, 0, 7, 9]
          ] 
        preprocess(self.board)
        

    def sudoku_tester(self, algorithm, *Args):
        '''
        Test the sudoku solver algorithm with the given board and optional arguments . DO NOT ADD THE ROOT AND GOAL CONDITION AS AN ARGUMENT
        '''
        path =[]
        
        goal_condition  = lambda node1: len(node1.value[2]) == 1
        # get the root of the choice tree
        root = get_new_choice_tree(self.board)

        while root is not None:
           # Get the path to the first candidate node
           ans = algorithm(root, goal_condition, [], *Args)

           choice = ans[-1]
           # If no candidate node is found, try it
           path.append(choice)
           try_node(choice, self.board)

           ans = []
          # Get the new root
           root = get_new_choice_tree(self.board)
        return path
