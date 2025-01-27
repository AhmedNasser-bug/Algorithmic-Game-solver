from sys import*
from os import getcwd
path.append(getcwd())
from setup import*
from Algorithms import*
from Maze_Solver.Maze import *

def show_maze_path(maze:Maze, path:list[Node]):
    for node in path:
        row, col = node.value[0], node.value[1]
        maze.maze[row][col] = '*'
        print(maze.maze)
        sleep(0.5)
        print("Press any key to continue...")
        system("pause > 0")
        if (row, col) != maze.goal: system("cls")