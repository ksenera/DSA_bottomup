#______________GIVEN________________
'''Given a sorted list of integers find two numbers that 
   add up to the target. Return their indices. 
   Ex: 2 + 7 = 9 =====> nums[0] + nums[1] = target 
'''
nums = [2, 7, 11, 15]
target = 9 

"""
___________PLAIN ENGLISH___________
 1) what are my edge cases?
   - no numbers add up to target 
   - empty list 
   - negative numbers only 

 2) what boundary conditions exist?
   - 

"""

#_________FUNCTION SKELETON_________
def find_two(nums):
    pass

#_________ASSERT STATEMENTS_________
assert find_two(nums) == target

"""
_______IMMEDIATE FEEDBACK LOG_______
my assertion is wrong:
    the function should return indices not the target value

function signature missing target parameter:
    given ordered list alone won't tell func to know what to 
    look for. 
"""