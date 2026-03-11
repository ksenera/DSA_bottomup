"""
SLIDING WIN:  "expand right until broken, shrink left until fixed"

contiguous subarray + constraint → sliding window 

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
