# Pattern 01: Hash Map / Set Lookup

## Diagram + Intuition

### Pattern Diagram
```text
for x in items:
  need info about x?
    -> check map/set in O(1)
  then update map/set
```

### Read-the-Question Trigger Cues
- "duplicate", "frequency", "first unique", "pair sum"
- Brute force would compare many pairs.

### Intuition Anchor
- "I need memory of what I have already seen."

### 3-Second Pattern Check
- Can I answer faster if I store `value -> count/index/state`?

## What This Pattern Solves
Use this pattern when you need constant-time lookups for values you have already seen.  
It is the default pattern for:
- duplicate detection
- counting frequency
- reverse lookup (`value -> index`)
- complement matching (`target - x`)

## Recognition Signals
- Problem asks: "contains duplicate", "first unique", "count occurrences", "find pair summing to target".
- Brute force is `O(n^2)` from nested comparisons.
- You can solve by remembering prior elements while scanning once.

## Core Intuition
Trade extra memory for speed.  
Instead of repeatedly searching the array/string, store useful facts in a hash table:
- set for membership (`seen`)
- map for counts (`freq[x]`)
- map for metadata (`last_index[x]`, `first_position[x]`)

## Step-by-Step Method
1. Decide what the hash structure should store.
2. Traverse input once from left to right.
3. Before inserting the current value, check whether required information already exists.
4. Update structure with current value.
5. Return answer as soon as condition is met (when allowed).

## Detailed Example (Two Sum)
Given `nums = [2, 7, 11, 15], target = 9`:
1. Start with empty map `index_of`.
2. At `2`, complement is `7`, not in map. Store `index_of[2] = 0`.
3. At `7`, complement is `2`, found in map at index `0`.
4. Return `[0, 1]`.

This avoids checking all pairs and runs in one pass.

## Complexity
- Time: `O(n)` average
- Space: `O(n)`

## Python Template
```python
def solve(nums, target):
    info = {}  # value -> index/count/metadata

    for i, x in enumerate(nums):
        need = target - x
        if need in info:
            return [info[need], i]
        info[x] = i

    return []
```

## Common Pitfalls
- Updating map before checking complement can break cases with same element reuse.
- Forgetting collisions are abstracted by language runtime, but worst-case can degrade.
- Misusing set when frequency count is required (set loses multiplicity).
- Returning values instead of indices when prompt asks indices.

## Variations
- Frequency table with `dict`/`Counter` for anagrams, mode, grouping.
- Set-based dedupe when only presence matters.
- Prefix-sum hash map for subarray-sum problems.
- Character map for string window constraints.

## Interview Tips
- Start with brute force `O(n^2)`, then say: "We can cut repeated scans with a hash map."
- Explicitly state what key/value represent.
- Mention average `O(1)` hash operations and `O(n)` space tradeoff.

## Practice Problems
- Two Sum
- Contains Duplicate
- Valid Anagram
- First Unique Character in a String
- Subarray Sum Equals K
