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
   - no solution given all params

REMEMBER: two pointers = one ptr at start and one ptr at end
          *-----> <-----* move them toward each other. 

"""

#_________FUNCTION SKELETON_________
def find_two(nums, target):
    pass

#_________ASSERT STATEMENTS_________
# NORMAL CASE: nums = [2, 7, 11, 15], target = 9 
# Ex: 2 + 7 = 9 =====> nums[0] + nums[1] = target
assert find_two(nums, target) == [0, 1]

# EMPTY LIST: nums = [], target = 9
assert find_two(nums, target) == [] 
#wrong - assert find_two(nums, target) == IndexError 

# NO SOLN EXISTS: nums = [2, 7, 11, 15], target = 100
assert find_two(nums, target) == [] 
#not consistent - assert find_two(nums, target) == None

"""
_______IMMEDIATE FEEDBACK LOG_______
my assertion is wrong:
    the function should return indices not the target value

function signature missing target parameter:
    given ordered list alone won't tell func to know what to 
    look for. 

my assertion for empty is wrong:
    can't assert an exception like that. IndexError is something 
    that crashes your program not a return value

None for no solution works too but be consistent:
    either [] for none or None for none

"""