from sys import*
from os import getcwd
path.append(getcwd())
from Algorithms.algo_setup import*


path = []
found = False
def DLS(node:Node, goal_condition,  limit , goal_condition_args,level = 0 ):
  
  if goal_condition(node, *goal_condition_args):
    path.append(node)
    found = True
    return
  if level == limit or node == None:
      return 

  found = False
  path.append(node)

  for child in node.children:
    DLS(child, goal_condition, limit,  goal_condition_args, level + 1)

  return found

def IterativeDS(root:Node, goal_condition, *goal_condition_args):
  global path

  # Get Real number of arguments
  real_args = []
  for goal_condition_arg in goal_condition_args:
    if isinstance(goal_condition_arg,tuple):
         goal_condition_arg = idx(goal_condition_arg[0], goal_condition_arg[1])
    if goal_condition_arg : real_args.append(goal_condition_arg)

  path = []
  limit = 0
  MaxDepth = Node.max_depth(root) 

  # for loop to iterate the number of levels
  found = False
  while limit <= MaxDepth and found == False:
    DLS(root, goal_condition, limit, real_args)
    if found == True: break
    limit += 1
  return path