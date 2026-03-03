# Monotonic Stack: A Deep Dive

---

## 1. What Is It? (Definition & Core Components)

A **monotonic stack** is a stack that maintains its elements in a strictly monotonic order — either entirely non-decreasing (monotonic increasing stack) or entirely non-decreasing (monotonic decreasing stack) — by popping elements that violate the order before pushing a new element. It is not a new data structure; it is a **usage pattern** applied to a regular stack to solve a family of problems about finding the nearest greater or smaller element for each position in an array.

```
REGULAR STACK:         MONOTONIC INCREASING STACK:
  Push anything          Only push if new element ≥ top
  No ordering            Pop until top ≤ new element, then push
  Pop in LIFO order      Always sorted bottom→top (smallest→largest)

MONOTONIC DECREASING STACK:
  Pop until top ≥ new element, then push
  Always sorted bottom→top (largest→smallest)

EXAMPLE — build monotonic increasing stack from [3, 1, 4, 1, 5, 9, 2, 6]:

  Process 3: stack=[]      → push 3.   stack=[3]
  Process 1: stack=[3]     → 1<3, pop 3; push 1.   stack=[1]
  Process 4: stack=[1]     → 4>1, push 4.   stack=[1,4]
  Process 1: stack=[1,4]   → 1<4, pop 4; 1≤1, push 1.   stack=[1,1]
  Process 5: stack=[1,1]   → 5>1, push 5.   stack=[1,1,5]
  Process 9: stack=[1,1,5] → 9>5, push 9.   stack=[1,1,5,9]
  Process 2: stack=[1,1,5,9] → 2<9 pop, 2<5 pop, 2>1 push.   stack=[1,1,2]
  Process 6: stack=[1,1,2] → 6>2, push 6.   stack=[1,1,2,6]
```

**Core components:**

- **Stack** — the underlying LIFO data structure; stores indices (usually) or values
- **Monotonic property** — the invariant: elements from bottom to top are always increasing OR always decreasing
- **Pop condition** — the trigger: when a new element violates the monotonic property, pop elements until the property is restored
- **The moment of pop** — the critical insight: when element `arr[i]` causes `arr[j]` to be popped, `arr[i]` is the **answer** (next greater/smaller element) for `arr[j]`
- **Store indices, not values** — almost always store array indices rather than values, so you can compute distances and access values simultaneously
- **Increasing stack** — bottom to top: small → large; used to find **next greater element**
- **Decreasing stack** — bottom to top: large → small; used to find **next smaller element**
- **Processing direction** — left to right processes "next" (rightward) problems; right to left processes "previous" (leftward) problems

---

## 2. The Physical Analogy: The Queue at a Concert

Imagine people standing in a line to enter a concert, each with a height. A bouncer looks at the line from the entrance side and only cares about people they can actually see from behind — meaning they can only see someone if no taller person is in between.

```
CONCERT LINE (heights):  [3, 1, 4, 1, 5, 9, 2, 6]
                          A  B  C  D  E  F  G  H

QUESTION: For each person, who is the NEXT TALLER person to their right?

A(3): Looking right → B(1) shorter, C(4) TALLER → answer: C
B(1): Looking right → C(4) TALLER → answer: C
C(4): Looking right → D(1) shorter, E(5) TALLER → answer: E
D(1): Looking right → E(5) TALLER → answer: E
E(5): Looking right → F(9) TALLER → answer: F
F(9): Looking right → G(2) shorter, H(6) shorter → answer: NONE
G(2): Looking right → H(6) TALLER → answer: H
H(6): Looking right → nobody → answer: NONE

NAIVE: For each person, scan all people to the right.  O(n²)
MONOTONIC STACK: One pass, O(n).

THE STACK = "people waiting to find their next taller person."
When F(9) arrives, everyone shorter pops off the stack
because F is their answer. They stop waiting.
```

This analogy captures the core insight: **elements wait in the stack until their answer arrives. When a new element arrives and is taller (or shorter, depending on variant), it IS the answer for all elements it causes to pop.**

---

## 3. The Four Problem Variants

All monotonic stack problems are combinations of two axes:

```
AXIS 1: Direction         AXIS 2: Relation
  → Next (rightward)        > Greater
  ← Previous (leftward)     < Smaller

FOUR VARIANTS:
  1. Next Greater Element     (increasing stack, left→right)
  2. Next Smaller Element     (decreasing stack, left→right)
  3. Previous Greater Element (decreasing stack, right→left or left→right)
  4. Previous Smaller Element (increasing stack, right→left or left→right)

STACK TYPE × DIRECTION:
  ┌──────────────────────────────────────────────────────┐
  │              NEXT          │         PREVIOUS        │
  ├────────────────────────────┼─────────────────────────┤
  │ GREATER: decreasing stack  │ GREATER: decreasing     │
  │          (pop when new >   │          stack, same    │
  │           top, new=answer) │          pass direction │
  ├────────────────────────────┼─────────────────────────┤
  │ SMALLER: increasing stack  │ SMALLER: increasing     │
  │          (pop when new <   │          stack, same    │
  │           top, new=answer) │          pass direction │
  └──────────────────────────────────────────────────────┘
```

---

## 4. Next Greater Element — Full Mechanics

### Algorithm

```
PROBLEM: For each arr[i], find the index of the nearest element
         to its RIGHT that is strictly greater than arr[i].
         Return -1 if no such element exists.

ALGORITHM (monotonic decreasing stack):
  Initialize stack = []  (stores indices)
  Initialize result = [-1] × n

  For i from 0 to n-1:
    WHILE stack is not empty AND arr[stack.top()] < arr[i]:
        j = stack.pop()
        result[j] = i           ← arr[i] is the next greater for arr[j]
    stack.push(i)

  Elements remaining in stack at end: no greater element exists → result=-1 ✅
```

### Step-by-Step Trace

```
arr = [4, 5, 2, 10, 8]
       0  1  2   3  4

result = [-1, -1, -1, -1, -1]
stack  = []

────────────────────────────
i=0, arr[0]=4:
  Stack empty → push 0.
  stack=[0]   (represents value 4)

────────────────────────────
i=1, arr[1]=5:
  arr[stack.top()]=arr[0]=4 < arr[1]=5 → POP 0
    result[0] = 1   ← next greater of arr[0]=4 is arr[1]=5 ✅
  Stack empty → push 1.
  stack=[1]   (represents value 5)

────────────────────────────
i=2, arr[2]=2:
  arr[stack.top()]=arr[1]=5 > arr[2]=2 → no pop.
  Push 2.
  stack=[1, 2]   (values: 5, 2)

────────────────────────────
i=3, arr[3]=10:
  arr[stack.top()]=arr[2]=2 < arr[3]=10 → POP 2
    result[2] = 3   ← next greater of arr[2]=2 is arr[3]=10 ✅
  arr[stack.top()]=arr[1]=5 < arr[3]=10 → POP 1
    result[1] = 3   ← next greater of arr[1]=5 is arr[3]=10 ✅
  Stack empty → push 3.
  stack=[3]   (value: 10)

────────────────────────────
i=4, arr[4]=8:
  arr[stack.top()]=arr[3]=10 > arr[4]=8 → no pop.
  Push 4.
  stack=[3, 4]   (values: 10, 8)

────────────────────────────
END OF ARRAY:
  Remaining in stack: [3, 4]
  result[3] = -1  (no element > 10 to the right)
  result[4] = -1  (no element > 8 to the right)

FINAL RESULT: [1, 3, 3, -1, -1]

VERIFICATION:
  arr[0]=4: next greater is arr[1]=5 at index 1 ✅
  arr[1]=5: next greater is arr[3]=10 at index 3 ✅
  arr[2]=2: next greater is arr[3]=10 at index 3 ✅
  arr[3]=10: no element > 10 to the right ✅
  arr[4]=8: no element to the right ✅
```

### Why the Stack Is Decreasing

```
STACK STATE at any point: bottom → top = decreasing order of values.

After processing [4,5,2,10,8]:
  At i=2: stack contains indices [1,2] → values [5,2]   (5>2: decreasing ✅)
  At i=4: stack contains indices [3,4] → values [10,8]  (10>8: decreasing ✅)

WHY DECREASING?
  When we push arr[i], we first pop everything SMALLER than arr[i].
  So everything remaining in the stack is ≥ arr[i].
  arr[i] is pushed last → it's the smallest element in the stack.
  All previous elements are larger (or the stack would have popped them).
  Result: bottom (largest) → top (smallest) = DECREASING. ✅

INVARIANT PROOF:
  Suppose stack has [a, b, c] with a≥b≥c (top=c).
  When we push d:
    Pop c if d > c, then b if d > b, then a if d > a.
    Whatever remains is ≥ d.
    After pushing d: [remaining ≥ d, d] → still decreasing ✅
```

---

## 5. Previous Smaller Element

```
PROBLEM: For each arr[i], find the nearest element to the LEFT
         that is strictly smaller than arr[i].

ALGORITHM (monotonic increasing stack, same left→right pass):

  stack = []
  result = [-1] × n

  For i from 0 to n-1:
    WHILE stack is not empty AND arr[stack.top()] >= arr[i]:
        stack.pop()           ← pop elements that are NOT the answer
    result[i] = stack.top()   ← current stack top IS the answer for i
    stack.push(i)             ← arr[i] might be the answer for future elements

KEY DIFFERENCE from "next greater":
  In "next greater": popped element gets the answer (arr[i] is their answer).
  In "previous smaller": the element that SURVIVES popping is the answer.

TRACE: arr = [3, 7, 1, 8, 5]
              0  1  2  3  4

  i=0, arr=3: stack=[]  → pop nothing, result[0]=-1, push 0. stack=[0]
  i=1, arr=7: arr[0]=3 < 7, don't pop. result[1]=0 (arr[0]=3<7). push 1. stack=[0,1]
  i=2, arr=1: arr[1]=7≥1→pop 1; arr[0]=3≥1→pop 0; stack=[]. result[2]=-1. push 2. stack=[2]
  i=3, arr=8: arr[2]=1 < 8, don't pop. result[3]=2 (arr[2]=1<8). push 3. stack=[2,3]
  i=4, arr=5: arr[3]=8≥5→pop 3; arr[2]=1 < 5, don't pop. result[4]=2 (arr[2]=1<5). push 4. stack=[2,4]

  RESULT: [-1, 0, -1, 2, 2]
  VERIFICATION:
    arr[0]=3: no smaller to left → -1 ✅
    arr[1]=7: arr[0]=3 < 7 → index 0 ✅
    arr[2]=1: no smaller to left → -1 ✅
    arr[3]=8: arr[2]=1 < 8 → index 2 ✅
    arr[4]=5: arr[2]=1 < 5 → index 2 ✅
```

---

## 6. The Cause-Effect Relationship

The power of the monotonic stack comes from one fundamental cause-effect chain:

```
CAUSE: A new element arr[i] is processed.
EFFECT (immediate): All stack elements smaller than arr[i] are popped.
MEANING: arr[i] IS the "next greater element" for everything it pops.

CAUSE: arr[i] is pushed onto the stack.
EFFECT (future): arr[i] will be the answer for future elements, OR
                 will be popped by a future element that is arr[i]'s answer.

CAUSE: An element remains in the stack at the end.
EFFECT: It has no next greater element (answer = -1 or ∞).

THIS ONE PASS ACHIEVES O(n) BECAUSE:
  Each element is pushed EXACTLY ONCE.
  Each element is popped EXACTLY ONCE.
  Total pushes + pops = 2n operations.
  Total work = O(n) regardless of input.

  Contrast with naive: O(n²) — for each element, potentially scan all.
  The stack "remembers" unresolved elements so we never scan backwards.
```

---

## 7. Classic Problem 1 — Daily Temperatures

```
PROBLEM: Given temperatures[i], find how many days until a warmer temperature.
         Return 0 if no warmer day exists.

  temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
  output        = [1,  1,  4,  2,  1,  1,  0,  0]

  73 → warmer in 1 day (74)
  75 → warmer in 4 days (76 at index 6, distance = 6-2 = 4)

SOLUTION (next greater element, store distances):

def dailyTemperatures(temps):
    n = len(temps)
    result = [0] * n
    stack = []   # stores indices

    for i in range(n):
        while stack and temps[stack[-1]] < temps[i]:
            j = stack.pop()
            result[j] = i - j    ← DISTANCE, not just index ✅
        stack.append(i)

    return result

TRACE: [73, 74, 75, 71, 69, 72, 76, 73]
        0    1   2   3   4   5   6   7

i=0(73): stack=[0]
i=1(74): 73<74→pop 0, result[0]=1-0=1. stack=[1]
i=2(75): 74<75→pop 1, result[1]=2-1=1. stack=[2]
i=3(71): 75>71→push. stack=[2,3]
i=4(69): 71>69→push. stack=[2,3,4]
i=5(72): 69<72→pop 4, result[4]=5-4=1.
         71<72→pop 3, result[3]=5-3=2.
         75>72→push. stack=[2,5]
i=6(76): 72<76→pop 5, result[5]=6-5=1.
         75<76→pop 2, result[2]=6-2=4.
         stack empty→push. stack=[6]
i=7(73): 76>73→push. stack=[6,7]

End: result[6]=0, result[7]=0 (remain in stack)

OUTPUT: [1, 1, 4, 2, 1, 1, 0, 0] ✅
```

---

## 8. Classic Problem 2 — Largest Rectangle in Histogram

One of the most elegant and important monotonic stack problems.

```
PROBLEM: Given heights of bars in a histogram, find the largest
         rectangle that can be formed.

  heights = [2, 1, 5, 6, 2, 3]
  answer  = 10  (bars at indices 2 and 3, height 5, width 2 → area=10)

  ┌─┐
  │ │
  │ │ ┌─┐
  │ │ │ │ ┌─┐
  │ │ │ │ │ │ ┌─┐
  └─┤ │ │ │ │ │ │ ┌─┐
    │ └─┴─┘ │ │ └─┤ │
    │       └─┘   └─┘
    2  1  5  6  2  3

KEY INSIGHT:
  For each bar i, the largest rectangle USING bar i's height extends
  left and right as far as bars of height ≥ arr[i] continue.
  Width = (first_bar_shorter_on_right - 1) - (first_bar_shorter_on_left + 1) + 1
        = right_boundary - left_boundary - 1

  We need: for each bar, the nearest shorter bar on the LEFT and RIGHT.
  → EXACTLY what monotonic stack computes! (next/previous smaller element)

ALGORITHM:
  Use monotonic increasing stack (values increasing bottom→top).
  When a bar is popped (because a shorter bar arrives):
    The popped bar's rectangle is fully determined:
      - Height: the popped bar's height
      - Right boundary: current index (first shorter bar to right)
      - Left boundary: new stack top (first shorter bar to left)

def largestRectangleArea(heights):
    n = len(heights)
    stack = []   # monotonic increasing (indices)
    max_area = 0

    for i in range(n + 1):
        # Sentinel: treat height[-1] as 0 to flush remaining stack at end
        h = heights[i] if i < n else 0

        while stack and heights[stack[-1]] > h:
            height = heights[stack.pop()]      # popped bar's height
            width  = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, height * width)

        stack.append(i)

    return max_area

TRACE: heights = [2, 1, 5, 6, 2, 3]

i=0(h=2): stack=[0]
i=1(h=1): 2>1→pop 0.
  height=2, stack=[], width=1 (stack empty→width=i=1)
  area=2×1=2. max=2.
  push 1. stack=[1]
i=2(h=5): 1<5→push. stack=[1,2]
i=3(h=6): 5<6→push. stack=[1,2,3]
i=4(h=2): 6>2→pop 3. height=6, left=stack[-1]=2, width=4-2-1=1. area=6. max=6.
          5>2→pop 2. height=5, left=stack[-1]=1, width=4-1-1=2. area=10. max=10. ✅
          1<2→stop. push 4. stack=[1,4]
i=5(h=3): 2<3→push. stack=[1,4,5]
i=6(sentinel h=0):
  3>0→pop 5. height=3, left=stack[-1]=4, width=6-4-1=1. area=3.
  2>0→pop 4. height=2, left=stack[-1]=1, width=6-1-1=4. area=8.
  1>0→pop 1. height=1, stack=[], width=6. area=6.

ANSWER: 10 ✅  (indices 2-3, height 5, width 2)
```

---

## 9. Classic Problem 3 — Trapping Rain Water

```
PROBLEM: Given elevation heights, compute how much rain water is trapped.

  heights = [0, 1, 0, 2, 1, 0, 1, 3, 1, 0, 1, 2]
  answer  = 6 units of water

  Visualization:
       ┌─┐
       │W│             ┌─┐
  ┌─┐  │W│ ┌─┐  ┌─┐  │W│ ┌─┐  ┌─┐
  │ │WW│ │W│ │WW│ │WW│ │W│ │WW│ │
  0  1  0  2  1  0  1  3  1  0  1  2

  W = water trapped

MONOTONIC STACK APPROACH:
  Think of filling water horizontally, layer by layer.
  When we find a "valley" (current height > stack top),
  we can trap water between the stack top (valley floor)
  and the walls on both sides.

def trap(height):
    stack = []   # monotonic decreasing
    water = 0

    for i in range(len(height)):
        while stack and height[stack[-1]] < height[i]:
            bottom_idx = stack.pop()          # valley floor
            if not stack: break               # no left wall → no water

            left_wall  = stack[-1]
            width      = i - left_wall - 1
            bounded_height = min(height[left_wall], height[i]) - height[bottom_idx]
            water += width * bounded_height

        stack.append(i)

    return water

TRACE (simplified): heights=[0,1,0,2,1,0,1,3,1,0,1,2]

  When i=3(h=2), stack has [0,2] (values 0,0):
    pop 2 (height=0): left=1(h=1), right=3(h=2)
    bounded = min(1,2)-0=1, width=3-1-1=1, water+=1×1=1

  When i=7(h=3): multiple pops fill in 5 more units of water.

FINAL ANSWER: 6 ✅
```

---

## 10. Classic Problem 4 — Sum of Subarray Minimums

```
PROBLEM: Find sum of min(subarray) for all subarrays.
  arr = [3, 1, 2, 4]

  Subarrays and their minimums:
  [3]=3, [1]=1, [2]=2, [4]=4
  [3,1]=1, [1,2]=1, [2,4]=2
  [3,1,2]=1, [1,2,4]=1
  [3,1,2,4]=1
  Sum = 3+1+2+4 + 1+1+2 + 1+1 + 1 = 17

NAIVE: O(n²) or O(n³)
MONOTONIC STACK: O(n)

KEY INSIGHT:
  For each element arr[i], count how many subarrays have arr[i] as their minimum.
  If arr[i] is the minimum of k subarrays, it contributes arr[i] × k to the total.

  "How many subarrays have arr[i] as minimum?"
  = (left_count) × (right_count)
  where:
    left_count  = distance to previous SMALLER element (how far left arr[i] dominates)
    right_count = distance to next SMALLER OR EQUAL element (how far right it dominates)

  Using ≤ on one side prevents double-counting equal elements.

def sumSubarrayMins(arr):
    n = len(arr)
    MOD = 10**9 + 7
    stack = []   # monotonic increasing
    result = 0

    for i in range(n + 1):
        while stack and (i == n or arr[stack[-1]] >= arr[i]):
            mid = stack.pop()
            left  = stack[-1] if stack else -1
            right = i

            # arr[mid] is minimum for all subarrays between left and right
            count = (mid - left) * (right - mid)
            result = (result + arr[mid] * count) % MOD

        stack.append(i)

    return result

TRACE: arr=[3,1,2,4]

  i=1(arr=1): pop 0 (arr[0]=3≥1).
    mid=0, left=-1, right=1
    count=(0-(-1))×(1-0) = 1×1 = 1
    result += 3×1 = 3

  i=4(sentinel): pop 3(arr=4), pop 2(arr=2), pop 1(arr=1)
    mid=3: left=2, right=4, count=1×1=1, result+=4×1=4  → result=7
    mid=2: left=1, right=4, count=1×2=2, result+=2×2=4  → result=11
    mid=1: left=-1, right=4, count=2×3=6, result+=1×6=6 → result=17

ANSWER: 17 ✅
```

---

## 11. Circular Array — Next Greater Element II

```
PROBLEM: Find next greater element in a CIRCULAR array.
  [1, 2, 1]: the circular next greater of the last 1 wraps around to 2.

  answer = [2, -1, 2]

TRICK: Process the array TWICE (indices 0 to 2n-1).
  Use i % n to wrap indices.
  On second pass, don't push indices ≥ n (or use actual index, not value index).

def nextGreaterElementII(nums):
    n = len(nums)
    result = [-1] * n
    stack = []

    for i in range(2 * n):
        while stack and nums[stack[-1]] < nums[i % n]:
            j = stack.pop()
            result[j] = nums[i % n]   ← circular: i%n wraps around
        if i < n:
            stack.append(i)           ← only push real indices (first pass)

    return result

TRACE: [1, 2, 1] processed as [1, 2, 1, 1, 2, 1]

  i=0(1): push 0. stack=[0]
  i=1(2): 1<2→pop 0. result[0]=2. stack=[1]
  i=2(1): 2>1→push 2. stack=[1,2]
  i=3(1%3=0→arr=1): 1≤1→don't pop. (don't push, i≥n)
  i=4(4%3=1→arr=2): arr[2]=1<2→pop 2. result[2]=2. ✅
                    arr[1]=2≤2→stop. (don't push, i≥n)
  i=5: nothing remaining that gets an answer.

  result=[2,-1,2] ✅
```

---

## 12. The "Why" Questions

### Why store indices instead of values?

```
SCENARIO: arr = [5, 3, 5, 2, 7]
  Two elements with value 5 exist at indices 0 and 2.

  If we store VALUES: when we see 7 and want to pop all < 7,
    we pop 5 — but WHICH 5? Index 0 or index 2?
    Cannot determine distances. Cannot record correct results.

  If we store INDICES:
    stack = [0, 2, 3]  (values: 5, 5, 2)
    When i=4 (value 7): pop 3 → result[3]=4 (distance=1)
                        pop 2 → result[2]=4 (distance=2)
                        pop 0 → result[0]=4 (distance=4)
    All correct — indices are unique even for equal values ✅

RULE: Almost always store INDICES in the monotonic stack.
  Access value via arr[stack.top()].
  Compute distance via i - stack.top().
  Record result via result[stack.pop()] = i.
```

### Why is the total time O(n) despite the while loop?

```
AMORTIZED ANALYSIS:

  Operations performed: push and pop.
  Each element is pushed EXACTLY ONCE (when i reaches it).
  Each element is popped AT MOST ONCE (when a larger/smaller element arrives).

  Total pushes: n (one per element).
  Total pops:   ≤ n (each element popped at most once).
  Total operations: ≤ 2n.

  The while loop may run many iterations for a single element,
  but those iterations are "paid for" by previous pushes.

  POTENTIAL FUNCTION ARGUMENT:
    Define Φ = size of stack.
    Each push: O(1) work + Φ increases by 1.
    Each pop: O(1) work + Φ decreases by 1.
    Total amortized work = actual work - ΔΦ ≤ 2n.

  CONCRETE EXAMPLE of "misleading" while loop:
    arr = [5, 4, 3, 2, 1, 10]
    For i=5(value=10): while loop pops 5 elements.
    But those 5 elements were each pushed ONCE before this.
    Total pushes: 6.  Total pops: 5.  Total: 11 operations.
    Still O(n) ✅

  The key: you can never pop more elements than you've pushed.
  Pushes = n → pops ≤ n → total = O(n).
```

### Why does the stack maintain the monotonic property automatically?

```
PROOF OF INVARIANT:
  Claim: after processing element arr[i], the stack is decreasing
         (for next greater element problem).

  BASE CASE: empty stack is trivially decreasing ✅

  INDUCTIVE STEP: Assume stack is decreasing before processing arr[i].
    We pop all elements smaller than arr[i].
    After popping: stack top (if exists) is ≥ arr[i].
    We push arr[i].
    New stack: [..., element ≥ arr[i], arr[i]]
    This is still decreasing (last element arr[i] is smallest) ✅

  THE PROPERTY IS SELF-ENFORCING:
    We pop violating elements → property restored → push maintains it.
    There's no separate "check if monotonic" step needed.
    The pop-then-push mechanism IS the maintenance mechanism. ✅
```

---

## 13. "What If" Edge Cases

| What If...? | What Happens |
|---|---|
| Empty array | Stack stays empty; result array is empty; no iterations |
| Single element | Pushed, never popped; result[-1] = 0 or -1 depending on problem |
| All elements equal | Decreasing stack variant: nothing ever popped (equal elements don't trigger pop); all results = -1; increasing variant: everything pops immediately |
| Strictly decreasing array [5,4,3,2,1] | For next greater: nothing ever popped until end; all results = -1; stack stays full |
| Strictly increasing array [1,2,3,4,5] | For next greater: every new element pops previous; each result[i] = i+1 |
| Duplicate elements | Equal elements need careful handling; use strict vs non-strict inequality deliberately to avoid double-counting |
| Very large array (n=10^6) | Stack can hold at most n elements; O(n) space; O(n) time; no issue |
| Negative values | Works fine; comparisons work the same for negative numbers |
| Circular array | Process 2n elements using i%n; only push first n indices to stack |
| Sentinel value at end | Append 0 or -∞ to force remaining stack to flush; common trick for histogram problems |

### Equal Elements — The Double-Counting Problem

```
PROBLEM: arr = [2, 2, 2] — previous smaller element for each?

  Correct answer: [-1, -1, -1]
  (No element is strictly smaller than any other)

WRONG CODE (strict pop for previous smaller):
  i=0(2): stack=[]. result[0]=-1. push 0. stack=[0]
  i=1(2): arr[0]=2 is NOT < arr[1]=2 → don't pop.
          result[1] = stack.top() = 0   ← WRONG! arr[0]=2 is not SMALLER than 2

FIX: Use >= when popping for "previous smaller":
  Pop while arr[stack.top()] >= arr[i]:  ← pop EQUAL elements too
  i=1(2): arr[0]=2 ≥ 2 → pop 0. stack=[]. result[1]=-1 ✅
  i=2(2): stack=[1]. arr[1]=2 ≥ 2 → pop 1. stack=[]. result[2]=-1 ✅

GENERAL RULE:
  For STRICT comparisons (next STRICTLY greater):
    Pop while arr[top] <= arr[i]   (pop equal elements)
  For NON-STRICT (next greater or equal):
    Pop while arr[top] < arr[i]    (keep equal elements)

  In sum of subarray minimums: use >= on one side and > on the other
  to prevent double-counting subarrays with equal minimum elements.

  This is one of the subtler aspects — always clarify the problem's
  equality semantics before choosing the comparison operator.
```

---

## 14. Monotonic Queue — The Extension

```
A MONOTONIC QUEUE (deque) extends the monotonic stack idea to a SLIDING WINDOW,
supporting both front-removal (expired elements) and back-popping (monotonic property).

PROBLEM: Sliding window maximum — maximum in every window of size k.
  arr = [1, 3, -1, -3, 5, 3, 6, 7]  k = 3
  output = [3, 3, 5, 5, 6, 7]

MONOTONIC DECREASING DEQUE:
  Front: holds the maximum of the current window (largest element).
  Back: new elements are added, removing smaller elements first (like monotonic stack).
  Front removal: when front element is outside the window (index too old).

from collections import deque

def maxSlidingWindow(nums, k):
    dq = deque()   # stores indices, values decreasing front→back
    result = []

    for i in range(len(nums)):
        # Remove elements outside window from front
        while dq and dq[0] < i - k + 1:
            dq.popleft()

        # Remove elements smaller than current from back (monotonic property)
        while dq and nums[dq[-1]] < nums[i]:
            dq.pop()

        dq.append(i)

        # Window complete: front is maximum
        if i >= k - 1:
            result.append(nums[dq[0]])

    return result

TRACE: [1,3,-1,-3,5,3,6,7], k=3

  i=0(1): dq=[0]
  i=1(3): 1<3→pop 0. dq=[1]
  i=2(-1): 3>-1→push. dq=[1,2]. Window [1,3,-1]: result=[nums[1]=3]
  i=3(-3): -1>-3→push. dq=[1,2,3].
           Front 1 is within window [1,3]. result=[3,nums[1]=3]
  i=4(5): -3<5→pop 3; -1<5→pop 2; 3<5→pop 1. dq=[4].
           result=[3,3,nums[4]=5]
  i=5(3): 5>3→push. dq=[4,5]. result=[3,3,5,nums[4]=5]
  i=6(6): 3<6→pop 5; 5<6→pop 4. dq=[6]. result=[3,3,5,5,nums[6]=6]
  i=7(7): 6<7→pop 6. dq=[7]. result=[3,3,5,5,6,nums[7]=7]

  OUTPUT: [3,3,5,5,6,7] ✅

KEY DIFFERENCE from monotonic stack:
  Stack: elements only removed from back (pop when property violated).
  Queue: elements removed from BACK (property) AND FRONT (window expiry).
  The front removal is what makes it a SLIDING window structure.
```

---

## 15. Real-World Applications

| Domain | Problem | Monotonic Stack's Role |
|---|---|---|
| **Stock market** | Span of stock prices (days since price ≥ today) | Previous greater element on prices |
| **Meteorology** | Days until warmer weather | Daily temperatures problem directly |
| **Architecture** | Largest rectangular floor plan in a floor-plan grid | Largest rectangle in histogram |
| **Hydraulics** | Water retention between walls | Trapping rain water |
| **Computer graphics** | Visible surface determination | Previous greater element for occlusion |
| **Compilers** | Operator precedence parsing | Monotonic stack for expression evaluation |
| **Database query optimization** | Merge interval optimization | Stack-based range merging |
| **Task scheduling** | Finding the next higher-priority task | Next greater element on priority array |
| **Image processing** | Finding dominant features in histograms | Histogram rectangle problem |
| **Financial risk** | Maximum drawdown in price series | Sliding window min/max |

### Stock Span Problem — Real Trading Application

```
PROBLEM: For each day's stock price, find the SPAN:
  the number of consecutive days (including today) for which
  the price was ≤ today's price.

  prices = [100, 80, 60, 70, 60, 75, 85]
  spans  = [1,   1,  1,  2,  1,  4,  6]

  Day 5 (price=75): prices [60, 70, 60, 75] are all ≤ 75 → span=4
  Day 6 (price=85): prices [80, 60, 70, 60, 75, 85] are... wait:
    80 > 75: span stops at day 1.
    Actually span=6: [60, 70, 60, 75, 85] from day 1 to 6 AND 80<85,
    so day 1 (80) ≤ 85 → span=6.

SOLUTION (previous greater element):
  span[i] = i - (index of previous day with price > today) if exists
           = i + 1 if no such day

def stockSpan(prices):
    n = len(prices)
    stack = []   # stores indices, monotonic decreasing prices
    spans = []

    for i in range(n):
        while stack and prices[stack[-1]] <= prices[i]:
            stack.pop()
        spans.append(i - stack[-1] if stack else i + 1)
        stack.append(i)

    return spans

TRACE: [100, 80, 60, 70, 60, 75, 85]

  i=0(100): stack=[]. span=0+1=1. push 0. stack=[0]
  i=1(80):  100>80, no pop. span=1-0=1. push 1. stack=[0,1]
  i=2(60):  80>60, no pop. span=2-1=1. push 2. stack=[0,1,2]
  i=3(70):  60≤70→pop 2; 80>70, stop. span=3-1=2. push 3. stack=[0,1,3]
  i=4(60):  70>60, no pop. span=4-3=1. push 4. stack=[0,1,3,4]
  i=5(75):  60≤75→pop 4; 70≤75→pop 3; 80>75, stop. span=5-1=4. push 5. stack=[0,1,5]
  i=6(85):  75≤85→pop 5; 80≤85→pop 1; 100>85, stop. span=6-0=6. push 6.

  SPANS: [1, 1, 1, 2, 1, 4, 6] ✅
```

---

## 16. Comparison With Related Concepts

```
              ┌──────────────────────────────────────────────────────────┐
              │         STACK-BASED AND RANGE QUERY PATTERNS             │
              └──────────────────────────┬───────────────────────────────┘
                                         │
       ┌──────────────────┬──────────────┼──────────────┬────────────────┐
       ▼                  ▼             ▼              ▼                ▼
  MONOTONIC STACK     SEGMENT TREE   SPARSE TABLE   TWO POINTERS    BINARY SEARCH
  ───────────────     ────────────   ────────────   ────────────    ─────────────
  O(n) total          O(n log n)     O(n log n)     O(n)            O(log n)
  O(1) amortized      O(log n)/query O(1)/query     per element     per query
  One-time answers    Dynamic range  Static range   Window-based    Sorted arrays
  for ALL elements    queries        queries        problems        only
  No preprocessing    Preprocessing  Preprocessing  No preprocess   Needs sort
  Next/prev           Aggregate      Aggregate      Contiguous      Existence/
  greater/smaller     any range      idempotent     subarrays       position
  Streaming data      Random access  Random access  Ordered scan    Ordered data
  Left/right          Any range      Any range      Adjacent only   Any index
  neighbors           any time       read-only
```

**Monotonic Stack vs Segment Tree:**
Segment tree answers arbitrary range queries repeatedly. Monotonic stack answers a specific structural question (next/previous greater/smaller) for ALL elements in one pass. For the next-greater-element problem, segment tree would require n separate queries — O(n log n). Monotonic stack answers all n in O(n) total.

**Monotonic Stack vs Two Pointers:**
Both are O(n) techniques for array problems. Two pointers works on contiguous subarrays with a window that expands/contracts. Monotonic stack works on non-contiguous "nearest neighbor" relationships. Two pointers when the relationship is between adjacent elements of a window; monotonic stack when searching for the nearest element satisfying a condition.

**Monotonic Stack vs Brute Force:**
The fundamental improvement: brute force re-scans for every element, visiting already-processed elements again. Monotonic stack processes each element exactly twice (push + pop), never revisiting. The stack "memorizes" relevant unresolved elements so the inner scan becomes amortized O(1).

---

## 17. The Decision Framework

```
SHOULD I USE A MONOTONIC STACK?

Does the problem ask about NEAREST elements satisfying a condition?
    │
    ├── "Find the nearest GREATER/SMALLER element to the left/right"
    │       → Monotonic stack ✅ (core use case)
    │
    ├── "For each element, how many days/positions until condition"
    │       → Monotonic stack, store distances ✅
    │
    ├── "Largest rectangle / area involving heights"
    │       → Monotonic stack (histogram rectangle pattern) ✅
    │
    ├── "Water trapped / pooling between walls"
    │       → Monotonic stack (rain water pattern) ✅
    │
    ├── "Sum/product involving subarrays where element is min/max"
    │       → Monotonic stack (contribution counting) ✅
    │
    ├── "Sliding window maximum/minimum"
    │       → Monotonic DEQUE (extends monotonic stack) ✅
    │
    ├── "Arbitrary range sum/min/max with updates"
    │       → Segment tree (not monotonic stack) ❌
    │
    └── "Find ALL elements greater/smaller in a range"
            → Monotonic stack gives only NEAREST, not all ❌

KEY SIGNAL PHRASES:
  "next greater/smaller"
  "previous greater/smaller"
  "nearest taller/shorter"
  "days until warmer"
  "first smaller to the left/right"
  "largest rectangle"
  "trapped water"
  "stock span"
  "subarray minimum/maximum sum"
```

---

## 18. Tips for Long-Term Retention

**1. The concert queue image**
Picture people in a line, each waiting to find the next taller person. New arrivals instantly answer the "who's taller" question for everyone shorter already in line — those people leave the queue (pop). The new arrival joins the queue (push) to wait for their own answer. This single image encodes: what the stack contains (waiting elements), what pop means (answer found), what push means (joining the waiting line), and why the stack stays decreasing (shorter waiters always wait in front of taller ones).

**2. The moment of pop is the moment of truth**
When element `arr[i]` causes `arr[j]` to be popped: `arr[i]` IS the answer for `arr[j]`. This cause-effect relationship is the entire algorithm. Burning this into memory: "the element that causes the pop is the answer for the popped element." Every variant of the algorithm is just a different formulation of what "the answer" means.

**3. Four variants from two binary choices**
Next vs Previous × Greater vs Smaller = 4 variants. All four use the same stack mechanism; only the comparison direction and when you record the answer changes. Next Greater: decreasing stack, record on pop. Previous Smaller: increasing stack, record on push (the surviving top). Understand one variant fully and derive the others by symmetry.

**4. O(n) because push + pop = 2n total**
Whenever someone doubts O(n) due to the while loop: "Each element is pushed exactly once and popped at most once. Total operations ≤ 2n." This argument is clean, memorable, and complete. The inner while loop is not an independent O(n) per iteration — it's amortized across the entire array.

**5. Always store indices, not values**
This rule almost never has exceptions. Indices are unique (values may repeat), enable distance computation, and can always retrieve the value via `arr[index]`. The reflex should be: "push index i, access value as arr[i]." Building this habit eliminates an entire class of bugs.

**6. Sentinel values eliminate special-casing**
Appending 0 or -∞ to the array forces all remaining stack elements to flush at the end, giving them their "no answer exists" result automatically. This transforms "process array, then handle remaining stack" into "process array with sentinel, stack is always empty at end." Cleaner code, fewer bugs.

**7. Monotonic stack = deferred comparison resolution**
The conceptual synthesis: brute force resolves each comparison immediately (scan all future elements). Monotonic stack DEFERS resolution until the answer arrives naturally. Elements wait in the stack until their answer appears. This deferral, combined with the stack's ordering, ensures each element waits exactly as long as needed and is resolved in O(1) amortized time. Recognizing "deferred resolution until answer arrives" as a pattern helps identify when to reach for a monotonic stack.

---

A monotonic stack is fundamentally a **structured waiting mechanism** for answering "nearest neighbor" questions about array elements. The stack is not just a container — it is a carefully maintained queue of unresolved questions, each element waiting for its specific answer. The monotonic property ensures that when an answer arrives, it resolves exactly the right questions (all elements it dominates) and no others. The amortized O(n) cost emerges naturally: each question is asked once (push) and answered once (pop), giving a total of 2n operations regardless of the complexity of the relationships involved. What appears to be a simple stack with a comparison filter is, in practice, one of the most elegant examples of turning an O(n²) brute-force scan into an O(n) one-pass algorithm through the insight that the order of resolution mirrors the order of processing.
