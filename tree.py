class Node:
    def __init__(self, val):
        self.val = val 
        self.left = None 
        self.right = None 

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

# test empty tree first 
assert find_max(None) == float('-inf')

# single node
root = Node(5)
assert find_max(root) == root.val

# only negatives 
root2 = Node(-3)
root2.left = Node(-7)
root2.right = Node(-1)
assert find_max(root2) == root2.right

# ________________________________________________________________

## example for max_depth here is a symmetric binary tree
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
# returned 3 in terminal correct 

# March 9 2026
# ─────────────────
# PROBLEM
# Max depth of binary tree

# WHAT I WROTE
# node1 = 1 instead of node1 = Node(1)

# WHAT WAS WRONG
# Created integer not Node instance
# dot notation fails on primitives

# WHY IT HAPPENED
# Forgot to call the class constructor
# knew the class existed but didn't instantiate it

# THE INVARIANT
# Class exists ≠ instance exists
# ClassName(params) is always required to create an object
# raw values have no properties
# ─────────────────



def is_symmetric(node):
    if node is None:
        return True
    if node.left.left == node.right.right:
        return True
    if node.left.right == node.right.left:
        return True 
    
# WRONG 

# tdd assert statements before code going forth 


def mirror(left, right):
    if left is None and right is None:
        return True 
    if left is None and right is not None:
        return False 
    if left is not None and right is None:
        return False 
    if left is not None and right is not None:
        if left.val != right.val:
            return False
        return mirror(left.left, right.right) and mirror(left.right, right.left)
    
assert mirror(None, None) == True
assert mirror(Node(1), None) == False 


root = Node(1)
root.left = Node(2)
root.right = Node(2)
root.left.left = Node(3)
root.left.right = Node(4)
root.right.left = Node(4)
root.right.right = Node(3)

print (mirror(root.left, root.right))

root2 = Node(1)
root2.left = Node(2)
root2.right = Node(2)
root2.left.right = Node(3)
root2.right.right = Node(3)

print(mirror(root2.left, root2.right))

# March 9 2026
# ─────────────────────────────────────
# PROBLEM
# Symmetric Tree (Leetcode #101)

# ─────────────────────────────────────
# ERRORS LOGGED

# ERROR 1
# WHAT I WROTE
# node1 = 1 instead of node1 = Node(1)

# WHAT WAS WRONG
# Created integer not Node instance
# dot notation fails on primitives

# WHY IT HAPPENED
# Knew the class existed
# forgot to instantiate it

# INVARIANT
# Class exists ≠ instance exists
# ClassName(params) always required
# raw values have no properties

# ─────────────────────────────────────
# ERROR 2
# WHAT I WROTE
# if left.left and right is None

# WHAT WAS WRONG
# left.left accesses a child property
# I was trying to check if left itself exists

# WHY IT HAPPENED
# Confused checking the node you received
# vs checking its children
# Children only come up in the recursive case
# not the base cases

# INVARIANT
# Base cases check the parameters you received
# Recursive case checks their children
# Never mix these two layers

# ─────────────────────────────────────
# ERROR 3
# WHAT I WROTE
# && instead of and

# WHAT WAS WRONG
# && is C++ and Java syntax
# Python uses plain English

# WHY IT HAPPENED
# Cross language syntax bleed

# INVARIANT
# Python logical operators
# && → and
# || → or
# !  → not

# ─────────────────────────────────────
# ERROR 4
# WHAT I WROTE
# if left.left == right.right:
#     return True

# WHAT WAS WRONG
# Two things wrong
# 1. == compares object references not values
#    should be left.val == right.val
# 2. Checking children with == is not recursion
#    recursion means calling the function itself

# WHY IT HAPPENED
# Did not fully understand what recursion meant
# thought recursion was a concept not literally
# calling the same function again

# INVARIANT
# Recursion = function calls itself with smaller input
# mirror(left.left, right.right)
# is not a comparison
# it is a recursive call that eventually hits a base case

# ─────────────────────────────────────
# COMPRESSION DECISIONS MADE THIS SESSION

# DECISION 1 — TDD AS DEFAULT PROBLEM SOLVING STRUCTURE
# Old approach
# read problem → try to write solution → blank IDE panic

# New approach
# read problem
# ↓
# write function shell with pass
# ↓
# write assert statements outside function
# ↓
# implement until all assertions pass

# Why this works
# assertions force enumeration of physical realities
# physical realities become base cases naturally
# POE is formalized as code
# assert = predict
# run = observe
# AssertionError = explain

# ─────────────────────────────────────
# DECISION 2 — TESTING FRAMEWORK PROGRESSION
# Level 1 now → assert statements for DSA practice
# Level 2 later → unittest built into Python
# Level 3 Perceivable project → pytest industry standard

# ─────────────────────────────────────
# DECISION 3 — RECURSIVE FRAME SHIFT
# All previous problems → solve(node) one parameter
# Symmetric tree → mirror(left, right) two parameters simultaneously

# When you see a problem comparing two subtrees
# the function signature changes to two parameters
# This is the tell that the problem requires
# a different recursive frame

# ─────────────────────────────────────
# DECISION 4 — BASE CASE DERIVATION METHOD
# Don't guess base cases
# Enumerate physical realities first

# For any two node comparison:
# L = None, R = None  → answer known → base case
# L = Node, R = None  → answer known → base case
# L = None, R = Node  → answer known → base case
# L = Node, R = Node  → answer unknown → recursive case

# Base cases are simply situations where
# the answer is already determined
# Only recurse when the answer is not yet known

# ─────────────────────────────────────
# BIG PICTURE PATTERN LOCKED TODAY
# induction proof structure = recursion structure
# base case = k=0 known answer
# k+1 case = recursive call with smaller input
# same mental model different vocabulary
# ─────────────────────────────────────