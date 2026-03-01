# Pattern 10: Monotonic Stack

## At a Glance

| Item | Summary |
|---|---|
| Use when | You need nearest greater/smaller element or span boundaries in linear time |
| Main tradeoff | Extra `O(n)` stack space for eliminating repeated neighbor scans |
| Typical runtime | `O(n)` amortized |
| Main structures | stack of indices with monotonic values (increasing/decreasing) |
| Common prompts | next greater/smaller, daily temperatures, histogram area, subarray min/max contributions |

## Related Playbook

- Full interview question set for this pattern:
  [Pattern 10 Top 10 Questions Playbook](./questions/10-monotonic-stack-top-10-questions.md)

## Diagram + Intuition

### Pattern Diagram

```text
Monotonic decreasing stack (for next greater):

indices on stack:   [ ... j, k ] where nums[j] >= nums[k]
current index i arrives with value nums[i]

while stack not empty and nums[stack.top] < nums[i]:
  popped = stack.pop()
  resolve answer for popped using i

push i
```

### Read-the-Question Trigger Cues

- "Next greater/smaller", "previous greater/smaller", nearest boundary/span.
- Need for each index: closest index to left/right with relation.
- Histogram/subarray contribution problems requiring left and right blocking boundaries.
- Brute force scans left/right for each element (`O(n^2)`).

### Intuition Anchor

- "Unresolved indices wait on stack until a future value breaks monotonic order and resolves them."

### 3-Second Pattern Check

- Can each element be resolved when a breaker appears?
- Can I enforce one monotonic order in a stack?
- Does each index push once and pop once?

## Decision Table: What to Store

| Prompt shape | Structure | Key -> value | Typical query |
|---|---|---|---|
| next greater to right | decreasing stack | index -> unresolved value | pop while smaller than current |
| next smaller to right | increasing stack | index -> unresolved value | pop while larger than current |
| previous smaller/greater | monotonic stack during forward scan | index -> nearest left boundary | top after cleanup is previous boundary |
| daily temperatures distance | decreasing stack of indices | `index -> wait days` | `i - popped_index` on pop |
| largest rectangle histogram | increasing stack + sentinel | `index -> nearest smaller left/right` | compute width on pop |
| subarray min/max contribution | two boundary arrays/stacks | `index -> span length left/right` | contribution = value * left * right |

## Universal Invariant

Before coding, say this sentence out loud:

- "At index `i`, stack contains unresolved indices in strict monotonic order; any index removed from stack has now found its nearest valid boundary."

If this invariant is unclear, the implementation will usually fail on edge cases.

## Step-by-Step Method (Easy Version)

Use this exact flow while coding:

1. Write default answer first (`-1`, `0`, or array of defaults).
2. Choose monotonic direction from query:
   decreasing stack for next greater, increasing stack for next smaller.
3. Store indices (not values) in stack.
4. For each index `i`, pop while current value violates stack monotonic rule.
5. Resolve popped indices immediately using current index/value.
6. Push current index.
7. Post-process remaining indices (no boundary found) or run sentinel pass if needed.

Fill-in template:

```python
def solve(nums):
    ans = [default] * len(nums)
    stack = []  # indices with chosen monotonic invariant

    for i, x in enumerate(nums):
        while stack and breaks_invariant(nums[stack[-1]], x):
            j = stack.pop()
            ans[j] = resolve_with_current(i, j)
        stack.append(i)

    # leftover indices keep default (or finalize in second pass)
    return ans
```

## Query/Update Order Rules

### A) Pop while broken, resolve, then push (most common)

Use for next greater/smaller and daily temperatures.

```python
for i, x in enumerate(nums):
    while stack and nums[stack[-1]] < x:
        j = stack.pop()
        ans[j] = i - j
    stack.append(i)
```

### B) Cleanup with strict/non-strict comparator, then read top

Use when answer for current index is previous smaller/greater.

```python
for i, x in enumerate(nums):
    while stack and nums[stack[-1]] >= x:
        stack.pop()
    prev_smaller[i] = stack[-1] if stack else -1
    stack.append(i)
```

### C) Two-pass boundaries (left and right spans)

Use for contribution/histogram variants.

```python
left = previous_strict_less(nums)       # pass 1
right = next_less_or_equal(nums)        # pass 2
for i, x in enumerate(nums):
    contribution = x * (i - left[i]) * (right[i] - i)
```

## Detailed Example (Daily Temperatures)

**Input:** `temps = [73, 74, 75, 71, 69, 72, 76, 73]`

1. Start empty decreasing stack of indices.
2. At `74`, pop `73` index and set wait `1`.
3. At `75`, pop `74` index and set wait `1`.
4. At `72`, pop `69` and `71`, resolve waits.
5. At `76`, pop all smaller unresolved temperatures and resolve.
6. Leftover indices have no warmer day, keep `0`.

Why it works: each day waits on stack until first warmer day arrives; that first breaker is the nearest warmer day.

## Reusable Python Templates

### 1) Membership (Any Next Greater Exists)

```python
def has_any_next_greater(nums):
    stack = []  # decreasing values by index

    for i, x in enumerate(nums):
        while stack and nums[stack[-1]] < x:
            return True
        stack.append(i)

    return False
```

Example:

```python
has_any_next_greater([5, 4, 3])  # False
has_any_next_greater([2, 1, 3])  # True
```

### 2) Boundary Indexes (Previous Smaller Element)

```python
def previous_smaller_index(nums):
    ans = [-1] * len(nums)
    stack = []  # increasing stack by value

    for i, x in enumerate(nums):
        while stack and nums[stack[-1]] >= x:
            stack.pop()
        ans[i] = stack[-1] if stack else -1
        stack.append(i)

    return ans
```

Example:

```python
previous_smaller_index([3, 7, 8, 4])  # [-1, 0, 1, 0]
previous_smaller_index([2, 2, 2])  # [-1, -1, -1]
```

### 3) Value -> Index Distance (Daily Temperatures)

```python
def daily_temperatures(temps):
    ans = [0] * len(temps)
    stack = []  # decreasing temperatures by index

    for i, t in enumerate(temps):
        while stack and temps[stack[-1]] < t:
            j = stack.pop()
            ans[j] = i - j
        stack.append(i)

    return ans
```

Example:

```python
daily_temperatures([73,74,75,71,69,72,76,73])  # [1,1,4,2,1,1,0,0]
daily_temperatures([30,40,50,60])  # [1,1,1,0]
```

### 4) Histogram Area (Sentinel Monotonic Stack)

```python
def largest_rectangle_area(heights):
    stack = []  # increasing heights by index
    best = 0

    for i in range(len(heights) + 1):
        curr = 0 if i == len(heights) else heights[i]
        while stack and heights[stack[-1]] > curr:
            h = heights[stack.pop()]
            left = stack[-1] if stack else -1
            width = i - left - 1
            best = max(best, h * width)
        stack.append(i)

    return best
```

Example:

```python
largest_rectangle_area([2,1,5,6,2,3])  # 10
largest_rectangle_area([2,4])  # 4
```

## Complexity

Let:

- `n` = number of elements.

Per-operation cost:

- Stack push/pop/top checks are `O(1)`.

End-to-end cost (most interview problems):

| Variant | Time (average) | Space |
|---|---|---|
| next greater/smaller per index | `O(n)` amortized | `O(n)` |
| previous boundary index | `O(n)` amortized | `O(n)` |
| daily temperatures | `O(n)` amortized | `O(n)` |
| largest rectangle in histogram | `O(n)` amortized | `O(n)` |
| sum of subarray minimums | `O(n)` amortized | `O(n)` |

Interview note:

- Amortized proof: each index is pushed once and popped once, so total stack operations are linear.

## Edge-Case Checklist (Pre-Submit)

Use this as a final pass before you finish coding.

### Contract Checks

- Return type matches prompt exactly: index, distance, count, area, or boolean.
- Default for unresolved elements is correct (`-1` or `0` as required).
- If circular array variant, wrap behavior is handled explicitly.
- If prompt expects values vs indices, convert correctly before return.

### Data-Rule Checks

- Stack stores indices when position/distance is required.
- Comparator strictness (`<`, `<=`, `>`, `>=`) matches duplicate semantics.
- Pop loop fully restores monotonic invariant before push.
- Boundary computations use correct left/right exclusion formulas.
- Sentinel logic is included where final pops are needed.

### Input Boundary Checks

- Empty and single-element input handled safely.
- Strictly increasing/decreasing arrays handled.
- All-equal values handled under chosen comparator rules.
- Negative and zero values handled where relevant.
- Large `n` does not trigger nested rescans.

### Pattern-Specific Checks

- Next-greater style resolves popped index with current index.
- Previous-boundary style computes answer after cleanup, before push.
- Histogram width formula is `right - left - 1`.
- Contribution problems use consistent tie-breaking on one side strict, other side non-strict.

### Quick Sanity Tests (Run Mentally)

| Scenario | Example | What should happen |
|---|---|---|
| no greater exists | `[5,4,3]` | all defaults for next greater |
| immediate greater | `[1,2]` | first resolves with distance `1` |
| duplicates | `[2,2,2]` | behavior follows chosen strictness |
| histogram valley | `[2,1,2]` | largest area is `3` |
| mixed temps | standard Daily Temperatures sample | matches expected waits |

## Common Pitfalls

- Storing values instead of indices when distance or width is needed.
- Using wrong strictness in comparator and breaking duplicate handling.
- Forgetting to flush unresolved bars via sentinel in histogram problems.
- Mixing left-boundary and right-boundary definitions.
- Applying monotonic stack where window expiry logic requires deque instead.

## When Not Ideal

- Need fixed-size moving-window max/min with expiration (use monotonic deque).
- No nearest-boundary structure exists; relation is non-local/non-monotonic.
- Dynamic updates/queries interleaved (segment tree/Fenwick may fit better).
- Small input where simpler quadratic scan is acceptable and clearer.

## Variations

- Next Greater Element I/II (including circular arrays).
- Daily Temperatures.
- Largest Rectangle in Histogram.
- Trapping Rain Water (stack version).
- Sum of Subarray Minimums / Maximums contribution style.

## Interview Tips

- Use this 20-second opener:
  "I’ll keep unresolved indices in a monotonic stack so each index is pushed and popped once, giving linear time."
- State invariant before coding:
  increasing or decreasing stack by value, and what unresolved means.
- Declare comparator strictness out loud:
  "`<` vs `<=` decides duplicate boundary ownership."
- Mention amortized argument:
  total pops across loop are at most `n`.
- Before finishing, test one increasing case and one duplicate case.

## Interviewer Questions While Coding (Important)

| Interviewer asks | How to answer quickly |
|---|---|
| Why stack, not nested loops? | Stack tracks unresolved nearest-boundary candidates and resolves them in amortized linear time. |
| Why indices instead of values? | Indices allow distance/width calculation and value lookup. |
| Which monotonic direction do you need? | Decreasing for next greater, increasing for next smaller. |
| Why this comparator strictness? | It controls duplicate ownership and prevents double counting in boundary spans. |
| Why `O(n)` despite while-pop loop? | Each index is popped at most once overall. |
| How do leftovers get handled? | Keep defaults or force resolution with sentinel/final pass. |
| How do histogram widths work? | On pop, current index is first smaller right boundary; stack top is previous smaller left boundary. |
| When should I use deque instead? | When elements must expire by sliding-window boundaries. |
| Most common bug? | Off-by-one width errors and wrong duplicate comparator. |

## Practice Ladder (2 Deep Interview Walkthroughs)

### 1) Daily Temperatures

Problem:

- Given temperatures array, return for each day how many days until a warmer temperature. If none, return `0`.

What interviewer is testing:

- Can you choose correct monotonic direction?
- Can you resolve distances on pop?
- Can you justify amortized complexity?

#### What to Say in First 30 Seconds

Use this script:

"Brute force checks future days for each index, which is quadratic.  
I will keep indices of unresolved days in a decreasing stack of temperatures.  
When a warmer day arrives, I pop colder days and fill their distance with index difference.  
Each index enters/leaves stack once, so time is linear."

#### Solution A: Brute Force

Idea:

- For each day, scan right until a warmer day appears.

```python
def daily_temps_bruteforce(temps):
    n = len(temps)
    ans = [0] * n

    for i in range(n):
        for j in range(i + 1, n):
            if temps[j] > temps[i]:
                ans[i] = j - i
                break

    return ans
```

Complexity:

- Time `O(n^2)`, Space `O(1)` extra.

#### Solution B: Right-to-Left Jump Pointers

Idea:

- Use answers to skip segments when searching warmer day.

```python
def daily_temps_jump(temps):
    n = len(temps)
    ans = [0] * n

    for i in range(n - 2, -1, -1):
        j = i + 1
        while j < n and temps[j] <= temps[i] and ans[j] > 0:
            j += ans[j]
        if j < n and temps[j] > temps[i]:
            ans[i] = j - i

    return ans
```

Complexity:

- Better in practice than brute force, but worst-case can still degrade.

Interviewer tradeoff answer:

- "Jump pointers are clever but less standard; monotonic stack gives clean guaranteed linear behavior."

#### Solution C: Monotonic Decreasing Stack (Optimal)

Idea:

- Unresolved colder days stay on stack until warmer day appears.

```python
def daily_temps_optimal(temps):
    ans = [0] * len(temps)
    stack = []  # indices, temps decreasing

    for i, t in enumerate(temps):
        while stack and temps[stack[-1]] < t:
            j = stack.pop()
            ans[j] = i - j
        stack.append(i)

    return ans
```

Complexity:

- Time `O(n)`, Space `O(n)`.

What to say while solving with interviewer:

1. "Stack invariant: temperatures at stack indices are decreasing."
2. "When current temperature is higher, it resolves popped indices."
3. "Distance is current index minus popped index."
4. "I’ll test increasing and flat sequences."

Common interviewer follow-up and answer:

| Interviewer asks | Good answer |
|---|---|
| Why decreasing stack? | We need first warmer day, so colder unresolved days should be popped by warmer current day. |
| What about equal temperatures? | Use strict `<` so equal temp is not considered warmer. |
| Why defaults `0`? | Prompt requires `0` when no warmer day exists. |

### 2) Largest Rectangle in Histogram

Problem:

- Given bar heights, return largest rectangle area in histogram.

What interviewer is testing:

- Can you map area to nearest smaller boundaries?
- Can you handle sentinel and width off-by-one correctly?
- Can you explain why each bar is finalized at pop time?

#### What to Say in First 30 Seconds

Use this script:

"Each bar’s max rectangle is determined by first smaller bar on left and right.  
I will keep an increasing stack of bar indices.  
When current height is smaller, popped bar’s right boundary is current index and left boundary is new stack top.  
I compute area on pop and use a sentinel pass to flush remaining bars in `O(n)`."

#### Solution A: Brute Force Expansion

Idea:

- For each bar, expand left and right while bars are at least that tall.

```python
def largest_rect_bruteforce(heights):
    n = len(heights)
    best = 0

    for i in range(n):
        h = heights[i]
        left = i
        while left - 1 >= 0 and heights[left - 1] >= h:
            left -= 1
        right = i
        while right + 1 < n and heights[right + 1] >= h:
            right += 1
        best = max(best, h * (right - left + 1))

    return best
```

Complexity:

- Time `O(n^2)`, Space `O(1)`.

#### Solution B: Precompute Left/Right Smaller Arrays

Idea:

- Two monotonic passes for previous smaller and next smaller.

```python
def largest_rect_two_pass(heights):
    n = len(heights)
    left = [-1] * n
    right = [n] * n
    stack = []

    for i in range(n):
        while stack and heights[stack[-1]] >= heights[i]:
            stack.pop()
        left[i] = stack[-1] if stack else -1
        stack.append(i)

    stack.clear()
    for i in range(n - 1, -1, -1):
        while stack and heights[stack[-1]] >= heights[i]:
            stack.pop()
        right[i] = stack[-1] if stack else n
        stack.append(i)

    best = 0
    for i, h in enumerate(heights):
        best = max(best, h * (right[i] - left[i] - 1))
    return best
```

Complexity:

- Time `O(n)`, Space `O(n)`.

Interviewer tradeoff answer:

- "Two-pass is clean for boundaries; single-pass stack with sentinel is more compact."

#### Solution C: Single-Pass Sentinel Stack (Optimal)

Idea:

- Finalize bar areas immediately when a smaller bar appears.

```python
def largest_rect_optimal(heights):
    stack = []  # increasing heights by index
    best = 0

    for i in range(len(heights) + 1):
        curr = 0 if i == len(heights) else heights[i]

        while stack and heights[stack[-1]] > curr:
            h = heights[stack.pop()]
            left = stack[-1] if stack else -1
            width = i - left - 1
            best = max(best, h * width)

        stack.append(i)

    return best
```

Complexity:

- Time `O(n)`, Space `O(n)`.

What to say while solving with interviewer:

1. "Increasing stack means unresolved bars with non-decreasing heights."
2. "On pop, current index is first smaller on right."
3. "Stack top after pop is first smaller on left."
4. "Width is `right - left - 1`."

Common interviewer follow-up and answer:

| Interviewer asks | Good answer |
|---|---|
| Why sentinel `0` at end? | Forces all remaining bars to pop and get finalized. |
| Why strict `>` vs `>=`? | Comparator choice manages duplicate ownership; either works with consistent boundary rules. |
| Most common bug? | Incorrect width formula or forgetting left boundary after pop. |
