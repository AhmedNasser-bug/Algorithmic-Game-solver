from sys import*
from os import getcwd
path.append(getcwd())
from Algorithms.algo_setup import*

'''
Start by defining all paths to goal 
Graph them 
Run Hill climbing on the graph
'''
def hill_climb(root:Node, goal_condition, *goal_condition_args):
  # Preprocessing args
  real_args = []
  for goal_condition_arg in goal_condition_args:
    if isinstance(goal_condition_arg,tuple):
        goal_condition_arg = idx(goal_condition_arg[0], goal_condition_arg[1])
    if goal_condition_arg: real_args.append(goal_condition_arg)


  path = [root]
  current = root
  next_node = root

  while next_node is not None and not goal_condition(current, *real_args):

    next_node = None

    for child in current.children:
      
      if child.cost <= current.cost:
        next_node = child
        break

    if next_node is not None:
      current = next_node

    path.append(current)
  return path


