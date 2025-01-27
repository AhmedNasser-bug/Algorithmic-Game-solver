from sys import*
from os import getcwd
path.append(getcwd())
from setup import*



created = set()
def get_distance(node1, node2):
    '''
    Calculate the Manhattan distance between two nodes.
    '''
    return abs(node1[0] - node2[0]) + abs(node1[1] - node2[1])


def create_node(parent, move, target):
    '''
    Create a new node with full information such as distance, cost
    '''
    new_val = (parent.value[0] + move[0], parent.value[1] + move[1]) 
    distance_to_goal = get_distance(new_val, target)
    new_node = Node(new_val, [], 1, distance_to_goal)

    return new_node


def in_bounds(node, width, length):
    """
    This function checks if the given node's coordinates are within the bounds of the maze.

    Parameters:
    node (Node): The node whose coordinates need to be checked.
    width (int): The width of the maze in cells.
    length (int): The length of the maze in cells.

    Returns:
    bool: True if the node's coordinates are within the maze bounds, False otherwise.
    """
    new_val = node.value
    return 0 <= new_val[1] < width and 0 <= new_val[0] < length

def valid_node(node, width, length):
    return node.value not in created and in_bounds(node, width, length)

def get_children(node, target, width, length, maze):
    """
    This function generates child nodes for the given node in the maze based on valid moves (up, down, left, right).
    It constructs a list of child nodes that are within the bounds of the maze and have not been visited yet.

    Parameters:
    node (Node): The parent node from which child nodes are generated.
    target (tuple): The coordinates of the target node in the maze.
    width (int): The width of the maze in cells.
    length (int): The length of the maze in cells.

    Returns:
    list: A list of child nodes that are within the bounds of the maze and have not been visited yet.
    """
    moves = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    children = []
    for move in moves:
        new_node = create_node(node, move, target)

        if valid_node(new_node, width, length) and maze[new_node.value[0]][new_node.value[1]] == 0:
            children.append(new_node)
            created.add(new_node.value)

    return children


def get_graph_root(maze, start, target_cell):
    """
    This function constructs a graph representation of a maze using the BFS algorithm.
    The graph is represented by a tree where each node corresponds to a cell in the maze.
    The function starts from the given start node and explores the maze by generating child nodes
    based on valid moves (up, down, left, right) until the target node is reached.

    Parameters:
    maze (list of lists): A 2D list representing the maze. Each cell contains either '0' (empty) or '1' (wall).
    start (tuple): The coordinates of the starting node in the maze.
    target (tuple): The coordinates of the target node in the maze.

    Returns:
    Node: The root node of the constructed graph. The graph is represented by the root node and its children.
    """
    global created
    created = set()
    que = deque()
    root = Node(start, [], 1, 0)
    LENGTH = len(maze)
    WIDTH = len(maze[0])

    que.append(root)

    while que:
        cur_maze_cell = que.popleft()
        cur_maze_cell.children = get_children(cur_maze_cell, target_cell, WIDTH, LENGTH, maze)

        for neighbor_cell in cur_maze_cell.children:
            que.append(neighbor_cell)

    return root
