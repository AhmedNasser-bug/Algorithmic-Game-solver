from sys import*
from os import getcwd
path.append(getcwd())
from Algorithms.algo_setup import*


def bestfirstsearch(root:Node, goal_condition, *goal_condition_args):
  '''
  Perform a best-first search on the given tree root using the provided goal condition.
  '''
  # Get the real number of args for the goal condition function
  real_args = []
  for goal_conition_arg in goal_condition_args:
    if goal_conition_arg:
      if isinstance(goal_conition_arg,tuple):
        goal_conition_arg = idx(goal_conition_arg[0], goal_conition_arg[1])
      real_args.append(goal_conition_arg)

  heuristic=[]
  visited = set()

  visited.add(root.value)
  path = []
  heappush(heuristic,root)

  while heuristic:
    node = heappop(heuristic)

    if goal_condition(node,*real_args):
      return path + [node]   

    path.append(node)

      # Add the neighboring cells to the heuristic heap

    for child in node.children:
        if child.value not in visited:
          visited.add(child.value)
          heappush(heuristic, child)
    

  raise Exception("No path found")




