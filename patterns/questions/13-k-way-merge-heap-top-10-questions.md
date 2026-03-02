# Pattern 13 Interview Playbook: K-Way Merge (Heap)

This playbook is aligned with [Pattern 13: K-Way Merge (Heap)](../13-k-way-merge-heap.md).

Use it when you must repeatedly select the smallest (or largest) among `k` sorted frontiers.

## Pattern Snapshot

| Prompt shape | Heap content | Next push rule |
|---|---|---|
| merge k sorted arrays/lists | `(value, list_id, idx)` | push next from same list |
| merge k sorted linked lists | `(node.val, uid, node)` | push `node.next` |
| kth smallest across sorted sources | same frontier tuples | pop `k` times |
| smallest range across k lists | one head from each list + current max | advance popped list |
| row-wise sorted matrix kth | `(matrix[r][c], r, c)` | push `(r, c+1)` |
| pair-sum frontier | `(sum, i, j)` | push neighbor with larger `j` |

## Query-Update Rules

- Keep exactly one active frontier element per source where possible.
- Pop best frontier element, then advance only that source.
- Track metadata (`list_id`, `index`, or node pointer) to avoid rescans.
- Stop early when goal is rank-based (`kth`, first `k` outputs).
- Amortized thinking: each element is pushed/popped at most once in classic merge.

---

## Q1. Merge K Sorted Lists

### Problem
Given `k` sorted linked lists, merge them into one sorted linked list.

Example: `[[1,4,5],[1,3,4],[2,6]] -> [1,1,2,3,4,4,5,6]`

### Brute Force Solution

#### Pseudocode
```text
values = []
FOR each list head in lists:
    WHILE head exists:
        APPEND head.val to values
        head = head.next

SORT values
BUILD new linked list from values
RETURN new head
```

#### Python
```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def merge_k_lists_bruteforce(lists):
    values = []

    for head in lists:
        cur = head
        while cur:
            values.append(cur.val)
            cur = cur.next

    values.sort()

    dummy = ListNode(0)
    tail = dummy
    for x in values:
        tail.next = ListNode(x)
        tail = tail.next

    return dummy.next
```

#### Complexity
- Time: `O(N log N)`
- Space: `O(N)`

### Optimal Solution (Min-Heap on List Heads)

#### Pseudocode
```text
heap = empty min-heap
uid = 0

FOR each head in lists:
    IF head exists:
        PUSH (head.val, uid, head)
        uid += 1

dummy = new node
tail = dummy

WHILE heap not empty:
    (_, _, node) = POP heap
    tail.next = node
    tail = tail.next

    IF node.next exists:
        PUSH (node.next.val, uid, node.next)
        uid += 1

tail.next = null
RETURN dummy.next
```

#### Python
```python
import heapq


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def merge_k_lists_optimal(lists):
    heap = []
    uid = 0

    for head in lists:
        if head:
            heapq.heappush(heap, (head.val, uid, head))
            uid += 1

    dummy = ListNode(0)
    tail = dummy

    while heap:
        _, _, node = heapq.heappop(heap)
        tail.next = node
        tail = tail.next

        if node.next:
            heapq.heappush(heap, (node.next.val, uid, node.next))
            uid += 1

    tail.next = None
    return dummy.next
```

#### Complexity
- Time: `O(N log k)`
- Space: `O(k)`

---

## Q2. Kth Smallest Element in a Sorted Matrix

### Problem
Given a row-wise sorted matrix and integer `k`, return the kth smallest element.

Example: `matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8 -> 13`

### Brute Force Solution

#### Pseudocode
```text
flat = []
FOR each row in matrix:
    APPEND all values to flat
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
- Time: `O(MN log(MN))`
- Space: `O(MN)`

### Optimal Solution (Row Frontier Min-Heap)

#### Pseudocode
```text
m = row count
heap = empty min-heap

FOR r from 0 to m - 1:
    IF row r non-empty:
        PUSH (matrix[r][0], r, 0)

REPEAT k - 1 times:
    (val, r, c) = POP heap
    IF c + 1 < row_length(r):
        PUSH (matrix[r][c + 1], r, c + 1)

RETURN heap.root.value
```

#### Python
```python
import heapq


def kth_smallest_matrix_optimal(matrix, k):
    heap = []

    for r, row in enumerate(matrix):
        if row:
            heapq.heappush(heap, (row[0], r, 0))

    for _ in range(k - 1):
        _, r, c = heapq.heappop(heap)
        if c + 1 < len(matrix[r]):
            heapq.heappush(heap, (matrix[r][c + 1], r, c + 1))

    return heap[0][0]
```

#### Complexity
- Time: `O((m + k) log m)`
- Space: `O(m)`

---

## Q3. Find K Pairs with Smallest Sums

### Problem
Given sorted arrays `nums1`, `nums2`, return `k` pairs with smallest sums.

Example: `nums1 = [1,7,11], nums2 = [2,4,6], k = 3 -> [[1,2],[1,4],[1,6]]`

### Brute Force Solution

#### Pseudocode
```text
pairs = []
FOR each a in nums1:
    FOR each b in nums2:
        APPEND (a + b, a, b)

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
- Time: `O(mn log(mn))`
- Space: `O(mn)`

### Optimal Solution (K-Way Frontier over Rows)

#### Pseudocode
```text
IF nums1 empty OR nums2 empty OR k == 0:
    RETURN []

heap = empty min-heap
FOR i from 0 to min(k, len(nums1)) - 1:
    PUSH (nums1[i] + nums2[0], i, 0)

ans = []
WHILE heap not empty AND len(ans) < k:
    (sum, i, j) = POP heap
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

## Q4. Smallest Range Covering Elements from K Lists

### Problem
Given `k` sorted lists, find smallest interval `[L, R]` such that each list contributes at least one number inside the interval.

Example: `[[4,10,15,24,26],[0,9,12,20],[5,18,22,30]] -> [20,24]`

### Brute Force Solution

#### Pseudocode
```text
flat = []
FOR list_id in [0..k-1]:
    FOR value in lists[list_id]:
        APPEND (value, list_id) to flat

SORT flat by value
count = frequency map for list_ids
covered = 0
left = 0
best = large interval

FOR right from 0 to len(flat)-1:
    ADD flat[right].list_id to count
    IF first occurrence of that list_id:
        covered += 1

    WHILE covered == k:
        UPDATE best using [flat[left].value, flat[right].value]
        REMOVE flat[left].list_id from count
        IF count becomes 0:
            covered -= 1
        left += 1

RETURN best
```

#### Python
```python
def smallest_range_bruteforce(nums):
    flat = []
    for lid, arr in enumerate(nums):
        for x in arr:
            flat.append((x, lid))

    flat.sort()

    k = len(nums)
    count = [0] * k
    covered = 0
    left = 0
    best_l, best_r = -10**9, 10**9

    for right in range(len(flat)):
        x, lid = flat[right]
        if count[lid] == 0:
            covered += 1
        count[lid] += 1

        while covered == k:
            lval = flat[left][0]
            rval = flat[right][0]
            if rval - lval < best_r - best_l or (rval - lval == best_r - best_l and lval < best_l):
                best_l, best_r = lval, rval

            left_lid = flat[left][1]
            count[left_lid] -= 1
            if count[left_lid] == 0:
                covered -= 1
            left += 1

    return [best_l, best_r]
```

#### Complexity
- Time: `O(N log N)` where `N` is total elements
- Space: `O(N + k)`

### Optimal Solution (Heap + Current Max)

#### Pseudocode
```text
heap = empty min-heap
curr_max = -infinity

FOR each list i:
    PUSH (lists[i][0], i, 0)
    curr_max = max(curr_max, lists[i][0])

best = [heap.root.value, curr_max]

WHILE heap size == k:
    (val, i, j) = POP heap

    UPDATE best using [val, curr_max]

    IF j + 1 == len(lists[i]):
        BREAK

    next_val = lists[i][j + 1]
    PUSH (next_val, i, j + 1)
    curr_max = max(curr_max, next_val)

RETURN best
```

#### Python
```python
import heapq


def smallest_range_optimal(nums):
    heap = []
    curr_max = -10**18

    for i, arr in enumerate(nums):
        heapq.heappush(heap, (arr[0], i, 0))
        curr_max = max(curr_max, arr[0])

    best_l, best_r = heap[0][0], curr_max

    while len(heap) == len(nums):
        val, i, j = heapq.heappop(heap)

        if curr_max - val < best_r - best_l or (curr_max - val == best_r - best_l and val < best_l):
            best_l, best_r = val, curr_max

        if j + 1 == len(nums[i]):
            break

        nxt = nums[i][j + 1]
        heapq.heappush(heap, (nxt, i, j + 1))
        curr_max = max(curr_max, nxt)

    return [best_l, best_r]
```

#### Complexity
- Time: `O(N log k)`
- Space: `O(k)`

---

## Q5. Employee Free Time

### Problem
Given employee schedules (each employee has sorted non-overlapping busy intervals), return common free intervals.

Example: `[[[1,2],[5,6]], [[1,3]], [[4,10]]] -> [[3,4]]`

### Brute Force Solution

#### Pseudocode
```text
intervals = flatten all employee intervals
SORT intervals by start

merged = []
FOR interval in sorted intervals:
    IF merged empty OR interval.start > merged.last.end:
        APPEND interval
    ELSE:
        merged.last.end = max(merged.last.end, interval.end)

free = []
FOR i from 1 to len(merged) - 1:
    APPEND [merged[i-1].end, merged[i].start]

RETURN free
```

#### Python
```python
def employee_free_time_bruteforce(schedule):
    intervals = []

    for emp in schedule:
        for s, e in emp:
            intervals.append([s, e])

    intervals.sort(key=lambda x: x[0])

    merged = []
    for s, e in intervals:
        if not merged or s > merged[-1][1]:
            merged.append([s, e])
        else:
            merged[-1][1] = max(merged[-1][1], e)

    free = []
    for i in range(1, len(merged)):
        free.append([merged[i - 1][1], merged[i][0]])

    return free
```

#### Complexity
- Time: `O(T log T)` where `T` total intervals
- Space: `O(T)`

### Optimal Solution (K-Way Merge on Interval Starts)

#### Pseudocode
```text
heap = empty min-heap of (start, end, emp_id, idx)

FOR each employee emp_id:
    IF schedule[emp_id] non-empty:
        PUSH first interval with metadata

IF heap empty:
    RETURN []

POP first interval
prev_end = its end
PUSH next interval of same employee if exists

free = []
WHILE heap not empty:
    (start, end, emp_id, idx) = POP heap

    IF start > prev_end:
        APPEND [prev_end, start] to free
        prev_end = end
    ELSE:
        prev_end = max(prev_end, end)

    PUSH next interval from same employee if exists

RETURN free
```

#### Python
```python
import heapq


def employee_free_time_optimal(schedule):
    heap = []

    for emp_id, emp in enumerate(schedule):
        if emp:
            s, e = emp[0]
            heapq.heappush(heap, (s, e, emp_id, 0))

    if not heap:
        return []

    s, e, emp_id, idx = heapq.heappop(heap)
    prev_end = e

    if idx + 1 < len(schedule[emp_id]):
        ns, ne = schedule[emp_id][idx + 1]
        heapq.heappush(heap, (ns, ne, emp_id, idx + 1))

    free = []

    while heap:
        s, e, emp_id, idx = heapq.heappop(heap)

        if s > prev_end:
            free.append([prev_end, s])
            prev_end = e
        else:
            prev_end = max(prev_end, e)

        if idx + 1 < len(schedule[emp_id]):
            ns, ne = schedule[emp_id][idx + 1]
            heapq.heappush(heap, (ns, ne, emp_id, idx + 1))

    return free
```

#### Complexity
- Time: `O(T log k)`
- Space: `O(k)`

---

## Q6. Merge K Sorted Arrays

### Problem
Given `k` sorted arrays, return one globally sorted array.

Example: `[[1,4,7],[2,5],[3,6,9]] -> [1,2,3,4,5,6,7,9]`

### Brute Force Solution

#### Pseudocode
```text
out = []
FOR each array arr:
    APPEND all values from arr to out
SORT out
RETURN out
```

#### Python
```python
def merge_k_arrays_bruteforce(arrays):
    out = []
    for arr in arrays:
        out.extend(arr)

    out.sort()
    return out
```

#### Complexity
- Time: `O(N log N)`
- Space: `O(N)`

### Optimal Solution (Classic K-Way Merge Heap)

#### Pseudocode
```text
heap = empty min-heap
FOR each array i:
    IF array non-empty:
        PUSH (arrays[i][0], i, 0)

out = []
WHILE heap not empty:
    (val, i, j) = POP heap
    APPEND val to out

    IF j + 1 < len(arrays[i]):
        PUSH (arrays[i][j + 1], i, j + 1)

RETURN out
```

#### Python
```python
import heapq


def merge_k_arrays_optimal(arrays):
    heap = []

    for i, arr in enumerate(arrays):
        if arr:
            heapq.heappush(heap, (arr[0], i, 0))

    out = []

    while heap:
        val, i, j = heapq.heappop(heap)
        out.append(val)

        if j + 1 < len(arrays[i]):
            heapq.heappush(heap, (arrays[i][j + 1], i, j + 1))

    return out
```

#### Complexity
- Time: `O(N log k)`
- Space: `O(k)` plus output

---

## Q7. Kth Smallest Number in M Sorted Lists

### Problem
Given `m` sorted lists and integer `k`, return kth smallest element in combined sorted order.

Example: `lists = [[2,6,8],[3,6,7],[1,3,4]], k = 5 -> 4`

### Brute Force Solution

#### Pseudocode
```text
flat = []
FOR each list arr:
    APPEND all values to flat
SORT flat
RETURN flat[k - 1]
```

#### Python
```python
def kth_smallest_m_lists_bruteforce(lists, k):
    flat = []
    for arr in lists:
        flat.extend(arr)

    flat.sort()
    return flat[k - 1]
```

#### Complexity
- Time: `O(N log N)`
- Space: `O(N)`

### Optimal Solution (Frontier Heap, Pop K Times)

#### Pseudocode
```text
heap = empty min-heap
FOR each list i:
    IF list non-empty:
        PUSH (lists[i][0], i, 0)

count = 0
WHILE heap not empty:
    (val, i, j) = POP heap
    count += 1
    IF count == k:
        RETURN val

    IF j + 1 < len(lists[i]):
        PUSH (lists[i][j + 1], i, j + 1)
```

#### Python
```python
import heapq


def kth_smallest_m_lists_optimal(lists, k):
    heap = []

    for i, arr in enumerate(lists):
        if arr:
            heapq.heappush(heap, (arr[0], i, 0))

    popped = 0

    while heap:
        val, i, j = heapq.heappop(heap)
        popped += 1

        if popped == k:
            return val

        if j + 1 < len(lists[i]):
            heapq.heappush(heap, (lists[i][j + 1], i, j + 1))

    return None
```

#### Complexity
- Time: `O((m + k) log m)`
- Space: `O(m)`

---

## Q8. Kth Smallest Prime Fraction

### Problem
Given sorted array `arr` containing `1` and primes, return kth smallest fraction `arr[i] / arr[j]` where `i < j`.

Example: `arr = [1,2,3,5], k = 3 -> [2,5]`

### Brute Force Solution

#### Pseudocode
```text
fractions = []
FOR i from 0 to n - 1:
    FOR j from i + 1 to n - 1:
        APPEND (arr[i]/arr[j], i, j)

SORT fractions by value
RETURN [arr[i], arr[j]] at index k - 1
```

#### Python
```python
def kth_smallest_prime_fraction_bruteforce(arr, k):
    frac = []
    n = len(arr)

    for i in range(n):
        for j in range(i + 1, n):
            frac.append((arr[i] / arr[j], i, j))

    frac.sort(key=lambda t: t[0])
    _, i, j = frac[k - 1]
    return [arr[i], arr[j]]
```

#### Complexity
- Time: `O(n^2 log n)`
- Space: `O(n^2)`

### Optimal Solution (K-Way Fraction Frontier)

#### Pseudocode
```text
n = len(arr)
heap = empty min-heap

FOR denominator j from 1 to n - 1:
    PUSH (arr[0]/arr[j], 0, j)

REPEAT k - 1 times:
    (_, i, j) = POP heap
    IF i + 1 < j:
        PUSH (arr[i + 1]/arr[j], i + 1, j)

(_, i, j) = POP heap
RETURN [arr[i], arr[j]]
```

#### Python
```python
import heapq


def kth_smallest_prime_fraction_optimal(arr, k):
    n = len(arr)
    heap = []

    for j in range(1, n):
        heapq.heappush(heap, (arr[0] / arr[j], 0, j))

    for _ in range(k - 1):
        _, i, j = heapq.heappop(heap)
        if i + 1 < j:
            heapq.heappush(heap, (arr[i + 1] / arr[j], i + 1, j))

    _, i, j = heapq.heappop(heap)
    return [arr[i], arr[j]]
```

#### Complexity
- Time: `O((n + k) log n)`
- Space: `O(n)`

---

## Q9. Find Kth Smallest Sum of a Matrix With Sorted Rows

### Problem
Given matrix `mat` where each row is sorted, choose exactly one element from each row. Return kth smallest possible sum.

Example: `mat = [[1,3,11],[2,4,6]], k = 5 -> 7`

### Brute Force Solution

#### Pseudocode
```text
all_sums = []

DFS(row, curr_sum):
    IF row == number_of_rows:
        APPEND curr_sum to all_sums
        RETURN

    FOR x in mat[row]:
        DFS(row + 1, curr_sum + x)

CALL DFS(0, 0)
SORT all_sums
RETURN all_sums[k - 1]
```

#### Python
```python
def kth_smallest_sum_matrix_bruteforce(mat, k):
    all_sums = []

    def dfs(r, curr):
        if r == len(mat):
            all_sums.append(curr)
            return

        for x in mat[r]:
            dfs(r + 1, curr + x)

    dfs(0, 0)
    all_sums.sort()
    return all_sums[k - 1]
```

#### Complexity
- Time: `O((c^r) log(c^r))` for `r` rows and `c` columns
- Space: `O(c^r)`

### Optimal Solution (Iterative K-Way Merge of Partial Sums)

#### Pseudocode
```text
FUNCTION merge_top_k_sums(a, b, k):
    # a and b sorted ascending
    heap = empty min-heap

    FOR i from 0 to min(k, len(a)) - 1:
        PUSH (a[i] + b[0], i, 0)

    out = []
    WHILE heap not empty AND len(out) < k:
        (s, i, j) = POP heap
        APPEND s to out

        IF j + 1 < len(b):
            PUSH (a[i] + b[j + 1], i, j + 1)

    RETURN out

sums = [0]
FOR each row in mat:
    sums = merge_top_k_sums(sums, row, k)

RETURN sums[k - 1]
```

#### Python
```python
import heapq


def kth_smallest_sum_matrix_optimal(mat, k):
    def merge_top_k_sums(a, b, k):
        if not a or not b:
            return []

        heap = []
        for i in range(min(k, len(a))):
            heapq.heappush(heap, (a[i] + b[0], i, 0))

        out = []
        while heap and len(out) < k:
            s, i, j = heapq.heappop(heap)
            out.append(s)

            if j + 1 < len(b):
                heapq.heappush(heap, (a[i] + b[j + 1], i, j + 1))

        return out

    sums = [0]
    for row in mat:
        sums = merge_top_k_sums(sums, row, k)

    return sums[k - 1]
```

#### Complexity
- Time: `O(r * k log k)`
- Space: `O(k)`

---

## Q10. Median of K Sorted Arrays

### Problem
Given `k` sorted arrays, return median of all elements.

Example: `[[1,3,5],[2,4,6]] -> 3.5`

### Brute Force Solution

#### Pseudocode
```text
flat = []
FOR each array arr:
    APPEND all values to flat

SORT flat
n = len(flat)

IF n odd:
    RETURN flat[n // 2]
ELSE:
    RETURN (flat[n//2 - 1] + flat[n//2]) / 2
```

#### Python
```python
def median_k_sorted_arrays_bruteforce(arrays):
    flat = []
    for arr in arrays:
        flat.extend(arr)

    flat.sort()
    n = len(flat)

    if n % 2 == 1:
        return flat[n // 2]

    return (flat[n // 2 - 1] + flat[n // 2]) / 2
```

#### Complexity
- Time: `O(N log N)`
- Space: `O(N)`

### Optimal Solution (K-Way Merge Until Middle)

#### Pseudocode
```text
heap = empty min-heap
N = total elements across arrays

FOR each array i:
    IF array non-empty:
        PUSH (arrays[i][0], i, 0)

t1 = (N - 1) // 2
t2 = N // 2
prev = curr = 0

FOR count from 0 to t2:
    (curr, i, j) = POP heap

    IF count > 0:
        prev = previous popped value

    IF j + 1 < len(arrays[i]):
        PUSH (arrays[i][j + 1], i, j + 1)

IF N odd:
    RETURN curr
ELSE:
    RETURN (prev + curr) / 2
```

#### Python
```python
import heapq


def median_k_sorted_arrays_optimal(arrays):
    heap = []
    total = 0

    for i, arr in enumerate(arrays):
        total += len(arr)
        if arr:
            heapq.heappush(heap, (arr[0], i, 0))

    if total == 0:
        return None

    t1 = (total - 1) // 2
    t2 = total // 2
    prev = None
    curr = None

    for count in range(t2 + 1):
        val, i, j = heapq.heappop(heap)
        prev, curr = curr, val

        if j + 1 < len(arrays[i]):
            heapq.heappush(heap, (arrays[i][j + 1], i, j + 1))

    if total % 2 == 1:
        return curr

    if t1 == t2:
        return curr
    return (prev + curr) / 2
```

#### Complexity
- Time: `O((N/2) log k)` worst-case `O(N log k)`
- Space: `O(k)`

---

## Rapid Recall Checklist

- Keep one candidate per source in the heap.
- Heap tuple must include enough metadata to advance that source.
- Pop best, then push next from same source.
- For range problems, track global max alongside min-heap.
- Stop early once rank objective (`k`) is achieved.
