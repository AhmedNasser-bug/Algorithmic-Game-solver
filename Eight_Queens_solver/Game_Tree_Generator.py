from sys import *
from os import getcwd
path.append(getcwd())
from setup import *


# CORRECT
def get_string_board(board):
    string = []
    rows = len(board)
    cols = len(board)
    for i in range(rows):
        for j in range(cols):
            string.append(board[i][j])
    return "".join(string)

# CORRECT
def get_board_string(board_string):
    board = []
    row, col = [], 0
    for chr in board_string:
        row.append(chr)
        col += 1
        if col == 8:
            board.append(row)
            row, col = [], 0
    return board

# CORRECT
def in_bounds(row, col):
    return 0 <= row < 8 and 0 <= col < 8

# Correct
def valid_queen(cell, board):
    row = cell[0]
    col = cell[1]
    board[row][col] = '*'
    # mark the row as invalid
    for cell_idx in range(8):
        if board[row][cell_idx] == 'Q': 
            board[row][col] ='Q'
            return False
    # mark the column as invalid
    for cell_idx in range(8):
        if board[cell_idx][col] == 'Q' : 
            return False
    # mark the two diagonals as invalid
    for cell_idx in range(8):
        if (in_bounds(cell_idx + row, cell_idx + col) and board[cell_idx + row][cell_idx + col]  == 'Q') or \
        (in_bounds(row - cell_idx, col - cell_idx) and board[row - cell_idx][col - cell_idx] == 'Q') or\
        (in_bounds(row + cell_idx, col - cell_idx) and board[row + cell_idx][col - cell_idx] == 'Q') or \
        (in_bounds(row - cell_idx, col + cell_idx) and board[row - cell_idx][col + cell_idx] == 'Q') :
            board[row][col] ='Q'
            return False
    # mark the box as invalid
    box_row, box_col = row - 1, col - 1
    for i in range(3):
        for j in range(3):
            if  in_bounds(box_row + i, box_col + j) and board[box_row+i][ box_col+j] == 'Q':
                board[row][col] ='Q'
                return False 
    board[row][col] ='Q'
    return True

# CORRECT
def is_solved_board(board):
    for i in range(8):
        for j in range(8):
            if board[i][j] == 'Q' :
                if valid_queen((i,j), board):
                    continue
                else:
                    return False
    return True

# CORRECT
def heauristic_function(board):
    heuristic = 8
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == 'Q' and valid_queen((row, col), board): heuristic -= 1
    return heuristic

# CORRECT
def get_node(board:list[list[str]]):
    heuristic = heauristic_function(board) # invalid queens
    cost = heuristic # valid queens
    board = get_string_board(board)
    return Node(board, [], cost, heuristic)

# CORRECT
def swap_col(board, col1, col2):
        for i in range(8):
            board[i][col1], board[i][col2] = board[i][col2], board[i][col1]

# Correct
def get_board():
    temp = [['*' for j in range(8)] for i in range(8)]
    for i in range(8):
        temp[i][i] = 'Q'
    return temp

def get_children(board):
    children = []
    board = get_board_string(board)

    for i in range(len(board)):

        col = i % 8
        # swap the queen with the current cell
        swap_col(board, 0 , col)
        child = get_node(board)
        children.append(child)
        swap_col(board, col, 0)

    board = get_string_board(board)
    shuffle(children)
    return children

def evaluation_function(node):
        return node.heuristic == 0

def get_tree_root(board_start):

        que = deque()
        root = get_node(board_start)
        que.append(root)
        
        visited = set([root.value])

        while que:
            cur = que.popleft()
            # Calculate the children of the current node
            cur.children = get_children(cur.value)
            # if the current node is the goal , return the root
            if evaluation_function(cur):
                return root

            for child in cur.children:
                #if child is not built , add it to the tree 
                if child.value not in visited:
                    visited.add(child.value)
                    que.append(child)

        return root


if __name__ == "__main__":
    board_start = get_board()
    board_string = get_string_board(board_start)
    root = get_tree_root(board_start)