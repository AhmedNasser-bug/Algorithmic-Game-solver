from random import *
def get_direction():
    right = (0, 1)
    left = (0, -1)
    up = (-1, 0)
    down = (1, 0)
    chance = randint(1,100)
    
    direction = None
    if chance <= 100: # Go right
        direction = right
    if chance <= 50: # Go down
        direction = down
    if chance <= 20: # Go up
        direction = up
    if chance <= 10: # Go left
        direction = left

    return direction


def get_valid_path(maze, start, goal) -> list[tuple]: # O(inf)
    '''
    Returns a list of tuples containing a valid path from the given start to the given goal
    '''
    path = [start]
    width = len(maze[0])
    length = len(maze)

    while start != goal:
        # Choose a random direction
        direction = get_direction()
        new_block = (start[0] + direction[0], start[1] + direction[1])
        
        # Check if the new block is within the boundaries of the maze 
        while  not (0 <= new_block[1] < width and 0 <= new_block[0] < length):
            direction = get_direction()
            new_block = (start[0] + direction[0], start[1] + direction[1])

        start = (new_block[0], new_block[1])
        path.append(start)

    return path

def get_empty_maze(rows_num, cols_num):
    '''
    This function generates an empty maze of given dimensions.
    '''
    maze_template = [[1 for _ in range(cols_num)]for _ in range(rows_num)]
    return maze_template
    

def complicate_maze(maze, rows, cols, path, complexity):
    '''
    This function adds crossroads to the maze at random locations along the path.
    '''
    # Add obstacles to the maze at random locations along the path, with a given complexity level.
    crosses = complexity 
    while crosses > 0:
        cross_point = path[randint(0, len(path)-1)]
        length = complexity
        direction = get_direction()

        while length:
            # Longer paths with a given complexity level
            cross_point = (cross_point[0] + direction[0], cross_point[1] + direction[1])
            if 0 <= cross_point[1] < cols and 0 <= cross_point[0] < rows:
                maze[cross_point[0]][cross_point[1]] = 0
                path.append(cross_point)
                length -= 1
            else:
                break
        crosses -= 1
    
    
def get_maze(rows, cols, complexity):
    '''
    This function generates a maze of given dimensions and complexity level.
    '''
    maze_template = get_empty_maze(rows, cols)
    # Get a random generated valid path for the maze
    valid_path = get_valid_path(maze_template, (0,0),(rows-1,cols-1))

    # label the path in the matrix
    for cell in valid_path:
        maze_template[cell[0]][cell[1]] = 0

    # Add obstacles to the maze    
    complicate_maze(maze_template, rows, cols, valid_path, complexity)
    
    return maze_template



