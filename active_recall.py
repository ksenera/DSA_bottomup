# linked list takes Node as input 
# no head the starting point of the linked list
def linked_list(head):
    # define head no put the parameter into a variable 
    curr = head # save into curr 
    prev = None # None -> A -> B -> C -> D -> None 
    # wanna get D -> C -> B -> A - > None 
    