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
    = at every push i know what curr_min is. 2nd stack stores min at each step in parallel
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
push(val):  append val to main stack
            append min(val, curr top of min_stack) to min_stack 
            if min_stack = [] append val directly 
pop():      remove last element from main stack
            remove last element from min_stack
top():      return last element of main stack 
getMin():   return last element of min stack 
TRANSLATE: 
append => self.stack.append(val)
remove last => self.stack.pop()
last element => self.stack[-1]
min of two => min(a,b)
empty check => if not self.stack 
"""

class MinStack:
    def __init__(self):
        self.stack = [] # main stack
        self.min_stack = [] # parallel stack that only tracks minimums
    def push(self, value):
        self.stack.append(value) # stack is list type which has append as method
        # if self.min_stack == []: WRONG
        #     self.min_stack.append(value) WRONG
        # self.min_stack.min(value, self.min_stack.top()) WRONG
        if not self.min_stack:
            self.min_stack.append(value)
        else:
            self.min_stack.append(min(value, self.min_stack[-1]))
    def pop(self):
        self.stack.pop() # uses list's pop
        self.min_stack.pop()
    def top(self):
        # WRONG return self.stack[-1] and self.min_stack[-1]
        # gives access to stack thru self and -1 last index on list
        return self.stack[-1]
    def getMin(self):
        # WRONG return min(self.min_stack.top())
        return self.min_stack[-1]
    
ms = MinStack()
ms.push(-2)
# WRONG print(f"ms={ms}")
print(f"ms={ms.stack}, min={ms.min_stack}")
ms.push(0)
print(f"ms={ms.stack}, min={ms.min_stack}")
ms.push(-3)
print(f"ms={ms.stack}, min={ms.min_stack}")
assert ms.getMin() == -3
ms.pop()
print(f"ms={ms.stack}, min={ms.min_stack}")
assert ms.top() == 0 
assert ms.getMin() == -2 




"""
    BUGS 
    1) min_stack append logic 
    self.min_stack.min(value, self.min_stack.top())
    .min() and .top() don't exist on list

    2) return self.stack[-1] and self.min_stack[-1]  # returns both

    3) return min(self.min_stack.top())  # .top() doesn't exist on list
"""
