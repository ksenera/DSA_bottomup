# linked list takes Node as input 
# no head the starting point of the linked list
def linked_list(head):
    # define head no put the parameter into a variable 
    curr = head # save into curr 
    prev = None # None -> A -> B -> C -> D -> None 
    # wanna get D -> C -> B -> A -> None 

    # while A is not None == True 
    while curr is not None:
        # i have two errors in the while loop 
        # next node to A is B = A.next == B
        next_node = curr.next # get next node
        # B = prev overrides None 
        curr.next = prev # reverse it 
        prev = next 
        next = None
    # 1 error here 
    print(next)

def reverse_list(head):
    curr = head 
    prev = None 

    while curr is not None:
        next_node = curr.next # save next into a variable to track 
        curr.next = prev # reverse if A is curr and .next is B then reverse B is prev to A 
        prev = curr # error 1 slide prev forward 
        curr = next_node # error 2 why would next = None ???? slide curr forward
    return prev # prev is now the new head 

#error log entry 1:

#Error 1: used `next` instead of `next_node` — variable name inconsistency
#Error 2: wrote `next = None` instead of `curr = next_node` — lost the forward movement
#Error 3: printed instead of returned — forgot functions need to return values to be useful
#Why: had the logic right, syntax slipped on variable names under recall pressure
#Fix: name variables once, use exact same name throughout, always ask "does this function need to return something"

## Hashmap/ dictionary character counter 
# say i have a sentence. I wanna count the first and only occurence of any character 
sentence = "abracadabra"

# need the dictionary variable to assign key and add value. 

# Note: dictionary in Python = hashmap conceptually = unordered_map in C++
count = {} 

for char in sentence:
    if char in count:
        count[char] += 1
    else:
        count[char] = 1

print(count)

#error log entry 2:
#Error: wrote `if count in char` instead of `if char in count`
#Why: flipped the order under recall pressure
#Fix: read it as a question — "is this CHAR inside my COUNT dictionary" 
     #the thing you're looking for comes first, the container comes second
     #char in count = "is char a key in count" ✓
     #count in char = "is the whole dictionary inside one character" ✗



#__________________________________________________________________


def two_sum(sum, target):
    left = 0
    right = len(sum) - 1
    sum = left + right 
# ERROR 1: sum = left + right
# overwrote input array with index arithmetic
# INVARIANT: left and right are INDICES into the array
# actual sum = nums[left] + nums[right]
    
    while left < right:
        if sum < target:
# ERROR 3: sum < target → right -= 1
# WRONG DIRECTION
# if sum too small → need bigger values → move LEFT pointer right
# if sum too big → need smaller values → move RIGHT pointer left
# INVARIANT: squeeze inward based on comparison to target
            right -= 1
        if sum > target:
            left += 1 
        if sum == target:
            return list[left,right]
# ERROR 2: return list[left, right]
# list[] is not valid syntax
# CORRECT: return [left, right] or return [left+1, right+1] if 1-indexed
    return []

def two_sum(nums, target): # nums = the array or list, always
    left = 0 
    right = len(nums) - 1
    while left < right:
        curr_sum = nums[left] + nums[right] # compute from array values
        if curr_sum < target:
            left += 1 # too small → move left pointer right
        elif curr_sum > target:
            right -= 1 # too big → move right pointer left
        else:
            return [left +1, right +1]
    return []

def sliding_win(str):
    seen = {}
    left = 0 
    max_len = 0 
    for right in str:
# ERROR 1: for right in str
# iterates over characters not indices
# CORRECT: for right in range(len(s))
# then access char via s[right]

        if str[right] in seen and seen[str[right]] >= left:
            left = seen[str[right]] + 1
        seen[str[right]] = right 
# ERROR 2: max_len update outside loop
# same indentation error as first derivation
# INVARIANT: update state every iteration inside loop
    max_len = max(max_len, right - left + 1)
    return max_len

def group_ana(str):
    result = {}
    for word in str:
        word = "".join(sorted(word))
# ERROR 1: word = "".join(sorted(word))
# overwrote the original word with fingerprint
# fingerprint needs its OWN variable
# CORRECT: key = "".join(sorted(word))
        result.append(word)
# ERROR 2: result.append(word)
# result is a dict not a list — dicts don't have append
# CORRECT: result[key].append(word)
# need existence check first or use defaultdict
    return list[result[word]]
# ERROR 3: return list[result[word]]
# list[] is not valid syntax
# word is undefined at return time
# CORRECT: return list(result.values())


"""
The root cause across all 3 recall errors:
two_sum:    sum = left + right     → overwrote array with index math
group_ana:  word = "".join(...)    → overwrote original word with fingerprint
sliding:    for right in str       → iterated chars not indices
```

All three are the same class of error:
INVARIANT: never reuse a variable name for a different purpose
           always name what the variable actually holds
           nums holds numbers, key holds fingerprint, right holds index
"""
