"""
HASH MAP FAMILY SCAFFOLD
ITERATIVE 
QUESTION TYPE: grouping / counting / lookup
WHAT DO I TRACK: what information needs to be stored?
KEY: what do I use as the key?
VALUE: what do I store as the value?
COMBINE: how do I build the answer from the map?
INPUT TYPE:  what the function receives
OUTPUT TYPE: what the function returns

NOTES: 
- in python dict equality ignores insertion order 
{"e":1, "a":1, "t":1} == {"t":1, "e":1, "a":1}  # True
"""
# sorted(word) = the key that groups all anagrams together
# KEY:   sorted(word)          → "aet"
# VALUE: list of words → ["eat", "tea", "ate"]

# QUESTION TYPE: grouping 
# WHAT DO I TRACK: track unique identifier and store the group into the key
# KEY: is the fingerprint sorted word 
# VALUE: the list of words that can be made from sorted word
# COMBINE: first i get the word. then i sort it. then join back 
# TRANSLATE: need to check is key exists first then append to it 
# INPUT list of strings
# OUTPUT list of groups where each group is a list of anagrams.

# if char in counts:
#   counts[char] += 1
# else:
#   counts[char] = 0 

# invariant is check existence before updating

def group_anagrams():
    pass 

#happy path i have a word gets sorted and gives me group of words that are anagrams of og word 
# assert group_anagrams(word) = [group] WRONG — = is assignment
# assert group_anagrams(word) == [group] RIGHT - == comparison

#leetcode 49 Medium 
def group_anagrams(strs: List[str]) -> List[List[str]]:
    pass 

assert group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]) == [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]