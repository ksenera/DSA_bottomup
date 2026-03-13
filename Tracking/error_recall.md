# March 12 2026 — ACTIVE RECALL REP 2
─────────────────────────────────────
TWO POINTERS — two_sum
ERROR 1: sum = left + right
overwrote input array with index arithmetic
INVARIANT: left and right are INDICES into the array
actual sum = nums[left] + nums[right]

ERROR 2: return list[left, right]
list[] is not valid syntax
CORRECT: return [left, right] or return [left+1, right+1] if 1-indexed

ERROR 3: sum < target → right -= 1
WRONG DIRECTION
if sum too small → need bigger values → move LEFT pointer right
if sum too big → need smaller values → move RIGHT pointer left
INVARIANT: squeeze inward based on comparison to target

SLIDING WINDOW — sliding_win
ERROR 1: for right in str
iterates over characters not indices
CORRECT: for right in range(len(s))
then access char via s[right]

ERROR 2: max_len update outside loop
same indentation error as first derivation
INVARIANT: update state every iteration inside loop

GROUP ANAGRAMS — group_ana
ERROR 1: word = "".join(sorted(word))
overwrote the original word with fingerprint
fingerprint needs its OWN variable
CORRECT: key = "".join(sorted(word))

ERROR 2: result.append(word)
result is a dict not a list — dicts don't have append
CORRECT: result[key].append(word)
need existence check first or use defaultdict

ERROR 3: return list[result[word]]
list[] is not valid syntax
word is undefined at return time
CORRECT: return list(result.values())
─────────────────────────────────────