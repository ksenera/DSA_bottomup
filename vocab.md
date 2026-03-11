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