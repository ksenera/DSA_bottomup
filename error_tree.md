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