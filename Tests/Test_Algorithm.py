'''
TESTING PLAYGROUND
'''
from sys import*
from os import getcwd
path.append(getcwd())
from setup import *
from UI.GUI.MazeGUI import *
from UI.GUI.EightQueenGUI import *
from UI.CLI.MazeCLI import *
from UI.CLI.sudokuCLI import *
from UI.CLI.Eight_QueenCLI import * 
from Maze_Solver.Maze import *
from Sudoku_Solver.Sudoku import Sudoku
from Eight_Queens_solver.Eight_Queen import Eight_Queen
from Algorithms import BestFirstSearch, DLS, IDDFS, HillClimb


def sudoku_display(algorithm, *args):

    print("Here is an arbitrarily chosen sudoku board: " )
    board = [
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
    print(board)

    sud = Sudoku()
    path = sud.sudoku_tester(algorithm, *args)
    board = [
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
    fill_path_in_board(board, path)
    

def maze_display(algorithm, *args):
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))
    complexity = int(input("Enter the complexity level (advised to be the same number of a dimension): "))

    choice = int(input("Choose UI mode\n[1] Graphical user interface \n[2] Commandline interface\n Enter Choice: "))
    match choice:
        case 1:
            get_maze_gui(rows, cols, complexity, algorithm, *args)
        case 2:
            maze = Maze(rows, cols, complexity)
            path = algorithm(maze.root, maze.goal_condition, [(rows-1, cols-1)], *args)
            show_maze_path(maze, path)
            
    
def eight_queen_display(algorithm, *args):
    print("-Chose an arbitray permutation of queens-")
    choice = int(input("Choose UI mode\n[1] Graphical user interface \n[2] Command line interface\n Enter Choice: "))
    match choice:
        case 1:
            EightQueenGUI(algorithm, *args)
        case 2:
            board = Eight_Queen()
            path = algorithm(board.root, Eight_Queen.evaluation_function, [], *args)
            show_eqeen_path(path)

def main():

    #Choose Algorithm
    print("Choose Algorirthm\n[1] Best first search\n[2] Depth limited search\n[3] Iterative deepening depth first search\n[4] Hill climb search")
    choice = int(input("Choose Algorithm: "))
    algorithm = None
    algo_name = None
    args = []
    # Get Arguments for chosen algorithm
    match choice:
        case 1:
            algorithm = BestFirstSearch.bestfirstsearch
            algo_name = "best first search"
        case 2:
            algorithm = DLS.get_dls_path
            algo_name = "depth limited search"
            limit = int(input("Choose limit: "))
            args.append(limit)
        case 3:
            algorithm = IDDFS.IterativeDS
            algo_name = "iterative deepening depth first search"
        case 4:
            algorithm = HillClimb.hill_climb
            algo_name = "hill climb search"

    # Choose Game
    print("\nChoose Game\n[1] Sudoku\n[2] Maze\n[3] Eight Queens")
    choice = int(input("Choose Game: "))
    match choice:
        case 1:
            if args: sudoku_display(algorithm, args)
            else: sudoku_display(algorithm)
        case 2:
            if args: maze_display(algorithm, args)
            else: maze_display(algorithm)
        case 3:
            if args: eight_queen_display(algorithm, args)
            else: eight_queen_display(algorithm)

main()