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
 3) when do i move left ptr right and right ptr left?
   - since the list is sorted from smallest num to largest
    - move left ptr first WRONG 
   - to make sum smaller do i want bigger number or smaller number?
    - smaller number 
     - right ptr moves left to hit every num to get to smaller vals
   - if sum is too small: 
    - move left ptr right to get bigger value 
   - sum > target -> move R ptr L
   - sum < target -> move L ptr R 
   - sum == target -> found, return indices

"""

#___________FUNCTION___________
def find_two(nums, target):    
    # take care of empty list edge case
    if not nums:
        return []
    
    # define left and right ptrs 
    left = 0 
    right = len(nums) - 1
    
    # WRONG
    # sum = nums[left] + nums[right]
    # if sum > target:
    #     nums[right - 1] 
    # if sum < target:
    #     nums[left + 1]
    # if sum == target:
    #     return sum


    while left < right:
        # check sum 
        sum = nums[left] + nums[right]
        if sum > target:
            right -= 1
        if sum < target:
            left += 1
        if sum == target:
            # WRONG
            #return nums[left, right]
            return [left, right]
    # no soln exists
    return []


#_________ASSERT STATEMENTS_________
# NORMAL CASE: nums = [2, 7, 11, 15], target = 9 
# Ex: 2 + 7 = 9 =====> nums[0] + nums[1] = target
assert find_two(nums, target) == [0, 1]

# EMPTY LIST: nums = [], target = 9
assert find_two([], target) == [] 
#wrong - assert find_two(nums, target) == IndexError 

# NO SOLN EXISTS: nums = [2, 7, 11, 15], target = 100
assert find_two(nums, 100) == [] 
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

"""
_______IMMEDIATE ERROR LOG_______
Problem 1: no loop. checked sum once and stopped 
 - need to keep checking till pointers meet 
 - what loop runs until a condition is false = WHILE LOOP
Problem 2: not updating pointers:
 - accessing value nums[right -1] but not saving it anywhere
Problem 3: wrong return:
 - return sum returns value i need to return indices 
Problem 4: When the loop exits without finding a soln the 
function returns None implicitly:
 - explicitly return [] after the loop ends
"""


# March 9 2026
# ─────────────────
# PROBLEM
# Two pointers — two sum sorted array (Leetcode #167)

# KEY CONFUSION
# mixed up index and value repeatedly
# right is the position
# nums[right] is the value at that position
# moving the pointer means right -= 1
# not nums[right - 1]

# INVARIANT
# pointer = position tracker (integer)
# nums[pointer] = value at that position
# you move pointers
# you read values
# never confuse the two
# ─────────────────