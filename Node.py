from collections import *
class Node:
    def __init__(self, value = None, children:list = [] , cost = None, heuristic = None):
        self.value = value
        self.children = children
        self.heuristic = heuristic 
        self.cost = cost
        
    def __gt__(self, other):
        return self.heuristic > other.heuristic
    def __lt__(self, other):
        return self.heuristic < other.heuristic
    
    @staticmethod
    def max_depth(node):
        if not node.children :
            return 1
        max_len = 1
        for child in node.children:
            max_len = max(max_len, 1 + Node.max_depth(child))
        return max_len
    
    
    def add_children(self, children:list):
        self.children.extend(children)

    @staticmethod
    def get_node_with_value(root, value):
        '''Returns the node with the given value using DFS'''
        if root.value == value:
            return root
        
        for child in root.children:
            result = Node.get_node_with_value(child, value)
            if result is not None:
                return result
            
        return None
    @staticmethod
    def get_choices_root(nodes):

        root = nodes[0]
        for idx, node in enumerate(nodes):
           left = 2*idx + 1
           right = 2*idx + 2
           if left < len(nodes): node.children.append(nodes[left])
           if right < len(nodes): node.children.append(nodes[right])

        return root

    def __str__(self):
        return f"<{self.value}>"
    
    def __next_level(self, level):
        next_level = []
        for node in level:
            next_level.extend(node.children)
        return next_level
        
    def is_leaf(self):
        return len(self.children) == 0
    
    def print_levels(self):
        root = Node(self.value, self.children)
        height = Node.max_depth(root)
        cur_level = [self.value]
        for _ in range(height):
            print(cur_level)
            cur_level = self.__next_level(cur_level)


