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