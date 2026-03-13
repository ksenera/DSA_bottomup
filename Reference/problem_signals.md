# VALUE problem signals 
"find the maximum"
"find the sum"  
"does this value exist"
→ you care about WHAT is in the array
→ iterate by value: for num in nums

# POSITION problem signals 
"find the index"
"return indices"
"move toward each other"
"subarray from i to j"
→ you care about WHERE in the array
→ iterate by index: for i in range(len(nums))

# TWO POINTERS always position problem 
Things that MEET are at POSITIONS
left = 0              # position: start
right = len(nums) - 1 # position: end
nums[left]            # value AT that position
nums[right]           # value AT that position

# QUESTION TO ASK
"do I need to know WHERE I am in the array?"
→ yes → use index
→ no  → use value directly