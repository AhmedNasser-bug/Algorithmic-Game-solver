from sys import *
from os import getcwd
path.append(getcwd())
from Algorithms.algo_setup import *

def bfs(root:Node, goal_condition, *goal_condition_args):
    '''
    Perform a breadth-first search on the given tree root using the provided goal condition.
    '''
    # Get the real number of args for the goal condition function
    real_args = []
    for goal_condition_arg in goal_condition_args:
        if goal_condition_arg:
            if isinstance(goal_condition_arg, tuple):
                goal_condition_arg = idx(goal_condition_arg[0], goal_condition_arg[1])
            real_args.append(goal_condition_arg)
    
    que = deque([root])
    path = [root]
    visited = set([root.value])

    while que:
        current = que.popleft()

        if goal_condition(current, *real_args):
            return path
        
        for neighbor in current.children:
            if neighbor.value not in visited:
                path.append(neighbor)
                visited.add(neighbor.value)
                que.append(neighbor)
            else:
                continue