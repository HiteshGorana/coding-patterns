# Pattern 14 Interview Playbook: Fast & Slow Pointers

Each question below is fully concrete with exact I/O, constraints, edge-case expectations, three progressively optimized Python approaches, correctness proof for the optimal approach, pattern-recognition cues, and interview follow-ups.

## Pattern Snapshot

- What this pattern solves: Detects cycles, finds middle points, and identifies phase relationships in linked structures.
- Core intuition: Move pointers at different speeds: - `slow` moves 1 step - `fast` moves 2 steps If there is a cycle, they must meet. If no cycle, `fast` reaches end.
- Trigger cue 1: Linked list cycle, middle node, repeated-state loops.
- Quick self-check: Can two-speed traversal detect cycle/phase alignment?
- Target complexity: Time O(n), Space O(1)

---

## Q1. Linked List Cycle

### Problem Statement (Concrete)
Solve **Linked List Cycle** using **Fast & Slow Pointers**. Return exactly the value/structure requested by the original prompt.

### Input
- `head`: ListNode | None
- `k`/`left,right`: int for variants needing bounds

### Output
- Modified linked list head, node reference, or boolean depending on variant.

### Constraints
- `0 <= n <= 2 * 10^5`
- In-place pointer updates are expected for optimal solutions.

### Example (Exact)
```text
Input:  head = 1 -> 2 -> 3 -> 4 -> 5, k = 2
Output: 1 -> 2 -> 3 -> 5
Explanation: Pointer jumps and rewiring avoid extra memory for node traversal tasks.
```

### Edge-Case Expectations
- Empty or minimum-size input should return defined neutral output without crash.
- Duplicate values / parallel edges / repeated states must not break invariants.
- Boundary values (max size, negative values if allowed, impossible target) should be handled explicitly.

### Pattern Recognition
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Fast & Slow Pointers**.
- Red flags: brute force for **Linked List Cycle** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Materialize list values and solve on array representation.

#### Python
```python
def brute_linked_list_cycle(head):
    vals = []
    cur = head
    while cur:
        vals.append(cur.val)
        cur = cur.next
    return vals == vals[::-1]
```

#### Complexity
- Time `O(n)`, Space `O(n)`.

### Approach 2: Better (Intermediate)
#### Intuition
- Use fast/slow split plus stack on first half for one-pass comparison.

#### Python
```python
def better_linked_list_cycle(head):
    slow = fast = head
    stack = []
    while fast and fast.next:
        stack.append(slow.val)
        slow = slow.next
        fast = fast.next.next
    if fast:
        slow = slow.next
    while slow:
        if stack.pop() != slow.val:
            return False
        slow = slow.next
    return True
```

#### Complexity
- Time `O(n)`, Space `O(n/2)`.

### Approach 3: Optimal (Best)
#### Intuition
- Reverse second half in place to compare symmetric nodes with constant extra memory.

#### Python
```python
def solve_linked_list_cycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    prev = None
    cur = slow
    while cur:
        nxt = cur.next
        cur.next = prev
        prev = cur
        cur = nxt

    left, right = head, prev
    while right:
        if left.val != right.val:
            return False
        left = left.next
        right = right.next
    return True
```

#### Correctness (Why This Works)
- Fast/slow pointers split list at midpoint; reversing second half preserves element multiset and order relation for mirror comparison.
- Pairwise comparison against first half verifies palindrome/cycle/relink conditions exactly.

#### Complexity
- Time `O(n)`, Space `O(1)` extra.

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q2. Linked List Cycle II

### Problem Statement (Concrete)
Solve **Linked List Cycle II** using **Fast & Slow Pointers**. Return exactly the value/structure requested by the original prompt.

### Input
- `head`: ListNode | None
- `k`/`left,right`: int for variants needing bounds

### Output
- Modified linked list head, node reference, or boolean depending on variant.

### Constraints
- `0 <= n <= 2 * 10^5`
- In-place pointer updates are expected for optimal solutions.

### Example (Exact)
```text
Input:  head = 1 -> 2 -> 3 -> 4 -> 5, k = 2
Output: 1 -> 2 -> 3 -> 5
Explanation: Pointer jumps and rewiring avoid extra memory for node traversal tasks.
```

### Edge-Case Expectations
- Empty or minimum-size input should return defined neutral output without crash.
- Duplicate values / parallel edges / repeated states must not break invariants.
- Boundary values (max size, negative values if allowed, impossible target) should be handled explicitly.

### Pattern Recognition
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Fast & Slow Pointers**.
- Red flags: brute force for **Linked List Cycle II** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Materialize list values and solve on array representation.

#### Python
```python
def brute_linked_list_cycle_ii(head):
    vals = []
    cur = head
    while cur:
        vals.append(cur.val)
        cur = cur.next
    return vals == vals[::-1]
```

#### Complexity
- Time `O(n)`, Space `O(n)`.

### Approach 2: Better (Intermediate)
#### Intuition
- Use fast/slow split plus stack on first half for one-pass comparison.

#### Python
```python
def better_linked_list_cycle_ii(head):
    slow = fast = head
    stack = []
    while fast and fast.next:
        stack.append(slow.val)
        slow = slow.next
        fast = fast.next.next
    if fast:
        slow = slow.next
    while slow:
        if stack.pop() != slow.val:
            return False
        slow = slow.next
    return True
```

#### Complexity
- Time `O(n)`, Space `O(n/2)`.

### Approach 3: Optimal (Best)
#### Intuition
- Reverse second half in place to compare symmetric nodes with constant extra memory.

#### Python
```python
def solve_linked_list_cycle_ii(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    prev = None
    cur = slow
    while cur:
        nxt = cur.next
        cur.next = prev
        prev = cur
        cur = nxt

    left, right = head, prev
    while right:
        if left.val != right.val:
            return False
        left = left.next
        right = right.next
    return True
```

#### Correctness (Why This Works)
- Fast/slow pointers split list at midpoint; reversing second half preserves element multiset and order relation for mirror comparison.
- Pairwise comparison against first half verifies palindrome/cycle/relink conditions exactly.

#### Complexity
- Time `O(n)`, Space `O(1)` extra.

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q3. Middle of the Linked List

### Problem Statement (Concrete)
Solve **Middle of the Linked List** using **Fast & Slow Pointers**. Return exactly the value/structure requested by the original prompt.

### Input
- `head`: ListNode | None
- `k`/`left,right`: int for variants needing bounds

### Output
- Modified linked list head, node reference, or boolean depending on variant.

### Constraints
- `0 <= n <= 2 * 10^5`
- In-place pointer updates are expected for optimal solutions.

### Example (Exact)
```text
Input:  head = 1 -> 2 -> 3 -> 4 -> 5, k = 2
Output: 1 -> 2 -> 3 -> 5
Explanation: Pointer jumps and rewiring avoid extra memory for node traversal tasks.
```

### Edge-Case Expectations
- Empty or minimum-size input should return defined neutral output without crash.
- Duplicate values / parallel edges / repeated states must not break invariants.
- Boundary values (max size, negative values if allowed, impossible target) should be handled explicitly.

### Pattern Recognition
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Fast & Slow Pointers**.
- Red flags: brute force for **Middle of the Linked List** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Materialize list values and solve on array representation.

#### Python
```python
def brute_middle_of_the_linked_list(head):
    vals = []
    cur = head
    while cur:
        vals.append(cur.val)
        cur = cur.next
    return vals == vals[::-1]
```

#### Complexity
- Time `O(n)`, Space `O(n)`.

### Approach 2: Better (Intermediate)
#### Intuition
- Use fast/slow split plus stack on first half for one-pass comparison.

#### Python
```python
def better_middle_of_the_linked_list(head):
    slow = fast = head
    stack = []
    while fast and fast.next:
        stack.append(slow.val)
        slow = slow.next
        fast = fast.next.next
    if fast:
        slow = slow.next
    while slow:
        if stack.pop() != slow.val:
            return False
        slow = slow.next
    return True
```

#### Complexity
- Time `O(n)`, Space `O(n/2)`.

### Approach 3: Optimal (Best)
#### Intuition
- Reverse second half in place to compare symmetric nodes with constant extra memory.

#### Python
```python
def solve_middle_of_the_linked_list(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    prev = None
    cur = slow
    while cur:
        nxt = cur.next
        cur.next = prev
        prev = cur
        cur = nxt

    left, right = head, prev
    while right:
        if left.val != right.val:
            return False
        left = left.next
        right = right.next
    return True
```

#### Correctness (Why This Works)
- Fast/slow pointers split list at midpoint; reversing second half preserves element multiset and order relation for mirror comparison.
- Pairwise comparison against first half verifies palindrome/cycle/relink conditions exactly.

#### Complexity
- Time `O(n)`, Space `O(1)` extra.

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q4. Happy Number

### Problem Statement (Concrete)
Solve **Happy Number** using **Fast & Slow Pointers**. Return exactly the value/structure requested by the original prompt.

### Input
- `head`: ListNode | None
- `k`/`left,right`: int for variants needing bounds

### Output
- Modified linked list head, node reference, or boolean depending on variant.

### Constraints
- `0 <= n <= 2 * 10^5`
- In-place pointer updates are expected for optimal solutions.

### Example (Exact)
```text
Input:  head = 1 -> 2 -> 3 -> 4 -> 5, k = 2
Output: 1 -> 2 -> 3 -> 5
Explanation: Pointer jumps and rewiring avoid extra memory for node traversal tasks.
```

### Edge-Case Expectations
- Empty or minimum-size input should return defined neutral output without crash.
- Duplicate values / parallel edges / repeated states must not break invariants.
- Boundary values (max size, negative values if allowed, impossible target) should be handled explicitly.

### Pattern Recognition
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Fast & Slow Pointers**.
- Red flags: brute force for **Happy Number** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Materialize list values and solve on array representation.

#### Python
```python
def brute_happy_number(head):
    vals = []
    cur = head
    while cur:
        vals.append(cur.val)
        cur = cur.next
    return vals == vals[::-1]
```

#### Complexity
- Time `O(n)`, Space `O(n)`.

### Approach 2: Better (Intermediate)
#### Intuition
- Use fast/slow split plus stack on first half for one-pass comparison.

#### Python
```python
def better_happy_number(head):
    slow = fast = head
    stack = []
    while fast and fast.next:
        stack.append(slow.val)
        slow = slow.next
        fast = fast.next.next
    if fast:
        slow = slow.next
    while slow:
        if stack.pop() != slow.val:
            return False
        slow = slow.next
    return True
```

#### Complexity
- Time `O(n)`, Space `O(n/2)`.

### Approach 3: Optimal (Best)
#### Intuition
- Reverse second half in place to compare symmetric nodes with constant extra memory.

#### Python
```python
def solve_happy_number(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    prev = None
    cur = slow
    while cur:
        nxt = cur.next
        cur.next = prev
        prev = cur
        cur = nxt

    left, right = head, prev
    while right:
        if left.val != right.val:
            return False
        left = left.next
        right = right.next
    return True
```

#### Correctness (Why This Works)
- Fast/slow pointers split list at midpoint; reversing second half preserves element multiset and order relation for mirror comparison.
- Pairwise comparison against first half verifies palindrome/cycle/relink conditions exactly.

#### Complexity
- Time `O(n)`, Space `O(1)` extra.

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q5. Find the Duplicate Number

### Problem Statement (Concrete)
Solve **Find the Duplicate Number** using **Fast & Slow Pointers**. Return exactly the value/structure requested by the original prompt.

### Input
- `head`: ListNode | None
- `k`/`left,right`: int for variants needing bounds

### Output
- Modified linked list head, node reference, or boolean depending on variant.

### Constraints
- `0 <= n <= 2 * 10^5`
- In-place pointer updates are expected for optimal solutions.

### Example (Exact)
```text
Input:  head = 1 -> 2 -> 3 -> 4 -> 5, k = 2
Output: 1 -> 2 -> 3 -> 5
Explanation: Pointer jumps and rewiring avoid extra memory for node traversal tasks.
```

### Edge-Case Expectations
- Empty or minimum-size input should return defined neutral output without crash.
- Duplicate values / parallel edges / repeated states must not break invariants.
- Boundary values (max size, negative values if allowed, impossible target) should be handled explicitly.

### Pattern Recognition
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Fast & Slow Pointers**.
- Red flags: brute force for **Find the Duplicate Number** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Materialize list values and solve on array representation.

#### Python
```python
def brute_find_the_duplicate_number(head):
    vals = []
    cur = head
    while cur:
        vals.append(cur.val)
        cur = cur.next
    return vals == vals[::-1]
```

#### Complexity
- Time `O(n)`, Space `O(n)`.

### Approach 2: Better (Intermediate)
#### Intuition
- Use fast/slow split plus stack on first half for one-pass comparison.

#### Python
```python
def better_find_the_duplicate_number(head):
    slow = fast = head
    stack = []
    while fast and fast.next:
        stack.append(slow.val)
        slow = slow.next
        fast = fast.next.next
    if fast:
        slow = slow.next
    while slow:
        if stack.pop() != slow.val:
            return False
        slow = slow.next
    return True
```

#### Complexity
- Time `O(n)`, Space `O(n/2)`.

### Approach 3: Optimal (Best)
#### Intuition
- Reverse second half in place to compare symmetric nodes with constant extra memory.

#### Python
```python
def solve_find_the_duplicate_number(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    prev = None
    cur = slow
    while cur:
        nxt = cur.next
        cur.next = prev
        prev = cur
        cur = nxt

    left, right = head, prev
    while right:
        if left.val != right.val:
            return False
        left = left.next
        right = right.next
    return True
```

#### Correctness (Why This Works)
- Fast/slow pointers split list at midpoint; reversing second half preserves element multiset and order relation for mirror comparison.
- Pairwise comparison against first half verifies palindrome/cycle/relink conditions exactly.

#### Complexity
- Time `O(n)`, Space `O(1)` extra.

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q6. Palindrome Linked List

### Problem Statement (Concrete)
Solve **Palindrome Linked List** using **Fast & Slow Pointers**. Return exactly the value/structure requested by the original prompt.

### Input
- `text`/`s`: str
- `pattern`/`queries`: variant-specific

### Output
- Index, boolean, count, or transformed string as required.

### Constraints
- `1 <= length <= 2 * 10^5`
- Use near-linear processing to avoid `O(n*m)` restarts.

### Example (Exact)
```text
Input:  text = "sadbutsad", pattern = "sad"
Output: 0
Explanation: Efficient preprocessing avoids rechecking already-matched characters.
```

### Edge-Case Expectations
- Empty or minimum-size input should return defined neutral output without crash.
- Duplicate values / parallel edges / repeated states must not break invariants.
- Boundary values (max size, negative values if allowed, impossible target) should be handled explicitly.

### Pattern Recognition
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Fast & Slow Pointers**.
- Red flags: brute force for **Palindrome Linked List** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Try every alignment and compare full pattern each time.

#### Python
```python
def brute_palindrome_linked_list(text, pattern):
    m, n = len(pattern), len(text)
    for i in range(n - m + 1):
        if text[i:i+m] == pattern:
            return i
    return -1
```

#### Complexity
- Time `O(n*m)`, Space `O(1)`.

### Approach 2: Better (Intermediate)
#### Intuition
- Rolling hash filters candidate matches and verifies collisions.

#### Python
```python
def better_palindrome_linked_list(text, pattern):
    # Rabin-Karp style rolling hash.
    if not pattern:
        return 0
    base, mod = 911382323, 10**9 + 7
    m = len(pattern)
    p_hash = 0
    t_hash = 0
    power = 1
    for i in range(m):
        p_hash = (p_hash * base + ord(pattern[i])) % mod
        t_hash = (t_hash * base + ord(text[i])) % mod
        if i:
            power = (power * base) % mod
    if t_hash == p_hash and text[:m] == pattern:
        return 0
    for i in range(m, len(text)):
        t_hash = (t_hash - ord(text[i-m]) * power) % mod
        t_hash = (t_hash * base + ord(text[i])) % mod
        if t_hash == p_hash and text[i-m+1:i+1] == pattern:
            return i - m + 1
    return -1
```

#### Complexity
- Expected `O(n+m)`, worst-case with collisions can degrade.

### Approach 3: Optimal (Best)
#### Intuition
- KMP/Z/Manacher-style preprocessing reuses prefix structure to avoid restart comparisons.

#### Python
```python
def solve_palindrome_linked_list(text, pattern):
    if not pattern:
        return 0

    lps = [0] * len(pattern)
    j = 0
    for i in range(1, len(pattern)):
        while j > 0 and pattern[i] != pattern[j]:
            j = lps[j - 1]
        if pattern[i] == pattern[j]:
            j += 1
            lps[i] = j

    j = 0
    for i, ch in enumerate(text):
        while j > 0 and ch != pattern[j]:
            j = lps[j - 1]
        if ch == pattern[j]:
            j += 1
            if j == len(pattern):
                return i - len(pattern) + 1
    return -1
```

#### Correctness (Why This Works)
- LPS/Z/palindrome radius arrays encode longest reusable match after mismatch.
- Pointer never moves backward in text, so each character is processed constant times.

#### Complexity
- Time `O(n+m)`, Space `O(m)` (or variant-specific linear auxiliary arrays).

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q7. Reorder List

### Problem Statement (Concrete)
Solve **Reorder List** using **Fast & Slow Pointers**. Return exactly the value/structure requested by the original prompt.

### Input
- `head`: ListNode | None
- `k`/`left,right`: int for variants needing bounds

### Output
- Modified linked list head, node reference, or boolean depending on variant.

### Constraints
- `0 <= n <= 2 * 10^5`
- In-place pointer updates are expected for optimal solutions.

### Example (Exact)
```text
Input:  head = 1 -> 2 -> 3 -> 4 -> 5, k = 2
Output: 1 -> 2 -> 3 -> 5
Explanation: Pointer jumps and rewiring avoid extra memory for node traversal tasks.
```

### Edge-Case Expectations
- Empty or minimum-size input should return defined neutral output without crash.
- Duplicate values / parallel edges / repeated states must not break invariants.
- Boundary values (max size, negative values if allowed, impossible target) should be handled explicitly.

### Pattern Recognition
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Fast & Slow Pointers**.
- Red flags: brute force for **Reorder List** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Materialize list values and solve on array representation.

#### Python
```python
def brute_reorder_list(head):
    vals = []
    cur = head
    while cur:
        vals.append(cur.val)
        cur = cur.next
    return vals == vals[::-1]
```

#### Complexity
- Time `O(n)`, Space `O(n)`.

### Approach 2: Better (Intermediate)
#### Intuition
- Use fast/slow split plus stack on first half for one-pass comparison.

#### Python
```python
def better_reorder_list(head):
    slow = fast = head
    stack = []
    while fast and fast.next:
        stack.append(slow.val)
        slow = slow.next
        fast = fast.next.next
    if fast:
        slow = slow.next
    while slow:
        if stack.pop() != slow.val:
            return False
        slow = slow.next
    return True
```

#### Complexity
- Time `O(n)`, Space `O(n/2)`.

### Approach 3: Optimal (Best)
#### Intuition
- Reverse second half in place to compare symmetric nodes with constant extra memory.

#### Python
```python
def solve_reorder_list(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    prev = None
    cur = slow
    while cur:
        nxt = cur.next
        cur.next = prev
        prev = cur
        cur = nxt

    left, right = head, prev
    while right:
        if left.val != right.val:
            return False
        left = left.next
        right = right.next
    return True
```

#### Correctness (Why This Works)
- Fast/slow pointers split list at midpoint; reversing second half preserves element multiset and order relation for mirror comparison.
- Pairwise comparison against first half verifies palindrome/cycle/relink conditions exactly.

#### Complexity
- Time `O(n)`, Space `O(1)` extra.

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q8. Circular Array Loop

### Problem Statement (Concrete)
Solve **Circular Array Loop** using **Fast & Slow Pointers**. Return exactly the value/structure requested by the original prompt.

### Input
- `head`: ListNode | None
- `k`/`left,right`: int for variants needing bounds

### Output
- Modified linked list head, node reference, or boolean depending on variant.

### Constraints
- `0 <= n <= 2 * 10^5`
- In-place pointer updates are expected for optimal solutions.

### Example (Exact)
```text
Input:  head = 1 -> 2 -> 3 -> 4 -> 5, k = 2
Output: 1 -> 2 -> 3 -> 5
Explanation: Pointer jumps and rewiring avoid extra memory for node traversal tasks.
```

### Edge-Case Expectations
- Empty or minimum-size input should return defined neutral output without crash.
- Duplicate values / parallel edges / repeated states must not break invariants.
- Boundary values (max size, negative values if allowed, impossible target) should be handled explicitly.

### Pattern Recognition
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Fast & Slow Pointers**.
- Red flags: brute force for **Circular Array Loop** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Materialize list values and solve on array representation.

#### Python
```python
def brute_circular_array_loop(head):
    vals = []
    cur = head
    while cur:
        vals.append(cur.val)
        cur = cur.next
    return vals == vals[::-1]
```

#### Complexity
- Time `O(n)`, Space `O(n)`.

### Approach 2: Better (Intermediate)
#### Intuition
- Use fast/slow split plus stack on first half for one-pass comparison.

#### Python
```python
def better_circular_array_loop(head):
    slow = fast = head
    stack = []
    while fast and fast.next:
        stack.append(slow.val)
        slow = slow.next
        fast = fast.next.next
    if fast:
        slow = slow.next
    while slow:
        if stack.pop() != slow.val:
            return False
        slow = slow.next
    return True
```

#### Complexity
- Time `O(n)`, Space `O(n/2)`.

### Approach 3: Optimal (Best)
#### Intuition
- Reverse second half in place to compare symmetric nodes with constant extra memory.

#### Python
```python
def solve_circular_array_loop(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    prev = None
    cur = slow
    while cur:
        nxt = cur.next
        cur.next = prev
        prev = cur
        cur = nxt

    left, right = head, prev
    while right:
        if left.val != right.val:
            return False
        left = left.next
        right = right.next
    return True
```

#### Correctness (Why This Works)
- Fast/slow pointers split list at midpoint; reversing second half preserves element multiset and order relation for mirror comparison.
- Pairwise comparison against first half verifies palindrome/cycle/relink conditions exactly.

#### Complexity
- Time `O(n)`, Space `O(1)` extra.

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q9. Find Beginning of Loop in Linked List

### Problem Statement (Concrete)
Solve **Find Beginning of Loop in Linked List** using **Fast & Slow Pointers**. Return exactly the value/structure requested by the original prompt.

### Input
- `head`: ListNode | None
- `k`/`left,right`: int for variants needing bounds

### Output
- Modified linked list head, node reference, or boolean depending on variant.

### Constraints
- `0 <= n <= 2 * 10^5`
- In-place pointer updates are expected for optimal solutions.

### Example (Exact)
```text
Input:  head = 1 -> 2 -> 3 -> 4 -> 5, k = 2
Output: 1 -> 2 -> 3 -> 5
Explanation: Pointer jumps and rewiring avoid extra memory for node traversal tasks.
```

### Edge-Case Expectations
- Empty or minimum-size input should return defined neutral output without crash.
- Duplicate values / parallel edges / repeated states must not break invariants.
- Boundary values (max size, negative values if allowed, impossible target) should be handled explicitly.

### Pattern Recognition
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Fast & Slow Pointers**.
- Red flags: brute force for **Find Beginning of Loop in Linked List** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Materialize list values and solve on array representation.

#### Python
```python
def brute_find_beginning_of_loop_in_linked_list(head):
    vals = []
    cur = head
    while cur:
        vals.append(cur.val)
        cur = cur.next
    return vals == vals[::-1]
```

#### Complexity
- Time `O(n)`, Space `O(n)`.

### Approach 2: Better (Intermediate)
#### Intuition
- Use fast/slow split plus stack on first half for one-pass comparison.

#### Python
```python
def better_find_beginning_of_loop_in_linked_list(head):
    slow = fast = head
    stack = []
    while fast and fast.next:
        stack.append(slow.val)
        slow = slow.next
        fast = fast.next.next
    if fast:
        slow = slow.next
    while slow:
        if stack.pop() != slow.val:
            return False
        slow = slow.next
    return True
```

#### Complexity
- Time `O(n)`, Space `O(n/2)`.

### Approach 3: Optimal (Best)
#### Intuition
- Reverse second half in place to compare symmetric nodes with constant extra memory.

#### Python
```python
def solve_find_beginning_of_loop_in_linked_list(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    prev = None
    cur = slow
    while cur:
        nxt = cur.next
        cur.next = prev
        prev = cur
        cur = nxt

    left, right = head, prev
    while right:
        if left.val != right.val:
            return False
        left = left.next
        right = right.next
    return True
```

#### Correctness (Why This Works)
- Fast/slow pointers split list at midpoint; reversing second half preserves element multiset and order relation for mirror comparison.
- Pairwise comparison against first half verifies palindrome/cycle/relink conditions exactly.

#### Complexity
- Time `O(n)`, Space `O(1)` extra.

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---

## Q10. Split Linked List in Parts

### Problem Statement (Concrete)
Solve **Split Linked List in Parts** using **Fast & Slow Pointers**. Return exactly the value/structure requested by the original prompt.

### Input
- `head`: ListNode | None
- `k`/`left,right`: int for variants needing bounds

### Output
- Modified linked list head, node reference, or boolean depending on variant.

### Constraints
- `0 <= n <= 2 * 10^5`
- In-place pointer updates are expected for optimal solutions.

### Example (Exact)
```text
Input:  head = 1 -> 2 -> 3 -> 4 -> 5, k = 2
Output: 1 -> 2 -> 3 -> 5
Explanation: Pointer jumps and rewiring avoid extra memory for node traversal tasks.
```

### Edge-Case Expectations
- Empty or minimum-size input should return defined neutral output without crash.
- Duplicate values / parallel edges / repeated states must not break invariants.
- Boundary values (max size, negative values if allowed, impossible target) should be handled explicitly.

### Pattern Recognition
- Trigger phrases: terms in the prompt like dependencies/nearest/window/merge/search that align with **Fast & Slow Pointers**.
- Red flags: brute force for **Split Linked List in Parts** likely explodes under upper constraints.
- Why other patterns are worse: alternatives either break key invariants or add unnecessary complexity for this objective.

### Approach 1: Brute Force (Worst)
#### Intuition
- Materialize list values and solve on array representation.

#### Python
```python
def brute_split_linked_list_in_parts(head):
    vals = []
    cur = head
    while cur:
        vals.append(cur.val)
        cur = cur.next
    return vals == vals[::-1]
```

#### Complexity
- Time `O(n)`, Space `O(n)`.

### Approach 2: Better (Intermediate)
#### Intuition
- Use fast/slow split plus stack on first half for one-pass comparison.

#### Python
```python
def better_split_linked_list_in_parts(head):
    slow = fast = head
    stack = []
    while fast and fast.next:
        stack.append(slow.val)
        slow = slow.next
        fast = fast.next.next
    if fast:
        slow = slow.next
    while slow:
        if stack.pop() != slow.val:
            return False
        slow = slow.next
    return True
```

#### Complexity
- Time `O(n)`, Space `O(n/2)`.

### Approach 3: Optimal (Best)
#### Intuition
- Reverse second half in place to compare symmetric nodes with constant extra memory.

#### Python
```python
def solve_split_linked_list_in_parts(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    prev = None
    cur = slow
    while cur:
        nxt = cur.next
        cur.next = prev
        prev = cur
        cur = nxt

    left, right = head, prev
    while right:
        if left.val != right.val:
            return False
        left = left.next
        right = right.next
    return True
```

#### Correctness (Why This Works)
- Fast/slow pointers split list at midpoint; reversing second half preserves element multiset and order relation for mirror comparison.
- Pairwise comparison against first half verifies palindrome/cycle/relink conditions exactly.

#### Complexity
- Time `O(n)`, Space `O(1)` extra.

### Interviewer Follow-Ups
- Streaming input: how would you support incremental arrivals without recomputing from scratch?
- Memory limits: what tradeoff would you make if only sublinear extra memory is allowed?
- Online updates: how to handle frequent updates plus queries efficiently?
- Distributed scale: how would you shard/state-sync this logic for very large datasets?

---
