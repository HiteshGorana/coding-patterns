# Prefix Sum: A Deep Dive

---

## 1. What Is It? (Definition & Core Components)

A **prefix sum** (also called a cumulative sum or scan) is a precomputed array where each element stores the sum of all original elements from the beginning of the array up to and including that position. Once built, it answers "what is the sum of elements between index L and R?" in **O(1)** — regardless of array size or query range.

```
ORIGINAL ARRAY:
  index:  0    1    2    3    4    5
  arr:   [3,   1,   4,   1,   5,   9]

PREFIX SUM ARRAY:
  index:  0    1    2    3    4    5
  pre:   [3,   4,   8,   9,  14,  23]

  pre[0] = 3                     (just arr[0])
  pre[1] = 3 + 1 = 4             (arr[0..1])
  pre[2] = 3 + 1 + 4 = 8        (arr[0..2])
  pre[3] = 3 + 1 + 4 + 1 = 9    (arr[0..3])
  pre[4] = 3 + 1 + 4 + 1 + 5 = 14  (arr[0..4])
  pre[5] = 3 + 1 + 4 + 1 + 5 + 9 = 23  (arr[0..5])

RANGE QUERY sum(L=1, R=4):
  = pre[4] - pre[0]
  = 14 - 3
  = 11   ✅  (1 + 4 + 1 + 5 = 11)
```

**Core components:**

- **Original array** — the input data whose range sums you want to query
- **Prefix sum array** — the precomputed auxiliary array; `pre[i]` = sum of `arr[0..i]`
- **Build phase** — one O(n) pass to construct the prefix sum array from the original
- **Query phase** — the O(1) subtraction formula that answers any range sum
- **The recurrence** — `pre[i] = pre[i-1] + arr[i]` — each prefix sum is the previous one plus the current element
- **The query formula** — `sum(L, R) = pre[R] - pre[L-1]` — the algebraic core of the technique

The entire power of prefix sum comes from one insight: **the sum of a range is the difference of two cumulative totals**. Build the totals once, answer any question instantly.

---

## 2. The Physical Analogy: Odometer Readings

Imagine a car driving a route with checkpoints, and the odometer records total distance traveled from the start:

```
CHECKPOINTS:
  City A → City B → City C → City D → City E → City F

DISTANCES BETWEEN CITIES (arr):
  A→B: 3km    B→C: 1km    C→D: 4km    D→E: 1km    E→F: 5km

ODOMETER READINGS at each city (prefix sum):
  At A: 0km   (start)
  At B: 3km
  At C: 4km
  At D: 8km
  At E: 9km
  At F: 14km

QUESTION: How far is it from City C to City E?

  Distance(C→E) = Odometer(E) - Odometer(C)
                = 9km - 4km
                = 5km ✅   (4 + 1 = 5, verified)
```

You don't re-drive the route to measure the C→E distance. You subtract two **already-recorded** odometer readings. This is exactly prefix sum: **precompute the running total so any sub-journey distance is a single subtraction**.

The odometer analogy captures all key properties:
- Odometer readings are monotonically increasing (for positive distances)
- Subtracting two readings gives the distance between them
- You record readings once; queries are free thereafter
- The odometer doesn't know in advance which sub-journey you'll ask about — it records everything, making all queries possible

---

## 3. The Algebraic Foundation

The query formula isn't magic — it's pure algebra:

```
DEFINITION:
  pre[i] = arr[0] + arr[1] + ... + arr[i]

RANGE SUM sum(L, R) = arr[L] + arr[L+1] + ... + arr[R]

ALGEBRAIC DERIVATION:
  pre[R]   = arr[0] + arr[1] + ... + arr[L-1] + arr[L] + ... + arr[R]
  pre[L-1] = arr[0] + arr[1] + ... + arr[L-1]

  pre[R] - pre[L-1] = arr[L] + arr[L+1] + ... + arr[R]
                    = sum(L, R)  ✅

VISUAL PROOF:

  pre[R]:   [████████████████████████████████████]
             arr[0]...arr[L-1] | arr[L]...arr[R]
                  ↑ cancel this ↑

  pre[L-1]: [████████████████]
             arr[0]...arr[L-1]

  Difference: [████████████████]
               arr[L]...arr[R]    ← exactly the range we want
```

```
THE L=0 EDGE CASE:
  sum(0, R) = arr[0] + arr[1] + ... + arr[R] = pre[R]

  Formula: pre[R] - pre[L-1] = pre[R] - pre[-1]
  But pre[-1] doesn't exist!

  COMMON FIX — 1-indexed prefix sum array:
    pre[0] = 0  (sentinel: "sum of zero elements")
    pre[i] = pre[i-1] + arr[i-1]   for i = 1..n

    Query sum(L, R) (1-indexed):
      = pre[R] - pre[L-1]
      Works for L=1: pre[R] - pre[0] = pre[R] - 0 = pre[R] ✅

  This sentinel approach eliminates ALL edge cases cleanly.
  Most implementations use 1-indexed prefix sums for this reason.
```

---

## 4. Build and Query Implementation

### Standard (0-indexed)

```python
def build(arr):
    n = len(arr)
    pre = [0] * n
    pre[0] = arr[0]
    for i in range(1, n):
        pre[i] = pre[i-1] + arr[i]    # recurrence: each = previous + current
    return pre

def query(pre, L, R):
    if L == 0:
        return pre[R]                  # edge case: L=0, no subtraction needed
    return pre[R] - pre[L-1]          # general case
```

### Sentinel (1-indexed) — Recommended

```python
def build(arr):
    n = len(arr)
    pre = [0] * (n + 1)               # pre[0] = 0 sentinel
    for i in range(1, n + 1):
        pre[i] = pre[i-1] + arr[i-1]
    return pre

def query(pre, L, R):                 # L, R are 0-indexed into original arr
    return pre[R+1] - pre[L]          # shift indices for 1-indexed pre

# OR equivalently (if L, R are 1-indexed):
def query(pre, L, R):
    return pre[R] - pre[L-1]          # always works, including L=1
```

```
BUILD TRACE for arr = [3, 1, 4, 1, 5, 9]:

  i=0: pre[0] = 0                     (sentinel)
  i=1: pre[1] = pre[0] + arr[0] = 0 + 3 = 3
  i=2: pre[2] = pre[1] + arr[1] = 3 + 1 = 4
  i=3: pre[3] = pre[2] + arr[2] = 4 + 4 = 8
  i=4: pre[4] = pre[3] + arr[3] = 8 + 1 = 9
  i=5: pre[5] = pre[4] + arr[4] = 9 + 5 = 14
  i=6: pre[6] = pre[5] + arr[5] = 14 + 9 = 23

  pre = [0, 3, 4, 8, 9, 14, 23]
         ↑
       sentinel

QUERY sum(1, 4) [0-indexed, arr[1..4] = 1+4+1+5 = 11]:
  = pre[5] - pre[1]   (using 1-indexed pre with shift)
  = 14 - 3
  = 11 ✅
```

---

## 5. The Complexity Transformation

```
WITHOUT PREFIX SUM:

  Build:        O(1)  (no preprocessing)
  Single query: O(n)  (sum elements L through R)
  k queries:    O(k×n)

  For n=10,000 and k=10,000 queries:
    10,000 × 10,000 = 100,000,000 operations

WITH PREFIX SUM:

  Build:        O(n)  (one pass)
  Single query: O(1)  (one subtraction)
  k queries:    O(n + k)

  For n=10,000 and k=10,000 queries:
    10,000 + 10,000 = 20,000 operations

SPEEDUP: 100,000,000 / 20,000 = 5,000× faster ✅

BREAK-EVEN POINT:
  Prefix sum is worth it when: O(n + k) < O(k × n)
  n + k < k × n
  n < k × n - k = k(n-1)
  n/(n-1) < k
  For large n: k > ~1 query makes prefix sum worthwhile

In practice: almost always worth it if you have ≥ 2 range queries.
```

---

## 6. 2D Prefix Sum

The technique extends naturally to two dimensions, enabling O(1) sum queries over any rectangular subarray.

### Building the 2D Prefix Sum

```
ORIGINAL 2D GRID:
  arr[i][j]:
  1  2  3
  4  5  6
  7  8  9

PRE[i][j] = sum of all elements in rectangle from (0,0) to (i-1, j-1)
  (1-indexed, so pre[0][*] = pre[*][0] = 0)

BUILDING PRE:
  pre[i][j] = arr[i-1][j-1]        (current element)
            + pre[i-1][j]          (sum above)
            + pre[i][j-1]          (sum to left)
            - pre[i-1][j-1]        (remove double-counted top-left)

INCLUSION-EXCLUSION VISUALIZATION:

  pre[i-1][j]:   ████████     (rectangle above current row)
  pre[i][j-1]:      ████████  (rectangle left of current col)
  These two overlap at: pre[i-1][j-1]  ← counted twice, subtract once
  Add: arr[i-1][j-1]  ← the current cell itself

BUILD TRACE (1-indexed):

  pre:    0  0  0  0
          0  1  3  6
          0  5 12 21
          0 12 27 45

  pre[2][2] = arr[1][1] + pre[1][2] + pre[2][1] - pre[1][1]
            = 5 + 3 + 5 - 1 = 12 ✅
  (Sum of top-left 2×2: 1+2+4+5 = 12)
```

### Querying a 2D Rectangle

```
QUERY: Sum of rectangle from (r1,c1) to (r2,c2) (0-indexed original)
  = pre[r2+1][c2+1]
  - pre[r1][c2+1]
  - pre[r2+1][c1]
  + pre[r1][c1]

VISUAL (inclusion-exclusion):

  pre[r2+1][c2+1]: ████████████████   (entire top-left rectangle to (r2,c2))
  pre[r1][c2+1]:   ████████           (strip above the query rectangle)
  pre[r2+1][c1]:   ████               (strip left of the query rectangle)
  pre[r1][c1]:     ██                 (top-left corner, subtracted twice → add back)

  Result: ████████                    (the query rectangle) ✅

EXAMPLE: Sum of center 2×2 [(1,1) to (2,2)] in:
  1  2  3
  4  5  6
  7  8  9

  = pre[3][3] - pre[1][3] - pre[3][1] + pre[1][1]
  = 45 - 6 - 21 + 1
  = 19 ✅  (5+6+8+9 = 28... wait)

  Let me recount: (1,1)=5,(1,2)=6,(2,1)=8,(2,2)=9 → 5+6+8+9=28

  Recheck pre build:
  pre[3][3]=45, pre[1][3]=6, pre[3][1]=12, pre[1][1]=1
  = 45 - 6 - 12 + 1 = 28 ✅
```

---

## 7. Prefix Sum for Non-Sum Queries

The prefix sum idea generalizes beyond summation to any **associative and invertible** operation.

### Prefix XOR

```
ORIGINAL: [3, 1, 4, 1, 5]
PREFIX XOR: [3, 2, 6, 7, 2]
  pre_xor[i] = arr[0] XOR arr[1] XOR ... XOR arr[i]

RANGE XOR(L, R):
  = pre_xor[R] XOR pre_xor[L-1]
  (XOR is its own inverse: a XOR a = 0)

WHY IT WORKS:
  pre_xor[R]   = a[0] XOR ... XOR a[L-1] XOR a[L] XOR ... XOR a[R]
  pre_xor[L-1] = a[0] XOR ... XOR a[L-1]

  XOR them together: the a[0]..a[L-1] terms cancel (x XOR x = 0)
  Result: a[L] XOR ... XOR a[R] ✅

APPLICATIONS: Range XOR queries in competitive programming,
  cryptographic checksums, parity checks.
```

### Prefix Product (With Caution)

```
ORIGINAL: [2, 3, 4, 5]
PREFIX PRODUCT: [2, 6, 24, 120]

RANGE PRODUCT(L, R):
  = pre_prod[R] / pre_prod[L-1]
  (division is the inverse of multiplication)

CAVEAT: Division fails if any element is 0!
  For arrays with zeros: handle separately.
  For modular arithmetic: use modular inverse instead.
```

### Prefix Max/Min (Not Directly)

```
Prefix max is computable:
  pre_max[i] = max(arr[0..i])

But range max CANNOT be answered via subtraction:
  max(L, R) ≠ pre_max[R] - pre_max[L-1]  (max has no inverse)

For range max/min: use Sparse Table (O(n log n) build, O(1) query)
                   or Segment Tree (O(n) build, O(log n) query)

CRITICAL INSIGHT: Prefix sum works because addition has an INVERSE (subtraction).
  XOR works because XOR is its own inverse.
  Multiplication works (with care) because division is its inverse.
  Max/Min DON'T work because there's no inverse operation.
```

---

## 8. The Subarray Sum Equals K Pattern

One of prefix sum's most elegant applications: counting subarrays with a specific sum.

```
PROBLEM: Count subarrays of arr with sum exactly equal to k.

arr = [1, 1, 1]   k = 2
Answer: 2  ([arr[0..1]] and [arr[1..2]])

NAIVE: O(n²) — check every pair (L, R)

PREFIX SUM + HASHMAP: O(n)

KEY INSIGHT:
  sum(L, R) = k
  ⟺ pre[R] - pre[L-1] = k
  ⟺ pre[L-1] = pre[R] - k

  For each position R, we want to COUNT how many previous
  prefix sums equal (pre[R] - k).

  Store prefix sum FREQUENCIES in a hashmap as we scan.

ALGORITHM:
  count = 0
  freq = {0: 1}    ← 0 prefix sum seen once (empty prefix, handles L=0)
  running_sum = 0

  FOR each element x in arr:
      running_sum += x
      complement = running_sum - k
      count += freq.get(complement, 0)   ← how many valid L positions?
      freq[running_sum] = freq.get(running_sum, 0) + 1

TRACE: arr=[1,1,1], k=2

  freq={0:1}, sum=0

  x=1: sum=1, complement=1-2=-1, count+=freq[-1]=0, freq={0:1,1:1}
  x=1: sum=2, complement=2-2=0,  count+=freq[0]=1,  freq={0:1,1:1,2:1}  count=1
  x=1: sum=3, complement=3-2=1,  count+=freq[1]=1,  freq={0:1,1:1,2:1,3:1} count=2

  Answer: 2 ✅

WHY {0:1}?
  Handles the case where the subarray starts at index 0.
  If running_sum == k at position R, complement = 0.
  freq[0] = 1 says "yes, there's one empty prefix with sum 0"
  → subarray arr[0..R] is a valid answer.
```

---

## 9. Difference Array — The Inverse of Prefix Sum

The **difference array** is prefix sum's dual: where prefix sum answers range queries efficiently, difference array performs range updates efficiently.

```
DIFFERENCE ARRAY DEFINITION:
  diff[0] = arr[0]
  diff[i] = arr[i] - arr[i-1]   for i > 0

  ORIGINAL: [3,  1,  4,  1,  5,  9]
  DIFF:     [3, -2,  3, -3,  4,  4]

RECONSTRUCTION:
  Prefix sum of diff array = original array
  arr[i] = diff[0] + diff[1] + ... + diff[i]
         = running sum of diff

RANGE UPDATE:
  "Add v to all elements arr[L..R]"

  NAIVE: O(n) — loop through L to R and add v

  DIFF ARRAY: O(1) update
    diff[L] += v      ← start adding v from position L
    diff[R+1] -= v    ← stop adding v after position R

  Then reconstruct with prefix sum: O(n)

  TOTAL for m updates then one reconstruction:
    NAIVE: O(m×n)
    DIFF + PREFIX SUM: O(m + n)   ← huge savings for many updates
```

**Step-by-step trace:**

```
arr = [1, 1, 1, 1, 1]
diff = [1, 0, 0, 0, 0]   (initial difference array)

UPDATE 1: Add 3 to arr[1..3]:
  diff[1] += 3  → diff = [1, 3, 0, 0, 0]
  diff[4] -= 3  → diff = [1, 3, 0, 0, -3]

UPDATE 2: Add 1 to arr[2..4]:
  diff[2] += 1  → diff = [1, 3, 1, 0, -3]
  diff[5] -= 1  → diff = [1, 3, 1, 0, -3, -1]  (out of bounds, ignore or extend)

RECONSTRUCT (prefix sum of diff):
  arr[0] = 1
  arr[1] = 1 + 3 = 4
  arr[2] = 4 + 1 = 5
  arr[3] = 5 + 0 = 5
  arr[4] = 5 + (-3) = 2

Final arr: [1, 4, 5, 5, 2]

VERIFY manually:
  Original [1,1,1,1,1]
  +3 to [1..3]: [1,4,4,4,1]
  +1 to [2..4]: [1,4,5,5,2] ✅
```

```
PREFIX SUM vs DIFFERENCE ARRAY — DUALITY:

  PREFIX SUM:
    Build: O(n)     Update: O(n) (rebuild)
    Query: O(1)     Use when: many queries, rare updates

  DIFFERENCE ARRAY:
    Build: O(n)     Update: O(1) per range update
    Query: O(n) (reconstruct then index)
    Use when: many range updates, then read final state

  They are INVERSES:
    Prefix sum of difference array = original array
    Difference array of prefix sum array = original array

  TOGETHER: They form a complete toolkit for
    - Static arrays with many range queries → Prefix sum
    - Dynamic arrays with many range updates → Difference array
    - Both → Segment tree or BIT (Fenwick tree)
```

---

## 10. The "Why" Questions

### Why O(1) queries after O(n) preprocessing instead of O(log n)?

```
Segment trees and Fenwick trees give O(log n) for BOTH queries AND updates.
Prefix sum gives O(1) for queries but O(n) for updates (must rebuild).

TRADEOFF:
  Static data (no updates) → Prefix sum (O(1) query is unbeatable)
  Dynamic data (frequent updates) → Segment tree / BIT (O(log n) both)

Prefix sum's O(1) query is the absolute theoretical minimum —
you cannot answer a range sum query in less than O(1).
Prefix sum achieves this lower bound by paying the O(n) preprocessing cost.
This is "offline" query answering: pay upfront, query for free.
```

### Why does the formula work only for invertible operations?

```
CORE ALGEBRAIC REQUIREMENT:
  We need: f(L, R) = g(pre[R], pre[L-1])
  where g "removes" the prefix [0..L-1] from [0..R].

  For ADDITION: g is subtraction (inverse of addition). Works. ✅
  For XOR: g is XOR itself (XOR is self-inverse). Works. ✅
  For MULTIPLICATION: g is division (inverse of multiplication). Works (if no zeros). ✅
  For MAX: g would need to "un-max" — impossible. MAX has no inverse. ❌

  The prefix sum technique requires an inverse operation.
  It's essentially computing: "result up to R" minus "result up to L-1"
  Whatever "minus" means for your operation, it must exist.
```

### Why does the sentinel pre[0]=0 simplify everything?

```
WITHOUT SENTINEL (0-indexed):
  sum(0, R) = pre[R]          ← special case
  sum(L, R) = pre[R]-pre[L-1] ← general case
  Must handle L=0 separately in code → error-prone

WITH SENTINEL (1-indexed, pre[0]=0):
  sum(L, R) = pre[R] - pre[L-1]  ← ALWAYS, including L=1
  L=1: pre[R] - pre[0] = pre[R] - 0 = pre[R] ✅

The sentinel represents "the sum of zero elements" = 0.
It's the additive identity, so subtracting it has no effect.
This elegance — one formula handles all cases — is why
most implementations use 1-indexed prefix sums with a sentinel.
```

---

## 11. "What If" Edge Cases

| What If...? | What Happens |
|---|---|
| Array has negative numbers | Prefix sum works fine; sums can decrease; pre[i] ≤ pre[i-1] is possible |
| Array is empty | Empty prefix sum array; no queries possible; return 0 or handle as special case |
| L = R (single element query) | `pre[R] - pre[L-1]` = `pre[R] - pre[R-1]` = `arr[R]` ✅ Works correctly |
| L = 0 (query from start) | Use sentinel: `pre[R] - pre[0]` = `pre[R] - 0` = `pre[R]` ✅ |
| L > R (invalid range) | Undefined behavior; must validate input; many implementations return 0 |
| Array updated after building | Prefix sum is stale; must rebuild O(n) or use Fenwick tree for O(log n) updates |
| Very large values | Integer overflow risk; use long/int64 instead of int |
| Floating point values | Works; floating point precision issues may accumulate over large ranges |
| 2D query where r1=0 or c1=0 | Sentinel row/column (pre[0][j]=pre[i][0]=0) handles this automatically |
| All elements are zero | Prefix sum array is all zeros; all range queries return 0 |

### The Integer Overflow Problem

```
ARRAY: [10^9, 10^9, 10^9, 10^9, 10^9]   (five billion)

32-bit integer max: 2^31 - 1 ≈ 2.1 × 10^9

pre[4] = 5 × 10^9 > 2.1 × 10^9 → OVERFLOW → wrong answer!

FIX: Use 64-bit integers (long in Java, int64 in C++, Python auto-handles)

pre = [0] * (n + 1)          # Python: no overflow
pre = new long[n + 1];       // Java: use long
pre = vector<long long>(n+1) // C++: use long long

RULE: If sum of all elements might exceed 2 billion, use 64-bit integers.
      For competitive programming: ALWAYS use 64-bit by default.
```

---

## 12. Advanced Patterns

### Subarray Sum Divisible by K

```
PROBLEM: Count subarrays with sum divisible by k.

KEY INSIGHT:
  sum(L, R) % k == 0
  ⟺ (pre[R] - pre[L-1]) % k == 0
  ⟺ pre[R] % k == pre[L-1] % k

  Count pairs of positions with equal prefix sum mod k!

ALGORITHM:
  freq = {0: 1}      ← empty prefix has remainder 0
  running_sum = 0
  count = 0

  FOR x in arr:
      running_sum += x
      remainder = ((running_sum % k) + k) % k  ← handle negative remainders
      count += freq.get(remainder, 0)
      freq[remainder] = freq.get(remainder, 0) + 1

  [(running_sum % k) + k) % k]: ensures positive remainder in Python/Java too

arr=[4,5,0,-2,-3,1], k=5

  sum=4,  rem=4, count+=0, freq={0:1,4:1}
  sum=9,  rem=4, count+=1, freq={0:1,4:2}     ← sum[1..2]=5 divisible by 5
  sum=9,  rem=4, count+=2, freq={0:1,4:3}     ← sum[0..2]=9... wait
  ... (continue)

Answer counts all pairs with equal remainders: C(n, 2) for n equal remainders ✅
```

### Equilibrium Index

```
PROBLEM: Find index i where sum(arr[0..i-1]) == sum(arr[i+1..n-1])

APPROACH WITH PREFIX SUM:
  total = sum of entire array
  left_sum = 0

  FOR i in range(n):
      right_sum = total - left_sum - arr[i]
      IF left_sum == right_sum:
          return i  ← equilibrium index
      left_sum += arr[i]

  No prefix array needed — maintain running prefix sum!

arr = [1, 7, 3, 6, 5, 6]   total = 28

  i=0: left=0,  right=28-0-1=27.  0≠27
  i=1: left=1,  right=28-1-7=20.  1≠20
  i=2: left=8,  right=28-8-3=17.  8≠17
  i=3: left=11, right=28-11-6=11. 11==11 → return 3 ✅

  arr[0..2] = 1+7+3 = 11
  arr[4..5] = 5+6   = 11  ✅
```

### Maximum Subarray Sum (Kadane's Relationship)

```
Prefix sum illuminates WHY Kadane's algorithm works:

Maximum subarray sum = max over all (L,R) of (pre[R] - pre[L-1])
                     = max over R of (pre[R] - min over L≤R of pre[L-1])

Kadane's algorithm implicitly tracks:
  - pre[R]: the running sum up to R
  - min prefix sum seen so far: the optimal "starting point" to subtract

max_sum = float('-inf')
min_prefix = 0      ← pre[-1] = 0 (empty prefix)
running = 0

FOR x in arr:
    running += x                           ← this IS pre[R]
    max_sum = max(max_sum, running - min_prefix)  ← subtract best pre[L-1]
    min_prefix = min(min_prefix, running)  ← update minimum prefix seen

This is prefix sum + greedy tracking of the minimum prefix sum.
Kadane's algorithm IS prefix sum with smart tracking. ✅
```

---

## 13. Real-World Applications

| Domain | Problem | Prefix Sum's Role |
|---|---|---|
| **Databases** | Cumulative aggregations (running totals) | Pre-computed prefix sums on indexed columns |
| **Finance** | Portfolio cumulative returns, drawdown analysis | Prefix sum over daily returns |
| **Image processing** | Summed area tables (box filter, integral image) | 2D prefix sum for O(1) rectangular region sums |
| **Machine learning** | Batch normalization statistics | Prefix sum over activations for fast mean/variance |
| **Competitive programming** | Range sum, range XOR, subarrays with property | Core technique in nearly every contest |
| **Game development** | Terrain height sums, region damage totals | 2D prefix sum for spatial queries |
| **Statistics** | Cumulative distribution functions | Prefix sum over frequency arrays |
| **Signal processing** | Moving average computation | Sliding window over prefix sums |
| **Traffic analysis** | Vehicles between two checkpoints | Prefix count array |
| **Rendering** | Fast area light calculations | 2D prefix sum (integral image) |

### Integral Image — 2D Prefix Sum in Computer Vision

```
PROBLEM: Detect faces in images using Haar features.
  Haar feature = difference of pixel sums in two rectangles.
  Computed for every position and scale = millions of rectangle sums.
  At 30fps video: must compute billions of sums per second.

WITHOUT INTEGRAL IMAGE:
  Each rectangle sum: O(width × height)
  Millions of features × millions of positions = impossible in real-time

WITH INTEGRAL IMAGE (2D prefix sum of pixel values):
  Build: O(width × height) — one pass
  Each rectangle sum: O(1) — four array lookups + three additions
  Billions of sums: instantly feasible ✅

VIOLA-JONES ALGORITHM (2001):
  Built real-time face detection using integral images.
  Integral image = 2D prefix sum of grayscale pixel values.
  Used in: every digital camera's face detection,
           Snapchat filters, passport photo verification.

This is perhaps the most impactful application of prefix sums
in computer vision history.
```

### Moving Average with Prefix Sum

```
PROBLEM: Compute moving average of stock price over last k days.

arr = [100, 102, 101, 105, 110, 108, 107]   k = 3

PREFIX SUM: pre = [0, 100, 202, 303, 408, 518, 626, 733]

Moving average at day i (0-indexed):
  = sum(i-k+1, i) / k
  = (pre[i+1] - pre[i-k+1]) / k

  Day 2 (i=2): (pre[3] - pre[0]) / 3 = 303/3 = 101.0
  Day 3 (i=3): (pre[4] - pre[1]) / 3 = (408-100)/3 = 102.67
  Day 4 (i=4): (pre[5] - pre[2]) / 3 = (518-202)/3 = 105.33

O(n) build + O(1) per average = O(n) total
vs O(n×k) naive
```

---

## 14. Comparison With Related Techniques

```
              ┌──────────────────────────────────────────────────────────┐
              │              RANGE QUERY DATA STRUCTURES                  │
              └──────────────────────────┬───────────────────────────────┘
                                         │
       ┌──────────────────┬──────────────┼──────────────┬────────────────┐
       ▼                  ▼             ▼              ▼                ▼
  PREFIX SUM          SEGMENT         FENWICK       SPARSE          SQRT
                       TREE           TREE          TABLE           DECOMP.
  ──────────          ───────         ───────       ──────          ──────
  Build:  O(n)        O(n)            O(n log n)    O(n log n)      O(n√n)
  Query:  O(1)        O(log n)        O(log n)      O(1)            O(√n)
  Update: O(n)        O(log n)        O(log n)      O(n log n)      O(√n)
                                                    (rebuild)
  Operations: +,XOR,× any           +, XOR          idempotent      any
  Space: O(n)         O(n)           O(n)            O(n log n)      O(n)
  Static? Yes         No             No              Yes             No
```

**Prefix Sum vs Segment Tree:**
Prefix sum is strictly better for static data with sum queries (O(1) vs O(log n) queries). Segment tree is strictly better when data changes (O(log n) updates vs O(n) rebuild). For the specific case of static range sum queries, prefix sum is the optimal choice with no competition.

**Prefix Sum vs Fenwick Tree (Binary Indexed Tree):**
Fenwick tree generalizes prefix sum to support O(log n) point updates alongside O(log n) prefix queries. It's prefix sum with dynamic update capability at the cost of no longer being O(1) per query. When you need both updates and queries frequently — Fenwick tree. When data is static — prefix sum.

**Prefix Sum vs Sparse Table:**
Sparse table achieves O(1) range queries for idempotent operations (max, min, GCD) — operations without inverses. Prefix sum achieves O(1) for invertible operations (sum, XOR). They complement each other: prefix sum for sum, sparse table for max/min.

---

## 15. Tips for Long-Term Retention

**1. The odometer image**
Always picture an odometer on a road trip. Distance between two cities = odometer reading at destination minus reading at departure. You don't re-drive the journey; you subtract two numbers. This single image encodes the entire technique: precompute cumulative readings, answer distance questions with subtraction.

**2. The formula is just algebra**
`sum(L, R) = pre[R] - pre[L-1]` isn't a trick to memorize — it's the algebraic consequence of the prefix sum definition. Derive it once from scratch: write out what `pre[R]` and `pre[L-1]` mean, subtract, watch the terms cancel. After deriving it yourself, you'll never forget it.

**3. Always use a sentinel (pre[0] = 0)**
This single habit eliminates all edge cases. 1-indexed prefix sum with `pre[0] = 0` means the formula `pre[R] - pre[L-1]` works for ALL L including L=1 (or L=0 in 0-indexed arrays with the sentinel). Write the sentinel; don't special-case L=0.

**4. Prefix sum = precompute to answer queries offline**
The conceptual pattern is: you don't know which queries are coming, so you precompute everything that lets you answer any query instantly. This "offline preprocessing" pattern appears in many algorithms. Recognizing it helps you identify when prefix sum applies: "I have many range queries on static data — precompute prefix sums."

**5. Difference array is prefix sum's inverse**
If prefix sum answers "what is the sum over this range?", difference array enables "add this value to this range efficiently." They're duals. Prefix sum of difference array = original. Whenever you see "many range updates, then read result" — reach for difference array. Whenever you see "many range queries, rarely update" — reach for prefix sum.

**6. The subarray sum pattern: `pre[R] - pre[L-1] = k` → `pre[L-1] = pre[R] - k`**
This algebraic rewrite turns "find subarrays with sum k" into "at each position R, count how many previous prefix sums equal `pre[R] - k`." That rewrite unlocks O(n) solutions for a whole family of problems. Internalize it as a reflex: subarray sum condition → rewrite as prefix sum equation → use hashmap to count.

---

Prefix sum is fundamentally about **paying a small fixed cost to eliminate repetitive work forever**. The O(n) build is the investment; the O(1) queries are the dividend. Every time you answer a range query in O(1) instead of O(n), you're spending a credit you earned during preprocessing. The mathematics is simple addition and subtraction, but the insight — that cumulative totals encode all possible range sums, and that any range sum is just the difference of two cumulative totals — turns a naive O(n) per query problem into something that answers billions of queries as fast as you can read memory. That transformation, from linear to constant, achieved through the simplest of arithmetic, is what makes prefix sum one of the most elegant and ubiquitous ideas in all of algorithm design.
