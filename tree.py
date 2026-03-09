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

node1 = Node(1)
node2 = Node(2)
node3 = Node(3) 
node4 = Node(4)
node5 = Node(5)

node1.left = node2
node2.left = node4

def max_depth(node):
    if node is None:
        return 0
    
    left_depth = max_depth(node.left)
    right_depth = max_depth(node.right)

    return (max(left_depth, right_depth) + 1)
print(max_depth(node1))
