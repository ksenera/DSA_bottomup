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