from sys import*
from os import getcwd
path.append(getcwd())
from Maze_Solver.MazeGraphBuilder import get_graph_root
from Maze_Solver.MazeBuilder import get_maze
from setup import*
from Algorithms import BestFirstSearch



class Maze:

    def __init__(self, rows:int, cols:int, complexity:int):
        self.maze = get_maze(rows, cols, complexity)
        self.start = (0,0)
        self.goal = (rows-1, cols-1)
        self.root = get_graph_root(self.maze, self.start, self.goal)
       

    def goal_condition(self, node:Node, goal_value:idx):
        return node.value == (goal_value.row, goal_value.col)
    
    def joint(self):
         self.optimal_path = BestFirstSearch.bestfirstsearch(self.root, self.goal_condition, self.goal)
         joint = self.optimal_path[len(self.optimal_path)//2]
         return joint

    @staticmethod
    def solve(maze, algorithm, *args) -> tuple[int, int]:
        '''
        Returns the path from the start to the goal using the given algorithm
        '''
        path = algorithm(maze.root, maze.goal_condition, *args)
        return path