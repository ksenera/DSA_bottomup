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

# happy path i have a word gets sorted and gives me group of words 
# that are anagrams of og word 
# assert group_anagrams(word) = [group] WRONG — = is assignment
# assert group_anagrams(word) == [group] RIGHT - == comparison

def group_anagrams_copy(strs):        # strs here = PARAMETER
                                  # it's a placeholder name
                                  # caller passes the actual value

    strs = ["eat","tea","tan"]   # this OVERWRITES the parameter
                                  # now strs always = this hardcoded list
                                  # your assert input gets ignored


# Delete that line inside the function. 
# The parameter `strs` already holds whatever you pass in 
# via the assert.

#anchor: "store while scanning, retrieve in O(1)"
#key invariant: sorted(word) = fingerprint
#mechanics: "".join(sorted(word)), list(result.values())

#leetcode 49 Medium 
def group_anagrams(strs):
    result = {} 
    for word in strs:
        key = "".join(sorted(word))
        if key not in result:
            result[key] = [] 
        result[key].append(word)
    print(result)
    # to get list of lists I need values 
    # return result[] WRONG
    return list(result.values())


assert group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]) == [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
assert group_anagrams(["bat", "cat", "rat"]) == [["bat"], ["rat", "art"], ["cat", "act"]]
assert group_anagrams([]) == []

# March 11 2026
# ─────────────────
# PROBLEM
# Group Anagrams — implementation

# ERROR 1
# WHAT I WROTE: key = word.join(sorted(word))
# WHAT WAS WRONG: word becomes the separator
# FIX: "".join(sorted(word)) — empty string = no separator
# CONNECT: same mistake pattern as node.left vs max_value(node.left)
#           — used the object itself instead of operating on it

# ERROR 2
# WHAT I WROTE: assert result == [["eat"],["tea"]...]
# WHAT WAS WRONG: dict output order not guaranteed
# FIX: print + visual verify for grouping problems
# ─────────────────