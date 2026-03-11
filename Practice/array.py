list = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

curr_sum = 0 
best_sum = 0 

#for i in list:
    #curr_sum += i
    #if curr_sum <= 0:
        #curr_sum = 0
    # Also the best_sum = curr_sum should not be 
    # inside the else. It should be independent. 
    # What if curr_sum is positive but you just 
    # reset it? you'd miss updating best_sum
    
    #else:
        #best_sum = curr_sum
        
        #print(best_sum) 

# cleaner version 
for i in list:
    curr_sum += i
    if curr_sum < 0:
        curr_sum = 0
    if curr_sum > best_sum:
        best_sum = curr_sum
    print(f"i={i}, curr_sum={curr_sum}, best_sum={best_sum}")

print(best_sum)


# March 9 2026
# ─────────────────
# PROBLEM
# Maximum subarray sum (Kadane's algorithm)

# WHAT I WROTE
# if curr_sum <= 0:
#     curr_sum = 0
# else:
#     best_sum = curr_sum

# WHAT WAS WRONG
# Linked reset and update together in if/else
# best_sum only updated when curr_sum was positive
# but if curr_sum was positive and just reset
# best_sum would never get updated

# WHY IT HAPPENED
# Treated two independent decisions as one decision
# Reset condition and best tracking are separate things
# that both happen every iteration regardless of each other

# THE INVARIANT
# If two things need to happen every iteration
# they are two separate if statements not if/else
# if/else means only one of them ever runs
# two ifs means both always get checked

# REAL WORLD CONNECTION
# Bank account daily changes
# Running total goes negative = losing streak = cut it
# best_sum = best streak you ever had

# QUESTIONS TO ASK FOR ANY SUBARRAY PROBLEM
# 1. Is there a condition where I reset?
# 2. Do I need the best version of the running total?
# ─────────────────