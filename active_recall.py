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

