from sys import*
from os import getcwd
path.append(getcwd())
from Algorithms.algo_setup import*




def iterative_DLS(root:Node, goal_condition, limit, *goal_condition_args):
   global goal_found
   que = deque()
   que.append(root)
   path = []
   visited = set()
   #limit = limit[0]
   while que:
      cur = que.pop()
      path.append(cur)
      if isinstance(limit, list): limit = limit[0]
      limit -= 1
      for child in cur.children:
            if goal_condition(child, *goal_condition_args):
               goal_found = True
               path.append(child)
               return path
            if limit == 0:
               return path

            if child.value not in visited:
               visited.add(child.value)
               que.append(child)
               path.append(child)
   return path
       
      

            

def get_dls_path(root:Node, goal_condition, goal_condition_args:list, limit):
    if not isinstance(goal_condition_args, list): goal_condition_args = [goal_condition_args]

    real_args = []
    for goal_condition_arg in goal_condition_args: 
       if isinstance(goal_condition_arg,tuple):
         goal_condition_arg = idx(goal_condition_arg[0], goal_condition_arg[1])
       if goal_condition_arg: real_args.append(goal_condition_arg)

    
    return iterative_DLS(root, goal_condition, limit, *real_args)
    
