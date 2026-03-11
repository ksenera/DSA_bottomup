"""
SLIDING WIN:  "expand right until broken, shrink left until fixed"

contiguous subarray + constraint → sliding window 

PREDICTION:  sliding window? hashmap? two pointers?
SIGNAL:      what in the problem description triggered that?
FAMILY:      confirmed archetype
CATEGORY:    specific to this problem

CATEGORY:  longest substring with constraint
LOCAL:     is this character already in my window?
BASE CASE: empty string → return 0
COMBINE:   expand right, shrink left, track max length
INPUT:     string s
OUTPUT:    integer — length of longest valid window
TRANSLATE:
  "right moves forward"         → for r in range(len(s))
  "repeat found"                → if s[r] in seen and seen[s[r]] >= left
  "shrink left past repeat"     → left = seen[s[r]] + 1
  "store position"              → seen[s[r]] = r
  "track max"                   → max_len = max(max_len, r - left + 1)

# DETERMINISTIC OUTPUT → strict assert
- linked list, trees, two pointers, sliding window
- assert reverse_list(head) == expected
"""


# LC 3 — Longest Substring Without Repeating Characters
# Given a string s, find the length of the longest substring without repeating characters.

# signal => contiguous subarray = longest substr 
# signal => constraint = with/o repeating chars
# prediction => must be sliding window problem 
# family => confirmed archetype sliding window 


"""
PREDICTION:  slide window
SIGNAL:      longest substr && w/o repeating chars == contiguous && constraint
FAMILY:      sliding window
CATEGORY:    longest substr with constraint 
LOCAL:       what does one character tell me as right moves forward?
             it tells me if it exists or not
BASE CASE:   "" == 0
INPUT:       the whole string
OUTPUT:      length of longest substr 

COMBINE:     as right moves forward, left must fix window 
             if constraint broken aka char repeated
             what has to happen physically step by step 
             for this one sentence to be true?

TRANSLATE:   one sentence per line 
            "right moves forward"     → that's one action
            "check constraint"        → is the char already seen?
            "constraint broken"       → where was it last seen?
            "fix window"              → move left past it
            "track best"              → record max length after each valid window

            "right moves forward one char at a time"  → for r in range(len(s))
            "char already in window"                  → seen y/n 
            "move left past the repeat"               →
            "update char position"                    →
            "track longest window seen"               →
"""
def long_substr(s):
    seen = 0 # track if char was seen at beginning no chars seen so init to 0
    for r in range(len(s)): # right moves forward 
        pass 

# all happy path as there is string and returned the length aka does this character exist
assert long_substr("abcabcbb") == 3
assert long_substr("bbbbb") == 1
assert long_substr("pwwkew") == 3 

# base case empty string return 0 
assert long_substr("") == 0 
