# Pattern 15: Linked List Reversal / In-place Operations

## Diagram + Intuition

### Pattern Diagram
```text
prev <- curr -> next
save next, reverse pointer, advance
```

### Read-the-Question Trigger Cues
- Reverse list/all/part/k-group in O(1) extra space.

### Intuition Anchor
- "Pointer rewiring with strict bookkeeping."

### 3-Second Pattern Check
- Can I do this with `prev, curr, next` safely?

## What This Pattern Solves
Efficiently rewires linked list pointers without extra arrays/stacks.

## Recognition Signals
- Reverse all or part of linked list.
- "In-place" requirement with `O(1)` extra space.
- Need block-wise reversals like `k` group or subrange reversal.

## Core Intuition
Track three pointers per step:
- `prev`
- `curr`
- `next_node`

Reverse one pointer direction at a time while preserving access to remaining list.

## Step-by-Step Method (Full Reverse)
1. Initialize `prev = None`, `curr = head`.
2. Save `next_node = curr.next`.
3. Set `curr.next = prev`.
4. Move `prev = curr`, `curr = next_node`.
5. Repeat until `curr` is `None`.
6. `prev` is new head.

## Step-by-Step Method (Reverse Sublist `left..right`)
1. Walk to node before `left`.
2. Reverse exactly `right-left+1` nodes.
3. Reconnect:
   - predecessor -> new sublist head
   - old sublist head -> node after reversed part

## Complexity
- Time: `O(n)`
- Space: `O(1)`

## Python Template
```python
def reverse_list(head):
    prev = None
    curr = head
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev
```

## Common Pitfalls
- Losing remainder of list by reassigning `next` before saving it.
- Incorrect reconnection for partial reverse.
- Returning original head after reversal.
- Mishandling `k`-group tail when remaining length < `k`.

## Variations
- Reverse Linked List II
- Reverse Nodes in k-Group
- Swap Nodes in Pairs
- Reorder List (split + reverse + merge)

## Interview Tips
- Draw pointer transitions on 3 nodes before coding.
- Name temporary variables clearly (`nxt` helps avoid bugs).
- Mention this is pointer safety problem more than algorithmic complexity.

## Practice Problems
- Reverse Linked List
- Reverse Linked List II
- Reverse Nodes in k-Group
- Reorder List
