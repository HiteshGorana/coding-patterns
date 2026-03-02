# Pattern 14 Interview Playbook: Fast & Slow Pointers

This playbook is aligned with [Pattern 14: Fast & Slow Pointers](../14-fast-slow-pointers.md).

Use it when the prompt involves cycle detection, middle finding, or phase alignment in linked structures/sequences.

## Pattern Snapshot

| Prompt shape | Pointer speeds | Outcome |
|---|---|---|
| detect cycle in linked list | `slow +1`, `fast +2` | meet => cycle |
| find cycle entry | meet first, then reset one pointer to head | second meet => entry |
| middle of linked list | `slow +1`, `fast +2` until end | `slow` at middle |
| sequence cycle (happy number) | apply transition function with two speeds | detect loop without hash set |
| compare list halves | use fast/slow to split, reverse second half | `O(1)` extra symmetry check |
| one-pass nth-from-end | keep fixed gap between fast and slow | slow lands before target |

## Query-Update Rules

- Always guard `fast` and `fast.next` before jumping two steps.
- Use node identity (`is`) for linked list cycle detection.
- For cycle-entry problems: after first meet, reset one pointer to head and move both by one.
- For odd-length split logic, skip middle node when needed before comparing halves.
- For one-pass removal, create a dummy head and keep `n`-step gap.

---

## Q1. Linked List Cycle

### Problem
Given `head` of a linked list, return `True` if the list contains a cycle, else `False`.

Example: `3 -> 2 -> 0 -> -4` with tail connecting to node index `1` -> `True`

### Brute Force Solution

#### Pseudocode
```text
seen = empty set
cur = head

WHILE cur is not null:
    IF cur in seen:
        RETURN True
    ADD cur to seen
    cur = cur.next

RETURN False
```

#### Python
```python
def has_cycle_bruteforce(head):
    seen = set()
    cur = head

    while cur:
        if cur in seen:
            return True
        seen.add(cur)
        cur = cur.next

    return False
```

#### Complexity
- Time: `O(n)`
- Space: `O(n)`

### Optimal Solution (Floyd's Tortoise and Hare)

#### Pseudocode
```text
slow = head
fast = head

WHILE fast is not null AND fast.next is not null:
    slow = slow.next
    fast = fast.next.next

    IF slow == fast:
        RETURN True

RETURN False
```

#### Python
```python
def has_cycle_optimal(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow is fast:
            return True

    return False
```

#### Complexity
- Time: `O(n)`
- Space: `O(1)`

---

## Q2. Linked List Cycle II

### Problem
Given `head` of a linked list, return the node where the cycle begins. If no cycle, return `None`.

Example: `3 -> 2 -> 0 -> -4` with tail connecting to node index `1` -> return node with value `2`

### Brute Force Solution

#### Pseudocode
```text
seen = empty set
cur = head

WHILE cur is not null:
    IF cur in seen:
        RETURN cur
    ADD cur to seen
    cur = cur.next

RETURN null
```

#### Python
```python
def detect_cycle_start_bruteforce(head):
    seen = set()
    cur = head

    while cur:
        if cur in seen:
            return cur
        seen.add(cur)
        cur = cur.next

    return None
```

#### Complexity
- Time: `O(n)`
- Space: `O(n)`

### Optimal Solution (Floyd Meet + Reset)

#### Pseudocode
```text
slow = head
fast = head

WHILE fast and fast.next:
    slow = slow.next
    fast = fast.next.next
    IF slow == fast:
        BREAK

IF no meeting happened:
    RETURN null

p1 = head
p2 = slow
WHILE p1 != p2:
    p1 = p1.next
    p2 = p2.next

RETURN p1
```

#### Python
```python
def detect_cycle_start_optimal(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            break
    else:
        return None

    p1 = head
    p2 = slow

    while p1 is not p2:
        p1 = p1.next
        p2 = p2.next

    return p1
```

#### Complexity
- Time: `O(n)`
- Space: `O(1)`

---

## Q3. Middle of the Linked List

### Problem
Given `head` of a singly linked list, return the middle node. If two middle nodes exist, return the second one.

Example: `1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8` -> return node with value `5`

### Brute Force Solution

#### Pseudocode
```text
n = 0
cur = head
WHILE cur:
    n += 1
    cur = cur.next

steps = n // 2
cur = head
REPEAT steps times:
    cur = cur.next

RETURN cur
```

#### Python
```python
def middle_node_bruteforce(head):
    n = 0
    cur = head

    while cur:
        n += 1
        cur = cur.next

    cur = head
    for _ in range(n // 2):
        cur = cur.next

    return cur
```

#### Complexity
- Time: `O(n)`
- Space: `O(1)`

### Optimal Solution (Fast + Slow in One Pass)

#### Pseudocode
```text
slow = head
fast = head

WHILE fast and fast.next:
    slow = slow.next
    fast = fast.next.next

RETURN slow
```

#### Python
```python
def middle_node_optimal(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow
```

#### Complexity
- Time: `O(n)`
- Space: `O(1)`

---

## Q4. Happy Number

### Problem
Given integer `n`, return `True` if it is a happy number, else `False`.

Example: `n = 19 -> True`

### Brute Force Solution

#### Pseudocode
```text
FUNCTION next_num(x):
    sum = 0
    WHILE x > 0:
        digit = x mod 10
        sum += digit * digit
        x = x // 10
    RETURN sum

seen = empty set
WHILE n != 1 AND n not in seen:
    ADD n to seen
    n = next_num(n)

RETURN n == 1
```

#### Python
```python
def is_happy_bruteforce(n):
    def next_num(x):
        s = 0
        while x > 0:
            d = x % 10
            s += d * d
            x //= 10
        return s

    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = next_num(n)

    return n == 1
```

#### Complexity
- Time: `O(m)` transitions until repeat/1
- Space: `O(m)`

### Optimal Solution (Cycle Detection on Number Sequence)

#### Pseudocode
```text
FUNCTION next_num(x): ...

slow = n
fast = n

REPEAT:
    slow = next_num(slow)
    fast = next_num(next_num(fast))
UNTIL slow == fast

RETURN slow == 1
```

#### Python
```python
def is_happy_optimal(n):
    def next_num(x):
        s = 0
        while x > 0:
            d = x % 10
            s += d * d
            x //= 10
        return s

    slow = n
    fast = n

    while True:
        slow = next_num(slow)
        fast = next_num(next_num(fast))
        if slow == fast:
            break

    return slow == 1
```

#### Complexity
- Time: `O(m)`
- Space: `O(1)`

---

## Q5. Find the Duplicate Number

### Problem
Given `nums` of length `n + 1` where each number is in `[1, n]`, return the duplicate number.

Example: `nums = [1,3,4,2,2] -> 2`

### Brute Force Solution

#### Pseudocode
```text
seen = empty set
FOR x in nums:
    IF x in seen:
        RETURN x
    ADD x to seen
```

#### Python
```python
def find_duplicate_bruteforce(nums):
    seen = set()

    for x in nums:
        if x in seen:
            return x
        seen.add(x)

    return -1
```

#### Complexity
- Time: `O(n)`
- Space: `O(n)`

### Optimal Solution (Floyd on Implicit Linked List)

#### Pseudocode
```text
slow = nums[0]
fast = nums[0]

REPEAT:
    slow = nums[slow]
    fast = nums[nums[fast]]
UNTIL slow == fast

finder = nums[0]
WHILE finder != slow:
    finder = nums[finder]
    slow = nums[slow]

RETURN finder
```

#### Python
```python
def find_duplicate_optimal(nums):
    slow = nums[0]
    fast = nums[0]

    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break

    finder = nums[0]
    while finder != slow:
        finder = nums[finder]
        slow = nums[slow]

    return finder
```

#### Complexity
- Time: `O(n)`
- Space: `O(1)`

---

## Q6. Palindrome Linked List

### Problem
Given `head` of a linked list, return `True` if it is a palindrome, else `False`.

Example: `1 -> 2 -> 2 -> 1 -> True`

### Brute Force Solution

#### Pseudocode
```text
vals = []
cur = head
WHILE cur:
    APPEND cur.val to vals
    cur = cur.next

RETURN vals == reverse(vals)
```

#### Python
```python
def is_palindrome_list_bruteforce(head):
    vals = []
    cur = head

    while cur:
        vals.append(cur.val)
        cur = cur.next

    return vals == vals[::-1]
```

#### Complexity
- Time: `O(n)`
- Space: `O(n)`

### Optimal Solution (Split + Reverse Second Half)

#### Pseudocode
```text
IF head is null OR head.next is null:
    RETURN True

slow = head
fast = head
WHILE fast and fast.next:
    slow = slow.next
    fast = fast.next.next

IF fast is not null:   # odd length
    slow = slow.next

reverse list starting at slow -> right_head
left = head
right = right_head
WHILE right:
    IF left.val != right.val:
        RETURN False
    left = left.next
    right = right.next

RETURN True
```

#### Python
```python
def is_palindrome_list_optimal(head):
    if not head or not head.next:
        return True

    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    if fast:
        slow = slow.next

    prev = None
    cur = slow
    while cur:
        nxt = cur.next
        cur.next = prev
        prev = cur
        cur = nxt

    left = head
    right = prev
    while right:
        if left.val != right.val:
            return False
        left = left.next
        right = right.next

    return True
```

#### Complexity
- Time: `O(n)`
- Space: `O(1)` extra

---

## Q7. Reorder List

### Problem
Given list `L0 -> L1 -> ... -> Ln`, reorder it to `L0 -> Ln -> L1 -> Ln-1 -> ...`.

Example: `1 -> 2 -> 3 -> 4 -> 5` becomes `1 -> 5 -> 2 -> 4 -> 3`

### Brute Force Solution

#### Pseudocode
```text
nodes = []
cur = head
WHILE cur:
    APPEND cur to nodes
    cur = cur.next

i = 0
j = len(nodes) - 1
WHILE i < j:
    nodes[i].next = nodes[j]
    i += 1
    IF i == j:
        BREAK
    nodes[j].next = nodes[i]
    j -= 1

nodes[i].next = null
```

#### Python
```python
def reorder_list_bruteforce(head):
    if not head:
        return

    nodes = []
    cur = head
    while cur:
        nodes.append(cur)
        cur = cur.next

    i, j = 0, len(nodes) - 1
    while i < j:
        nodes[i].next = nodes[j]
        i += 1

        if i == j:
            break

        nodes[j].next = nodes[i]
        j -= 1

    nodes[i].next = None
```

#### Complexity
- Time: `O(n)`
- Space: `O(n)`

### Optimal Solution (Middle + Reverse + Merge)

#### Pseudocode
```text
IF head null OR head.next null:
    RETURN

# find middle
slow = head
fast = head
WHILE fast.next and fast.next.next:
    slow = slow.next
    fast = fast.next.next

# split and reverse second half
second = slow.next
slow.next = null
reverse second -> rev

# merge first and reversed second
first = head
WHILE rev:
    t1 = first.next
    t2 = rev.next

    first.next = rev
    rev.next = t1

    first = t1
    rev = t2
```

#### Python
```python
def reorder_list_optimal(head):
    if not head or not head.next:
        return

    slow = head
    fast = head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    second = slow.next
    slow.next = None

    prev = None
    cur = second
    while cur:
        nxt = cur.next
        cur.next = prev
        prev = cur
        cur = nxt

    first = head
    second = prev
    while second:
        t1 = first.next
        t2 = second.next

        first.next = second
        second.next = t1

        first = t1
        second = t2
```

#### Complexity
- Time: `O(n)`
- Space: `O(1)` extra

---

## Q8. Remove Nth Node From End of List

### Problem
Given `head` and integer `n`, remove the nth node from the end and return head.

Example: `1 -> 2 -> 3 -> 4 -> 5, n = 2 -> 1 -> 2 -> 3 -> 5`

### Brute Force Solution

#### Pseudocode
```text
length = 0
cur = head
WHILE cur:
    length += 1
    cur = cur.next

idx_from_start = length - n
IF idx_from_start == 0:
    RETURN head.next

cur = head
REPEAT idx_from_start - 1 times:
    cur = cur.next

cur.next = cur.next.next
RETURN head
```

#### Python
```python
def remove_nth_from_end_bruteforce(head, n):
    length = 0
    cur = head

    while cur:
        length += 1
        cur = cur.next

    idx = length - n
    if idx == 0:
        return head.next

    cur = head
    for _ in range(idx - 1):
        cur = cur.next

    cur.next = cur.next.next
    return head
```

#### Complexity
- Time: `O(n)`
- Space: `O(1)`

### Optimal Solution (One Pass with Fixed Gap)

#### Pseudocode
```text
dummy = new node pointing to head
fast = dummy
slow = dummy

REPEAT n times:
    fast = fast.next

WHILE fast.next:
    fast = fast.next
    slow = slow.next

slow.next = slow.next.next
RETURN dummy.next
```

#### Python
```python
def remove_nth_from_end_optimal(head, n):
    dummy = ListNode(0, head)
    fast = dummy
    slow = dummy

    for _ in range(n):
        fast = fast.next

    while fast.next:
        fast = fast.next
        slow = slow.next

    slow.next = slow.next.next
    return dummy.next
```

#### Complexity
- Time: `O(n)`
- Space: `O(1)`

---

## Q9. Circular Array Loop

### Problem
Given circular array `nums` where each value is jump length (positive forward, negative backward), return `True` if there is a cycle of length > 1 with same direction.

Example: `nums = [2,-1,1,2,2] -> True`

### Brute Force Solution

#### Pseudocode
```text
n = len(nums)

FOR each start in [0..n-1]:
    direction = nums[start] > 0
    seen_step = empty map
    idx = start
    step = 0

    WHILE True:
        IF direction of nums[idx] differs:
            BREAK

        next_idx = (idx + nums[idx]) mod n
        IF next_idx == idx:
            BREAK

        IF idx in seen_step:
            IF step - seen_step[idx] > 1:
                RETURN True
            BREAK

        seen_step[idx] = step
        idx = next_idx
        step += 1

RETURN False
```

#### Python
```python
def circular_array_loop_bruteforce(nums):
    n = len(nums)

    for start in range(n):
        direction = nums[start] > 0
        seen_step = {}
        idx = start
        step = 0

        while True:
            if (nums[idx] > 0) != direction:
                break

            nxt = (idx + nums[idx]) % n
            if nxt == idx:
                break

            if idx in seen_step:
                if step - seen_step[idx] > 1:
                    return True
                break

            seen_step[idx] = step
            idx = nxt
            step += 1

    return False
```

#### Complexity
- Time: `O(n^2)`
- Space: `O(n)` per start in worst case

### Optimal Solution (Fast/Slow with Direction Guard)

#### Pseudocode
```text
FUNCTION advance(nums, i, direction):
    IF direction of nums[i] differs:
        RETURN -1

    nxt = (i + nums[i]) mod n
    IF nxt == i:    # 1-length loop invalid
        RETURN -1

    RETURN nxt

FOR each index i:
    IF nums[i] == 0:
        CONTINUE

    direction = nums[i] > 0
    slow = i
    fast = i

    WHILE True:
        slow = advance(nums, slow, direction)
        fast = advance(nums, fast, direction)
        IF fast != -1:
            fast = advance(nums, fast, direction)

        IF slow == -1 OR fast == -1:
            BREAK
        IF slow == fast:
            RETURN True

    # cleanup this traversal path to avoid rework
    idx = i
    WHILE nums[idx] != 0 AND (nums[idx] > 0) == direction:
        nxt = (idx + nums[idx]) mod n
        nums[idx] = 0
        idx = nxt

RETURN False
```

#### Python
```python
def circular_array_loop_optimal(nums):
    n = len(nums)

    def advance(i, direction):
        if (nums[i] > 0) != direction:
            return -1

        nxt = (i + nums[i]) % n
        if nxt == i:
            return -1

        return nxt

    for i in range(n):
        if nums[i] == 0:
            continue

        direction = nums[i] > 0
        slow = i
        fast = i

        while True:
            slow = advance(slow, direction)
            fast = advance(fast, direction)
            if fast != -1:
                fast = advance(fast, direction)

            if slow == -1 or fast == -1:
                break

            if slow == fast:
                return True

        idx = i
        while nums[idx] != 0 and (nums[idx] > 0) == direction:
            nxt = (idx + nums[idx]) % n
            nums[idx] = 0
            idx = nxt

    return False
```

#### Complexity
- Time: `O(n)` amortized
- Space: `O(1)`

---

## Q10. Maximum Twin Sum of a Linked List

### Problem
Given an even-length linked list, twin of node `i` is node `n-1-i`. Return maximum twin sum.

Example: `5 -> 4 -> 2 -> 1 -> 6 -> 3` -> max twin sum is `11`

### Brute Force Solution

#### Pseudocode
```text
vals = []
cur = head
WHILE cur:
    APPEND cur.val
    cur = cur.next

best = 0
n = len(vals)
FOR i from 0 to n/2 - 1:
    best = max(best, vals[i] + vals[n - 1 - i])

RETURN best
```

#### Python
```python
def pair_sum_bruteforce(head):
    vals = []
    cur = head

    while cur:
        vals.append(cur.val)
        cur = cur.next

    best = 0
    n = len(vals)

    for i in range(n // 2):
        best = max(best, vals[i] + vals[n - 1 - i])

    return best
```

#### Complexity
- Time: `O(n)`
- Space: `O(n)`

### Optimal Solution (Middle + Reverse + Pair Scan)

#### Pseudocode
```text
slow = head
fast = head
WHILE fast and fast.next:
    slow = slow.next
    fast = fast.next.next

reverse list starting at slow -> right
left = head
best = 0

WHILE right:
    best = max(best, left.val + right.val)
    left = left.next
    right = right.next

RETURN best
```

#### Python
```python
def pair_sum_optimal(head):
    slow = head
    fast = head

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

    left = head
    right = prev
    best = 0

    while right:
        best = max(best, left.val + right.val)
        left = left.next
        right = right.next

    return best
```

#### Complexity
- Time: `O(n)`
- Space: `O(1)` extra

---

## Rapid Recall Checklist

- Cycle detect: `slow +1`, `fast +2`, identity comparison.
- Cycle entry: after first meet, reset one pointer to head.
- Middle: second middle is returned when using `while fast and fast.next`.
- Half-compare problems: find middle, reverse second half, compare/merge.
- One-pass removal from end: keep a fixed pointer gap with a dummy head.
