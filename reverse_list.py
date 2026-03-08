def reverse_list(head):
    prev = None 
    curr = head 

    while curr is not None:
        print(f"prev={prev.val if prev else None}, curr={curr.val}, next={curr.next.val if curr.next else None}")
        next_node = curr.next # next is a property of the current node we are standing on
        curr.next = prev
        prev = curr 
        curr = next_node 
        print(f" after flip: prev={prev.val}, curr={curr.val if curr else None}")

        #prev=None, curr=A, next=B
 #after flip: prev=A, curr=B
#prev=A, curr=B, next=c
 #after flip: prev=B, curr=c
#prev=B, curr=c, next=D
 #after flip: prev=c, curr=D
#prev=c, curr=D, next=None
 #after flip: prev=D, curr=None

    return prev 


class Node:
    def __init__(self, val):
        self.val = val 
        self.next = None 

a = Node("A")
b = Node("B")
c = Node("c")
d = Node("D")

a.next = b 
b.next = c 
c.next = d 

result = reverse_list(a)