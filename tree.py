def find_max(node):
    if node is None:
        return float('-inf')
    # did 0 first but what if a tree contains only negative numbers. 
    left_max = find_max()
    # left_max = find_max(node.val) WRONG 
    # need to pass a node, find_max expects a node object not a number
    # find_max function needs to the whole node to access both 
    # .val and .next children 
    # if im standing at curr_node -> child1Left && curr_node -> child2Right how do i 
    # access left child of curr_node

class Node:
    def __init__(self, val):
        self.val = val 
        self.left = None 
        self.right = None 