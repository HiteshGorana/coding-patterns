# Pattern 14: Fast & Slow Pointers

## Diagram + Intuition

### Pattern Diagram
```text
slow = +1, fast = +2
if cycle -> they meet
```

### Read-the-Question Trigger Cues
- Linked list cycle, middle node, repeated-state loops.

### Intuition Anchor
- "Different speeds expose structure without extra memory."

### 3-Second Pattern Check
- Can two-speed traversal detect cycle/phase alignment?

## What This Pattern Solves
Detects cycles, finds middle points, and identifies phase relationships in linked structures.

## Recognition Signals
- Linked list cycle detection.
- Need middle node without length precomputation.
- "Find start of cycle" or repeated-state cycle in sequence.

## Core Intuition
Move pointers at different speeds:
- `slow` moves 1 step
- `fast` moves 2 steps

If there is a cycle, they must meet.  
If no cycle, `fast` reaches end.

## Step-by-Step Method (Cycle Detection)
1. Initialize `slow = head`, `fast = head`.
2. Move `slow` by 1 and `fast` by 2 while possible.
3. If pointers meet, cycle exists.
4. If `fast` or `fast.next` is `None`, no cycle.

## Finding Cycle Start
After first meeting:
1. Place one pointer at head.
2. Move both pointers one step at a time.
3. Their meeting point is cycle entry.

## Detailed Example (Middle of Linked List)
1. Move `slow` by 1, `fast` by 2.
2. When `fast` reaches end, `slow` is at middle.
3. For even length, decide whether first/second middle is required by loop condition.

## Complexity
- Time: `O(n)`
- Space: `O(1)`

## Python Template
```python
def has_cycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            return True
    return False
```

## Common Pitfalls
- Null pointer checks in wrong order (`fast.next` before `fast`).
- Comparing values instead of node identity.
- Wrong reset logic when finding cycle entry.
- Off-by-one behavior for middle node on even length lists.

## Variations
- Linked List Cycle I/II
- Happy Number (cycle in computed sequence)
- Find middle node
- Reorder list split point

## Interview Tips
- State Floyd's cycle detection by name.
- Mention proof idea: relative speed closes distance mod cycle length.
- Clarify identity comparison semantics in chosen language.

## Practice Problems
- Linked List Cycle
- Linked List Cycle II
- Middle of the Linked List
- Happy Number
