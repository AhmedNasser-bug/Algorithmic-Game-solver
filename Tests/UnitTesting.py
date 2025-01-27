'''
TESTING PLAYGROUND
'''
from sys import*
from os import getcwd
path.append(getcwd())
from setup import *
from UI.GUI.MazeGUI import *
from UI.CLI.MazeCLI import *
from UI.CLI.sudokuCLI import *
from UI.CLI.Eight_QueenCLI import * 
from Maze_Solver.Maze import Maze
from Sudoku_Solver import sudokuGenerator
from Eight_Queens_solver.Eight_Queen import Eight_Queen
from Algorithms import AlphaBetaPruning, bidirectional_search, BestFirstSearch, DLS, IDDFS, Genetic_Algorithm, HillClimb, min_max

