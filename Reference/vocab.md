# PYTHON MECHANICS NOTE
List, Dict, Tuple from typing module = type hints only
Python built-ins: list, dict, tuple (lowercase) = actual types
List[str] is just telling the reader what type to expect
list is the actual object you create and use
from typing import List → only needed if you use capital List

# Group Anagrams 
# VOCAB LOG
- "".join(sorted(word))   → sort string, no separator
- list(result.values())   → all dict values as list
- defaultdict(list)       → auto-initializes missing keys to []


# Sliding Window
# VOCAB LOG
- seen = {}  vs  seen = 0
- f"label={variable}"
- right - left + 1  for window size
- max_len tracking variable
- indentation — update every iter vs only on break
# DEBUGGING
- print(f"label={variable}")   → print variable value with label
variable gets evaluated, label is just text
So whatever you want to see, name it and put the variable after `=` inside `{}`
print AFTER you have values, BEFORE you return

nums = [2, 7, 11, 15]  # this is a list
# ACCESS
nums[0]        # first element
nums[-1]       # last element
nums[i]        # element at index i

# LENGTH
len(nums)      # number of elements

# ADD
nums.append(x)     # add to end
nums.insert(i, x)  # add at index i

# REMOVE
nums.pop()         # remove last → returns it
nums.pop(i)        # remove at index i → returns it

# ITERATE
for i in range(len(nums)):  # iterate by INDEX
    nums[i]                 # access element by index

for num in nums:            # iterate by VALUE
    num                     # element directly, no index

# SLICE
nums[l:r]      # elements from index l to r-1

# SORT
sorted(nums)   # returns new sorted list
nums.sort()    # sorts in place

# MY MIXUP 
for right in nums:          # right = VALUE (char, int)
for right in range(len(nums)):  # right = INDEX (0,1,2...)

# ASSIGNMENT INVARIANT
left side = box name (label)
right side = value going into box
never reuse box name for different purpose
new purpose = new box name