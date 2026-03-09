list = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

curr_sum = 0 
best_sum = 0 

for i in list:
    curr_sum += i
    if curr_sum <= 0:
        curr_sum = 0
    else:
        best_sum = curr_sum
        
        print(best_sum) 

