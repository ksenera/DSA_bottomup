SCAFFOLD
1. CATEGORY:    what type of problem is this?
2. LOCAL:       what does one step/element need to know?
3. BASE CASE:   when do I stop and what do I return?
4. COMBINE:     what do I do with the results?

TREES
category:  depth / value / relationship / path / count
local:     what does one node need to know?
base case: what does None return?
combine:   what do I do with left and right results?

ARRAYS
category:  find / count / optimize / search
local:     what does one element tell me?
base case: empty array or single element returns what?
combine:   reset, accumulate, or compare?

LINKED LIST
category:  traverse / reverse / detect / merge
local:     what does one node need to know?
base case: when curr is None stop
combine:   save next, reverse, slide forward

HASHMAPS
category:  count / group / lookup / existence
local:     what do I store as key, what as value?
base case: key exists or doesn't
combine:   update count or return stored value

TWO POINTERS
category:  pair / partition / palindrome
local:     what do left and right tell me together?
base case: pointers meet or cross
combine:   move left or move right based on comparison

SLIDING WINDOW
category:  substring / subarray with constraint
local:     what does adding/removing one element change?
base case: window size violated
combine:   expand right, shrink left

BINARY SEARCH
category:  find target in sorted / find boundary
local:     is target left or right of midpoint?
base case: left > right means not found
combine:   eliminate half the search space

DYNAMIC PROGRAMMING
category:  optimize / count / exists
local:     what previous result does current depend on?
base case: smallest subproblem answer
combine:   recurrence relation f(n) = f(n-1) + something

GRAPHS
category:  connectivity / path / cycle / traversal
local:     what neighbors haven't I visited?
base case: visited all nodes or found target
combine:   BFS queue or DFS recursive call

Step 1 — what question is this problem asking?
         (value / depth / relationship / path / count)

Step 2 — what does one node need to know?
         (local thinking only, ignore the rest)

Step 3 — what does None return?
         (your base case falls out of this)

Step 4 — what do I do with left and right results?
         (combine, compare, pass up)


print AFTER you have values to show
print BEFORE you return
what do I want to verify at this moment in the code?
how do I generate the right questions from first principles
so I never blank on a new problem?


RECURSIVE TREE 
1. what is the VALUE at each node?     → find_max
2. how far DOWN does this go?          → max_depth
3. are two subtrees RELATED?           → symmetric, same tree
4. what PATH leads somewhere?          → path sum, LCA
5. what is the COUNT of something?     → count nodes, count leaves

QUESTION TYPE: depth / value / relationship / path / count
LOCAL QUESTION: what does one node need to know?
BASE CASE: what does None return and why?
COMBINE: what do I do with left and right?

MY REAL LIFE EXAMPLE:
"okay so this is a depth question — 
how far down does the tree go.

at any single node I only need to know 
how deep my left side is and how deep my right side is.

if I hit None that's depth zero — nothing there.

then I return 1 plus whichever side is deeper."