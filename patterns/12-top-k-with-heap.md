# Pattern 12: Top K with Heap

## At a Glance

| Item | Summary |
|---|---|
| Use when | You need only the best `k` items (or kth item), not full sorted order |
| Main tradeoff | Keep only `k` candidates in heap for speed/memory vs full sorting |
| Typical runtime | `O(n log k)` for size-`k` heap scan |
| Main structures | min-heap for top-k largest, max-heap simulation for top-k smallest/closest |
| Common prompts | kth largest/smallest, top k frequent, k closest points, streaming kth largest |

## Related Playbook

- Full interview question set for this pattern:
  [Pattern 12 Top 10 Questions Playbook](./questions/12-top-k-with-heap-top-10-questions.md)

## Diagram + Intuition

### Pattern Diagram

```text
Top-k largest with min-heap of size k:

heap root = smallest among current top-k

for each value x:
  if heap size < k:
    push x
  elif x > heap root:
    replace root with x

heap always stores best k seen so far
```

### Read-the-Question Trigger Cues

- "top k", "kth largest/smallest", "k closest", streaming k-best updates.
- Need partial ranking only, not total order of all `n` elements.
- `n` is large and `k` is relatively small.
- Repeated inserts/queries ask for current kth boundary.

### Intuition Anchor

- "Keep only candidates that can still belong to final top-k."

### 3-Second Pattern Check

- Do I need only k best items, not full sorted output?
- Can root of a size-`k` heap act as cutoff threshold?
- Can I discard candidates worse than current threshold immediately?

## Decision Table: What to Store

| Prompt shape | Structure | Key -> value | Typical query |
|---|---|---|---|
| kth largest in array | min-heap size `k` | candidate value | compare with root |
| top k frequent | frequency map + min-heap | `(freq, value)` | replace if freq larger |
| k closest points | max-heap size `k` (via negative key) | `(-distance, point)` | replace farthest kept |
| stream kth largest | persistent min-heap size `k` | values in stream | root is kth largest |
| top k smallest | max-heap size `k` | negative value or custom key | compare against max kept |
| merge-like top-k combinations | heap of tuples | tuple fields for ordering | pop/push next candidate |

## Universal Invariant

Before coding, say this sentence out loud:

- "After processing any prefix of input, heap contains exactly the best `k` candidates from that prefix under my ranking rule, and root is the current cutoff."

If this invariant is unclear, the implementation will usually fail on edge cases.

## Step-by-Step Method (Easy Version)

Use this exact flow while coding:

1. Write default return first (`[]`, `0`, `-1`, or sentinel by prompt).
2. Define ranking direction (largest/smallest/frequency/distance).
3. Choose heap type and key so root is the worst among kept `k`.
4. Iterate items once.
5. If heap size `< k`, push item.
6. Else compare item with root threshold; if better, replace root.
7. Return root (for kth) or heap contents (sorted if required by prompt).

Fill-in template:

```python
import heapq

def solve(items, k):
    if k <= 0:
        return ...

    heap = []  # keep worst-of-best at root

    for item in items:
        key = rank_key(item)
        if len(heap) < k:
            heapq.heappush(heap, (key, item))
        elif key > heap[0][0]:   # adjust comparator by objective
            heapq.heapreplace(heap, (key, item))

    return finalize(heap)
```

## Query/Update Order Rules

### A) Fill to `k`, then compare and replace (most common)

Use for kth largest and top-k largest by value.

```python
for x in nums:
    if len(heap) < k:
        heapq.heappush(heap, x)
    elif x > heap[0]:
        heapq.heapreplace(heap, x)
```

### B) Build global counts first, then heap-select

Use for top-k frequent elements.

```python
freq = Counter(nums)
for val, f in freq.items():
    if len(heap) < k:
        heappush(heap, (f, val))
    elif f > heap[0][0]:
        heapreplace(heap, (f, val))
```

### C) Initialize from first `k`, heapify, then scan rest

Use when input is indexable and you want fewer branch checks.

```python
heap = nums[:k]
heapq.heapify(heap)
for x in nums[k:]:
    if x > heap[0]:
        heapq.heapreplace(heap, x)
```

## Detailed Example (Kth Largest Element)

**Input:** `nums = [3, 2, 1, 5, 6, 4], k = 2`

1. Start empty min-heap (size limit `2`).
2. Push `3`, `2` -> heap root is `2` (current 2nd largest threshold).
3. Read `1`: not greater than root `2`, ignore.
4. Read `5`: greater than root, replace `2` -> heap `[3,5]`.
5. Read `6`: replace `3` -> heap `[5,6]`.
6. Read `4`: not greater than root `5`, ignore.
7. Root `5` is answer (2nd largest).

Why it works: heap always stores best two values seen so far; root is smallest among those best two.

## Reusable Python Templates

### 1) Membership (Would Value Be in Top K Largest?)

```python
import heapq

def is_in_top_k_largest(nums, k, target):
    if k <= 0:
        return False

    heap = []
    for x in nums:
        if len(heap) < k:
            heapq.heappush(heap, x)
        elif x > heap[0]:
            heapq.heapreplace(heap, x)

    return len(heap) == k and target >= heap[0]
```

Example:

```python
is_in_top_k_largest([3,2,1,5,6,4], 2, 6)  # True
is_in_top_k_largest([3,2,1,5,6,4], 2, 4)  # False
```

### 2) Frequency Count (Top K Frequent Elements)

```python
import heapq
from collections import Counter

def top_k_frequent(nums, k):
    if k <= 0:
        return []

    freq = Counter(nums)
    heap = []  # (frequency, value)

    for val, f in freq.items():
        if len(heap) < k:
            heapq.heappush(heap, (f, val))
        elif f > heap[0][0]:
            heapq.heapreplace(heap, (f, val))

    return [val for _, val in heap]
```

Example:

```python
top_k_frequent([1,1,1,2,2,3], 2)  # [1,2] (order may vary)
top_k_frequent([4,4,4,5,5,6], 1)  # [4]
```

### 3) Value -> Record (K Closest Points)

```python
import heapq

def k_closest(points, k):
    if k <= 0:
        return []

    heap = []  # max-heap via negative distance: (-dist2, x, y)

    for x, y in points:
        d2 = x * x + y * y
        item = (-d2, x, y)
        if len(heap) < k:
            heapq.heappush(heap, item)
        elif -heap[0][0] > d2:
            heapq.heapreplace(heap, item)

    return [[x, y] for _, x, y in heap]
```

Example:

```python
k_closest([[1,3],[-2,2]], 1)  # [[-2,2]]
k_closest([[3,3],[5,-1],[-2,4]], 2)  # two closest points (order may vary)
```

### 4) Streaming Kth Largest (Persistent Heap)

```python
import heapq

class KthLargest:
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
        return self.heap[0] if self.heap else None
```

Example:

```python
obj = KthLargest(3, [4, 5, 8, 2])
obj.add(3)   # 4
obj.add(10)  # 5
```

## Complexity

Let:

- `n` = number of input items.
- `u` = number of unique values (for frequency variants).
- `k` = requested top-k size.

Per-operation cost:

- Heap push/pop/replace on size `k`: `O(log k)`.

End-to-end cost (most interview problems):

| Variant | Time (average) | Space |
|---|---|---|
| kth largest via size-`k` heap scan | `O(n log k)` | `O(k)` |
| top-k frequent (count + heap) | `O(n + u log k)` | `O(u + k)` |
| k closest points (size-`k` heap) | `O(n log k)` | `O(k)` |
| stream add operation | `O(log k)` per insert | `O(k)` |
| full sort baseline | `O(n log n)` | depends on sort implementation |

Interview note:

- Use heap when `k << n`; if `k` is near `n`, sorting may be similarly practical.

## Edge-Case Checklist (Pre-Submit)

Use this as a final pass before you finish coding.

### Contract Checks

- Return type matches prompt exactly: kth value, list of values, list of records, or class behavior.
- If output must be sorted, add final sort step intentionally.
- For invalid `k` (`k <= 0`, `k > n`), behavior matches prompt contract.
- Tie handling matches requirements (any order vs deterministic order).

### Data-Rule Checks

- Heap type and comparator direction are correct for objective.
- Root represents worst among kept best candidates.
- Replacement condition uses strictness consistent with tie policy.
- Tuple ordering in heap is intentional (`(freq, value)`, `(-dist, point)`, etc.).
- For frequency problems, count map is built correctly before heap updates.

### Input Boundary Checks

- Empty input and single-element input handled safely.
- `k = 1` and `k = n` produce correct results.
- Duplicate-heavy inputs behave correctly.
- Negative values and mixed signs handled for numeric ranking.
- Large `n` avoids accidental full-sort fallback if not intended.

### Pattern-Specific Checks

- Size-`k` invariant holds after each iteration.
- Root is interpreted correctly as kth boundary.
- Heap output is acknowledged as unsorted unless post-processed.
- Streaming variant preserves state across calls.

### Quick Sanity Tests (Run Mentally)

| Scenario | Example | What should happen |
|---|---|---|
| smallest valid `k` | `k=1` | root is global best under objective |
| largest valid `k` | `k=n` | heap contains all elements |
| duplicates around boundary | repeated values near kth cutoff | tie handling remains consistent |
| empty/invalid | `nums=[]`, bad `k` | returns prompt-defined default |
| stream updates | add values above/below root | root updates only when threshold beaten |

## Common Pitfalls

- Using wrong heap direction for objective and getting inverted results.
- Forgetting to cap heap at size `k`, leading to `O(n log n)` behavior.
- Assuming heap array is fully sorted.
- Tuple key mistakes in Python (`(value, freq)` vs `(freq, value)`).
- Not clarifying tie behavior when frequencies/distances are equal.

## When Not Ideal

- Need full sorted order of all elements (sorting may be simpler).
- Require deterministic ranked order with many ties and complex rules.
- Need strict linear average selection of kth only (quickselect can be better average-case).
- Heavy dynamic deletions and rank queries (balanced BST/order-statistics tree may fit better).

## Variations

- Kth Largest/Smallest Element.
- Top K Frequent Elements.
- K Closest Points to Origin.
- Kth Smallest in Sorted Matrix / K-way heap variants.
- Streaming Kth Largest or median (two-heaps).

## Interview Tips

- Use this 20-second opener:
  "I only need top `k`, so I keep a size-`k` heap where root is cutoff; each new candidate either joins or is discarded."
- State heap invariant before coding:
  "Heap stores best `k` seen so far; root is worst among them."
- Mention complexity comparison:
  `O(n log k)` vs `O(n log n)` sorting.
- Clarify output contract:
  kth only, unsorted top-k, or sorted top-k.
- Mention alternative:
  quickselect for kth-only average `O(n)`.

## Interviewer Questions While Coding (Important)

| Interviewer asks | How to answer quickly |
|---|---|
| Why heap over sorting? | We need only top `k`; heap avoids ordering all `n` elements. |
| Why min-heap for k largest? | Root should be current kth largest threshold (smallest among kept top-k). |
| Why keep heap size fixed? | Preserves `O(log k)` updates and `O(k)` memory. |
| Is heap output sorted? | No, it is partial order; sort at end only if required. |
| What about ties? | Define replacement strictness and output order policy explicitly. |
| Could quickselect be better? | For kth-only queries, average `O(n)` quickselect is strong, but heap is simpler and stream-friendly. |
| Streaming support? | Persistent size-`k` heap gives `O(log k)` per add. |
| Complexity? | Typically `O(n log k)` time and `O(k)` heap space. |
| Most common bug? | Reversed comparator/heap type causing wrong cutoff logic. |

## Practice Ladder (2 Deep Interview Walkthroughs)

### 1) Kth Largest Element in an Array

Problem:

- Given array `nums` and integer `k`, return the kth largest element.

What interviewer is testing:

- Can you choose partial-order strategy over full sort?
- Can you maintain fixed-size heap invariant?
- Can you discuss quickselect tradeoff?

#### What to Say in First 30 Seconds

Use this script:

"I only need kth largest, not full sorted array.  
I’ll keep a min-heap of size `k` containing current top-k values.  
For each number, if it beats heap root, it replaces root; otherwise ignore.  
After one pass, root is kth largest.  
Time is `O(n log k)` and space is `O(k)`."

#### Solution A: Full Sort

Idea:

- Sort descending and return index `k-1`.

```python
def kth_largest_sort(nums, k):
    nums = sorted(nums, reverse=True)
    return nums[k - 1]
```

Complexity:

- Time `O(n log n)`, Space depends on sorting implementation.

#### Solution B: Quickselect (Average Linear)

Idea:

- Partition around pivot until target index is placed.

```python
def kth_largest_quickselect(nums, k):
    target = len(nums) - k

    def partition(l, r):
        pivot = nums[r]
        i = l
        for j in range(l, r):
            if nums[j] <= pivot:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
        nums[i], nums[r] = nums[r], nums[i]
        return i

    l, r = 0, len(nums) - 1
    while l <= r:
        p = partition(l, r)
        if p == target:
            return nums[p]
        if p < target:
            l = p + 1
        else:
            r = p - 1
```

Complexity:

- Average time `O(n)`, worst-case `O(n^2)`, Space `O(1)` iterative.

Interviewer tradeoff answer:

- "Quickselect is faster average for single query; heap is simpler, stable, and supports streaming."

#### Solution C: Min-Heap of Size K (Canonical)

Idea:

- Maintain top-k largest candidates only.

```python
import heapq

def kth_largest_heap(nums, k):
    heap = []
    for x in nums:
        if len(heap) < k:
            heapq.heappush(heap, x)
        elif x > heap[0]:
            heapq.heapreplace(heap, x)
    return heap[0]
```

Complexity:

- Time `O(n log k)`, Space `O(k)`.

What to say while solving with interviewer:

1. "Heap root is current kth largest threshold."
2. "Only values greater than root can enter top-k."
3. "Heap never exceeds size `k`."
4. "Return root after full scan."

Common interviewer follow-up and answer:

| Interviewer asks | Good answer |
|---|---|
| Why not max-heap all values? | Works, but uses `O(n)` memory and more operations than needed. |
| What if `k=n`? | Heap ends up containing all values; root is minimum element. |
| Need sorted top-k output? | Sort heap at end in descending order if required. |

### 2) Top K Frequent Elements

Problem:

- Given integer array `nums` and integer `k`, return the `k` most frequent elements.

What interviewer is testing:

- Can you combine counting with heap selection?
- Can you handle tuple ordering and tie behavior?
- Can you reason in terms of unique count `u`?

#### What to Say in First 30 Seconds

Use this script:

"I need top frequencies, so first I count occurrences with a hash map.  
Then I keep a min-heap of size `k` over `(frequency, value)`.  
If new frequency beats heap root frequency, replace root.  
Heap holds top-k frequent values in `O(n + u log k)` where `u` is unique count."

#### Solution A: Count + Sort by Frequency

Idea:

- Sort frequency pairs descending.

```python
from collections import Counter

def top_k_frequent_sort(nums, k):
    freq = Counter(nums)
    pairs = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    return [val for val, _ in pairs[:k]]
```

Complexity:

- Time `O(n + u log u)`, Space `O(u)`.

#### Solution B: Bucket Sort by Frequency

Idea:

- Frequency range is `1..n`; place values by count then scan from high to low.

```python
from collections import Counter

def top_k_frequent_bucket(nums, k):
    freq = Counter(nums)
    buckets = [[] for _ in range(len(nums) + 1)]
    for val, f in freq.items():
        buckets[f].append(val)

    out = []
    for f in range(len(buckets) - 1, 0, -1):
        for val in buckets[f]:
            out.append(val)
            if len(out) == k:
                return out
    return out
```

Complexity:

- Time `O(n)`, Space `O(n)`.

Interviewer tradeoff answer:

- "Bucket sort can be linear but uses larger memory; heap is memory-efficient when `k` is small."

#### Solution C: Count + Size-K Min-Heap (Canonical)

Idea:

- Keep only best `k` frequency pairs.

```python
import heapq
from collections import Counter

def top_k_frequent_heap(nums, k):
    freq = Counter(nums)
    heap = []

    for val, f in freq.items():
        if len(heap) < k:
            heapq.heappush(heap, (f, val))
        elif f > heap[0][0]:
            heapq.heapreplace(heap, (f, val))

    return [val for _, val in heap]
```

Complexity:

- Time `O(n + u log k)`, Space `O(u + k)`.

What to say while solving with interviewer:

1. "Map gives exact frequencies in one pass."
2. "Heap root is smallest frequency among current top-k."
3. "Only higher-frequency values replace root."
4. "Output order can be arbitrary unless prompt requests sorted."

Common interviewer follow-up and answer:

| Interviewer asks | Good answer |
|---|---|
| Why map first? | Heap selection needs comparable frequency keys. |
| What about equal frequencies? | Any valid top-k set is acceptable unless prompt requires tie order. |
| Could we do better than `u log k`? | Bucket method can be `O(n)` with higher memory usage. |
