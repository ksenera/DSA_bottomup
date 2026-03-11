# DSA_bottomup

A bottom-up algorithm learning system built on deductive reasoning,
not pattern memorization. Derive invariants from first principles,
compress to anchor sentences, encode through spaced active recall.

---

## Structure

- Encoding/    → recall from anchor only. no reference. blank reconstruction.
- Practice/    → first derivation. scaffold → translate → implement.
- Reference/   → notes, vocab, archetypes. read only during derive phase.
- Tracking/    → session state, transfer log. update after each session.

---

## Encoding/
- active_recall.py     → blank IDE recall sessions (no reference allowed)
- test_recall.py       → original implementations with inline error logs
- transfer_learning.py → signal/prediction/family log for new problems

## Practice/
- array.py             → array family problems
- dict.py              → dictionary/counting problems  
- group_anagrams.py    → LC49 HashMap grouping (derived, passing)
- reverse_list.py      → LC206 linked list reversal (derived, passing)
- sliding_window.py    → LC3 longest substring (derived, passing)
- stack.py             → LC155 Min Stack (in progress)
- tree.py              → LC104 max depth, LC100 max value, LC101 symmetric
- two_pointers.py      → LC167 Two Sum II (pending)

## Reference/
- notes.md             → all family scaffolds, anchor sentences, 
                         recognition signals, assert types, translate step
- vocab.md             → Python mechanics: join, sorted, defaultdict,
                         f-strings, dict patterns
- algo_archetype.md    → compressed archetype cards (in progress)

## Tracking/
- session_state.md     → current target, locked families, deadlines
- error_tree.md        → tree-specific mistake log
- transfer_learning.md → transfer problem log

---

## Progress
Locked:   HashMap, LinkedList, Trees (depth/value/symmetric), 
          TwoPointers, SlidingWindow
Current:  Stack → LC155 Min Stack
Next:     Backtracking → LC22 Generate Parentheses
Pending:  Two Sum II, Max Subarray, Kadane's active recall reps

---

## Method
problem → plain English → invariant → scaffold → translate → implement
anchor sentence per family → encode through blank IDE recall → transfer
