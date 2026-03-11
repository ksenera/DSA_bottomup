"""
ANCHOR STATEMENT
    STACK: "last in, first out — what did I just push?"
"""

"""
LC 155 — Min Stack
Design a stack that supports push, pop, top, and retrieving 
the minimum element in constant time O(1).
Implement the MinStack class:
    MinStack() initializes the stack object
    void push(int val) pushes the element val onto the stack
    void pop() removes the element on the top of the stack
    int top() gets the top element of the stack
    int getMin() retrieves the minimum element in the stack

Input:
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output:
[null,null,null,null,-3,null,0,-2]
"""

# PREDICTION:  stack problem where i put a plate on top. 
#              then remove plate from top and get the plate number from top.
#              then find plate with smallest number.
# SIGNAL:      "push", "pop", "top"
#              getMin in O(1)
# INPUT:       class, push/pop, top and getMin - WRONG
# OUTPUT:      nulls for class and stack operations push and pop. - WRONG
"""
for LC155 i have to design a data structure. INSTEAD OF INPUT/OUTPUT ASK
WHAT OPERATIONS must this support?
- class needs to: 
    - add element to stack
    - remove element to stack
    - find minimum in stack without rechecking whole stack
    - get top element from stack 
WHAT DO I TRACK internally to make each operation work?
- track value of elements to know minimum element 

--> if i push [-2, 0, -3] in that order then pop -3 i have [-2, 0] new min is -2
--> how do i know the previous minimum after a pop?
--> what do i need to track to answer that in O(1) without scanning whole stack
    = track value of elements to know minimum element 
--> what should that second list track at each push so that when i pop, ik new min. 
    = at every push i know what curr_min is. 2nd stack stores min at each step in para
--> when you pop from main stack you also pop from min stack. what left on top of min stack?
    = the minimum that was tracked up until the last operation
"""
#              int for plate with smallest number and plate# on top
# FAMILY:      STACK
# CATEGORY:    find minimum element aka integer in stack 
# LOCAL:
# TRACKING:       
# BASE CASE:   empty stack return null => [] == null
# COMBINE:     
# TRANSLATE:


"""
WHAT OPERATIONS:
                - push(int val), pop(), top(), getMin()
WHAT DO I TRACK:
                - self.stack = [] # main stack
                - self.min_stack = [] # parallel min stack, top always = curr_min
                main stack: [-2, 0, -3] -> pop -> [-2, 0]
                min stack: [-2, -2, -3] -> pop -> [-2, -2] <-- top = -2 = curr_min
push: 

pop:
top: 
getMin:
TRANSLATE: 
"""