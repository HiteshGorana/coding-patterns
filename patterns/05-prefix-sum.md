# Pattern 05: Prefix Sum

## Diagram + Intuition

### Pattern Diagram
```text
prefix[i] = sum of [0..i-1]
range(l,r) = prefix[r+1] - prefix[l]
```

### Read-the-Question Trigger Cues
- Many range sum queries.
- Count subarrays with target sum.

### Intuition Anchor
- "Convert every range to subtraction of two checkpoints."

### 3-Second Pattern Check
- Can I precompute cumulative state once and answer ranges quickly?

## What This Pattern Solves
Prefix sums convert repeated range-sum queries from linear to constant time.

## Recognition Signals
- Multiple queries on subarray sums/ranges.
- Need count of subarrays matching a condition on sums.
- Brute force recomputes sums repeatedly.

## Core Intuition
Define `prefix[i]` as sum of elements before index `i` (exclusive).  
Then any range sum can be computed as:
`sum(l..r) = prefix[r + 1] - prefix[l]`

For counting subarrays with target sum, store past prefix frequencies in a hash map.

## Step-by-Step Method (Range Query Form)
1. Build `prefix` array of size `n + 1`.
2. For each query `[l, r]`, compute difference in `O(1)`.

## Step-by-Step Method (Count Subarrays Sum = K)
1. Maintain running prefix sum `curr`.
2. For each element, needed prior prefix is `curr - k`.
3. Add `freq[curr - k]` to answer.
4. Increment `freq[curr]`.

## Detailed Example (Subarray Sum Equals K)
`nums = [1, 2, 3], k = 3`
1. Start `freq = {0: 1}`, `curr = 0`, `ans = 0`.
2. Read `1`: `curr=1`, need `-2`, not found. Add `freq[1]`.
3. Read `2`: `curr=3`, need `0`, found once -> `ans=1`. Add `freq[3]`.
4. Read `3`: `curr=6`, need `3`, found once -> `ans=2`.

## Complexity
- Build prefix: `O(n)`
- Query each range: `O(1)`
- Counting subarrays via hash map: `O(n)` time, `O(n)` space

## Python Template
```python
def count_subarrays_sum_k(nums, k):
    freq = {0: 1}
    curr = 0
    ans = 0

    for x in nums:
        curr += x
        ans += freq.get(curr - k, 0)
        freq[curr] = freq.get(curr, 0) + 1

    return ans
```

## Common Pitfalls
- Mixing inclusive/exclusive prefix indexing.
- Forgetting initial `freq[0] = 1`, which counts subarrays starting at index `0`.
- Using sliding window when negative numbers exist (window fails, prefix works).

## Variations
- 2D prefix sum for matrix range queries.
- Prefix XOR for XOR-range problems.
- Balance encoding (e.g., map `0 -> -1`) for equal counts.
- Difference array for range updates.

## Interview Tips
- Mention both forms: "prefix array for queries" and "prefix + hash for counting."
- Explicitly justify why negative numbers still work with prefix-hash.
- Show formula before coding to avoid index mistakes.

## Practice Problems
- Range Sum Query - Immutable
- Subarray Sum Equals K
- Continuous Subarray Sum
- Contiguous Array
