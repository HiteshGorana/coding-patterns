# Pattern 12 Interview Playbook: Top-K with Heap

This playbook is aligned with [Pattern 12: Top K with Heap](../12-top-k-with-heap.md).

Use it when you need only the best `k` candidates (or kth boundary), not full sorting.

## Pattern Snapshot

| Prompt shape | Heap choice | Root meaning |
|---|---|---|
| kth largest | min-heap (size `k`) | current kth largest |
| kth smallest | max-heap (size `k`) or min-heap frontier | current kth smallest boundary |
| top-k frequent | min-heap on frequency (size `k`) | weakest among selected |
| k closest points/elements | max-heap on distance (size `k`) | farthest among selected |
| streaming kth largest | persistent min-heap (size `k`) | live kth largest |
| choose up to k best feasible items | min-heap by constraint + max-heap by value | next feasible best choice |

## Query-Update Rules

- Keep heap size bounded to `k` when possible.
- Design heap root to represent the worst candidate among kept best candidates.
- If new candidate is better than root, replace root.
- For tie rules, include secondary sort keys in heap tuples.
- When feasibility constraints exist, move items into a second heap as they become valid.

---

## Q1. Kth Largest Element in an Array

### Problem
Given integer array `nums` and integer `k`, return the kth largest element in `nums`.

Example: `nums = [3,2,1,5,6,4], k = 2 -> 5`

### Brute Force Solution

#### Pseudocode
```text
SORT nums in descending order
RETURN nums[k - 1]
```

#### Python
```python
def kth_largest_bruteforce(nums, k):
    nums = sorted(nums, reverse=True)
    return nums[k - 1]
```

#### Complexity
- Time: `O(n log n)`
- Space: `O(n)` (or `O(1)` extra with in-place sort)

### Optimal Solution (Min-Heap of Size K)

#### Pseudocode
```text
heap = empty min-heap

FOR x in nums:
    IF heap size < k:
        PUSH x
    ELSE IF x > heap.root:
        REPLACE root with x

RETURN heap.root
```

#### Python
```python
import heapq


def kth_largest_optimal(nums, k):
    heap = []

    for x in nums:
        if len(heap) < k:
            heapq.heappush(heap, x)
        elif x > heap[0]:
            heapq.heapreplace(heap, x)

    return heap[0]
```

#### Complexity
- Time: `O(n log k)`
- Space: `O(k)`

---

## Q2. Top K Frequent Elements

### Problem
Given integer array `nums` and integer `k`, return the `k` most frequent elements.

Example: `nums = [1,1,1,2,2,3], k = 2 -> [1,2]`

### Brute Force Solution

#### Pseudocode
```text
BUILD frequency map
CONVERT to list of (value, freq)
SORT by freq descending
RETURN first k values
```

#### Python
```python
from collections import Counter


def top_k_frequent_bruteforce(nums, k):
    freq = Counter(nums)
    pairs = sorted(freq.items(), key=lambda p: p[1], reverse=True)
    return [val for val, _ in pairs[:k]]
```

#### Complexity
- Time: `O(n + u log u)` where `u` is unique values
- Space: `O(u)`

### Optimal Solution (Frequency Map + Min-Heap)

#### Pseudocode
```text
BUILD frequency map
heap = empty min-heap of (freq, value)

FOR each (value, freq):
    IF heap size < k:
        PUSH (freq, value)
    ELSE IF freq > heap.root.freq:
        REPLACE root with (freq, value)

RETURN values from heap
```

#### Python
```python
import heapq
from collections import Counter


def top_k_frequent_optimal(nums, k):
    freq = Counter(nums)
    heap = []

    for val, f in freq.items():
        if len(heap) < k:
            heapq.heappush(heap, (f, val))
        elif f > heap[0][0]:
            heapq.heapreplace(heap, (f, val))

    return [val for _, val in heap]
```

#### Complexity
- Time: `O(n + u log k)`
- Space: `O(u + k)`

---

## Q3. K Closest Points to Origin

### Problem
Given points in 2D and integer `k`, return `k` points closest to origin `(0,0)`.

Example: `points = [[1,3],[-2,2]], k = 1 -> [[-2,2]]`

### Brute Force Solution

#### Pseudocode
```text
SORT points by squared distance x^2 + y^2 ascending
RETURN first k points
```

#### Python
```python
def k_closest_points_bruteforce(points, k):
    points = sorted(points, key=lambda p: p[0] * p[0] + p[1] * p[1])
    return points[:k]
```

#### Complexity
- Time: `O(n log n)`
- Space: `O(n)`

### Optimal Solution (Max-Heap of Size K)

#### Pseudocode
```text
heap = empty max-heap simulated via negative key

FOR each point (x, y):
    d2 = x*x + y*y
    item = (-d2, x, y)

    IF heap size < k:
        PUSH item
    ELSE IF d2 < distance_of_current_farthest:
        REPLACE root

RETURN points stored in heap
```

#### Python
```python
import heapq


def k_closest_points_optimal(points, k):
    heap = []  # (-dist2, x, y)

    for x, y in points:
        d2 = x * x + y * y
        item = (-d2, x, y)

        if len(heap) < k:
            heapq.heappush(heap, item)
        elif -heap[0][0] > d2:
            heapq.heapreplace(heap, item)

    return [[x, y] for _, x, y in heap]
```

#### Complexity
- Time: `O(n log k)`
- Space: `O(k)`

---

## Q4. Find K Pairs with Smallest Sums

### Problem
Given two sorted arrays `nums1`, `nums2`, return `k` pairs `(u, v)` with smallest sums.

Example: `nums1 = [1,7,11], nums2 = [2,4,6], k = 3 -> [[1,2],[1,4],[1,6]]`

### Brute Force Solution

#### Pseudocode
```text
pairs = []
FOR each a in nums1:
    FOR each b in nums2:
        APPEND (a + b, a, b) to pairs

SORT pairs by sum
RETURN first k pairs as [a, b]
```

#### Python
```python
def k_smallest_pairs_bruteforce(nums1, nums2, k):
    pairs = []

    for a in nums1:
        for b in nums2:
            pairs.append((a + b, a, b))

    pairs.sort(key=lambda t: t[0])
    return [[a, b] for _, a, b in pairs[:k]]
```

#### Complexity
- Time: `O(m * n log(m * n))`
- Space: `O(m * n)`

### Optimal Solution (Best-First Min-Heap)

#### Pseudocode
```text
IF nums1 or nums2 empty OR k == 0:
    RETURN []

heap = empty min-heap of (sum, i, j)

FOR i from 0 to min(k, len(nums1)) - 1:
    PUSH (nums1[i] + nums2[0], i, 0)

ans = []
WHILE heap not empty AND len(ans) < k:
    (s, i, j) = POP heap
    APPEND [nums1[i], nums2[j]] to ans

    IF j + 1 < len(nums2):
        PUSH (nums1[i] + nums2[j + 1], i, j + 1)

RETURN ans
```

#### Python
```python
import heapq


def k_smallest_pairs_optimal(nums1, nums2, k):
    if not nums1 or not nums2 or k == 0:
        return []

    heap = []
    for i in range(min(k, len(nums1))):
        heapq.heappush(heap, (nums1[i] + nums2[0], i, 0))

    ans = []
    while heap and len(ans) < k:
        _, i, j = heapq.heappop(heap)
        ans.append([nums1[i], nums2[j]])

        if j + 1 < len(nums2):
            heapq.heappush(heap, (nums1[i] + nums2[j + 1], i, j + 1))

    return ans
```

#### Complexity
- Time: `O(k log min(k, m))`
- Space: `O(min(k, m))`

---

## Q5. Kth Smallest Element in a Sorted Matrix

### Problem
Given an `n x n` matrix where each row and column is sorted ascending, return the kth smallest element.

Example: `matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8 -> 13`

### Brute Force Solution

#### Pseudocode
```text
flat = empty list
FOR each row in matrix:
    APPEND all row values to flat

SORT flat
RETURN flat[k - 1]
```

#### Python
```python
def kth_smallest_matrix_bruteforce(matrix, k):
    flat = []
    for row in matrix:
        flat.extend(row)

    flat.sort()
    return flat[k - 1]
```

#### Complexity
- Time: `O(n^2 log(n^2))`
- Space: `O(n^2)`

### Optimal Solution (Row Frontier Min-Heap)

#### Pseudocode
```text
n = number of rows
heap = empty min-heap of (value, row, col)

FOR r from 0 to n - 1:
    PUSH (matrix[r][0], r, 0)

REPEAT k - 1 times:
    (val, r, c) = POP heap
    IF c + 1 < n:
        PUSH (matrix[r][c + 1], r, c + 1)

RETURN heap.root.value
```

#### Python
```python
import heapq


def kth_smallest_matrix_optimal(matrix, k):
    n = len(matrix)
    heap = []

    for r in range(n):
        heapq.heappush(heap, (matrix[r][0], r, 0))

    for _ in range(k - 1):
        _, r, c = heapq.heappop(heap)
        if c + 1 < n:
            heapq.heappush(heap, (matrix[r][c + 1], r, c + 1))

    return heap[0][0]
```

#### Complexity
- Time: `O((n + k) log n)`
- Space: `O(n)`

---

## Q6. Kth Largest Element in a Stream

### Problem
Design class `KthLargest` with constructor `KthLargest(k, nums)` and method `add(val)` that returns current kth largest value.

Example:
`KthLargest(3, [4,5,8,2]); add(3)->4, add(5)->5, add(10)->5, add(9)->8`

### Brute Force Solution

#### Pseudocode
```text
CLASS KthLargestBrute:
    STORE k and list nums

    METHOD add(val):
        APPEND val to nums
        SORT nums descending
        RETURN nums[k - 1]
```

#### Python
```python
class KthLargestBruteforce:
    def __init__(self, k, nums):
        self.k = k
        self.nums = nums[:]

    def add(self, val):
        self.nums.append(val)
        self.nums.sort(reverse=True)
        return self.nums[self.k - 1]
```

#### Complexity
- Per `add`: `O(n log n)`
- Space: `O(n)`

### Optimal Solution (Persistent Min-Heap of Size K)

#### Pseudocode
```text
CLASS KthLargestOptimal:
    STORE k and min-heap

    INIT with nums:
        FOR each x in nums:
            add(x)

    METHOD add(val):
        IF heap size < k:
            PUSH val
        ELSE IF val > heap.root:
            REPLACE root with val

        RETURN heap.root
```

#### Python
```python
import heapq


class KthLargestOptimal:
    def __init__(self, k, nums):
        self.k = k
        self.heap = []

        for x in nums:
            self.add(x)

    def add(self, val):
        if len(self.heap) < self.k:
            heapq.heappush(self.heap, val)
        elif val > self.heap[0]:
            heapq.heapreplace(self.heap, val)

        return self.heap[0]
```

#### Complexity
- Per `add`: `O(log k)`
- Space: `O(k)`

---

## Q7. The K Weakest Rows in a Matrix

### Problem
Given binary matrix `mat` (1s then 0s per row), return indices of the `k` weakest rows sorted by soldier count, then row index.

Example: `mat = [[1,1,0,0,0],[1,1,1,1,0],[1,0,0,0,0],[1,1,0,0,0],[1,1,1,1,1]], k = 3 -> [2,0,3]`

### Brute Force Solution

#### Pseudocode
```text
rows = []
FOR i from 0 to m - 1:
    soldiers = sum(mat[i])
    APPEND (soldiers, i) to rows

SORT rows ascending
RETURN first k indices
```

#### Python
```python
def k_weakest_rows_bruteforce(mat, k):
    rows = []

    for i, row in enumerate(mat):
        rows.append((sum(row), i))

    rows.sort()
    return [idx for _, idx in rows[:k]]
```

#### Complexity
- Time: `O(m * n + m log m)`
- Space: `O(m)`

### Optimal Solution (Max-Heap of Size K)

#### Pseudocode
```text
heap = empty heap of (-soldiers, -index)

FOR each row i:
    soldiers = sum(row i)
    PUSH (-soldiers, -i)

    IF heap size > k:
        POP heap root  # strongest among kept

remaining = convert heap items to (soldiers, index)
SORT remaining ascending by soldiers then index
RETURN indices in that order
```

#### Python
```python
import heapq


def k_weakest_rows_optimal(mat, k):
    heap = []

    for i, row in enumerate(mat):
        soldiers = sum(row)
        heapq.heappush(heap, (-soldiers, -i))

        if len(heap) > k:
            heapq.heappop(heap)

    remaining = [(-s, -i) for s, i in heap]
    remaining.sort()
    return [idx for _, idx in remaining]
```

#### Complexity
- Time: `O(m * n + m log k + k log k)`
- Space: `O(k)`

---

## Q8. Top K Frequent Words

### Problem
Given array of words, return `k` most frequent words sorted by frequency descending, then lexicographically ascending.

Example: `words = ["i","love","leetcode","i","love","coding"], k = 2 -> ["i","love"]`

### Brute Force Solution

#### Pseudocode
```text
BUILD frequency map
SORT unique words by key (-freq, word)
RETURN first k words
```

#### Python
```python
from collections import Counter


def top_k_frequent_words_bruteforce(words, k):
    freq = Counter(words)
    ordered = sorted(freq.keys(), key=lambda w: (-freq[w], w))
    return ordered[:k]
```

#### Complexity
- Time: `O(n + u log u)`
- Space: `O(u)`

### Optimal Solution (Custom Min-Heap of Size K)

#### Pseudocode
```text
DEFINE node comparison:
    lower frequency is worse
    if same frequency, lexicographically larger word is worse

heap = empty min-heap
FOR each (word, freq):
    PUSH node(freq, word)
    IF heap size > k:
        POP root (worst)

EXTRACT heap nodes and sort by (-freq, word)
RETURN words
```

#### Python
```python
import heapq
from collections import Counter


class WordNode:
    def __init__(self, freq, word):
        self.freq = freq
        self.word = word

    def __lt__(self, other):
        if self.freq == other.freq:
            return self.word > other.word
        return self.freq < other.freq


def top_k_frequent_words_optimal(words, k):
    freq = Counter(words)
    heap = []

    for word, f in freq.items():
        heapq.heappush(heap, WordNode(f, word))
        if len(heap) > k:
            heapq.heappop(heap)

    nodes = sorted(heap, key=lambda node: (-node.freq, node.word))
    return [node.word for node in nodes]
```

#### Complexity
- Time: `O(n + u log k + k log k)`
- Space: `O(u + k)`

---

## Q9. Minimum Cost to Hire K Workers

### Problem
Given arrays `quality`, `wage`, and integer `k`, hire exactly `k` workers with minimum total cost, where all chosen workers are paid at a common ratio meeting each worker's minimum wage.

Example: `quality = [10,20,5], wage = [70,50,30], k = 2 -> 105.0`

### Brute Force Solution

#### Pseudocode
```text
best = +infinity

FOR each combination C of k workers:
    ratio = max(wage[i] / quality[i]) for i in C
    cost = ratio * sum(quality[i]) for i in C
    best = min(best, cost)

RETURN best
```

#### Python
```python
from itertools import combinations


def mincost_hire_workers_bruteforce(quality, wage, k):
    n = len(quality)
    best = float('inf')

    for comb in combinations(range(n), k):
        ratio = max(wage[i] / quality[i] for i in comb)
        total_q = sum(quality[i] for i in comb)
        best = min(best, ratio * total_q)

    return best
```

#### Complexity
- Time: `O(C(n, k) * k)`
- Space: `O(k)`

### Optimal Solution (Sort by Ratio + Max-Heap on Quality)

#### Pseudocode
```text
workers = [(wage[i]/quality[i], quality[i]) for i]
SORT workers by ratio ascending

max_heap = empty heap storing negative quality
sum_q = 0
best = +infinity

FOR (ratio, q) in workers:
    PUSH -q into max_heap
    sum_q += q

    IF heap size > k:
        removed_q = -POP max_heap
        sum_q -= removed_q

    IF heap size == k:
        best = min(best, ratio * sum_q)

RETURN best
```

#### Python
```python
import heapq


def mincost_hire_workers_optimal(quality, wage, k):
    workers = sorted((w / q, q) for q, w in zip(quality, wage))

    max_heap = []
    sum_q = 0
    best = float('inf')

    for ratio, q in workers:
        heapq.heappush(max_heap, -q)
        sum_q += q

        if len(max_heap) > k:
            sum_q += heapq.heappop(max_heap)  # subtract removed quality

        if len(max_heap) == k:
            best = min(best, ratio * sum_q)

    return best
```

#### Complexity
- Time: `O(n log n + n log k)`
- Space: `O(k)`

---

## Q10. IPO

### Problem
Given at most `k` project picks, initial capital `w`, profits array, and capital requirements array, maximize final capital.

Example: `k = 2, w = 0, profits = [1,2,3], capital = [0,1,1] -> 4`

### Brute Force Solution

#### Pseudocode
```text
used = [False] * n
capital_now = w

REPEAT up to k times:
    best_profit = -1
    best_idx = -1

    FOR i from 0 to n - 1:
        IF not used[i] AND capital[i] <= capital_now:
            IF profits[i] > best_profit:
                best_profit = profits[i]
                best_idx = i

    IF best_idx == -1:
        BREAK

    used[best_idx] = True
    capital_now += profits[best_idx]

RETURN capital_now
```

#### Python
```python
def ipo_bruteforce(k, w, profits, capital):
    n = len(profits)
    used = [False] * n
    curr = w

    for _ in range(k):
        best_profit = -1
        best_idx = -1

        for i in range(n):
            if not used[i] and capital[i] <= curr and profits[i] > best_profit:
                best_profit = profits[i]
                best_idx = i

        if best_idx == -1:
            break

        used[best_idx] = True
        curr += profits[best_idx]

    return curr
```

#### Complexity
- Time: `O(k * n)`
- Space: `O(n)`

### Optimal Solution (Min-Capital Heap + Max-Profit Heap)

#### Pseudocode
```text
min_cap = heap of (capital[i], profit[i]) for all projects
max_profit = empty heap storing negative profit
curr = w

REPEAT up to k times:
    WHILE min_cap not empty AND min_cap.root.capital <= curr:
        POP project and PUSH -profit into max_profit

    IF max_profit is empty:
        BREAK

    curr += -POP max_profit

RETURN curr
```

#### Python
```python
import heapq


def ipo_optimal(k, w, profits, capital):
    min_cap = [(c, p) for c, p in zip(capital, profits)]
    heapq.heapify(min_cap)

    max_profit = []
    curr = w

    for _ in range(k):
        while min_cap and min_cap[0][0] <= curr:
            c, p = heapq.heappop(min_cap)
            heapq.heappush(max_profit, -p)

        if not max_profit:
            break

        curr += -heapq.heappop(max_profit)

    return curr
```

#### Complexity
- Time: `O((n + k) log n)`
- Space: `O(n)`

---

## Rapid Recall Checklist

- For top-k largest, keep a min-heap of size `k`.
- For top-k smallest/closest, keep a max-heap (via negative keys) of size `k`.
- Root should represent the current cutoff candidate.
- For ranking ties, encode secondary key directly in heap tuple/object.
- In feasibility-constrained picks, use two heaps: one for availability, one for best choice.
