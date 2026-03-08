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