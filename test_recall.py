# hashmap 

sentence = "abracadabra"

counts = {}

for char in sentence:
    if char in counts:
        counts[char] += 1
    else:
        counts[char] = 1 

print(counts)


# linked list reversal 

def reverse_list(head):
    curr = head 
    prev = None 

    while curr is not None:
        next_node = curr.next 
        curr.next = prev 
        prev = curr 
        curr = next_node
    
    return prev

# March 9 2026
# ─────────────────
# PROBLEM
# Linked list reversal cold recall rep 2

# WHAT I WROTE
# return next_node → then return reverse_list → then return curr

# WHAT WAS WRONG
# Didn't track which variable holds the answer at loop exit

# WHY IT HAPPENED
# Loop logic was perfect
# Blanked on what state each variable is in after loop terminates

# THE INVARIANT
# After a while loop ask: what is each variable's state right now?
# curr = None (loop exit condition)
# next_node = None (last iteration saved None)
# prev = new head (last real node processed)
# The answer is always in prev for linked list reversal
# ─────────────────

#___________________________________________________________________


# leetcode 387 first unique character in a string 
sentence = "abracadabra"
counts = {}

for char in sentence:
    if char in counts:
        counts[char] += 1
    else:
        counts[char] = 1

print(counts)

# leetcode 206 reverse linked list 
def reverse_linked_list(head):
    curr = head
    prev = None 
    # input None -> 1 -> 2 -> 3 -> 4 -> 5 -> None 
    # curr = 1 = head of list 
    # prev = nothing aka None 
    while curr is not None:
        # save next property into var
        next_node = curr.next # 1.next = 2
        curr.next = prev # do reversal 2 = prev
        prev = curr # move down list 
        curr = next_node 
    return prev # holds ans at exit of loop 

# For binary tree problems 

class Node():
    # WRONG
    # def __init__(self, value, left, right):
    #     self.val = value 
    #     self.next = next 
    #     self.left = left 
    #     self.right = right 

    #RIGHT
    def __init__(self, value):
        self.val = value 
        self.left = None 
        self.right = None

node0 = Node(None) # not empty tree Node object that exists but holds value None
# empty tree is just None no Node object at all 
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node6 = Node(6)
node7 = Node(7)

node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5
node3.left = node6
node3.right = node7

        
# leetcode 104 maximum depth of binary tree 
def max_depth(node):
    #WRONG
    # depth_counter = 0
    # if node is None:
    #     return 0
    # if node is not None:
    #     depth_counter += 1
    #     return depth_counter
    if node is None:
        return 0
    # store how deep is my left and right sides 
    left_side = max_depth(node.left)
    right_side = max_depth(node.right)
    result = max(left_side, right_side) + 1
    print(f"node={node.val}, left={left_side}, right={right_side}, depth={result}")
    return result

#base case is empty node returns what ?
# WRONG assert max_depth(node0) == None
assert max_depth(None) == 0 # empty tree
# empty tree ret 0 depth of nothing is ZERO NOT NULL
assert max_depth(node1) == 3

# QUESTION TYPE: depth / value / relationship / path / count
# LOCAL QUESTION: what does one node need to know?
# BASE CASE: what does None return and why?
# COMBINE: what do I do with left and right?

# find max val in binary tree 
def max_value(node):
    #Q: find value 
    #LQ: node needs to know it's value 
    #BC: none returns float('-inf')
    #C: check left sub tree get max val then check right subtree 

# base case empty tree 
    if node is None:
        return float('-inf')
    
    # WRONG
    # left = node.left
    # right = node.right
    left = max_value(node.left)
    right = max_value(node.right)

    return max(left, right, node.val)

# tree empty
assert max_value(None) == float('-inf')
# tree example nodes 1-7
assert max_value(node1) == 7
# negative values assertion ? 
root1 = Node(-9)
root1.left = Node(-4)
root1.right = Node(-6)
assert max_value(root1) == -4


# leetcode 101 symmetric tree 
def is_symmetric(left, right):
    pass



# leetcode 53 maximum subarrary Kadane's
# given input [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# return largest sum of contiguous subarray 
# 4 + -1 + 2 + 1 = 6 
def max_subarray():
    list = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

    for i in list:
        print(i)


# leetcode #167 two sum II sorted array 
# input: [2, 7, 11, 15], target = 9 
# return: indices of two numbers that sum to target 
def two_sum(left, right):
    pass 

"""
print AFTER you have values to show
print BEFORE you return
what do I want to verify at this moment in the code?
how do I generate the right questions from first principles
so I never blank on a new problem?
"""