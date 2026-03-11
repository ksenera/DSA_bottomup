# PYTHON MECHANICS NOTE
List, Dict, Tuple from typing module = type hints only
Python built-ins: list, dict, tuple (lowercase) = actual types
List[str] is just telling the reader what type to expect
list is the actual object you create and use
from typing import List → only needed if you use capital List

# Group Anagrams 
# VOCAB LOG
- "".join(sorted(word))   → sort string, no separator
- list(result.values())   → all dict values as list
- defaultdict(list)       → auto-initializes missing keys to []


# Sliding Window
# VOCAB LOG
- seen = {}  vs  seen = 0
- f"label={variable}"
- right - left + 1  for window size
- max_len tracking variable
- indentation — update every iter vs only on break
# DEBUGGING
- print(f"label={variable}")   → print variable value with label
variable gets evaluated, label is just text
So whatever you want to see, name it and put the variable after `=` inside `{}`
print AFTER you have values, BEFORE you return