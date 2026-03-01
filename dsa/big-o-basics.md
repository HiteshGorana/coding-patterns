# Big-O & Basics (Interview-Ready Guide)

Using `[TOPIC] = Big-O & Basics`.

## 0) Scope (Checklist)
- [x] Time vs space complexity
- [x] Big-O / Big-Omega / Big-Theta
- [x] Amortized analysis
- [x] Recurrence relations (Master theorem basics)
- [x] Complexity of common operations (array/hash/heap/BST)

## 1) Foundations

### Define Big-O & Basics
Big-O and complexity analysis describe how runtime or memory grows as input size `n` grows.

### Core components / terminology
- Input size `n`
- Primitive operation count
- Worst / average / best case
- Asymptotic notation
- Amortized cost
- Recurrence relation

### Mental model
Ignore machine-specific constants and focus on growth shape as `n` gets large:

`O(1) < O(log n) < O(n) < O(n log n) < O(n^2) < O(2^n) < O(n!)`

## 2) How it works

### Key process with cause-effect reasoning
1. Pick the input variable (`n`, or `n` and `m` if two dimensions exist).
2. Identify dominant operations (comparisons, hash lookups, swaps).
3. Count how often they execute:
   - Sequential blocks add.
   - Nested loops multiply.
   - Halving/doubling loops become logarithmic.
4. Keep dominant term (drop constants and lower-order terms).
5. Analyze space separately (aux arrays, recursion stack, hash maps).

### Relationships between parts
- Changing loop bounds changes operation count directly.
- Better data structures change operation costs (e.g., map lookup vs linear scan).
- Recursion branching/depth jointly determine runtime.

### Tiny worked example with trace
```text
for (i = 1; i <= n; i *= 2)
  for (j = 0; j < n; j++)
    work++
```

For `n = 8`:
- Outer loop values of `i`: `1, 2, 4, 8` -> 4 iterations
- Inner loop each time: 8 iterations
- Total work: `4 * 8 = 32`

Time: `O(n log n)`  
Space: `O(1)`

## 3) Patterns (Interview Templates)

### Common templates
1. Loop counting template
2. Summation template (`sum over iterations`)
3. Recurrence template (`T(n) = aT(n/b) + f(n)`)
4. Amortized template (expensive spikes averaged over many operations)

### Invariants and how to maintain them
- Loop invariant: variable moves monotonically toward stop condition.
- Two-variable analysis invariant: keep `n` and `m` separate.
- Recurrence invariant: correct base case and valid shrink factor.
- Amortized invariant: total work over sequence is bounded.

### Signals this is the right tool
- "Will this scale to large input?"
- "Can we improve from `O(n^2)`?"
- "What is the complexity of this code?"
- "Why is this operation amortized `O(1)`?"

## 4) Examples (Easy -> Medium -> Hard)

### Example 1 (Easy): Triangular nested loop
Problem: Analyze
```text
for i in 0..n-1:
  for j in i..n-1:
    work++
```
Approach: `n + (n-1) + ... + 1 = n(n+1)/2`  
Trace for `n=4`: `4 + 3 + 2 + 1 = 10`  
Complexity: Time `O(n^2)`, Space `O(1)`

ASCII:
```text
Row work counts:
4
3
2
1
```

### Example 2 (Medium): Dynamic array append
Problem: Append `m` values into an array that doubles capacity.

Approach:
- Most appends are `O(1)`.
- Resize steps copy old elements (`O(k)` at that moment).

Trace for `m=8`:
- Copies on growth: `1 + 2 + 4 = 7`
- Direct writes: `8`
- Total: `15` for 8 appends

Result: Worst single append `O(n)`, amortized append `O(1)`.

### Example 3 (Medium): Master theorem
Problem: `T(n) = 2T(n/2) + n`

Approach:
- `a=2`, `b=2`, `n^(log_b a)=n`
- `f(n)=n` matches
- Case 2 -> `T(n)=Theta(n log n)`

### Example 4 (Hard): Data structure choice by operation mix
Problem: Many `insert` and `extract-min` operations.

Approach:
- Unsorted array: insert `O(1)`, extract-min `O(n)`
- Min-heap: insert `O(log n)`, extract-min `O(log n)`

Conclusion: Heap is better when extract-min is frequent.

## 5) Why & What-if

### Edge cases and constraints
- `n = 0` or `n = 1`
- Hash map worst-case collisions can degrade to `O(n)`
- Unbalanced BST can degrade from `O(log n)` to `O(n)`

### Pitfalls and misconceptions
- Treating amortized as same as average-case.
- Mixing `n` and `m` into one variable incorrectly.
- Ignoring recursion stack space.
- Reporting only runtime and forgetting space.

### Why this works (intuition / proof sketch)
As `n -> infinity`, dominant growth terms overshadow constants and lower-order terms, so asymptotic class captures scalability.

### Variations when constraints change
- If recursion split is uneven, simple Master theorem may not apply.
- If pivots are poor, quicksort can degrade to `O(n^2)`.
- If memory is tight, prefer in-place algorithms even with higher time.

## 6) Complexity and Tradeoffs

### Common structure operation costs
| Structure | Access/Search | Insert | Delete | Notes |
|---|---:|---:|---:|---|
| Array | `O(1)` access / `O(n)` search | end amortized `O(1)` / middle `O(n)` | middle `O(n)` | cache friendly |
| Hash map/set | avg `O(1)` | avg `O(1)` | avg `O(1)` | worst `O(n)` |
| Binary heap | top `O(1)` | `O(log n)` | extract-top `O(log n)` | no sorted iteration |
| Balanced BST | `O(log n)` | `O(log n)` | `O(log n)` | keeps order |

### Tradeoffs
- Time vs space: memoization/hash maps speed up at memory cost.
- Precompute vs on-demand: prefix/suffix arrays improve repeated queries.
- Simpler but slower can win for tiny inputs due to constants.

### When to choose alternatives
- Need ordering: BST/heap over hash map.
- Need constant-time membership: hash set over list scan.
- Need contiguous memory speed: array/vector preferred.

## 7) Real-world uses
- Database query planning and join strategy.
- Caching systems (hash maps + eviction structures).
- Task schedulers (heaps for next job selection).
- Capacity planning and scalability forecasting.

## 8) Comparisons

### Big-O vs Big-Omega vs Big-Theta
- Big-O: upper bound
- Big-Omega: lower bound
- Big-Theta: tight bound

### Worst-case vs average-case vs amortized
- Worst-case: bound per operation for any input.
- Average-case: expected cost under a distribution.
- Amortized: guaranteed average over operation sequences.

### Asymptotic analysis vs benchmarking
- Asymptotic: growth trend.
- Benchmarking: real constants, hardware/cache/compiler effects.

## 9) Retention

### Cheat sheet
- Sequential blocks: add costs.
- Nested independent loops: multiply.
- Halving loop: logarithmic.
- Divide-and-conquer: recurrence.
- Drop constants/lower-order terms.
- Report time and space separately.

### Recall cues
- "Depth from shrinking, width from branching."
- "Spikes can still be amortized cheap."
- "Dominant term tells the scaling story."

### 10 practice questions
1. Easy: Analyze `for i in range(n): for j in range(n):`.
2. Easy: Why is binary search `O(log n)`?
3. Easy: Why is vector append amortized `O(1)`?
4. Medium: Solve `T(n) = T(n/2) + 1`.
5. Medium: Solve `T(n) = 2T(n/2) + n`.
6. Medium: Hash map vs BST for membership + ordered output.
7. Medium: Complexity of two-pointer scan on sorted array.
8. Hard: Quicksort best/avg/worst and reason.
9. Hard: Choose array/hash/heap/BST for mixed operation workload.
10. Hard: Analyze `for i=1..n: for j=1..n step i`.
