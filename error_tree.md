# March 9 2026
# ─────────────────
# PROBLEM
# is_symmetric — reasoning step before rep

# ERROR
# WHAT I SAID
# "we are checking depth not value"

# WHAT WAS WRONG
# Symmetric = mirror in both structure AND values
# Depth is irrelevant — a tall symmetric tree is still symmetric

# WHY IT HAPPENED
# Confused "we need to traverse levels" with "depth is the thing being checked"
# Traversal mechanism ≠ what you're measuring

# INVARIANT
# Any time a problem asks about RELATIONSHIPS between nodes
# you must check BOTH structure (does the node exist?) AND value (what does it hold?)
# Structure alone = shape comparison
# Value alone = ignores missing nodes
# You need both
# ─────────────────


# March 10 2026 15:11 pm 
# ─────────────────
# PROBLEM
# is_symmetric — function signature design

# ERROR
# WHAT I DID
# def is_symmetric(left, right): pass
# assert is_symmetric(None, None) == True
# assert is_symmetric(node1) == False
# assert is_symmetric(8, 9) == False

# WHAT WAS WRONG
# 3 different call signatures for the same function — inconsistent
# Passed raw integers instead of Node objects
# Mixed up the outer public function with the inner helper signature
# Likely bled in from two_sum(left, right) which genuinely takes two params

# WHY IT HAPPENED
# two_sum operates on two INDICES into an array — two params is correct there
# is_symmetric operates on one ROOT — the two-node comparison is internal
# Both problems involve comparing two things
# But WHERE the two things live is different:
#   two_sum: caller provides both
#   is_symmetric: caller provides root, YOU split into left/right internally

# INVARIANT
# When a problem gives you ONE data structure to analyze → 1 param outer function
# When a problem gives you TWO independent inputs to compare → 2 params
# If you need to compare two things internally, that's a helper, not the public API
# Raw primitives (8, 9) cannot be passed where Node objects are expected
# Always instantiate Node objects for tree assertions
# ─────────────────