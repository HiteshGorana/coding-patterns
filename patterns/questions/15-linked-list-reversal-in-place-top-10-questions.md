# Pattern 15 Interview Playbook: Linked List Reversal / In-Place Operations

This playbook is aligned with [Pattern 15: Linked List Reversal / In-place Operations](../15-linked-list-reversal-in-place.md).

Use it when the prompt asks for full/partial/block linked-list reversal with `O(1)` auxiliary pointer rewiring.

## Pattern Snapshot

| Prompt shape | Core pointers | Reconnect focus |
|---|---|---|
| reverse full list | `prev, curr, nxt` | return `prev` as new head |
| reverse sublist `[left, right]` | `pre_left, curr, nxt` | connect boundary nodes |
| reverse nodes in k-group | `group_prev, kth, group_next` | reconnect group tail/head |
| pair swap / small blocks | local two-node rewires | preserve chain continuity |
| split + reverse + merge | middle + reverse second half | weave lists safely |
| rotation via cycle break | `tail`, `new_tail` | cut circular link at right spot |

## Query-Update Rules

- Save `nxt = curr.next` before rewriting `curr.next`.
- Use a dummy head when operation may change original head.
- For segment reversals, track both predecessor and successor boundaries.
- For k-group reversal, verify group length before rewiring.
- After reversal, ensure tail points to remaining unreversed list.

---

## Q1. Reverse Linked List

### Problem
Given the head of a singly linked list, reverse the list and return the new head.

Example: `1 -> 2 -> 3 -> 4 -> 5` -> `5 -> 4 -> 3 -> 2 -> 1`

### Brute Force Solution

#### Pseudocode
```text
vals = []
cur = head
WHILE cur exists:
    APPEND cur.val to vals
    cur = cur.next

reverse vals
BUILD new linked list from vals
RETURN new head
```

#### Python
```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse_list_bruteforce(head):
    vals = []
    cur = head

    while cur:
        vals.append(cur.val)
        cur = cur.next

    vals.reverse()

    dummy = ListNode(0)
    tail = dummy
    for x in vals:
        tail.next = ListNode(x)
        tail = tail.next

    return dummy.next
```

#### Complexity
- Time: `O(n)`
- Space: `O(n)`

### Optimal Solution (In-Place Iterative Reverse)

#### Pseudocode
```text
prev = null
curr = head

WHILE curr exists:
    nxt = curr.next
    curr.next = prev
    prev = curr
    curr = nxt

RETURN prev
```

#### Python
```python
def reverse_list_optimal(head):
    prev = None
    curr = head

    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt

    return prev
```

#### Complexity
- Time: `O(n)`
- Space: `O(1)`

---

## Q2. Reverse Linked List II

### Problem
Given `head`, `left`, and `right`, reverse nodes from position `left` to `right` (1-indexed) and return head.

Example: `1 -> 2 -> 3 -> 4 -> 5`, `left = 2`, `right = 4` -> `1 -> 4 -> 3 -> 2 -> 5`

### Brute Force Solution

#### Pseudocode
```text
vals = linked list values as array
REVERSE vals[left-1 : right]
BUILD and RETURN new list from vals
```

#### Python
```python
def reverse_between_bruteforce(head, left, right):
    vals = []
    cur = head

    while cur:
        vals.append(cur.val)
        cur = cur.next

    i = left - 1
    j = right
    vals[i:j] = reversed(vals[i:j])

    dummy = ListNode(0)
    tail = dummy
    for x in vals:
        tail.next = ListNode(x)
        tail = tail.next

    return dummy.next
```

#### Complexity
- Time: `O(n)`
- Space: `O(n)`

### Optimal Solution (Boundary Rewire)

#### Pseudocode
```text
dummy.next = head
pre = dummy
MOVE pre to node before position left

curr = pre.next
prev = null
REPEAT right - left + 1 times:
    nxt = curr.next
    curr.next = prev
    prev = curr
    curr = nxt

left_tail = pre.next
pre.next = prev
left_tail.next = curr

RETURN dummy.next
```

#### Python
```python
def reverse_between_optimal(head, left, right):
    if not head or left == right:
        return head

    dummy = ListNode(0, head)
    pre = dummy

    for _ in range(left - 1):
        pre = pre.next

    curr = pre.next
    prev = None

    for _ in range(right - left + 1):
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt

    left_tail = pre.next
    pre.next = prev
    left_tail.next = curr

    return dummy.next
```

#### Complexity
- Time: `O(n)`
- Space: `O(1)`

---

## Q3. Reverse Nodes in k-Group

### Problem
Given `head` and `k`, reverse nodes in groups of size `k`. Remaining nodes less than `k` stay as-is.

Example: `1 -> 2 -> 3 -> 4 -> 5`, `k = 2` -> `2 -> 1 -> 4 -> 3 -> 5`

### Brute Force Solution

#### Pseudocode
```text
vals = values array
FOR i from 0 to n-1 step k:
    IF i + k <= n:
        REVERSE vals[i : i+k]

BUILD and RETURN new list from vals
```

#### Python
```python
def reverse_k_group_bruteforce(head, k):
    vals = []
    cur = head

    while cur:
        vals.append(cur.val)
        cur = cur.next

    for i in range(0, len(vals), k):
        if i + k <= len(vals):
            vals[i:i + k] = reversed(vals[i:i + k])

    dummy = ListNode(0)
    tail = dummy
    for x in vals:
        tail.next = ListNode(x)
        tail = tail.next

    return dummy.next
```

#### Complexity
- Time: `O(n)`
- Space: `O(n)`

### Optimal Solution (Group-by-Group In-Place)

#### Pseudocode
```text
dummy.next = head
group_prev = dummy

LOOP:
    kth = group_prev
    MOVE kth forward k steps
    IF kth is null:
        BREAK

    group_next = kth.next

    prev = group_next
    curr = group_prev.next
    WHILE curr != group_next:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt

    tmp = group_prev.next
    group_prev.next = kth
    group_prev = tmp

RETURN dummy.next
```

#### Python
```python
def reverse_k_group_optimal(head, k):
    dummy = ListNode(0, head)
    group_prev = dummy

    while True:
        kth = group_prev
        for _ in range(k):
            kth = kth.next
            if not kth:
                return dummy.next

        group_next = kth.next

        prev = group_next
        curr = group_prev.next
        while curr != group_next:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        tmp = group_prev.next
        group_prev.next = kth
        group_prev = tmp
```

#### Complexity
- Time: `O(n)`
- Space: `O(1)`

---

## Q4. Swap Nodes in Pairs

### Problem
Given `head`, swap every two adjacent nodes and return head.

Example: `1 -> 2 -> 3 -> 4` -> `2 -> 1 -> 4 -> 3`

### Brute Force Solution

#### Pseudocode
```text
vals = values array
FOR i from 0 to n-2 step 2:
    SWAP vals[i], vals[i+1]
BUILD new list and return
```

#### Python
```python
def swap_pairs_bruteforce(head):
    vals = []
    cur = head

    while cur:
        vals.append(cur.val)
        cur = cur.next

    for i in range(0, len(vals) - 1, 2):
        vals[i], vals[i + 1] = vals[i + 1], vals[i]

    dummy = ListNode(0)
    tail = dummy
    for x in vals:
        tail.next = ListNode(x)
        tail = tail.next

    return dummy.next
```

#### Complexity
- Time: `O(n)`
- Space: `O(n)`

### Optimal Solution (Local Pointer Rewire)

#### Pseudocode
```text
dummy.next = head
prev = dummy

WHILE prev.next and prev.next.next:
    a = prev.next
    b = a.next

    prev.next = b
    a.next = b.next
    b.next = a

    prev = a

RETURN dummy.next
```

#### Python
```python
def swap_pairs_optimal(head):
    dummy = ListNode(0, head)
    prev = dummy

    while prev.next and prev.next.next:
        a = prev.next
        b = a.next

        prev.next = b
        a.next = b.next
        b.next = a

        prev = a

    return dummy.next
```

#### Complexity
- Time: `O(n)`
- Space: `O(1)`

---

## Q5. Rotate List

### Problem
Given `head` and non-negative integer `k`, rotate list to the right by `k`.

Example: `1 -> 2 -> 3 -> 4 -> 5`, `k = 2` -> `4 -> 5 -> 1 -> 2 -> 3`

### Brute Force Solution

#### Pseudocode
```text
vals = values array
k = k mod n
ROTATE array right by k
BUILD and RETURN new list
```

#### Python
```python
def rotate_right_bruteforce(head, k):
    vals = []
    cur = head

    while cur:
        vals.append(cur.val)
        cur = cur.next

    n = len(vals)
    if n == 0:
        return None

    k %= n
    vals = vals[-k:] + vals[:-k] if k else vals

    dummy = ListNode(0)
    tail = dummy
    for x in vals:
        tail.next = ListNode(x)
        tail = tail.next

    return dummy.next
```

#### Complexity
- Time: `O(n)`
- Space: `O(n)`

### Optimal Solution (Make Cycle then Break)

#### Pseudocode
```text
IF head is null OR head.next is null OR k == 0:
    RETURN head

FIND length n and tail
k = k mod n
IF k == 0:
    RETURN head

tail.next = head  # make cycle
steps = n - k - 1
new_tail = head moved steps times
new_head = new_tail.next
new_tail.next = null

RETURN new_head
```

#### Python
```python
def rotate_right_optimal(head, k):
    if not head or not head.next or k == 0:
        return head

    n = 1
    tail = head
    while tail.next:
        tail = tail.next
        n += 1

    k %= n
    if k == 0:
        return head

    tail.next = head

    steps = n - k - 1
    new_tail = head
    for _ in range(steps):
        new_tail = new_tail.next

    new_head = new_tail.next
    new_tail.next = None

    return new_head
```

#### Complexity
- Time: `O(n)`
- Space: `O(1)`

---

## Q6. Reorder List

### Problem
Given `L0 -> L1 -> ... -> Ln`, reorder to `L0 -> Ln -> L1 -> Ln-1 -> ...`.

Example: `1 -> 2 -> 3 -> 4 -> 5` -> `1 -> 5 -> 2 -> 4 -> 3`

### Brute Force Solution

#### Pseudocode
```text
nodes = array of node pointers
i = 0, j = len(nodes) - 1

WHILE i < j:
    nodes[i].next = nodes[j]
    i += 1
    IF i == j:
        BREAK
    nodes[j].next = nodes[i]
    j -= 1

nodes[i].next = null
RETURN head
```

#### Python
```python
def reorder_list_bruteforce(head):
    if not head:
        return head

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
    return head
```

#### Complexity
- Time: `O(n)`
- Space: `O(n)`

### Optimal Solution (Middle + Reverse + Merge)

#### Pseudocode
```text
IF head null OR head.next null:
    RETURN head

# find middle
slow = head
fast = head
WHILE fast.next and fast.next.next:
    slow = slow.next
    fast = fast.next.next

# reverse second half
second = slow.next
slow.next = null
reverse second -> rev

# merge alternately
first = head
WHILE rev exists:
    t1 = first.next
    t2 = rev.next
    first.next = rev
    rev.next = t1
    first = t1
    rev = t2

RETURN head
```

#### Python
```python
def reorder_list_optimal(head):
    if not head or not head.next:
        return head

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

    return head
```

#### Complexity
- Time: `O(n)`
- Space: `O(1)`

---

## Q7. Palindrome Linked List

### Problem
Given `head`, return `True` if list is palindrome, else `False`.

Example: `1 -> 2 -> 2 -> 1 -> True`

### Brute Force Solution

#### Pseudocode
```text
vals = values array
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

### Optimal Solution (Reverse Second Half)

#### Pseudocode
```text
IF 0 or 1 node:
    RETURN True

slow = head
fast = head
WHILE fast and fast.next:
    slow = slow.next
    fast = fast.next.next

IF fast exists:  # odd length
    slow = slow.next

reverse from slow -> right
left = head

WHILE right exists:
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
- Space: `O(1)`

---

## Q8. Reverse Nodes in Even Length Groups

### Problem
Given linked list, split nodes into groups of sizes `1,2,3,...`; reverse a group only if its actual length is even.

Example: `1 -> 1 -> 0 -> 6 -> 5` -> `1 -> 0 -> 1 -> 5 -> 6`

### Brute Force Solution

#### Pseudocode
```text
vals = values array
group = 1
i = 0

WHILE i < n:
    length = min(group, n - i)
    IF length even:
        REVERSE vals[i : i + length]
    i += length
    group += 1

BUILD and RETURN new list from vals
```

#### Python
```python
def reverse_even_length_groups_bruteforce(head):
    vals = []
    cur = head

    while cur:
        vals.append(cur.val)
        cur = cur.next

    n = len(vals)
    group = 1
    i = 0

    while i < n:
        length = min(group, n - i)
        if length % 2 == 0:
            vals[i:i + length] = reversed(vals[i:i + length])
        i += length
        group += 1

    dummy = ListNode(0)
    tail = dummy
    for x in vals:
        tail.next = ListNode(x)
        tail = tail.next

    return dummy.next
```

#### Complexity
- Time: `O(n)`
- Space: `O(n)`

### Optimal Solution (In-Place Group Reversal)

#### Pseudocode
```text
dummy.next = head
prev_tail = dummy
group = 1

WHILE prev_tail.next exists:
    group_head = prev_tail.next
    curr = group_head
    count = 0

    WHILE curr exists AND count < group:
        curr = curr.next
        count += 1

    next_group_head = curr

    IF count even:
        prev = next_group_head
        node = group_head
        REPEAT count times:
            nxt = node.next
            node.next = prev
            prev = node
            node = nxt

        prev_tail.next = prev
        prev_tail = group_head
    ELSE:
        prev_tail = group_head moved count - 1 steps

    group += 1

RETURN dummy.next
```

#### Python
```python
def reverse_even_length_groups_optimal(head):
    dummy = ListNode(0, head)
    prev_tail = dummy
    group = 1

    while prev_tail.next:
        group_head = prev_tail.next
        curr = group_head
        count = 0

        while curr and count < group:
            curr = curr.next
            count += 1

        next_group_head = curr

        if count % 2 == 0:
            prev = next_group_head
            node = group_head

            for _ in range(count):
                nxt = node.next
                node.next = prev
                prev = node
                node = nxt

            prev_tail.next = prev
            prev_tail = group_head
        else:
            prev_tail = group_head
            for _ in range(count - 1):
                prev_tail = prev_tail.next

        group += 1

    return dummy.next
```

#### Complexity
- Time: `O(n)`
- Space: `O(1)`

---

## Q9. Add Two Numbers II

### Problem
Given two non-empty linked lists representing non-negative integers (most significant digit first), return sum as linked list.

Example: `7 -> 2 -> 4 -> 3` + `5 -> 6 -> 4` -> `7 -> 8 -> 0 -> 7`

### Brute Force Solution

#### Pseudocode
```text
CONVERT l1 to integer a
CONVERT l2 to integer b
sum = a + b
CONVERT sum digits to linked list
RETURN head
```

#### Python
```python
def add_two_numbers_ii_bruteforce(l1, l2):
    def to_int(node):
        x = 0
        while node:
            x = x * 10 + node.val
            node = node.next
        return x

    s = to_int(l1) + to_int(l2)
    digits = list(str(s))

    dummy = ListNode(0)
    tail = dummy
    for ch in digits:
        tail.next = ListNode(int(ch))
        tail = tail.next

    return dummy.next
```

#### Complexity
- Time: `O(n + m)`
- Space: `O(n + m)` for digits/result representation

### Optimal Solution (Reverse, Add, Reverse Back)

#### Pseudocode
```text
FUNCTION reverse(head): ...

r1 = reverse(l1)
r2 = reverse(l2)
carry = 0
dummy = new node
tail = dummy

WHILE r1 or r2 or carry:
    sum = carry
    IF r1: sum += r1.val, r1 = r1.next
    IF r2: sum += r2.val, r2 = r2.next

    tail.next = new node(sum mod 10)
    tail = tail.next
    carry = sum // 10

RETURN reverse(dummy.next)
```

#### Python
```python
def add_two_numbers_ii_optimal(l1, l2):
    def reverse(head):
        prev = None
        curr = head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev

    r1 = reverse(l1)
    r2 = reverse(l2)

    carry = 0
    dummy = ListNode(0)
    tail = dummy

    while r1 or r2 or carry:
        total = carry

        if r1:
            total += r1.val
            r1 = r1.next

        if r2:
            total += r2.val
            r2 = r2.next

        tail.next = ListNode(total % 10)
        tail = tail.next
        carry = total // 10

    return reverse(dummy.next)
```

#### Complexity
- Time: `O(n + m)`
- Space: `O(1)` extra (excluding output nodes)

---

## Q10. Maximum Twin Sum of a Linked List

### Problem
Given an even-length linked list, twin of index `i` is `n-1-i`; return maximum twin sum.

Example: `5 -> 4 -> 2 -> 1` -> `6`

### Brute Force Solution

#### Pseudocode
```text
vals = values array
best = 0
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

    n = len(vals)
    best = 0

    for i in range(n // 2):
        best = max(best, vals[i] + vals[n - 1 - i])

    return best
```

#### Complexity
- Time: `O(n)`
- Space: `O(n)`

### Optimal Solution (Reverse Second Half In-Place)

#### Pseudocode
```text
slow = head
fast = head
WHILE fast and fast.next:
    slow = slow.next
    fast = fast.next.next

reverse list from slow -> right
left = head
best = 0

WHILE right exists:
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
- Space: `O(1)`

---

## Rapid Recall Checklist

- Reversal invariant: before moving forward, `curr.next` must point backward safely.
- Use dummy nodes for head-changing operations (`left=1`, pair swap, k-group).
- For segment/group reverse, identify boundaries before rewiring.
- For split-reverse-merge tasks, cut the first half before reversing second half.
- Confirm final tail reconnection to avoid cycles or dropped nodes.
